---
id: get-user-profiles200-response
title: GetUserProfiles200Response
pagination_label: GetUserProfiles200Response
sidebar_label: GetUserProfiles200Response
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'GetUserProfiles200Response', 'GetUserProfiles200Response'] 
slug: /tools/sdk/python//models/get-user-profiles200-response
tags: ['SDK', 'Software Development Kit', 'GetUserProfiles200Response', 'GetUserProfiles200Response']
---

# GetUserProfiles200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_profiles** | [**[]UserProfile**](user-profile) |  | [optional] 
**metadata** | [**Metadata**](metadata) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.get_user_profiles200_response import GetUserProfiles200Response

get_user_profiles200_response = GetUserProfiles200Response(
user_profiles=[
                    sailpoint.nerm.models.user_profile.UserProfile(
                        id = '', 
                        uid = '', 
                        user_id = '', 
                        profile_id = '', 
                        ne_attribute_id = '', 
                        relationship_type = 'owner', )
                    ],
metadata=sailpoint.nerm.models.metadata.Metadata(
                    limit = 56, 
                    offset = 56, 
                    total = 56, 
                    next = '/endpoint?limit=10&offset=60', 
                    previous = '/endpoint?limit=10&offset=40', )
)

```
[[Back to top]](#) 

