---
id: roles
title: Roles
pagination_label: Roles
sidebar_label: Roles
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Roles', 'Roles'] 
slug: /tools/sdk/python//models/roles
tags: ['SDK', 'Software Development Kit', 'Roles', 'Roles']
---

# Roles


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**roles** | [**[]Role**](role) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.roles import Roles

roles = Roles(
roles=[
                    sailpoint.nerm.models.role.Role(
                        id = '', 
                        uid = 'sponsors_role', 
                        name = 'Sponsors', 
                        groups = [
                            'ad_group_name'
                            ], )
                    ]
)

```
[[Back to top]](#) 

