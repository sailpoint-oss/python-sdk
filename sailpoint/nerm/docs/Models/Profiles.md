---
id: profiles
title: Profiles
pagination_label: Profiles
sidebar_label: Profiles
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Profiles', 'Profiles'] 
slug: /tools/sdk/python//models/profiles
tags: ['SDK', 'Software Development Kit', 'Profiles', 'Profiles']
---

# Profiles


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profiles** | [**[]Profile**](profile) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.profiles import Profiles

profiles = Profiles(
profiles=[
                    sailpoint.nerm.models.profile.Profile(
                        id = '33f072dd-13b4-41e1-8ea0-16f2a59b57c8', 
                        uid = 'profileUid', 
                        name = 'Profile Name', 
                        profile_type_id = '33f072dd-13b4-41e1-8ea0-16f2a59b57c8', 
                        status = 'Active', 
                        id_proofing_status = 'pending', 
                        created_at = '2023-11-21T14:23:54.256-05:00', 
                        updated_at = '2023-11-21T14:23:54.256-05:00', 
                        attributes = {Non-Employee Profile ID=The Non-Employee Profile ID (will be returned for assignments, to be used during correlation configuration), text_attribute_uid=static text, date_attribute_uid=01/15/2020, profile_select_attribute_uid=Profile Name, profile_search_attribute_uid=Profile Name, multiple_profile_search_attribute_uid=Profile Name,Second Profile Name,Third Profile Name, multiple_profile_select_attribute_uid=Profile Name,Second Profile Name,Third Profile Name, contributor_select_attribute_uid=User Name (user_email@test.com), contributor_search_attribute_uid=User Name (user_email@test.com), multiple_contributor_search_attribute_uid=User Name (user_email@test.com),Second User Name (user_email@test.com),Third User Name (user_email@test.com), owner_select_attribute_uid=User Name (user_email@test.com), owner_search_attribute_uid=User Name (user_email@test.com), dropdown_attribute_uid=yes, no, tags_attribute_uid=yes, no, checkbox_attribute_uid=yes, no, text_area_uid=static text, radio_attribute_uid=yes, no}, )
                    ]
)

```
[[Back to top]](#) 

