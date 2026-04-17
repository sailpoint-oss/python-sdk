---
id: create-profile-page200-response
title: CreateProfilePage200Response
pagination_label: CreateProfilePage200Response
sidebar_label: CreateProfilePage200Response
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'CreateProfilePage200Response', 'CreateProfilePage200Response'] 
slug: /tools/sdk/python//models/create-profile-page200-response
tags: ['SDK', 'Software Development Kit', 'CreateProfilePage200Response', 'CreateProfilePage200Response']
---

# CreateProfilePage200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | [**Pages**](pages) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.create_profile_page200_response import CreateProfilePage200Response

create_profile_page200_response = CreateProfilePage200Response(
page=sailpoint.nerm.models.pages.Pages(
                    uid = 'page_uid', 
                    description = 'Page for workflow', 
                    name = 'My Page Name', 
                    archived = False, 
                    id = '2e06b876-f456-473d-bd65-b6435e0b6b2d', )
)

```
[[Back to top]](#) 

