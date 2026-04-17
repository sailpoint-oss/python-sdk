---
id: user1
title: User1
pagination_label: User1
sidebar_label: User1
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'User1', 'User1'] 
slug: /tools/sdk/python//models/user1
tags: ['SDK', 'Software Development Kit', 'User1', 'User1']
---

# User1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The user name | [required]
**email** | **str** | The user email | [required]
**type** |  **Enum** [  'NeprofileUser',    'NeaccessUser' ] | The user type | [required][default to 'NeprofileUser']
**profile_id** | **str** | The user profile id. Not required for NeprofileUser | [optional] 
**title** | **str** | The user description | [optional] 
**status** |  **Enum** [  'Active',    'Pending',    'Disabled' ] | The user status | [optional] 
**login** | **str** | The user login | [required]
**group_strings** | **str** | The user group strings | [optional] 
**locale** | **str** | The locale the user prefers to use | [optional] 
**password** | **str** | The user password. Not required for NeprofileUser | [optional] 
**sailpoint_identity_id** | **str** | The SailPoint Identity ID associated with this user | [optional] 
}

## Example

```python
from sailpoint.nerm.models.user1 import User1

user1 = User1(
name='Bob',
email='test@sailpoint.com',
type='NeprofileUser',
profile_id='db6f8e8b-65c2-47d5-a0db-90bcc4e9df9e',
title='my_user_title',
status='Active',
login='my_user',
group_strings='Administrator_group,Developer_group',
locale='fr-CA',
password='U*bF7hy9fW',
sailpoint_identity_id='db6f8e8b-65c2-47d5-a0db-90bcc4e9df9e'
)

```
[[Back to top]](#) 

