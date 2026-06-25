#!/usr/bin/env node
/**
 * build-versioned-sdk.js
 *
 * Python adaptation of the Go/TypeScript versioned SDK builder.
 * Builds one Python SDK sub-package per resource partition found in
 * the apis/ directory.  New partitions are discovered automatically — no
 * script updates required when new endpoints are added.
 *
 * Pipeline for each partition:
 *   1. Copy apis/ to .sdk-build-tmp/  (git-ignored, so source files stay clean)
 *   2. Apply prescript YAML fixes to the temp copy
 *   3. Bundle the partition openapi.yaml with redocly (resolves shared/ $refs)
 *   4. Run openapi-generator-cli with a dynamically generated config
 *   5. Run postscript.js on the generated output
 *
 * After all partitions are built:
 *   6. Regenerate sailpoint/__init__.py to expose the SailPoint namespace class
 *
 * On failure, structured error logs are written to build-errors/:
 *   build-errors/summary.md              — overview of all failures
 *   build-errors/<partition>-error.md    — self-contained per-partition report
 *                                          with error output + spec file contents
 *                                          (designed to be fed directly to an AI)
 *
 * Usage:
 *   node sdk-resources/build-versioned-sdk.js <path-to-apis-dir> [--partition <name>] [--keep-tmp]
 *
 * Options:
 *   --partition <name>   Build only the named partition (default: all)
 *   --keep-tmp           Do not delete .sdk-build-tmp after the build
 */

"use strict";

const fs   = require("fs");
const path = require("path");
const { spawnSync } = require("child_process");

// ---------------------------------------------------------------------------
// Constants
// ---------------------------------------------------------------------------

const SDK_ROOT      = path.resolve(__dirname, "..");
const SAILPOINT_DIR = path.join(SDK_ROOT, "sailpoint");

// Directories inside sailpoint/ that are never auto-generated and must be
// preserved during the clean step.
const CLEAN_PRESERVE_DIRS = new Set(["nerm", "nerm/v2025"]);
const TEMP_DIR      = path.join(SDK_ROOT, ".sdk-build-tmp");
const BUNDLED_DIR   = path.join(TEMP_DIR, "bundled");
const ERROR_DIR     = path.join(SDK_ROOT, "build-errors");
const JAR           = path.join(SDK_ROOT, "openapi-generator-cli.jar");
const POSTSCRIPT    = path.join(__dirname, "postscript.js");
const TEMPLATE_DIR  = path.join(__dirname, "resources");

const PACKAGE_NAME_PREFIX = "sailpoint";
const PACKAGE_VERSION     = "1.0.0";
const API_VERSION         = "v1";

// ---------------------------------------------------------------------------
// CLI args
// ---------------------------------------------------------------------------

const args = process.argv.slice(2);
if (args.length === 0 || args[0].startsWith("--")) {
  console.error("Usage: node sdk-resources/build-versioned-sdk.js <path-to-apis-dir> [--partition <name>] [--keep-tmp]");
  process.exit(1);
}

const apisDir       = path.resolve(args[0]);
const keepTmp       = args.includes("--keep-tmp");
const partitionIdx  = args.indexOf("--partition");
const onlyPartition = partitionIdx !== -1 ? args[partitionIdx + 1] : null;

// ---------------------------------------------------------------------------
// Utility: copy directory recursively
// ---------------------------------------------------------------------------

function copyDirSync(src, dest) {
  fs.mkdirSync(dest, { recursive: true });
  for (const entry of fs.readdirSync(src, { withFileTypes: true })) {
    const srcPath  = path.join(src, entry.name);
    const destPath = path.join(dest, entry.name);
    if (entry.isDirectory()) {
      copyDirSync(srcPath, destPath);
    } else {
      fs.copyFileSync(srcPath, destPath);
    }
  }
}

// ---------------------------------------------------------------------------
// Utility: walk directory, return all file paths
// ---------------------------------------------------------------------------

function walkSync(dir, files = []) {
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      walkSync(full, files);
    } else {
      files.push(full);
    }
  }
  return files;
}

// ---------------------------------------------------------------------------
// Utility: read a file safely (returns empty string if missing)
// ---------------------------------------------------------------------------

function readFileSafe(filePath) {
  try {
    return fs.readFileSync(filePath, "utf8");
  } catch {
    return "";
  }
}

// ---------------------------------------------------------------------------
// Prescript fixes (applied to the temp copy of apis/)
// ---------------------------------------------------------------------------

function applyPrescriptFixes(tempApisDir) {
  const files = walkSync(tempApisDir);
  let fixed = 0;

  for (const file of files) {
    if (!file.endsWith(".yaml") && !file.endsWith(".yml")) continue;

    let rawdata = fs.readFileSync(file, "utf8");
    let lines   = rawdata.split("\n");
    let out     = [];
    let changed = false;

    // Fix X-SailPoint-Experimental headers
    const experimentalFixed = rawdata.replace(
      /(- name: X-SailPoint-Experimental[\s\S]*?required: )true/g,
      "$1false"
    );
    if (experimentalFixed !== rawdata) {
      rawdata = experimentalFixed;
      lines   = rawdata.split("\n");
      changed = true;
    }

    // Fix transforms and sources transform schemas
    if (file.includes(path.join("transforms", "schemas", "transform.yaml")) ||
        file.includes(path.join("transforms", "schemas", "Transform.yaml")) ||
        file.includes(path.join("sources",    "schemas", "transform.yaml")) ||
        file.includes(path.join("sources",    "schemas", "Transform.yaml"))) {
      for (let line of lines) {
        if (line.includes("oneOf")) { line = line.replaceAll("oneOf:", "type: object"); changed = true; }
        if (!line.includes("- $ref:")) out.push(line);
      }
      lines = out; out = [];
    }

    // Fix workflow trigger schemas
    if (file.includes(path.join("workflows", "schemas", "workflowtrigger.yaml"))) {
      for (let line of lines) {
        if (line.includes("anyOf")) { line = line.replaceAll("anyOf:", "type: object"); changed = true; }
        if (!line.includes("- $ref:")) out.push(line);
      }
      lines = out; out = [];
    }

    // Fix search document schemas
    if (file.includes(path.join("search", "schemas", "searchdocument.yaml")) ||
        file.includes(path.join("search", "schemas", "SearchDocument.yaml")) ||
        file.includes(path.join("search", "schemas", "searchdocuments.yaml")) ||
        file.includes(path.join("search", "schemas", "SearchDocuments.yaml")) ||
        file.includes(path.join("documents", "SearchDocument.yaml")) ||
        file.includes(path.join("documents", "SearchDocuments.yaml"))) {
      lines = ["type: object"];
      changed = true;
    }

    // Fix accounts paths (Python-specific: oneOf → $ref to SlimAccount)
    if (file.includes(path.join("accounts", "paths")) && file.endsWith("accounts.yaml")) {
      for (let line of lines) {
        if (line.includes("oneOf")) {
          line = line.replaceAll("oneOf:", "$ref: '../schemas/SlimAccount.yaml'");
          changed = true;
        }
        if (line.includes("- $ref: '../schemas/SlimAccount.yaml'") ||
            line.includes("- $ref: '../schemas/FullAccount.yaml'")) {
          // skip
        } else {
          out.push(line);
        }
      }
      lines = out; out = [];
    }

    if (changed) {
      fs.writeFileSync(file, lines.join("\n"), "utf8");
      fixed++;
    }
  }

  console.log(`  prescript: fixed ${fixed} file(s) in temp copy`);
}

// ---------------------------------------------------------------------------
// Bundle a single partition's openapi.yaml with redocly
// ---------------------------------------------------------------------------

function bundlePartition(partitionName, tempApisDir) {
  const inputSpec  = path.join(tempApisDir, partitionName, "openapi.yaml");
  const outputSpec = path.join(BUNDLED_DIR, `${partitionName}.yaml`);

  fs.mkdirSync(BUNDLED_DIR, { recursive: true });

  const result = spawnSync(
    "npx",
    ["redocly", "bundle", inputSpec, "-o", outputSpec, "--force"],
    { encoding: "utf8" }
  );

  return {
    ok:     result.status === 0,
    stdout: result.stdout || "",
    stderr: result.stderr || "",
    outputSpec,
  };
}

// ---------------------------------------------------------------------------
// Generate per-partition config YAML (Python-specific)
// ---------------------------------------------------------------------------

function writePartitionConfig(partitionName) {
  const packageDir  = partitionName.replaceAll("-", "_");
  const packageName = `${PACKAGE_NAME_PREFIX}.${packageDir}`;

  const config = [
    `templateDir: ${TEMPLATE_DIR}`,
    `packageName: ${packageName}`,
    `packageVersion: ${PACKAGE_VERSION}`,
    `apiVersion: ${API_VERSION}`,
    `generateSourceCodeOnly: true`,
    `subModuleName: ${partitionName}`,
    `files:`,
    `  developerSite_code_examples.mustache:`,
    `    templateType: SupportingFiles`,
    `    destinationFilename: sailpoint/${packageDir}/docs/Examples/python_code_examples_overlay.yaml`,
    `  docs_methods_index.mustache:`,
    `    templateType: SupportingFiles`,
    `    destinationFilename: sailpoint/${packageDir}/docs/Methods/Index.md`,
    `  docs_models_index.mustache:`,
    `    templateType: SupportingFiles`,
    `    destinationFilename: sailpoint/${packageDir}/Index.md`,
  ].join("\n");

  const configPath = path.join(TEMP_DIR, `${partitionName}-config.yaml`);
  fs.writeFileSync(configPath, config, "utf8");
  return configPath;
}

// ---------------------------------------------------------------------------
// Run openapi-generator for a single partition
// ---------------------------------------------------------------------------

function generatePartition(partitionName, bundledSpec, configPath) {
  const packageDir = partitionName.replaceAll("-", "_");
  const outputDir  = path.join(SAILPOINT_DIR, packageDir);

  if (fs.existsSync(outputDir)) {
    fs.rmSync(outputDir, { recursive: true, force: true });
  }

  const result = spawnSync(
    "java",
    [
      "-jar", JAR,
      "generate",
      "-i", bundledSpec,
      "-g", "python",
      "-o", SDK_ROOT,
      "--global-property", "skipFormModel=false,apiDocs=true,modelDocs=true",
      "--config", configPath,
      "--api-name-suffix", "Api",
      "--enable-post-process-file",
    ],
    { encoding: "utf8", cwd: SDK_ROOT }
  );

  return {
    ok:        result.status === 0,
    stdout:    result.stdout || "",
    stderr:    result.stderr || "",
    outputDir,
    packageDir,
  };
}

// ---------------------------------------------------------------------------
// Version unversioned models when a versioned sibling exists
//
// After generation, if models/ contains both `accessrequestconfig.py` and
// `accessrequestconfigv2.py`, the base file is renamed to `accessrequestconfigv1.py`
// and all references within the package are updated to match.
//
// Pattern: a model file whose name (without .py) does NOT end in v\d+ but where
// another model file with the same base name + v\d+ suffix exists.
// ---------------------------------------------------------------------------

function escapeRegex(str) {
  return str.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
}

function versionUnversionedModels(outputDir) {
  const modelsDir = path.join(outputDir, "models");
  const testDir   = path.join(outputDir, "test");
  if (!fs.existsSync(modelsDir)) return 0;

  const modelFiles = fs.readdirSync(modelsDir)
    .filter(f => f.endsWith(".py") && f !== "__init__.py");

  const modelNames = new Set(modelFiles.map(f => f.slice(0, -3)));
  const toVersion  = [];

  for (const name of modelNames) {
    if (/v\d+$/.test(name)) continue; // already versioned
    const pattern = new RegExp(`^${escapeRegex(name)}v\\d+$`);
    if ([...modelNames].some(other => pattern.test(other))) {
      toVersion.push(name);
    }
  }

  if (toVersion.length === 0) return 0;

  // Build the full set of replacements first, then apply all at once before
  // renaming any files.  This avoids the ordering problem where a file renamed
  // in iteration N is no longer findable by iteration N+1 via the stale path
  // list.
  const replacements = toVersion.map(baseName => ({
    baseName,
    newBaseName:  `${baseName}v1`,
    className:    baseName[0].toUpperCase() + baseName.slice(1),
    newClassName: `${baseName[0].toUpperCase() + baseName.slice(1)}v1`,
    // \b…\b enforces a complete word match so "entitlement" can't match
    // inside "entitlementaccessrequestconfig" (where the next char is still a
    // word character).  (?!v) guards the already-versioned siblings (v2, …).
    classRe:  new RegExp(`\\b${escapeRegex(baseName[0].toUpperCase() + baseName.slice(1))}(?!v)\\b`, "g"),
    moduleRe: new RegExp(`\\b${escapeRegex(baseName)}(?!v)\\b`, "g"),
  }));

  // Pass 1: update content in all files (while every file still has its original name)
  const allFiles = walkSync(outputDir)
    .filter(f => f.endsWith(".py") || f.endsWith(".md") || f.endsWith(".yaml"));

  for (const f of allFiles) {
    let content = readFileSafe(f);
    let updated = content;
    for (const { classRe, moduleRe, newClassName, newBaseName } of replacements) {
      updated = updated.replace(classRe, newClassName).replace(moduleRe, newBaseName);
    }
    if (updated !== content) fs.writeFileSync(f, updated, "utf8");
  }

  // Pass 2: rename files (now that all content is consistent)
  for (const { baseName, newBaseName, className, newClassName } of replacements) {
    const oldModel = path.join(modelsDir, `${baseName}.py`);
    const newModel = path.join(modelsDir, `${newBaseName}.py`);
    if (fs.existsSync(oldModel)) fs.renameSync(oldModel, newModel);

    if (fs.existsSync(testDir)) {
      const oldTest = path.join(testDir, `test_${baseName}.py`);
      const newTest = path.join(testDir, `test_${newBaseName}.py`);
      if (fs.existsSync(oldTest)) fs.renameSync(oldTest, newTest);
    }

    console.log(`    versioned model: ${className} → ${newClassName}`);
  }

  return toVersion.length;
}

// ---------------------------------------------------------------------------
// Run postscript.js on the generated output
// ---------------------------------------------------------------------------

function runPostscript(outputDir) {
  const result = spawnSync(
    "node",
    [POSTSCRIPT, outputDir],
    { encoding: "utf8", cwd: SDK_ROOT }
  );

  return {
    ok:     result.status === 0,
    stdout: result.stdout || "",
    stderr: result.stderr || "",
  };
}

// ---------------------------------------------------------------------------
// Error logging
// ---------------------------------------------------------------------------

const MAX_FILE_BYTES = 20_000;

function collectSpecFiles(partitionName, tempApisDir) {
  const partDir = path.join(tempApisDir, partitionName);
  if (!fs.existsSync(partDir)) return {};

  const collected = {};
  const files = walkSync(partDir).filter(f => f.endsWith(".yaml"));

  for (const f of files) {
    const relPath = path.relative(path.join(tempApisDir, ".."), f);
    let content = readFileSafe(f);
    if (Buffer.byteLength(content, "utf8") > MAX_FILE_BYTES) {
      content = content.slice(0, MAX_FILE_BYTES) + "\n\n[... truncated — file exceeds 20 KB ...]";
    }
    collected[relPath] = content;
  }

  return collected;
}

function writeErrorReport(partitionName, step, errorOutput, tempApisDir, apisSourceDir) {
  fs.mkdirSync(ERROR_DIR, { recursive: true });

  const specFiles  = collectSpecFiles(partitionName, path.join(tempApisDir, "apis"));
  const sourceDir  = path.join(apisSourceDir, partitionName);
  const reportPath = path.join(ERROR_DIR, `${partitionName}-error.md`);

  const fileBlocks = Object.entries(specFiles)
    .map(([relPath, content]) => `### \`${relPath}\`\n\`\`\`yaml\n${content}\n\`\`\``)
    .join("\n\n");

  const report = `# SDK Build Error: \`${partitionName}\`

## Context for AI

This file is a self-contained error report for the \`${partitionName}\` API partition.
It contains the build error and all relevant OpenAPI spec files needed to diagnose and fix the problem.

**Source directory to fix:** \`${sourceDir}\`
**Failed step:** ${step}

---

## Error Output

\`\`\`
${errorOutput.trim()}
\`\`\`

---

## Fix Instructions

1. Read the error output above carefully.
2. Identify which spec file(s) below are causing the problem.
3. Apply fixes directly to the source files under \`${sourceDir}\`.
4. Do **not** edit files in \`.sdk-build-tmp/\` — those are generated copies.
5. After fixing, re-run the build for just this partition:
   \`\`\`bash
   node sdk-resources/build-versioned-sdk.js <path-to-apis> --partition ${partitionName}
   \`\`\`

---

## Spec Files

${fileBlocks || "_No spec files found._"}
`;

  fs.writeFileSync(reportPath, report, "utf8");
  return reportPath;
}

function writeSummaryReport(results, apisSourceDir) {
  fs.mkdirSync(ERROR_DIR, { recursive: true });

  const failureLines = results.failed.map(({ partition, step, reportPath }) =>
    `| \`${partition}\` | ${step} | [${path.basename(reportPath)}](./${path.basename(reportPath)}) |`
  ).join("\n");

  const summary = `# SDK Build Error Summary

**Date:** ${new Date().toISOString()}
**APIs directory:** \`${apisSourceDir}\`
**Total partitions:** ${results.total}
**Succeeded:** ${results.success.length}
**Failed:** ${results.failed.length}

## Failed Partitions

| Partition | Failed Step | Error Report |
|-----------|-------------|--------------|
${failureLines || "_(none)_"}

## How to Fix

Each error report in this directory is self-contained and can be given directly to an AI.
It includes the full error output and all relevant spec file contents.

Fix partitions one at a time:
\`\`\`bash
# Fix a single partition
node sdk-resources/build-versioned-sdk.js <path-to-apis> --partition <partition-name>

# Re-run all after fixes
node sdk-resources/build-versioned-sdk.js <path-to-apis>
\`\`\`
`;

  const summaryPath = path.join(ERROR_DIR, "summary.md");
  fs.writeFileSync(summaryPath, summary, "utf8");
  return summaryPath;
}

// ---------------------------------------------------------------------------
// Regenerate sailpoint/__init__.py from discovered partition packages
//
// Scans sailpoint/*/api/*_api.py files to discover generated API classes,
// then writes sailpoint/__init__.py exposing:
//   - Each API class as a named top-level export (AccountsApi, …)
//   - A SailPoint namespace class:
//       SailPoint.AccountsApi   — single partition
//       SailPoint.AccountsApi   — combined via multiple inheritance if two partitions
//                                 resolve to the same resource name
//   - Common utilities (Configuration, Paginator)
//
// Partition packages are detected by the presence of an api/ subdirectory.
// Multi-version: Python multiple inheritance gives the cleanest combination —
//   class AccountsApi(AccountsV2Api, AccountsV1Api): pass
//   MRO ensures the later-sorted class wins on name conflicts.
// ---------------------------------------------------------------------------

/** AccountsV1Api → AccountsApi */
function toResourceApiName(className) {
  return className.replace(/V\d+Api$/, "Api");
}

/** Extract numeric version from class name: AccountsV1Api → 1 */
function classApiVersion(className) {
  return parseInt(className.match(/V(\d+)Api$/)?.[1] ?? "1", 10);
}

function generateInitPy() {
  if (!fs.existsSync(SAILPOINT_DIR)) {
    console.log("  sailpoint/ directory not found, skipping __init__.py regeneration.");
    return;
  }

  const partitionDirs = fs.readdirSync(SAILPOINT_DIR)
    .filter(d => {
      const fullPath = path.join(SAILPOINT_DIR, d);
      if (!fs.statSync(fullPath).isDirectory()) return false;
      // Partition packages are identified by having an api/ subdirectory
      return fs.existsSync(path.join(fullPath, "api"));
    })
    .sort();

  if (partitionDirs.length === 0) {
    console.log("  No partition packages found, skipping __init__.py regeneration.");
    return;
  }

  // Collect { partDir, module, className } for each generated API class
  const partitions = [];
  for (const partDir of partitionDirs) {
    const apiDir = path.join(SAILPOINT_DIR, partDir, "api");
    if (!fs.existsSync(apiDir)) continue;

    const apiFiles = fs.readdirSync(apiDir).filter(f => f.endsWith("_api.py"));
    for (const apiFile of apiFiles) {
      const content  = readFileSafe(path.join(apiDir, apiFile));
      const match    = content.match(/^class (\w+)[(:]/m);
      if (match) {
        const className  = match[1];
        const moduleName = apiFile.replace(".py", "");
        partitions.push({ partDir, module: moduleName, className });
      }
    }
  }

  if (partitions.length === 0) {
    console.log("  No API classes found in partition packages, skipping __init__.py regeneration.");
    return;
  }

  // Group by resource name, sorted oldest→newest within each group
  const byResource = new Map();
  for (const p of partitions) {
    const key = toResourceApiName(p.className);
    if (!byResource.has(key)) byResource.set(key, []);
    byResource.get(key).push(p);
  }
  for (const group of byResource.values()) {
    group.sort((a, b) => classApiVersion(a.className) - classApiVersion(b.className));
  }

  // Write root-level shared support files — copied from a partition and patched
  // to be self-contained. This gives users a stable, partition-agnostic import:
  //   from sailpoint import ApiClient, Configuration
  //
  // Why copy instead of re-export: api_client.__deserialize does a dynamic
  // getattr(sailpoint.<partition>.models, klass) lookup which only works for
  // that one partition's models. By patching the copy we replace that with a
  // sys.modules scan over all loaded sailpoint.*.models, making it work for
  // every partition without users needing to know which partition they're using.
  const firstPartDir = partitions[0].partDir;
  const partitionPrefix = `sailpoint.${firstPartDir}`;

  function patchAndCopyRootFile(filename) {
    let content = readFileSafe(path.join(SAILPOINT_DIR, firstPartDir, filename));

    // Strip partition docstring header reference (cosmetic)
    content = content.replace(
      /Identity Security Cloud API - \S+/,
      "Identity Security Cloud API"
    );

    if (filename === "rest.py" || filename === "api_client.py") {
      // Fix: from sailpoint.<partition>.exceptions import → from sailpoint.exceptions import
      content = content.replace(
        new RegExp(`from ${partitionPrefix}\\.exceptions import`, "g"),
        "from sailpoint.exceptions import"
      );
    }

    if (filename === "api_client.py") {
      // Fix: from sailpoint.<partition>.api_response import → from sailpoint.api_response import
      content = content.replace(
        new RegExp(`from ${partitionPrefix}\\.api_response import`, "g"),
        "from sailpoint.api_response import"
      );
      // Fix: from sailpoint.<partition> import rest → from sailpoint import rest
      content = content.replace(
        new RegExp(`from ${partitionPrefix} import rest`, "g"),
        "from sailpoint import rest"
      );
      // Remove: import sailpoint.<partition>.models  (replaced by dynamic lookup below)
      content = content.replace(
        new RegExp(`^import ${partitionPrefix}\\.models\\s*\\n`, "m"),
        ""
      );
      // Ensure stdlib `sys` is imported (needed for the dynamic model lookup)
      if (!/^import sys\b/m.test(content)) {
        content = content.replace(/^(import \w)/, "import sys\n$1");
      }
      // Fix: klass = getattr(sailpoint.<partition>.models, klass)
      //   → dynamic search across all loaded sailpoint.*.models in sys.modules
      content = content.replace(
        new RegExp(`klass = getattr\\(${partitionPrefix.replace(/\./g, "\\.")}\\.models, klass\\)`),
        [
          "# Dynamic lookup across all loaded sailpoint.*.models",
          "                for _mod_name, _mod in list(sys.modules.items()):",
          '                    if (_mod_name.startswith("sailpoint.") and _mod_name.endswith(".models")',
          "                            and _mod is not None and hasattr(_mod, klass)):",
          "                        klass = getattr(_mod, klass)",
          "                        break",
          "                else:",
          "                    raise AttributeError(",
          "                        f\"Cannot find model class {klass!r} in any loaded sailpoint partition module\"",
          "                    )",
        ].join("\n")
      );
    }

    content = `# Auto-generated by build-versioned-sdk.js — DO NOT EDIT\n${content}`;
    fs.writeFileSync(path.join(SAILPOINT_DIR, filename), content, "utf8");
  }

  patchAndCopyRootFile("exceptions.py");
  patchAndCopyRootFile("api_response.py");
  patchAndCopyRootFile("rest.py");
  patchAndCopyRootFile("api_client.py");

  // Imports: one private alias per versioned class.
  // Use the partition dir as a disambiguating prefix so two partitions that
  // happen to generate the same class name (e.g. both NERM and ISC expose a
  // RolesApi) don't clobber each other's alias.
  const imports = partitions.map(p => {
    const alias = `_${p.partDir}__${p.className}`;
    return `from sailpoint.${p.partDir}.api.${p.module} import ${p.className} as ${alias}`;
  }).join("\n");

  // SailPoint namespace members and any combined-class declarations
  const combinedClassLines = [];
  const resourceExportLines = []; // top-level resource-named exports
  const nsMembers = [];

  for (const [resourceApiName, group] of byResource.entries()) {
    if (group.length === 1) {
      const alias = `_${group[0].partDir}__${group[0].className}`;
      resourceExportLines.push(`${resourceApiName} = ${alias}`);
      nsMembers.push(`    ${resourceApiName} = ${alias}`);
    } else {
      // Multi-version — Python multiple inheritance: latest first so its MRO wins
      const bases = [...group].reverse().map(p => `_${p.partDir}__${p.className}`).join(", ");
      const combinedVar = `_${resourceApiName}Combined`;
      combinedClassLines.push(`class ${combinedVar}(${bases}): pass`);
      resourceExportLines.push(`${resourceApiName} = ${combinedVar}`);
      nsMembers.push(`    ${resourceApiName} = ${combinedVar}`);
    }
  }

  // Combined classes must be declared BEFORE the resource export assignments
  // that reference them, otherwise Python raises a NameError at import time.
  const combinedSection = combinedClassLines.length > 0
    ? `\n# --- Combined multi-version API classes ---\n${combinedClassLines.join("\n")}\n`
    : "";

  const fileContent = `# Auto-generated by build-versioned-sdk.js — DO NOT EDIT
#
# Usage — flat imports (preferred):
#   from sailpoint import ApiClient, SourcesApi, Configuration
#   result = SourcesApi(ApiClient(configuration)).list_sources_v1_with_http_info()
#
# Usage — namespace (all resources under one import):
#   from sailpoint import SailPoint, ApiClient
#   api = SailPoint.SourcesApi(ApiClient(configuration))
#
# To import a class directly from a partition sub-package:
#   from sailpoint.sources import SourcesApi
#
# If two partitions share a resource name, SourcesApi automatically combines both
# via Python multiple inheritance — existing imports never change.

# --- Shared ApiClient ---
from sailpoint.api_client import ApiClient

# --- Partition API class imports (private) ---
${imports}
${combinedSection}
# --- Resource-named exports ---
${resourceExportLines.join("\n")}

# --- SailPoint namespace (all resources grouped, alternative style) ---
class SailPoint:
${nsMembers.join("\n")}

# --- Common utilities ---
from sailpoint.configuration import Configuration, ConfigurationParams
from sailpoint.paginator import Paginator
`;

  fs.writeFileSync(path.join(SAILPOINT_DIR, "__init__.py"), fileContent, "utf8");
  console.log(`  Wrote sailpoint/{exceptions,api_response,rest,api_client}.py (shared root support files)`);
  console.log(`  Wrote sailpoint/__init__.py — ${partitions.length} API class(es), ${byResource.size} resource(s) in SailPoint namespace`);
}

// ---------------------------------------------------------------------------
// Main
// ---------------------------------------------------------------------------

async function main() {
  if (!fs.existsSync(apisDir)) {
    console.error(`Error: apis directory not found: ${apisDir}`);
    process.exit(1);
  }

  if (!fs.existsSync(JAR)) {
    console.error(`Error: openapi-generator-cli.jar not found at ${JAR}`);
    console.error("  Download it with:");
    console.error("  wget -q https://repo1.maven.org/maven2/org/openapitools/openapi-generator-cli/7.12.0/openapi-generator-cli-7.12.0.jar -O openapi-generator-cli.jar");
    process.exit(1);
  }

  const allPartitions = fs.readdirSync(apisDir, { withFileTypes: true })
    .filter(e => e.isDirectory() && e.name !== "shared")
    .map(e => e.name)
    .sort();

  const partitions = onlyPartition
    ? allPartitions.filter(p => p === onlyPartition)
    : allPartitions;

  if (partitions.length === 0) {
    console.error(`No partitions found${onlyPartition ? ` matching '${onlyPartition}'` : ""} in ${apisDir}`);
    process.exit(1);
  }

  console.log(`\nFound ${partitions.length} partition(s) to build\n`);

  // Set up temp directory
  console.log(`[SETUP] Copying apis/ → ${path.relative(SDK_ROOT, TEMP_DIR)}/`);
  if (fs.existsSync(TEMP_DIR)) fs.rmSync(TEMP_DIR, { recursive: true, force: true });
  copyDirSync(apisDir, path.join(TEMP_DIR, "apis"));

  console.log("[SETUP] Applying prescript fixes to temp copy ...");
  applyPrescriptFixes(path.join(TEMP_DIR, "apis"));

  // Clear any previous error reports
  if (fs.existsSync(ERROR_DIR)) fs.rmSync(ERROR_DIR, { recursive: true, force: true });

  // Clean only the sailpoint/* directories and loose files that correspond to
  // partitions in this run's apisDir.  This prevents a NERM build from wiping
  // ISC partition output (or vice versa) when two separate builds are used.
  //
  // Partition output dir name = partition name with '-' → '_'.
  // Loose README files follow the same naming convention.
  // CLEAN_PRESERVE_DIRS entries are never touched regardless.
  // Skipped for single-partition rebuilds (--partition flag) since generatePartition
  // already deletes and regenerates that one directory.
  if (!onlyPartition && fs.existsSync(SAILPOINT_DIR)) {
    console.log("[CLEAN] Removing stale sailpoint/* directories for this build's partitions ...");

    // The output directory name for each partition in this run
    const thisRunDirs = new Set(partitions.map(p => p.replaceAll("-", "_")));

    const entries = fs.readdirSync(SAILPOINT_DIR, { withFileTypes: true });

    const staleDirs = entries
      .filter(e => e.isDirectory()
        && thisRunDirs.has(e.name)
        && !CLEAN_PRESERVE_DIRS.has(e.name)
        && fs.existsSync(path.join(SAILPOINT_DIR, e.name, "api")))
      .map(e => e.name);
    for (const d of staleDirs) {
      fs.rmSync(path.join(SAILPOINT_DIR, d), { recursive: true, force: true });
      console.log(`  removed sailpoint/${d}/`);
    }

    // Remove loose README files dropped by the generator for this run's partitions
    const looseFiles = entries
      .filter(e => {
        if (!e.isFile() || !e.name.endsWith("_README.md")) return false;
        // Match <packageDir>_README.md patterns for partitions in this run
        const stem = e.name.slice(0, -"_README.md".length);
        return thisRunDirs.has(stem);
      })
      .map(e => e.name);
    for (const f of looseFiles) {
      fs.rmSync(path.join(SAILPOINT_DIR, f));
      console.log(`  removed sailpoint/${f}`);
    }

    console.log(`  cleaned ${staleDirs.length} director${staleDirs.length === 1 ? "y" : "ies"}, ${looseFiles.length} loose file(s)\n`);
  }

  const results = {
    total:   partitions.length,
    success: [],
    failed:  [],
  };

  for (const partition of partitions) {
    console.log(`\n${"=".repeat(60)}`);
    console.log(`  Building: ${partition}`);
    console.log(`${"=".repeat(60)}`);

    // --- Step 1: Bundle ---
    console.log("  [1/5] Bundling spec ...");
    const bundle = bundlePartition(partition, path.join(TEMP_DIR, "apis"));
    if (!bundle.ok) {
      const errorOutput = [bundle.stdout, bundle.stderr].filter(Boolean).join("\n");
      console.error(`  ✗ bundling failed`);
      const reportPath = writeErrorReport(partition, "bundling", errorOutput, TEMP_DIR, apisDir);
      results.failed.push({ partition, step: "bundling", reportPath });
      continue;
    }

    // --- Step 2: Config ---
    console.log("  [2/5] Writing generator config ...");
    const configPath = writePartitionConfig(partition);

    // --- Step 3: Generate ---
    console.log("  [3/5] Generating Python SDK ...");
    const gen = generatePartition(partition, bundle.outputSpec, configPath);
    if (!gen.ok) {
      const errorOutput = [gen.stdout, gen.stderr].filter(Boolean).join("\n");
      console.error(`  ✗ generation failed`);
      const reportPath = writeErrorReport(partition, "generation", errorOutput, TEMP_DIR, apisDir);
      results.failed.push({ partition, step: "generation", reportPath });
      continue;
    }

    // --- Step 4: Version unversioned models ---
    console.log("  [4/5] Versioning unversioned models ...");
    const versioned = versionUnversionedModels(gen.outputDir);
    if (versioned > 0) {
      console.log(`    renamed ${versioned} unversioned model(s) to v1`);
    }

    // --- Step 5: Postscript ---
    console.log("  [5/5] Running postscript ...");
    const post = runPostscript(gen.outputDir);
    if (!post.ok) {
      const errorOutput = [post.stdout, post.stderr].filter(Boolean).join("\n");
      console.error("  ✗ postscript failed");
      const reportPath = writeErrorReport(partition, "postscript", errorOutput, TEMP_DIR, apisDir);
      results.failed.push({ partition, step: "postscript", reportPath });
      continue;
    }

    results.success.push(partition);
    console.log(`  ✓ ${partition} → sailpoint/${gen.packageDir}/`);
  }

  // Cleanup
  if (!keepTmp) {
    console.log("\n[CLEANUP] Removing .sdk-build-tmp/ ...");
    fs.rmSync(TEMP_DIR, { recursive: true, force: true });
  }

  // Regenerate sailpoint/__init__.py to include all current *_v1 packages
  console.log("\n[INDEX] Regenerating sailpoint/__init__.py ...");
  generateInitPy();

  // Write error reports
  if (results.failed.length > 0) {
    const summaryPath = writeSummaryReport(results, apisDir);
    console.log(`\n[ERRORS] ${results.failed.length} partition(s) failed.`);
    console.log(`  Summary:  ${path.relative(SDK_ROOT, summaryPath)}`);
    console.log(`  Reports:  ${path.relative(SDK_ROOT, ERROR_DIR)}/`);
    console.log(`\n  Failed partitions:`);
    for (const { partition, step, reportPath } of results.failed) {
      console.log(`    ✗ ${partition} (${step}) → ${path.relative(SDK_ROOT, reportPath)}`);
    }
  }

  // Summary
  console.log("\n" + "=".repeat(60));
  console.log("BUILD SUMMARY");
  console.log("=".repeat(60));
  console.log(`  Success: ${results.success.length} / ${results.total}`);
  console.log(`  Failed:  ${results.failed.length} / ${results.total}`);

  if (results.failed.length > 0) {
    process.exit(1);
  }
}

main().catch(err => {
  console.error(`Unexpected error: ${err.message}`);
  process.exit(1);
});
