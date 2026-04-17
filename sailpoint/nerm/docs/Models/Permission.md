---
id: permission
title: Permission
pagination_label: Permission
sidebar_label: Permission
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Permission', 'Permission'] 
slug: /tools/sdk/python//models/permission
tags: ['SDK', 'Software Development Kit', 'Permission', 'Permission']
---

# Permission


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The id of the permission | [optional] [readonly] 
**role_id** | **str** | The id of the role | [optional] 
**value** | **int** | The permissions level of access | [optional] 
**subject** | **int** | The type of permission | [optional] 
**subject_id** | **str** | The ID of the object that the permission is giving access to | [optional] 
}

## Example

```python
from sailpoint.nerm.models.permission import Permission

permission = Permission(
id='2e06b876-f456-473d-bd65-b6435e0b6b2d',
role_id='ef5d413f-ba18-49e6-9a72-bb115aa133ff',
value=1,
subject=1,
subject_id='db3d85ef-c324-458b-b206-58debaa96419'
)

```
[[Back to top]](#) 

