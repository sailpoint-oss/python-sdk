---
id: user-profiles
title: UserProfiles
pagination_label: UserProfiles
sidebar_label: UserProfiles
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'UserProfiles', 'UserProfiles'] 
slug: /tools/sdk/python//models/user-profiles
tags: ['SDK', 'Software Development Kit', 'UserProfiles', 'UserProfiles']
---

# UserProfiles


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_profiles** | [**[]UserProfile**](user-profile) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.user_profiles import UserProfiles

user_profiles = UserProfiles(
user_profiles=[
                    sailpoint.nerm.models.user_profile.UserProfile(
                        id = '', 
                        uid = '', 
                        user_id = '', 
                        profile_id = '', 
                        ne_attribute_id = '', 
                        relationship_type = 'owner', )
                    ]
)

```
[[Back to top]](#) 

