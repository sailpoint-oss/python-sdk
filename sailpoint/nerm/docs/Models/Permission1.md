---
id: permission1
title: Permission1
pagination_label: Permission1
sidebar_label: Permission1
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Permission1', 'Permission1'] 
slug: /tools/sdk/python//models/permission1
tags: ['SDK', 'Software Development Kit', 'Permission1', 'Permission1']
---

# Permission1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role_id** | **str** | The id of the role | [optional] 
**subject_id** | **str** | The ID of the object that the permission is giving access to | [optional] 
**value** |  **Enum** [  1,    2,    3,    4,    5,    6,    7 ] | The permissions level of access | [optional] 
**subject** |  **Enum** [  0,    1,    2,    3,    4,    5,    6,    7,    8,    9,    10,    11,    12,    13,    14,    15,    16,    17,    18,    19,    20,    21,    22,    23 ] | The type of permission | [optional] 
}

## Example

```python
from sailpoint.nerm.models.permission1 import Permission1

permission1 = Permission1(
role_id='ef5d413f-ba18-49e6-9a72-bb115aa133ff',
subject_id='db3d85ef-c324-458b-b206-58debaa96419',
value=1,
subject=0
)

```
[[Back to top]](#) 

