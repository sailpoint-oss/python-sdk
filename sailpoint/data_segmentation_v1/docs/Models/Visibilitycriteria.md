---
id: visibilitycriteria
title: Visibilitycriteria
pagination_label: Visibilitycriteria
sidebar_label: Visibilitycriteria
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Visibilitycriteria', 'Visibilitycriteria'] 
slug: /tools/sdk/python/v1/models/visibilitycriteria
tags: ['SDK', 'Software Development Kit', 'Visibilitycriteria', 'Visibilitycriteria']
---

# Visibilitycriteria


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expression** | [**Expression**](expression) |  | [optional] 
}

## Example

```python
from sailpoint.data_segmentation_v1.models.visibilitycriteria import Visibilitycriteria

visibilitycriteria = Visibilitycriteria(
expression=sailpoint.data_segmentation_v1.models.expression.Expression(
                    operator = 'EQUALS', 
                    attribute = 'location', 
                    value = sailpoint.data_segmentation_v1.models.value.Value(
                        type = 'STRING', ), 
                    children = [], )
)

```
[[Back to top]](#) 

