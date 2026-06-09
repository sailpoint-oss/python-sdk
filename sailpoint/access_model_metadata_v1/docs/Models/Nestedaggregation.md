---
id: nestedaggregation
title: Nestedaggregation
pagination_label: Nestedaggregation
sidebar_label: Nestedaggregation
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Nestedaggregation', 'Nestedaggregation'] 
slug: /tools/sdk/python/v1/models/nestedaggregation
tags: ['SDK', 'Software Development Kit', 'Nestedaggregation', 'Nestedaggregation']
---

# Nestedaggregation

The nested aggregation object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the nested aggregate to be included in the result. | [required]
**type** | **str** | The type of the nested object. | [required]
}

## Example

```python
from sailpoint.access_model_metadata_v1.models.nestedaggregation import Nestedaggregation

nestedaggregation = Nestedaggregation(
name='id',
type='access'
)

```
[[Back to top]](#) 

