---
id: range
title: Range
pagination_label: Range
sidebar_label: Range
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Range', 'Range'] 
slug: /tools/sdk/python/v1/models/range
tags: ['SDK', 'Software Development Kit', 'Range', 'Range']
---

# Range

The range of values to be filtered.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lower** | [**Bound**](bound) |  | [optional] 
**upper** | [**Bound**](bound) |  | [optional] 
}

## Example

```python
from sailpoint.saved_search_v1.models.range import Range

range = Range(
lower=sailpoint.saved_search_v1.models.bound.bound(
                    value = '1', 
                    inclusive = False, ),
upper=sailpoint.saved_search_v1.models.bound.bound(
                    value = '1', 
                    inclusive = False, )
)

```
[[Back to top]](#) 

