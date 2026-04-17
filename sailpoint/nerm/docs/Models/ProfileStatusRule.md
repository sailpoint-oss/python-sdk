---
id: profile-status-rule
title: ProfileStatusRule
pagination_label: ProfileStatusRule
sidebar_label: ProfileStatusRule
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'ProfileStatusRule', 'ProfileStatusRule'] 
slug: /tools/sdk/python//models/profile-status-rule
tags: ['SDK', 'Software Development Kit', 'ProfileStatusRule', 'ProfileStatusRule']
---

# ProfileStatusRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**uid** | **str** |  | [optional] [readonly] 
**type** |  **Enum** [  'ProfileStatusRule' ] |  | [required]
**comparison_operator** |  **Enum** [  '==',    '!=' ] |  | [optional] 
**value** |  **Enum** [  'Active',    'Inactive',    'Leave of absence',    'Terminated' ] |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.profile_status_rule import ProfileStatusRule

profile_status_rule = ProfileStatusRule(
id='',
uid='',
type='ProfileStatusRule',
comparison_operator='==',
value='Active'
)

```
[[Back to top]](#) 

