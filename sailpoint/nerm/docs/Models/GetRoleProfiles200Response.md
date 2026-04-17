---
id: get-role-profiles200-response
title: GetRoleProfiles200Response
pagination_label: GetRoleProfiles200Response
sidebar_label: GetRoleProfiles200Response
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'GetRoleProfiles200Response', 'GetRoleProfiles200Response'] 
slug: /tools/sdk/python//models/get-role-profiles200-response
tags: ['SDK', 'Software Development Kit', 'GetRoleProfiles200Response', 'GetRoleProfiles200Response']
---

# GetRoleProfiles200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role_profiles** | [**[]RoleProfile**](role-profile) |  | [optional] 
**metadata** | [**Metadata**](metadata) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.get_role_profiles200_response import GetRoleProfiles200Response

get_role_profiles200_response = GetRoleProfiles200Response(
role_profiles=[
                    sailpoint.nerm.models.role_profile.RoleProfile(
                        id = '', 
                        uid = '', 
                        role_id = '', 
                        profile_id = '', )
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

