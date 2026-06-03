---
id: v2026-schedule2-hours
title: Schedule2Hours
pagination_label: Schedule2Hours
sidebar_label: Schedule2Hours
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Schedule2Hours', 'V2026Schedule2Hours'] 
slug: /tools/sdk/python/v2026/models/schedule2-hours
tags: ['SDK', 'Software Development Kit', 'Schedule2Hours', 'V2026Schedule2Hours']
---

# Schedule2Hours


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**SelectorType**](selector-type) |  | [required]
**values** | **[]str** | The selected values.  | [required]
**interval** | **int** | The selected interval for RANGE selectors.  | [optional] 
}

## Example

```python
from sailpoint.v2026.models.schedule2_hours import Schedule2Hours

schedule2_hours = Schedule2Hours(
type='LIST',
values=[MON, WED],
interval=3
)

```
[[Back to top]](#) 

