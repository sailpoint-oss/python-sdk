---
id: submit-user-role-request
title: SubmitUserRoleRequest
pagination_label: SubmitUserRoleRequest
sidebar_label: SubmitUserRoleRequest
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'SubmitUserRoleRequest', 'SubmitUserRoleRequest'] 
slug: /tools/sdk/python//models/submit-user-role-request
tags: ['SDK', 'Software Development Kit', 'SubmitUserRoleRequest', 'SubmitUserRoleRequest']
---

# SubmitUserRoleRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_role** | [**UserRole1**](user-role1) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.submit_user_role_request import SubmitUserRoleRequest

submit_user_role_request = SubmitUserRoleRequest(
user_role=sailpoint.nerm.models.user_role_1.UserRole_1(
                    user_id = '', 
                    role_id = '', )
)

```
[[Back to top]](#) 

