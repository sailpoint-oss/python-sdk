---
id: role-profiles
title: RoleProfiles
pagination_label: RoleProfiles
sidebar_label: RoleProfiles
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'RoleProfiles', 'RoleProfiles'] 
slug: /tools/sdk/python//models/role-profiles
tags: ['SDK', 'Software Development Kit', 'RoleProfiles', 'RoleProfiles']
---

# RoleProfiles


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role_profiles** | [**[]RoleProfile**](role-profile) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.role_profiles import RoleProfiles

role_profiles = RoleProfiles(
role_profiles=[
                    sailpoint.nerm.models.role_profile.RoleProfile(
                        id = '', 
                        uid = '', 
                        role_id = '', 
                        profile_id = '', )
                    ]
)

```
[[Back to top]](#) 

