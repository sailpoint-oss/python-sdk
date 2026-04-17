---
id: profile-status-rule1
title: ProfileStatusRule1
pagination_label: ProfileStatusRule1
sidebar_label: ProfileStatusRule1
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'ProfileStatusRule1', 'ProfileStatusRule1'] 
slug: /tools/sdk/python//models/profile-status-rule1
tags: ['SDK', 'Software Development Kit', 'ProfileStatusRule1', 'ProfileStatusRule1']
---

# ProfileStatusRule1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** |  **Enum** [  'ProfileStatusRule' ] |  | [required]
**comparison_operator** |  **Enum** [  '==',    '!=' ] |  | [required]
**value** |  **Enum** [  'Active',    'Inactive',    'Leave of absence',    'Terminated' ] |  | [required]
}

## Example

```python
from sailpoint.nerm.models.profile_status_rule1 import ProfileStatusRule1

profile_status_rule1 = ProfileStatusRule1(
type='ProfileStatusRule',
comparison_operator='==',
value='Active'
)

```
[[Back to top]](#) 

