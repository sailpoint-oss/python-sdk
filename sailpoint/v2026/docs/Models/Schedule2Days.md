---
id: v2026-schedule2-days
title: Schedule2Days
pagination_label: Schedule2Days
sidebar_label: Schedule2Days
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Schedule2Days', 'V2026Schedule2Days'] 
slug: /tools/sdk/python/v2026/models/schedule2-days
tags: ['SDK', 'Software Development Kit', 'Schedule2Days', 'V2026Schedule2Days']
---

# Schedule2Days


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**SelectorType**](selector-type) |  | [required]
**values** | **[]str** | The selected values.  | [required]
**interval** | **int** | The selected interval for RANGE selectors.  | [optional] 
}

## Example

```python
from sailpoint.v2026.models.schedule2_days import Schedule2Days

schedule2_days = Schedule2Days(
type='LIST',
values=[MON, WED],
interval=3
)

```
[[Back to top]](#) 

