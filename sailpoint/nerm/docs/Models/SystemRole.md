---
id: system-role
title: SystemRole
pagination_label: SystemRole
sidebar_label: SystemRole
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'SystemRole', 'SystemRole'] 
slug: /tools/sdk/python//models/system-role
tags: ['SDK', 'Software Development Kit', 'SystemRole', 'SystemRole']
---

# SystemRole


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier for the object | [optional] [readonly] 
**uid** |  **Enum** [  'profile_contributor',    'profile_owner' ] | The user identifier for the object | [optional] [readonly] 
**name** |  **Enum** [  'Profile Contributor',    'Profile Owner' ] | The name of the role | [optional] 
}

## Example

```python
from sailpoint.nerm.models.system_role import SystemRole

system_role = SystemRole(
id='2e06b876-f456-473d-bd65-b6435e0b6b2d',
uid='profile_contributor',
name='Profile Contributor'
)

```
[[Back to top]](#) 

