---
id: profile
title: Profile
pagination_label: Profile
sidebar_label: Profile
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Profile', 'Profile'] 
slug: /tools/sdk/python//models/profile
tags: ['SDK', 'Software Development Kit', 'Profile', 'Profile']
---

# Profile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The objects ID | [optional] [readonly] 
**uid** | **str** | The objects UID | [optional] [readonly] 
**name** | **str** | This is the name of the profile. | [optional] 
**profile_type_id** | **str** | This is the ID of the profile type the profile belongs to | [optional] 
**status** |  **Enum** [  'Active',    'Inactive',    'On Leave',    'Terminated' ] | This is the status of the profile | [optional] 
**id_proofing_status** |  **Enum** [  'pending',    'pass',    'fail' ] | This is the ID proofing staus of the profile | [optional] 
**created_at** | **datetime** | The date and time the profile was created | [optional] 
**updated_at** | **datetime** | The date and time the profile was updated | [optional] 
**attributes** | **map[string]str** | Attributes that belong to this profile. | [optional] 
}

## Example

```python
from sailpoint.nerm.models.profile import Profile

profile = Profile(
id='33f072dd-13b4-41e1-8ea0-16f2a59b57c8',
uid='profileUid',
name='Profile Name',
profile_type_id='33f072dd-13b4-41e1-8ea0-16f2a59b57c8',
status='Active',
id_proofing_status='pending',
created_at='2023-11-21T14:23:54.256-05:00',
updated_at='2023-11-21T14:23:54.256-05:00',
attributes={Non-Employee Profile ID=The Non-Employee Profile ID (will be returned for assignments, to be used during correlation configuration), text_attribute_uid=static text, date_attribute_uid=01/15/2020, profile_select_attribute_uid=Profile Name, profile_search_attribute_uid=Profile Name, multiple_profile_search_attribute_uid=Profile Name,Second Profile Name,Third Profile Name, multiple_profile_select_attribute_uid=Profile Name,Second Profile Name,Third Profile Name, contributor_select_attribute_uid=User Name (user_email@test.com), contributor_search_attribute_uid=User Name (user_email@test.com), multiple_contributor_search_attribute_uid=User Name (user_email@test.com),Second User Name (user_email@test.com),Third User Name (user_email@test.com), owner_select_attribute_uid=User Name (user_email@test.com), owner_search_attribute_uid=User Name (user_email@test.com), dropdown_attribute_uid=yes, no, tags_attribute_uid=yes, no, checkbox_attribute_uid=yes, no, text_area_uid=static text, radio_attribute_uid=yes, no}
)

```
[[Back to top]](#) 

