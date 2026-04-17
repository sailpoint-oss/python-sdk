---
id: create-user-profiles-request
title: CreateUserProfilesRequest
pagination_label: CreateUserProfilesRequest
sidebar_label: CreateUserProfilesRequest
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'CreateUserProfilesRequest', 'CreateUserProfilesRequest'] 
slug: /tools/sdk/python//models/create-user-profiles-request
tags: ['SDK', 'Software Development Kit', 'CreateUserProfilesRequest', 'CreateUserProfilesRequest']
---

# CreateUserProfilesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_profiles** | [**[]UserProfile1**](user-profile1) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.create_user_profiles_request import CreateUserProfilesRequest

create_user_profiles_request = CreateUserProfilesRequest(
user_profiles=[
                    sailpoint.nerm.models.user_profile_1.UserProfile_1(
                        user_id = '', 
                        profile_id = '', 
                        ne_attribute_id = '', 
                        relationship_type = 'owner', )
                    ]
)

```
[[Back to top]](#) 

