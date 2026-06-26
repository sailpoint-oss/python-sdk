.PHONY: specs
specs:
	git clone https://github.com/sailpoint-oss/api-specs.git api-specs

.PHONY: clean-specs
clean-specs:
	rm -rf ./api-specs

APIS_DIR ?= api-specs/idn/src/main/yaml/apis

.PHONY: build
build:
	node sdk-resources/build-versioned-sdk.js $(APIS_DIR)

.PHONY: build-partition
build-partition:
	node sdk-resources/build-versioned-sdk.js $(APIS_DIR) --partition $(PARTITION)

.PHONY: test
test:
	pip install -r requirements.txt
	pip install -e .
	python validation_test.py -v
