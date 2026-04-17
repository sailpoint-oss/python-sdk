---
id: user-managers
title: UserManagers
pagination_label: UserManagers
sidebar_label: UserManagers
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'UserManagers', 'UserManagers'] 
slug: /tools/sdk/python//models/user-managers
tags: ['SDK', 'Software Development Kit', 'UserManagers', 'UserManagers']
---

# UserManagers


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_managers** | [**[]UserManager**](user-manager) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.user_managers import UserManagers

user_managers = UserManagers(
user_managers=[
                    sailpoint.nerm.models.user_manager.UserManager(
                        id = '', 
                        uid = '', 
                        user_id = '', 
                        manager_id = '', )
                    ]
)

```
[[Back to top]](#) 

