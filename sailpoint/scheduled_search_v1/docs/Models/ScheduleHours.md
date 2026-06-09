---
id: schedule-hours
title: ScheduleHours
pagination_label: ScheduleHours
sidebar_label: ScheduleHours
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'ScheduleHours', 'ScheduleHours'] 
slug: /tools/sdk/python/v1/models/schedule-hours
tags: ['SDK', 'Software Development Kit', 'ScheduleHours', 'ScheduleHours']
---

# ScheduleHours


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**Selectortype**](selectortype) |  | [required]
**values** | **[]str** | The selected values.  | [required]
**interval** | **int** | The selected interval for RANGE selectors.  | [optional] 
}

## Example

```python
from sailpoint.scheduled_search_v1.models.schedule_hours import ScheduleHours

schedule_hours = ScheduleHours(
type='LIST',
values=[MON, WED],
interval=3
)

```
[[Back to top]](#) 

