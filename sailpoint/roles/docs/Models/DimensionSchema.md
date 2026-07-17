---
id: dimension-schema
title: DimensionSchema
pagination_label: DimensionSchema
sidebar_label: DimensionSchema
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'DimensionSchema', 'DimensionSchema'] 
slug: /tools/sdk/python/roles/models/dimension-schema
tags: ['SDK', 'Software Development Kit', 'DimensionSchema', 'DimensionSchema']
---

# DimensionSchema

Contains a list of dimension attributes. Required only for Dynamic Roles

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dimension_attributes** | [**[]DimensionAttribute**](dimension-attribute) |  | [optional] 
}

## Example

```python
from sailpoint.roles.models.dimension_schema import DimensionSchema

dimension_schema = DimensionSchema(
dimension_attributes=[
                    sailpoint.roles.models.dimension_attribute.DimensionAttribute(
                        name = 'city', 
                        display_name = 'City', 
                        derived = True, )
                    ]
)

```
[[Back to top]](#) 

