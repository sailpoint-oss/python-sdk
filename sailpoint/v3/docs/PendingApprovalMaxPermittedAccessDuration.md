---
id: pending-approval-max-permitted-access-duration
title: PendingApprovalMaxPermittedAccessDuration
pagination_label: PendingApprovalMaxPermittedAccessDuration
sidebar_label: PendingApprovalMaxPermittedAccessDuration
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'PendingApprovalMaxPermittedAccessDuration', 'PendingApprovalMaxPermittedAccessDuration'] 
slug: /tools/sdk/python/v3/models/pending-approval-max-permitted-access-duration
tags: ['SDK', 'Software Development Kit', 'PendingApprovalMaxPermittedAccessDuration', 'PendingApprovalMaxPermittedAccessDuration']
---

# PendingApprovalMaxPermittedAccessDuration

The maximum duration for which the access is permitted.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **int** | The numeric value of the duration. | [optional] 
**time_unit** |  **Enum** [  'HOURS',    'DAYS',    'WEEKS',    'MONTHS' ] | The time unit for the duration. | [optional] 
}

## Example

```python
from sailpoint.v3.models.pending_approval_max_permitted_access_duration import PendingApprovalMaxPermittedAccessDuration

pending_approval_max_permitted_access_duration = PendingApprovalMaxPermittedAccessDuration(
value=5,
time_unit='DAYS'
)

```
[[Back to top]](#) 

