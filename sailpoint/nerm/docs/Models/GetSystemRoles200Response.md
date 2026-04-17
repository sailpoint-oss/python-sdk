---
id: get-system-roles200-response
title: GetSystemRoles200Response
pagination_label: GetSystemRoles200Response
sidebar_label: GetSystemRoles200Response
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'GetSystemRoles200Response', 'GetSystemRoles200Response'] 
slug: /tools/sdk/python//models/get-system-roles200-response
tags: ['SDK', 'Software Development Kit', 'GetSystemRoles200Response', 'GetSystemRoles200Response']
---

# GetSystemRoles200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**system_roles** | [**[]SystemRole**](system-role) |  | [optional] 
**metadata** | [**Metadata**](metadata) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.get_system_roles200_response import GetSystemRoles200Response

get_system_roles200_response = GetSystemRoles200Response(
system_roles=[
                    sailpoint.nerm.models.system_role.SystemRole(
                        id = '2e06b876-f456-473d-bd65-b6435e0b6b2d', 
                        uid = 'profile_contributor', 
                        name = 'Profile Contributor', )
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

