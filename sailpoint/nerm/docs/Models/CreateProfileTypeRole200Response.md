---
id: create-profile-type-role200-response
title: CreateProfileTypeRole200Response
pagination_label: CreateProfileTypeRole200Response
sidebar_label: CreateProfileTypeRole200Response
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'CreateProfileTypeRole200Response', 'CreateProfileTypeRole200Response'] 
slug: /tools/sdk/python//models/create-profile-type-role200-response
tags: ['SDK', 'Software Development Kit', 'CreateProfileTypeRole200Response', 'CreateProfileTypeRole200Response']
---

# CreateProfileTypeRole200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile_type_roles** | [**ProfileTypeRoles**](profile-type-roles) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.create_profile_type_role200_response import CreateProfileTypeRole200Response

create_profile_type_role200_response = CreateProfileTypeRole200Response(
profile_type_roles=sailpoint.nerm.models.profile_type_roles.ProfileTypeRoles(
                    profile_type_id = '2eb5773f-2486-452f-bdb3-796133b30862', 
                    role_id = '2eb5773f-2486-452f-bdb3-796133b30862', 
                    id = '2e06b876-f456-473d-bd65-b6435e0b6b2d', )
)

```
[[Back to top]](#) 

