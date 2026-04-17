---
id: role1
title: Role1
pagination_label: Role1
sidebar_label: Role1
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Role1', 'Role1'] 
slug: /tools/sdk/python//models/role1
tags: ['SDK', 'Software Development Kit', 'Role1', 'Role1']
---

# Role1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uid** | **str** |  | [optional] 
**type** |  **Enum** [  'NeprofileRole',    'NeaccessRole' ] |  | [optional] 
**name** | **str** |  | [optional] 
**groups** | **[]str** |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.role1 import Role1

role1 = Role1(
uid='sponsors_role',
type='NeprofileRole',
name='Sponsors',
groups=[
                    'ad_group_name'
                    ]
)

```
[[Back to top]](#) 

