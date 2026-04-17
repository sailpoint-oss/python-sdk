---
id: user-roles
title: UserRoles
pagination_label: UserRoles
sidebar_label: UserRoles
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'UserRoles', 'UserRoles'] 
slug: /tools/sdk/python//models/user-roles
tags: ['SDK', 'Software Development Kit', 'UserRoles', 'UserRoles']
---

# UserRoles


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_roles** | [**[]UserRole**](user-role) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.user_roles import UserRoles

user_roles = UserRoles(
user_roles=[
                    sailpoint.nerm.models.user_role.UserRole(
                        id = '', 
                        uid = '', 
                        user_id = '', 
                        role_id = '', )
                    ]
)

```
[[Back to top]](#) 

