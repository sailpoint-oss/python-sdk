---
id: v2026-dimension-criteria-key
title: DimensionCriteriaKey
pagination_label: DimensionCriteriaKey
sidebar_label: DimensionCriteriaKey
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'DimensionCriteriaKey', 'V2026DimensionCriteriaKey'] 
slug: /tools/sdk/python/v2026/models/dimension-criteria-key
tags: ['SDK', 'Software Development Kit', 'DimensionCriteriaKey', 'V2026DimensionCriteriaKey']
---

# DimensionCriteriaKey

Refers to a specific Identity attribute used in Dimension membership criteria.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**DimensionCriteriaKeyType**](dimension-criteria-key-type) |  | [required]
**var_property** | **str** | The name of the identity attribute to which the associated criteria applies. | [required]
}

## Example

```python
from sailpoint.v2026.models.dimension_criteria_key import DimensionCriteriaKey

dimension_criteria_key = DimensionCriteriaKey(
type='IDENTITY',
var_property='attribute.email'
)

```
[[Back to top]](#) 

