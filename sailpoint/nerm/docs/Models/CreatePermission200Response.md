---
id: create-permission200-response
title: CreatePermission200Response
pagination_label: CreatePermission200Response
sidebar_label: CreatePermission200Response
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'CreatePermission200Response', 'CreatePermission200Response'] 
slug: /tools/sdk/python//models/create-permission200-response
tags: ['SDK', 'Software Development Kit', 'CreatePermission200Response', 'CreatePermission200Response']
---

# CreatePermission200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**permission** | [**Permission**](permission) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.create_permission200_response import CreatePermission200Response

create_permission200_response = CreatePermission200Response(
permission=sailpoint.nerm.models.permission.Permission(
                    id = '2e06b876-f456-473d-bd65-b6435e0b6b2d', 
                    role_id = 'ef5d413f-ba18-49e6-9a72-bb115aa133ff', 
                    value = 1, 
                    subject = 1, 
                    subject_id = 'db3d85ef-c324-458b-b206-58debaa96419', )
)

```
[[Back to top]](#) 

