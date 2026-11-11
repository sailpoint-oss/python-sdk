---
id: reminderescalationtarget
title: Reminderescalationtarget
pagination_label: Reminderescalationtarget
sidebar_label: Reminderescalationtarget
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Reminderescalationtarget', 'Reminderescalationtarget'] 
slug: /tools/sdk/python/reminder-escalations/models/reminderescalationtarget
tags: ['SDK', 'Software Development Kit', 'Reminderescalationtarget', 'Reminderescalationtarget']
---

# Reminderescalationtarget

Escalation recipient. `identityId` is required for every `targetType` except `MANAGER_OF`, where it is optional.  * `MANAGER_OF` without `identityId` resolves the manager of each current assignee. * `MANAGER_OF` with `identityId` resolves the manager of that identity. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_type** |  **Enum** [  'MANAGER_OF',    'IDENTITY',    'GOVERNANCE_GROUP',    'ENTITLEMENT_OWNER',    'SOURCE_OWNER' ] | Kind of recipient this target resolves to. | [required]
**identity_id** | **str** | Identity the target applies to. Empty for a dynamic `MANAGER_OF` target. | [optional] [default to '']
}

## Example

```python
from sailpoint.reminder_escalations.models.reminderescalationtarget import Reminderescalationtarget

reminderescalationtarget = Reminderescalationtarget(
target_type='MANAGER_OF',
identity_id=''
)

```
[[Back to top]](#) 

