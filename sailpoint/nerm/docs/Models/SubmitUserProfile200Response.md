---
id: submit-user-profile200-response
title: SubmitUserProfile200Response
pagination_label: SubmitUserProfile200Response
sidebar_label: SubmitUserProfile200Response
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'SubmitUserProfile200Response', 'SubmitUserProfile200Response'] 
slug: /tools/sdk/python//models/submit-user-profile200-response
tags: ['SDK', 'Software Development Kit', 'SubmitUserProfile200Response', 'SubmitUserProfile200Response']
---

# SubmitUserProfile200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_profile** | [**UserProfile**](user-profile) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.submit_user_profile200_response import SubmitUserProfile200Response

submit_user_profile200_response = SubmitUserProfile200Response(
user_profile=sailpoint.nerm.models.user_profile.UserProfile(
                    id = '', 
                    uid = '', 
                    user_id = '', 
                    profile_id = '', 
                    ne_attribute_id = '', 
                    relationship_type = 'owner', )
)

```
[[Back to top]](#) 

