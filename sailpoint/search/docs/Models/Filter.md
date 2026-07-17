---
id: filter
title: Filter
pagination_label: Filter
sidebar_label: Filter
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Filter', 'Filter'] 
slug: /tools/sdk/python/search/models/filter
tags: ['SDK', 'Software Development Kit', 'Filter', 'Filter']
---

# Filter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **FilterType** |  | [optional] 
**range** | [**Range**](range) |  | [optional] 
**terms** | **[]str** | The terms to be filtered. | [optional] 
**exclude** | **bool** | Indicates if the filter excludes results. | [optional] [default to False]
}

## Example

```python
from sailpoint.search.models.filter import Filter

filter = Filter(
type='RANGE',
range=sailpoint.search.models.range.Range(
                    lower = sailpoint.search.models.bound.Bound(
                        value = '1', 
                        inclusive = False, ), 
                    upper = sailpoint.search.models.bound.Bound(
                        value = '1', 
                        inclusive = False, ), ),
terms=[
                    'account_count'
                    ],
exclude=False
)

```
[[Back to top]](#) 

