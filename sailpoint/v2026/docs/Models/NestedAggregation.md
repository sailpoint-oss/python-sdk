---
id: v2026-nested-aggregation
title: NestedAggregation
pagination_label: NestedAggregation
sidebar_label: NestedAggregation
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'NestedAggregation', 'V2026NestedAggregation'] 
slug: /tools/sdk/python/v2026/models/nested-aggregation
tags: ['SDK', 'Software Development Kit', 'NestedAggregation', 'V2026NestedAggregation']
---

# NestedAggregation

The nested aggregation object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the nested aggregate to be included in the result. | [required]
**type** | **str** | The type of the nested object. | [required]
}

## Example

```python
from sailpoint.v2026.models.nested_aggregation import NestedAggregation

nested_aggregation = NestedAggregation(
name='id',
type='access'
)

```
[[Back to top]](#) 

