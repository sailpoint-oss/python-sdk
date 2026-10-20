---
id: access-profile-reference
title: AccessProfileReference
pagination_label: AccessProfileReference
sidebar_label: AccessProfileReference
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'AccessProfileReference', 'AccessProfileReference'] 
slug: /tools/sdk/python/gov-certification/models/access-profile-reference
tags: ['SDK', 'Software Development Kit', 'AccessProfileReference', 'AccessProfileReference']
---

# AccessProfileReference


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The id of the Access Profile | [optional] 
**name** | **str** | Name of the Access Profile | [optional] 
**description** | **str** | Information about the Access Profile | [optional] 
}

## Example

```python
from sailpoint.gov_certification.models.access_profile_reference import AccessProfileReference

access_profile_reference = AccessProfileReference(
id='2c91808a7190d06e01719938fcd20792',
name='Employee-database-read-write',
description='Collection of entitlements to read/write the employee database'
)

```
[[Back to top]](#) 

