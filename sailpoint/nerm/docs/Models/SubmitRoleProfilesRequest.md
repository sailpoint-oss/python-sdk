---
id: submit-role-profiles-request
title: SubmitRoleProfilesRequest
pagination_label: SubmitRoleProfilesRequest
sidebar_label: SubmitRoleProfilesRequest
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'SubmitRoleProfilesRequest', 'SubmitRoleProfilesRequest'] 
slug: /tools/sdk/python//models/submit-role-profiles-request
tags: ['SDK', 'Software Development Kit', 'SubmitRoleProfilesRequest', 'SubmitRoleProfilesRequest']
---

# SubmitRoleProfilesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role_profiles** | [**[]RoleProfile1**](role-profile1) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.submit_role_profiles_request import SubmitRoleProfilesRequest

submit_role_profiles_request = SubmitRoleProfilesRequest(
role_profiles=[
                    sailpoint.nerm.models.role_profile_1.RoleProfile_1(
                        role_id = '', 
                        profile_id = '', )
                    ]
)

```
[[Back to top]](#) 

