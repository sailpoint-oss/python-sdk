---
id: source-entitlement-access-request-config-max-permitted-access-duration
title: SourceEntitlementAccessRequestConfigMaxPermittedAccessDuration
pagination_label: SourceEntitlementAccessRequestConfigMaxPermittedAccessDuration
sidebar_label: SourceEntitlementAccessRequestConfigMaxPermittedAccessDuration
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'SourceEntitlementAccessRequestConfigMaxPermittedAccessDuration', 'SourceEntitlementAccessRequestConfigMaxPermittedAccessDuration'] 
slug: /tools/sdk/python/sources/models/source-entitlement-access-request-config-max-permitted-access-duration
tags: ['SDK', 'Software Development Kit', 'SourceEntitlementAccessRequestConfigMaxPermittedAccessDuration', 'SourceEntitlementAccessRequestConfigMaxPermittedAccessDuration']
---

# SourceEntitlementAccessRequestConfigMaxPermittedAccessDuration

The maximum duration for which the access is permitted.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **int** | The numeric value of the duration. | [optional] 
**time_unit** |  **Enum** [  'HOURS',    'DAYS',    'WEEKS',    'MONTHS' ] | The time unit for the duration. | [optional] 
}

## Example

```python
from sailpoint.sources.models.source_entitlement_access_request_config_max_permitted_access_duration import SourceEntitlementAccessRequestConfigMaxPermittedAccessDuration

source_entitlement_access_request_config_max_permitted_access_duration = SourceEntitlementAccessRequestConfigMaxPermittedAccessDuration(
value=5,
time_unit='DAYS'
)

```
[[Back to top]](#) 

