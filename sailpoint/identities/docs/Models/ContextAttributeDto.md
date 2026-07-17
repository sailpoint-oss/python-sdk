---
id: context-attribute-dto
title: ContextAttributeDto
pagination_label: ContextAttributeDto
sidebar_label: ContextAttributeDto
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'ContextAttributeDto', 'ContextAttributeDto'] 
slug: /tools/sdk/python/identities/models/context-attribute-dto
tags: ['SDK', 'Software Development Kit', 'ContextAttributeDto', 'ContextAttributeDto']
---

# ContextAttributeDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute** | **str** | The name of the attribute | [optional] 
**value** | [**ContextAttributeDtoValue**](context-attribute-dto-value) |  | [optional] 
**derived** | **bool** | True if the attribute was derived. | [optional] [default to False]
}

## Example

```python
from sailpoint.identities.models.context_attribute_dto import ContextAttributeDto

context_attribute_dto = ContextAttributeDto(
attribute='location',
value=Austin,
derived=False
)

```
[[Back to top]](#) 

