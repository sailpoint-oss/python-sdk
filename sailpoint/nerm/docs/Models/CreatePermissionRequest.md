---
id: create-permission-request
title: CreatePermissionRequest
pagination_label: CreatePermissionRequest
sidebar_label: CreatePermissionRequest
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'CreatePermissionRequest', 'CreatePermissionRequest'] 
slug: /tools/sdk/python//models/create-permission-request
tags: ['SDK', 'Software Development Kit', 'CreatePermissionRequest', 'CreatePermissionRequest']
---

# CreatePermissionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**permission** | [**Permission1**](permission1) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.create_permission_request import CreatePermissionRequest

create_permission_request = CreatePermissionRequest(
permission=sailpoint.nerm.models.permission_1.Permission_1(
                    role_id = 'ef5d413f-ba18-49e6-9a72-bb115aa133ff', 
                    subject_id = 'db3d85ef-c324-458b-b206-58debaa96419', 
                    value = 1, 
                    subject = 0, )
)

```
[[Back to top]](#) 

