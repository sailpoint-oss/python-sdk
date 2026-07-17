---
id: dimension-criteria-key
title: DimensionCriteriaKey
pagination_label: DimensionCriteriaKey
sidebar_label: DimensionCriteriaKey
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'DimensionCriteriaKey', 'DimensionCriteriaKey'] 
slug: /tools/sdk/python/dimensions/models/dimension-criteria-key
tags: ['SDK', 'Software Development Kit', 'DimensionCriteriaKey', 'DimensionCriteriaKey']
---

# DimensionCriteriaKey

Refers to a specific Identity attribute used in Dimension membership criteria.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **DimensionCriteriaKeyType** |  | [required]
**var_property** | **str** | The name of the identity attribute to which the associated criteria applies. | [required]
}

## Example

```python
from sailpoint.dimensions.models.dimension_criteria_key import DimensionCriteriaKey

dimension_criteria_key = DimensionCriteriaKey(
type='IDENTITY',
var_property='attribute.email'
)

```
[[Back to top]](#) 

