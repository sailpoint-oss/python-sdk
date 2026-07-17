---
id: attribute-mappings-all-of-transform-definition-attributes-input
title: AttributeMappingsAllOfTransformDefinitionAttributesInput
pagination_label: AttributeMappingsAllOfTransformDefinitionAttributesInput
sidebar_label: AttributeMappingsAllOfTransformDefinitionAttributesInput
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'AttributeMappingsAllOfTransformDefinitionAttributesInput', 'AttributeMappingsAllOfTransformDefinitionAttributesInput'] 
slug: /tools/sdk/python/machine-account-mappings/models/attribute-mappings-all-of-transform-definition-attributes-input
tags: ['SDK', 'Software Development Kit', 'AttributeMappingsAllOfTransformDefinitionAttributesInput', 'AttributeMappingsAllOfTransformDefinitionAttributesInput']
---

# AttributeMappingsAllOfTransformDefinitionAttributesInput

Input Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The Type of Attribute | [optional] 
**attributes** | [**AttributeMappingsAllOfTransformDefinitionAttributesInputAttributes**](attribute-mappings-all-of-transform-definition-attributes-input-attributes) |  | [optional] 
}

## Example

```python
from sailpoint.machine_account_mappings.models.attribute_mappings_all_of_transform_definition_attributes_input import AttributeMappingsAllOfTransformDefinitionAttributesInput

attribute_mappings_all_of_transform_definition_attributes_input = AttributeMappingsAllOfTransformDefinitionAttributesInput(
type='accountAttribute',
attributes=sailpoint.machine_account_mappings.models.attribute_mappings_all_of_transform_definition_attributes_input_attributes.AttributeMappings_allOf_transformDefinition_attributes_input_attributes(
                    attribute_name = 'givenName', 
                    source_name = 'delimited-src', 
                    name = '8d3e0094e99445de98eef6c75e25jc04', )
)

```
[[Back to top]](#) 

