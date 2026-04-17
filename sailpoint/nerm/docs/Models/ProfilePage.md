---
id: profile-page
title: ProfilePage
pagination_label: ProfilePage
sidebar_label: ProfilePage
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'ProfilePage', 'ProfilePage'] 
slug: /tools/sdk/python//models/profile-page
tags: ['SDK', 'Software Development Kit', 'ProfilePage', 'ProfilePage']
---

# ProfilePage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uid** | **str** | The user-specified identifier of the page | [optional] 
**description** | **str** | The description of the page | [optional] 
**name** | **str** | The name of the page | [optional] 
**archived** | **bool** | Determines whether the page is archived | [optional] 
}

## Example

```python
from sailpoint.nerm.models.profile_page import ProfilePage

profile_page = ProfilePage(
uid='page_uid',
description='Page for workflow',
name='My Page Name',
archived=False
)

```
[[Back to top]](#) 

