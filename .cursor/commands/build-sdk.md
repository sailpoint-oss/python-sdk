# Build SDK and Run Validation Tests

## Overview

Build all API versions of the Python SDK from the OpenAPI specs and run the validation test suite. Use the same behavior as the GitHub action with default inputs: `api-specs-path=api-specs`, `skip-tests=false`.

Works on Windows, macOS, and Linux (no shell required).

## What to do

1. Run the build-and-validate script from the repository root:
   - **Command:** `python scripts/build_and_validate_sdk.py`
   - Run from the workspace root directory.
2. Use default options (do not set `API_SPECS_PATH` or `SKIP_TESTS` unless the user asks otherwise).
3. Report the outcome: whether the build and validation tests completed successfully or any errors that occurred.

If the user provides extra instructions after the command (e.g. "skip tests" or a different api-specs path), follow those:

- To skip tests: set env and run, e.g. `SKIP_TESTS=true python scripts/build_and_validate_sdk.py` (Unix/macOS) or `set SKIP_TESTS=true && python scripts/build_and_validate_sdk.py` (Windows cmd) or `$env:SKIP_TESTS="true"; python scripts/build_and_validate_sdk.py` (Windows PowerShell).
- Different api-specs path: `API_SPECS_PATH=<path> python scripts/build_and_validate_sdk.py` (Unix/macOS) or set `API_SPECS_PATH` then run the Python command (Windows).
