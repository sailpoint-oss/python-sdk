---
id: system-role-permission1
title: SystemRolePermission1
pagination_label: SystemRolePermission1
sidebar_label: SystemRolePermission1
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'SystemRolePermission1', 'SystemRolePermission1'] 
slug: /tools/sdk/python//models/system-role-permission1
tags: ['SDK', 'Software Development Kit', 'SystemRolePermission1', 'SystemRolePermission1']
---

# SystemRolePermission1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**system_role_id** | **str** | The id of the system role | [optional] 
**subject_id** | **str** | The ID of the object that the permission is giving access to | [optional] 
**value** |  **Enum** [  1,    2,    3,    4,    5,    6,    7 ] | The permissions level of access | [optional] 
**subject** |  **Enum** [  0,    2,    14 ] | The type of permission | [optional] 
}

## Example

```python
from sailpoint.nerm.models.system_role_permission1 import SystemRolePermission1

system_role_permission1 = SystemRolePermission1(
system_role_id='ef5d413f-ba18-49e6-9a72-bb115aa133ff',
subject_id='db3d85ef-c324-458b-b206-58debaa96419',
value=1,
subject=0
)

```
[[Back to top]](#) 

