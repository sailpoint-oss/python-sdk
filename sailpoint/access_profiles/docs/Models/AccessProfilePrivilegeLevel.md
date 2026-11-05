---
id: access-profile-privilege-level
title: AccessProfilePrivilegeLevel
pagination_label: AccessProfilePrivilegeLevel
sidebar_label: AccessProfilePrivilegeLevel
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'AccessProfilePrivilegeLevel', 'AccessProfilePrivilegeLevel'] 
slug: /tools/sdk/python/access-profiles/models/access-profile-privilege-level
tags: ['SDK', 'Software Development Kit', 'AccessProfilePrivilegeLevel', 'AccessProfilePrivilegeLevel']
---

# AccessProfilePrivilegeLevel

Effective privilege level calculated for the access profile.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effective** |  **Enum** [  'NONE',    'LOW',    'MEDIUM',    'HIGH',    'UNDETERMINED' ] | Effective privilege level of the access profile, derived from the highest privilege level of the entitlements it contains. `UNDETERMINED` indicates the level could not be calculated. | [optional] 
}

## Example

```python
from sailpoint.access_profiles.models.access_profile_privilege_level import AccessProfilePrivilegeLevel

access_profile_privilege_level = AccessProfilePrivilegeLevel(
effective='MEDIUM'
)

```
[[Back to top]](#) 

