---
id: submit-role-profile-request
title: SubmitRoleProfileRequest
pagination_label: SubmitRoleProfileRequest
sidebar_label: SubmitRoleProfileRequest
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'SubmitRoleProfileRequest', 'SubmitRoleProfileRequest'] 
slug: /tools/sdk/python//models/submit-role-profile-request
tags: ['SDK', 'Software Development Kit', 'SubmitRoleProfileRequest', 'SubmitRoleProfileRequest']
---

# SubmitRoleProfileRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role_profile** | [**RoleProfile1**](role-profile1) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.submit_role_profile_request import SubmitRoleProfileRequest

submit_role_profile_request = SubmitRoleProfileRequest(
role_profile=sailpoint.nerm.models.role_profile_1.RoleProfile_1(
                    role_id = '', 
                    profile_id = '', )
)

```
[[Back to top]](#) 

