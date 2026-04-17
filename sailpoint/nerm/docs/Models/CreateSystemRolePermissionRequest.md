---
id: create-system-role-permission-request
title: CreateSystemRolePermissionRequest
pagination_label: CreateSystemRolePermissionRequest
sidebar_label: CreateSystemRolePermissionRequest
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'CreateSystemRolePermissionRequest', 'CreateSystemRolePermissionRequest'] 
slug: /tools/sdk/python//models/create-system-role-permission-request
tags: ['SDK', 'Software Development Kit', 'CreateSystemRolePermissionRequest', 'CreateSystemRolePermissionRequest']
---

# CreateSystemRolePermissionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**system_role_permission** | [**SystemRolePermission1**](system-role-permission1) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.create_system_role_permission_request import CreateSystemRolePermissionRequest

create_system_role_permission_request = CreateSystemRolePermissionRequest(
system_role_permission=sailpoint.nerm.models.system_role_permission_1.SystemRolePermission_1(
                    system_role_id = 'ef5d413f-ba18-49e6-9a72-bb115aa133ff', 
                    subject_id = 'db3d85ef-c324-458b-b206-58debaa96419', 
                    value = 1, 
                    subject = 0, )
)

```
[[Back to top]](#) 

