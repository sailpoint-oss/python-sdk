---
id: dimensionschema
title: Dimensionschema
pagination_label: Dimensionschema
sidebar_label: Dimensionschema
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Dimensionschema', 'Dimensionschema'] 
slug: /tools/sdk/python/v1/models/dimensionschema
tags: ['SDK', 'Software Development Kit', 'Dimensionschema', 'Dimensionschema']
---

# Dimensionschema

Contains a list of dimension attributes. Required only for Dynamic Roles

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dimension_attributes** | [**[]Dimensionattribute**](dimensionattribute) |  | [optional] 
}

## Example

```python
from sailpoint.roles_v1.models.dimensionschema import Dimensionschema

dimensionschema = Dimensionschema(
dimension_attributes=[
                    sailpoint.roles_v1.models.dimensionattribute.dimensionattribute(
                        name = 'city', 
                        display_name = 'City', 
                        derived = True, )
                    ]
)

```
[[Back to top]](#) 

