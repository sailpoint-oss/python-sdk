---
id: create-profile-type-role-request
title: CreateProfileTypeRoleRequest
pagination_label: CreateProfileTypeRoleRequest
sidebar_label: CreateProfileTypeRoleRequest
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'CreateProfileTypeRoleRequest', 'CreateProfileTypeRoleRequest'] 
slug: /tools/sdk/python//models/create-profile-type-role-request
tags: ['SDK', 'Software Development Kit', 'CreateProfileTypeRoleRequest', 'CreateProfileTypeRoleRequest']
---

# CreateProfileTypeRoleRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile_type_role** | [**ProfileTypeRoles1**](profile-type-roles1) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.create_profile_type_role_request import CreateProfileTypeRoleRequest

create_profile_type_role_request = CreateProfileTypeRoleRequest(
profile_type_role=sailpoint.nerm.models.profile_type_roles_1.ProfileTypeRoles_1(
                    profile_type_id = '2eb5773f-2486-452f-bdb3-796133b30862', 
                    role_id = '2eb5773f-2486-452f-bdb3-796133b30862', )
)

```
[[Back to top]](#) 

