---
id: common-access-item-access
title: CommonAccessItemAccess
pagination_label: CommonAccessItemAccess
sidebar_label: CommonAccessItemAccess
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'CommonAccessItemAccess', 'CommonAccessItemAccess'] 
slug: /tools/sdk/python/iai-common-access/models/common-access-item-access
tags: ['SDK', 'Software Development Kit', 'CommonAccessItemAccess', 'CommonAccessItemAccess']
---

# CommonAccessItemAccess


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Common access ID | [optional] 
**type** | **CommonAccessType** |  | [optional] 
**name** | **str** | Common access name | [optional] 
**description** | **str** | Common access description | [optional] 
**owner_name** | **str** | Common access owner name | [optional] 
**owner_id** | **str** | Common access owner ID | [optional] 
}

## Example

```python
from sailpoint.iai_common_access.models.common_access_item_access import CommonAccessItemAccess

common_access_item_access = CommonAccessItemAccess(
id='',
type='ACCESS_PROFILE',
name='',
description='',
owner_name='',
owner_id=''
)

```
[[Back to top]](#) 

