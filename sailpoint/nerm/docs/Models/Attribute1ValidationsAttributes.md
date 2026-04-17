---
id: attribute1-validations-attributes
title: Attribute1ValidationsAttributes
pagination_label: Attribute1ValidationsAttributes
sidebar_label: Attribute1ValidationsAttributes
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Attribute1ValidationsAttributes', 'Attribute1ValidationsAttributes'] 
slug: /tools/sdk/python//models/attribute1-validations-attributes
tags: ['SDK', 'Software Development Kit', 'Attribute1ValidationsAttributes', 'Attribute1ValidationsAttributes']
---

# Attribute1ValidationsAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**validation_method** |  **Enum** [  'required',    'unique',    'date_format',    'days',    'characters',    'extension',    'numericality',    'email_format',    'custom_format',    'no_special_chars' ] | The type of validation to be applied | [optional] 
**value** | **str** | The value of the validator | [optional] 
**destroy** | **bool** | If the validator should be removed | [optional] 
}

## Example

```python
from sailpoint.nerm.models.attribute1_validations_attributes import Attribute1ValidationsAttributes

attribute1_validations_attributes = Attribute1ValidationsAttributes(
validation_method='required',
value='mm-dd-yyyy',
destroy=False
)

```
[[Back to top]](#) 

