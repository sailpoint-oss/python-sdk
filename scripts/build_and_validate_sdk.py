#!/usr/bin/env python3
"""
Build the Python SDK and run validation tests.
Cross-platform (Windows, macOS, Linux).

Prerequisites: Node.js, Python 3.x, Java 17+ on PATH.
Optional env: API_SPECS_PATH (default api-specs), SKIP_TESTS (default false).

Usage (from repo root):
  python scripts/build_and_validate_sdk.py
  SKIP_TESTS=true python scripts/build_and_validate_sdk.py
  API_SPECS_PATH=other-specs python scripts/build_and_validate_sdk.py
"""

import os
import shutil
import subprocess
import sys
import urllib.request


def repo_root():
    return os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


def main():
    root = repo_root()
    os.chdir(root)

    api_specs_path = os.environ.get("API_SPECS_PATH", "api-specs")
    skip_tests = os.environ.get("SKIP_TESTS", "false").lower() in ("1", "true", "yes")

    print(f"Building SDK (api-specs-path={api_specs_path}, skip-tests={skip_tests})")

    # Download OpenAPI Generator if not present
    jar_path = os.path.join(root, "openapi-generator-cli.jar")
    if not os.path.isfile(jar_path):
        print("Downloading OpenAPI Generator...")
        url = "https://repo1.maven.org/maven2/org/openapitools/openapi-generator-cli/7.12.0/openapi-generator-cli-7.12.0.jar"
        urllib.request.urlretrieve(url, jar_path)

    # Prescript
    print("Running prescript...")
    idn_path = os.path.join(api_specs_path, "idn")
    subprocess.run(["node", "sdk-resources/prescript.js", idn_path], check=True, cwd=root)

    def build_sdk(name, spec, config, out_dir, spec_subdir="idn"):
        print(f"Building {name} SDK...")
        sailpoint_dir = os.path.join(root, "sailpoint", out_dir)
        if os.path.isdir(sailpoint_dir):
            shutil.rmtree(sailpoint_dir)
        spec_path = os.path.join(api_specs_path, spec_subdir, spec)
        subprocess.run(
            [
                "java", "-jar", jar_path, "generate",
                "-i", spec_path,
                "-g", "python", "-o", ".",
                "--global-property", "skipFormModel=false,apiDocs=true,modelDocs=true",
                "--config", f"sdk-resources/{config}",
            ],
            check=True,
            cwd=root,
        )
        subprocess.run(
            ["node", "sdk-resources/postscript.js", sailpoint_dir],
            check=True,
            cwd=root,
        )

    build_sdk("V3", "sailpoint-api.v3.yaml", "v3-config.yaml", "v3")
    build_sdk("Beta", "sailpoint-api.beta.yaml", "beta-config.yaml", "beta")
    build_sdk("V2024", "sailpoint-api.v2024.yaml", "v2024-config.yaml", "v2024")
    build_sdk("V2025", "sailpoint-api.v2025.yaml", "v2025-config.yaml", "v2025")
    build_sdk("V2026", "sailpoint-api.v2026.yaml", "v2026-config.yaml", "v2026")
    build_sdk("NERM", "openapi.yaml", "nerm-config.yaml", "nerm", spec_subdir="nerm")
    build_sdk("NERM V2025", os.path.join("v2025", "v2025.yaml"), "v2025-nerm-config.yaml", os.path.join("nerm", "v2025"), spec_subdir="nerm")

    # Install and test (use current Python / venv)
    pip_cmd = [sys.executable, "-m", "pip"]
    print("Installing dependencies and SDK...")
    subprocess.run(pip_cmd + ["install", "-r", "requirements.txt"], check=True, cwd=root)
    subprocess.run(pip_cmd + ["install", "-e", "."], check=True, cwd=root)

    if not skip_tests:
        print("Running validation tests...")
        subprocess.run(
            [sys.executable, "validation_test.py", "-v"],
            check=True,
            cwd=root,
        )
    else:
        print(f"Skipping tests (SKIP_TESTS={os.environ.get('SKIP_TESTS', '')})")

    print("Done.")


if __name__ == "__main__":
    main()
