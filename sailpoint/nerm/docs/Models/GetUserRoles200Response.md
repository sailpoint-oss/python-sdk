---
id: get-user-roles200-response
title: GetUserRoles200Response
pagination_label: GetUserRoles200Response
sidebar_label: GetUserRoles200Response
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'GetUserRoles200Response', 'GetUserRoles200Response'] 
slug: /tools/sdk/python//models/get-user-roles200-response
tags: ['SDK', 'Software Development Kit', 'GetUserRoles200Response', 'GetUserRoles200Response']
---

# GetUserRoles200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_roles** | [**[]UserRole**](user-role) |  | [optional] 
**metadata** | [**Metadata**](metadata) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.get_user_roles200_response import GetUserRoles200Response

get_user_roles200_response = GetUserRoles200Response(
user_roles=[
                    sailpoint.nerm.models.user_role.UserRole(
                        id = '', 
                        uid = '', 
                        user_id = '', 
                        role_id = '', )
                    ],
metadata=sailpoint.nerm.models.metadata.Metadata(
                    limit = 56, 
                    offset = 56, 
                    total = 56, 
                    next = '/endpoint?limit=10&offset=60', 
                    previous = '/endpoint?limit=10&offset=40', )
)

```
[[Back to top]](#) 

