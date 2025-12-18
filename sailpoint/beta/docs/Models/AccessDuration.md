---
id: beta-access-duration
title: AccessDuration
pagination_label: AccessDuration
sidebar_label: AccessDuration
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'AccessDuration', 'BetaAccessDuration'] 
slug: /tools/sdk/python/beta/models/access-duration
tags: ['SDK', 'Software Development Kit', 'AccessDuration', 'BetaAccessDuration']
---

# AccessDuration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **int** | The numeric value representing the amount of time, which is defined in the **timeUnit**. | [optional] 
**time_unit** |  **Enum** [  'HOURS',    'DAYS',    'WEEKS',    'MONTHS' ] | The unit of time that corresponds to the **value**. It defines the scale of the time period. | [optional] 
}

## Example

```python
from sailpoint.beta.models.access_duration import AccessDuration

access_duration = AccessDuration(
value=6,
time_unit='MONTHS'
)

```
[[Back to top]](#) 

