---
id: visibility-criteria
title: VisibilityCriteria
pagination_label: VisibilityCriteria
sidebar_label: VisibilityCriteria
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'VisibilityCriteria', 'VisibilityCriteria'] 
slug: /tools/sdk/python/data-segmentation/models/visibility-criteria
tags: ['SDK', 'Software Development Kit', 'VisibilityCriteria', 'VisibilityCriteria']
---

# VisibilityCriteria


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expression** | [**Expression**](expression) |  | [optional] 
}

## Example

```python
from sailpoint.data_segmentation.models.visibility_criteria import VisibilityCriteria

visibility_criteria = VisibilityCriteria(
expression=sailpoint.data_segmentation.models.expression.Expression(
                    operator = 'EQUALS', 
                    attribute = 'location', 
                    value = sailpoint.data_segmentation.models.value.Value(
                        type = 'STRING', ), 
                    children = [], )
)

```
[[Back to top]](#) 

