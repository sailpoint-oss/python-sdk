---
id: selector
title: Selector
pagination_label: Selector
sidebar_label: Selector
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Selector', 'Selector'] 
slug: /tools/sdk/python/gov-certification/models/selector
tags: ['SDK', 'Software Development Kit', 'Selector', 'Selector']
---

# Selector


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** |  **Enum** [  'LIST',    'RANGE' ] | The type of a schedule selector - list or range. | [optional] 
**values** | **[]str** | A list of a selector values. | [optional] 
**interval** | **int** | Interval of the schedule selector | [optional] 
}

## Example

```python
from sailpoint.gov_certification.models.selector import Selector

selector = Selector(
type='LIST',
values=["1","2","3"],
interval=2
)

```
[[Back to top]](#) 

