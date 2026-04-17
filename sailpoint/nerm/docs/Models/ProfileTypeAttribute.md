---
id: profile-type-attribute
title: ProfileTypeAttribute
pagination_label: ProfileTypeAttribute
sidebar_label: ProfileTypeAttribute
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'ProfileTypeAttribute', 'ProfileTypeAttribute'] 
slug: /tools/sdk/python//models/profile-type-attribute
tags: ['SDK', 'Software Development Kit', 'ProfileTypeAttribute', 'ProfileTypeAttribute']
---

# ProfileTypeAttribute


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of ne attribute | [optional] [readonly] 
**uid** | **str** | Ne attribute's uid | [optional] [readonly] 
**label** | **str** | Ne attribute's label | [required][readonly] 
**synced** | **str** | synced_attribute ID if there is one | [optional] 
}

## Example

```python
from sailpoint.nerm.models.profile_type_attribute import ProfileTypeAttribute

profile_type_attribute = ProfileTypeAttribute(
id='1246d8b3-ac29-4015-8154-dea4434a73fa',
uid='1246d8b3-ac29-4015-8154-dea4434a73fa',
label='object',
synced='1246d8b3-ac29-4015-8154-dea4434a73fa'
)

```
[[Back to top]](#) 

