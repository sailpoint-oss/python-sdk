---
id: validation-errors
title: ValidationErrors
pagination_label: ValidationErrors
sidebar_label: ValidationErrors
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'ValidationErrors', 'ValidationErrors'] 
slug: /tools/sdk/python//models/validation-errors
tags: ['SDK', 'Software Development Kit', 'ValidationErrors', 'ValidationErrors']
---

# ValidationErrors


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **object** |  | [optional] 
**errors** | **object** |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.validation_errors import ValidationErrors

validation_errors = ValidationErrors(
error=The <object> failed to create/update,
errors={attribute=can't be blank}
)

```
[[Back to top]](#) 

