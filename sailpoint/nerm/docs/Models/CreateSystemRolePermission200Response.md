---
id: create-system-role-permission200-response
title: CreateSystemRolePermission200Response
pagination_label: CreateSystemRolePermission200Response
sidebar_label: CreateSystemRolePermission200Response
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'CreateSystemRolePermission200Response', 'CreateSystemRolePermission200Response'] 
slug: /tools/sdk/python//models/create-system-role-permission200-response
tags: ['SDK', 'Software Development Kit', 'CreateSystemRolePermission200Response', 'CreateSystemRolePermission200Response']
---

# CreateSystemRolePermission200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**system_role_permission** | [**SystemRolePermission**](system-role-permission) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.create_system_role_permission200_response import CreateSystemRolePermission200Response

create_system_role_permission200_response = CreateSystemRolePermission200Response(
system_role_permission=sailpoint.nerm.models.system_role_permission.SystemRolePermission(
                    id = '2e06b876-f456-473d-bd65-b6435e0b6b2d', 
                    system_role_id = 'ef5d413f-ba18-49e6-9a72-bb115aa133ff', 
                    value = 1, 
                    subject = 1, 
                    subject_id = 'db3d85ef-c324-458b-b206-58debaa96419', )
)

```
[[Back to top]](#) 

