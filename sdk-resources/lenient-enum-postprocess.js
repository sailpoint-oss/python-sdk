/**
 * Post-process generated model files to use Union[EnumType, str] for enum refs,
 * so that unknown enum values from the API are accepted as plain strings
 * (lenient enum validation).
 *
 * Usage: node lenient-enum-postprocess.js <sdk-path>
 * Example: node lenient-enum-postprocess.js ./sailpoint/v2025
 */

const fs = require("fs").promises;
const path = require("path");

const ENUM_CLASS_RE = /^\s*class\s+(\w+)\s*\([^)]*Enum\)/m;
const MODELS_SUBDIR = "models";

function extractEnumClassNames(content) {
  const names = new Set();
  let m;
  const re = new RegExp(ENUM_CLASS_RE.source, "gm");
  while ((m = re.exec(content)) !== null) {
    names.add(m[1]);
  }
  return names;
}

function isEnumFile(content) {
  return ENUM_CLASS_RE.test(content);
}

function applyLenientEnumToContent(content, enumNames) {
  if (enumNames.size === 0) return { content, changed: false };
  let text = content;
  let changed = false;

  for (const name of enumNames) {
    // Optional[EnumType] -> Optional[Union[EnumType, str]]
    const optRe = new RegExp(`Optional\\[${name}\\]`, "g");
    if (optRe.test(text)) {
      text = text.replace(optRe, `Optional[Union[${name}, str]]`);
      changed = true;
    }

    // List[EnumType] -> List[Union[EnumType, str]]
    const listRe = new RegExp(`List\\[${name}\\]`, "g");
    if (listRe.test(text)) {
      text = text.replace(listRe, `List[Union[${name}, str]]`);
      changed = true;
    }

    // , EnumType] -> , Union[EnumType, str]] (e.g. Dict[str, E], Annotated[E, ...])
    const commaRe = new RegExp(`, ${name}\\]`, "g");
    if (commaRe.test(text)) {
      text = text.replace(commaRe, `, Union[${name}, str]]`);
      changed = true;
    }

    // : EnumType = -> : Union[EnumType, str] = (required field type annotation)
    const annotRe = new RegExp(`: ${name} =`, "g");
    if (annotRe.test(text)) {
      text = text.replace(annotRe, `: Union[${name}, str] =`);
      changed = true;
    }
  }

  if (changed) {
    // Ensure Union is in a typing import line
    if (!/\bUnion\b/.test(text) || !/from typing import [^\n]*\bUnion\b/.test(text)) {
      const typingImportRe = /from typing import ([\w, ]+)/;
      const firstMatch = text.match(typingImportRe);
      if (firstMatch && !firstMatch[1].includes("Union")) {
        text = text.replace(typingImportRe, (match, imports) =>
          `from typing import ${imports.trim().replace(/\s*,?\s*$/, "")}, Union`
        );
      }
    }
  }

  return { content: text, changed };
}

async function main() {
  const sdkPath = process.argv[2];
  if (!sdkPath) {
    console.error("Usage: node lenient-enum-postprocess.js <sdk-path>");
    process.exit(1);
  }

  const modelsDir = path.join(path.resolve(sdkPath), MODELS_SUBDIR);
  let stat;
  try {
    stat = await fs.stat(modelsDir);
  } catch (e) {
    console.error(`Models directory not found: ${modelsDir}`);
    process.exit(1);
  }
  if (!stat.isDirectory()) {
    console.error(`Not a directory: ${modelsDir}`);
    process.exit(1);
  }

  const files = await fs.readdir(modelsDir);
  const pyFiles = files.filter((f) => f.endsWith(".py") && f !== "__init__.py");

  const enumNames = new Set();
  const enumFiles = new Set();

  for (const file of pyFiles) {
    const filePath = path.join(modelsDir, file);
    const content = await fs.readFile(filePath, "utf-8");
    const names = extractEnumClassNames(content);
    if (names.size > 0) {
      enumFiles.add(file);
      names.forEach((n) => enumNames.add(n));
    }
  }

  let fixCount = 0;
  for (const file of pyFiles) {
    if (enumFiles.has(file)) continue;
    const filePath = path.join(modelsDir, file);
    const content = await fs.readFile(filePath, "utf-8");
    const { content: newContent, changed } = applyLenientEnumToContent(content, enumNames);
    if (changed) {
      await fs.writeFile(filePath, newContent);
      fixCount += 1;
    }
  }

  console.log(`Lenient enums: updated ${fixCount} model files (${enumNames.size} enum types).`);
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
