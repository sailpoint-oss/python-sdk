---
id: user-profile
title: UserProfile
pagination_label: UserProfile
sidebar_label: UserProfile
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'UserProfile', 'UserProfile'] 
slug: /tools/sdk/python//models/user-profile
tags: ['SDK', 'Software Development Kit', 'UserProfile', 'UserProfile']
---

# UserProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**uid** | **str** |  | [optional] [readonly] 
**user_id** | **str** |  | [optional] 
**profile_id** | **str** |  | [optional] 
**ne_attribute_id** | **str** |  | [optional] 
**relationship_type** |  **Enum** [  'owner',    'contributor' ] |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.user_profile import UserProfile

user_profile = UserProfile(
id='',
uid='',
user_id='',
profile_id='',
ne_attribute_id='',
relationship_type='owner'
)

```
[[Back to top]](#) 

