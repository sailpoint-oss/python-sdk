---
id: submit-user-roles-request
title: SubmitUserRolesRequest
pagination_label: SubmitUserRolesRequest
sidebar_label: SubmitUserRolesRequest
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'SubmitUserRolesRequest', 'SubmitUserRolesRequest'] 
slug: /tools/sdk/python//models/submit-user-roles-request
tags: ['SDK', 'Software Development Kit', 'SubmitUserRolesRequest', 'SubmitUserRolesRequest']
---

# SubmitUserRolesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_roles** | [**[]UserRole1**](user-role1) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.submit_user_roles_request import SubmitUserRolesRequest

submit_user_roles_request = SubmitUserRolesRequest(
user_roles=[
                    sailpoint.nerm.models.user_role_1.UserRole_1(
                        user_id = '', 
                        role_id = '', )
                    ]
)

```
[[Back to top]](#) 

