---
id: accessprofilev2-privilege-level
title: Accessprofilev2PrivilegeLevel
pagination_label: Accessprofilev2PrivilegeLevel
sidebar_label: Accessprofilev2PrivilegeLevel
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Accessprofilev2PrivilegeLevel', 'Accessprofilev2PrivilegeLevel'] 
slug: /tools/sdk/python/access-profiles/models/accessprofilev2-privilege-level
tags: ['SDK', 'Software Development Kit', 'Accessprofilev2PrivilegeLevel', 'Accessprofilev2PrivilegeLevel']
---

# Accessprofilev2PrivilegeLevel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effective** |  **Enum** [  'NONE',    'LOW',    'MEDIUM',    'HIGH',    'UNDETERMINED' ] | Effective privilege level of the access profile, derived from the highest privilege level of the entitlements it contains. `UNDETERMINED` indicates the level could not be calculated. | [optional] 
}

## Example

```python
from sailpoint.access_profiles.models.accessprofilev2_privilege_level import Accessprofilev2PrivilegeLevel

accessprofilev2_privilege_level = Accessprofilev2PrivilegeLevel(
effective='MEDIUM'
)

```
[[Back to top]](#) 

