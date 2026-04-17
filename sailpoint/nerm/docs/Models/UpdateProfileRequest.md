---
id: update-profile-request
title: UpdateProfileRequest
pagination_label: UpdateProfileRequest
sidebar_label: UpdateProfileRequest
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'UpdateProfileRequest', 'UpdateProfileRequest'] 
slug: /tools/sdk/python//models/update-profile-request
tags: ['SDK', 'Software Development Kit', 'UpdateProfileRequest', 'UpdateProfileRequest']
---

# UpdateProfileRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile** | [**UpdateProfileRequestProfile**](update-profile-request-profile) |  | [required]
}

## Example

```python
from sailpoint.nerm.models.update_profile_request import UpdateProfileRequest

update_profile_request = UpdateProfileRequest(
profile={attributes={First Name=John, Last Name=Doe, Email=john.doe@sailpoint.com}}
)

```
[[Back to top]](#) 

