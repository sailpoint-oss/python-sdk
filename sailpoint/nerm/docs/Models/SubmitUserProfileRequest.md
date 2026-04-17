---
id: submit-user-profile-request
title: SubmitUserProfileRequest
pagination_label: SubmitUserProfileRequest
sidebar_label: SubmitUserProfileRequest
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'SubmitUserProfileRequest', 'SubmitUserProfileRequest'] 
slug: /tools/sdk/python//models/submit-user-profile-request
tags: ['SDK', 'Software Development Kit', 'SubmitUserProfileRequest', 'SubmitUserProfileRequest']
---

# SubmitUserProfileRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_profile** | [**UserProfile1**](user-profile1) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.submit_user_profile_request import SubmitUserProfileRequest

submit_user_profile_request = SubmitUserProfileRequest(
user_profile=sailpoint.nerm.models.user_profile_1.UserProfile_1(
                    user_id = '', 
                    profile_id = '', 
                    ne_attribute_id = '', 
                    relationship_type = 'owner', )
)

```
[[Back to top]](#) 

