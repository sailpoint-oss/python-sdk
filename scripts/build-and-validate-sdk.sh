#!/usr/bin/env bash
# Build the Python SDK and run validation tests.
# Uses default inputs: api-specs-path=api-specs, skip-tests=false.
#
# Prerequisites: Node.js, Python 3.x, Java 17+ on PATH.
# Optional: set API_SPECS_PATH to override api-specs location.

set -e

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

# Use project venv if present (so pip/python are available for install and tests)
if [ -f "$REPO_ROOT/.venv/bin/activate" ]; then
  echo "Activating virtual environment..."
  source "$REPO_ROOT/.venv/bin/activate"
fi

API_SPECS_PATH="${API_SPECS_PATH:-api-specs}"
SKIP_TESTS="${SKIP_TESTS:-false}"

echo "Building SDK (api-specs-path=$API_SPECS_PATH, skip-tests=$SKIP_TESTS)"

# Download OpenAPI Generator if not present
if [ ! -f openapi-generator-cli.jar ]; then
  echo "Downloading OpenAPI Generator..."
  wget -q https://repo1.maven.org/maven2/org/openapitools/openapi-generator-cli/7.12.0/openapi-generator-cli-7.12.0.jar -O openapi-generator-cli.jar
fi

# Prescript
echo "Running prescript..."
node sdk-resources/prescript.js "$API_SPECS_PATH/idn"

build_sdk() {
  local name=$1
  local spec=$2
  local config=$3
  local out_dir=$4
  echo "Building $name SDK..."
  rm -rf "./sailpoint/$out_dir"
  java -jar openapi-generator-cli.jar generate \
    -i "$API_SPECS_PATH/idn/$spec" \
    -g python -o . \
    --global-property skipFormModel=false,apiDocs=true,modelDocs=true \
    --config "sdk-resources/$config"
  node sdk-resources/postscript.js "./sailpoint/$out_dir"
}

build_sdk "V3"      "sailpoint-api.v3.yaml"    "v3-config.yaml"    "v3"
build_sdk "Beta"    "sailpoint-api.beta.yaml"  "beta-config.yaml"  "beta"
build_sdk "V2024"   "sailpoint-api.v2024.yaml" "v2024-config.yaml" "v2024"
build_sdk "V2025"   "sailpoint-api.v2025.yaml" "v2025-config.yaml" "v2025"
build_sdk "V2026"   "sailpoint-api.v2026.yaml" "v2026-config.yaml" "v2026"

# Install and test
echo "Installing dependencies and SDK..."
pip install -r requirements.txt
pip install -e .

if [ "$SKIP_TESTS" != "true" ]; then
  echo "Running validation tests..."
  python validation_test.py -v
else
  echo "Skipping tests (SKIP_TESTS=$SKIP_TESTS)"
fi

echo "Done."
