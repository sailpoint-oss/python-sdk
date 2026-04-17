---
id: create-profile-page-request
title: CreateProfilePageRequest
pagination_label: CreateProfilePageRequest
sidebar_label: CreateProfilePageRequest
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'CreateProfilePageRequest', 'CreateProfilePageRequest'] 
slug: /tools/sdk/python//models/create-profile-page-request
tags: ['SDK', 'Software Development Kit', 'CreateProfilePageRequest', 'CreateProfilePageRequest']
---

# CreateProfilePageRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | [**ProfilePage**](profile-page) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.create_profile_page_request import CreateProfilePageRequest

create_profile_page_request = CreateProfilePageRequest(
page=sailpoint.nerm.models.profile_page.ProfilePage(
                    uid = 'page_uid', 
                    description = 'Page for workflow', 
                    name = 'My Page Name', 
                    archived = False, )
)

```
[[Back to top]](#) 

