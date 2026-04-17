---
id: submit-role-profile200-response
title: SubmitRoleProfile200Response
pagination_label: SubmitRoleProfile200Response
sidebar_label: SubmitRoleProfile200Response
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'SubmitRoleProfile200Response', 'SubmitRoleProfile200Response'] 
slug: /tools/sdk/python//models/submit-role-profile200-response
tags: ['SDK', 'Software Development Kit', 'SubmitRoleProfile200Response', 'SubmitRoleProfile200Response']
---

# SubmitRoleProfile200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role_profile** | [**RoleProfile**](role-profile) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.submit_role_profile200_response import SubmitRoleProfile200Response

submit_role_profile200_response = SubmitRoleProfile200Response(
role_profile=sailpoint.nerm.models.role_profile.RoleProfile(
                    id = '', 
                    uid = '', 
                    role_id = '', 
                    profile_id = '', )
)

```
[[Back to top]](#) 

