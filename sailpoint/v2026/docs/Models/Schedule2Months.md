---
id: v2026-schedule2-months
title: Schedule2Months
pagination_label: Schedule2Months
sidebar_label: Schedule2Months
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Schedule2Months', 'V2026Schedule2Months'] 
slug: /tools/sdk/python/v2026/models/schedule2-months
tags: ['SDK', 'Software Development Kit', 'Schedule2Months', 'V2026Schedule2Months']
---

# Schedule2Months


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**SelectorType**](selector-type) |  | [required]
**values** | **[]str** | The selected values.  | [required]
**interval** | **int** | The selected interval for RANGE selectors.  | [optional] 
}

## Example

```python
from sailpoint.v2026.models.schedule2_months import Schedule2Months

schedule2_months = Schedule2Months(
type='LIST',
values=[MON, WED],
interval=3
)

```
[[Back to top]](#) 

