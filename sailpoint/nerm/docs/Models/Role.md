---
id: role
title: Role
pagination_label: Role
sidebar_label: Role
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Role', 'Role'] 
slug: /tools/sdk/python//models/role
tags: ['SDK', 'Software Development Kit', 'Role', 'Role']
---

# Role


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**uid** | **str** |  | [optional] [readonly] 
**name** | **str** |  | [optional] 
**groups** | **[]str** |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.role import Role

role = Role(
id='',
uid='sponsors_role',
name='Sponsors',
groups=[
                    'ad_group_name'
                    ]
)

```
[[Back to top]](#) 

