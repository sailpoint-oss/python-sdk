.PHONY: specs
specs:
	git clone https://github.com/sailpoint-oss/api-specs.git api-specs

.PHONY: clean-specs
clean-specs:
	rm -rf ./api-specs

APIS_DIR ?= api-specs/idn/apis

.PHONY: build
build:
	node sdk-resources/build-versioned-sdk.js $(APIS_DIR)

.PHONY: build-partition
build-partition:
	node sdk-resources/build-versioned-sdk.js $(APIS_DIR) --partition $(PARTITION)

# Builds only sailpoint/generic from sdk-resources/generic-api.yaml.
# Needs no api-specs checkout.
.PHONY: build-generic
build-generic:
	node sdk-resources/build-versioned-sdk.js --generic-only

.PHONY: test
test:
	pip install -r requirements.txt
	pip install -e .
	python generic_test.py -v
	python validation_test.py -v
