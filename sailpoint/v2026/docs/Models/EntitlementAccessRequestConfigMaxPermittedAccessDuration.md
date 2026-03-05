---
id: v2026-entitlement-access-request-config-max-permitted-access-duration
title: EntitlementAccessRequestConfigMaxPermittedAccessDuration
pagination_label: EntitlementAccessRequestConfigMaxPermittedAccessDuration
sidebar_label: EntitlementAccessRequestConfigMaxPermittedAccessDuration
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'EntitlementAccessRequestConfigMaxPermittedAccessDuration', 'V2026EntitlementAccessRequestConfigMaxPermittedAccessDuration'] 
slug: /tools/sdk/python/v2026/models/entitlement-access-request-config-max-permitted-access-duration
tags: ['SDK', 'Software Development Kit', 'EntitlementAccessRequestConfigMaxPermittedAccessDuration', 'V2026EntitlementAccessRequestConfigMaxPermittedAccessDuration']
---

# EntitlementAccessRequestConfigMaxPermittedAccessDuration

The maximum duration for which the access is permitted.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **int** | The numeric value of the duration. | [optional] 
**time_unit** |  **Enum** [  'HOURS',    'DAYS',    'WEEKS',    'MONTHS' ] | The time unit for the duration. | [optional] 
}

## Example

```python
from sailpoint.v2026.models.entitlement_access_request_config_max_permitted_access_duration import EntitlementAccessRequestConfigMaxPermittedAccessDuration

entitlement_access_request_config_max_permitted_access_duration = EntitlementAccessRequestConfigMaxPermittedAccessDuration(
value=5,
time_unit='DAYS'
)

```
[[Back to top]](#) 

