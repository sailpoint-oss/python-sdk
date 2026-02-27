# Build SDK and Run Validation Tests

## Overview

Build all API versions of the Python SDK from the OpenAPI specs and run the validation test suite. Use the same behavior as the GitHub action with default inputs: `api-specs-path=api-specs`, `skip-tests=false`.

## What to do

1. Run the build-and-validate script from the repository root:
   - **Command:** `./scripts/build-and-validate-sdk.sh`
   - Run from the workspace root directory.
2. Use default options (do not set `API_SPECS_PATH` or `SKIP_TESTS` unless the user asks otherwise).
3. Report the outcome: whether the build and validation tests completed successfully or any errors that occurred.

If the user provides extra instructions after the command (e.g. "skip tests" or a different api-specs path), follow those:

- To skip tests: run with `SKIP_TESTS=true ./scripts/build-and-validate-sdk.sh`
- Different api-specs path: run with `API_SPECS_PATH=<path> ./scripts/build-and-validate-sdk.sh`
