---
id: pages
title: Pages
pagination_label: Pages
sidebar_label: Pages
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Pages', 'Pages'] 
slug: /tools/sdk/python//models/pages
tags: ['SDK', 'Software Development Kit', 'Pages', 'Pages']
---

# Pages


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uid** | **str** | The user-specified identifier of the page | [optional] 
**description** | **str** | The description of the page | [optional] 
**name** | **str** | The name of the page | [optional] 
**archived** | **bool** | Determines whether the page is archived | [optional] 
**id** | **str** | The id of the form | [optional] [readonly] 
}

## Example

```python
from sailpoint.nerm.models.pages import Pages

pages = Pages(
uid='page_uid',
description='Page for workflow',
name='My Page Name',
archived=False,
id='2e06b876-f456-473d-bd65-b6435e0b6b2d'
)

```
[[Back to top]](#) 

