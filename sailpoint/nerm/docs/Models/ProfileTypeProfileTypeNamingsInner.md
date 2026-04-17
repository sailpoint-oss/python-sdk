---
id: profile-type-profile-type-namings-inner
title: ProfileTypeProfileTypeNamingsInner
pagination_label: ProfileTypeProfileTypeNamingsInner
sidebar_label: ProfileTypeProfileTypeNamingsInner
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'ProfileTypeProfileTypeNamingsInner', 'ProfileTypeProfileTypeNamingsInner'] 
slug: /tools/sdk/python//models/profile-type-profile-type-namings-inner
tags: ['SDK', 'Software Development Kit', 'ProfileTypeProfileTypeNamingsInner', 'ProfileTypeProfileTypeNamingsInner']
---

# ProfileTypeProfileTypeNamingsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the profile type naming. | [optional] 
**uid** | **str** | The user-specified identifier of the profile type naming. | [optional] 
**profile_type_id** | **str** | The ID of the associated profile type. | [optional] 
**ne_attribute_id** | **str** | The ID of the associated ne attribute. | [optional] 
**order** | **int** | The order that the namings are used in. | [optional] 
}

## Example

```python
from sailpoint.nerm.models.profile_type_profile_type_namings_inner import ProfileTypeProfileTypeNamingsInner

profile_type_profile_type_namings_inner = ProfileTypeProfileTypeNamingsInner(
id='33f072dd-13b4-41e1-8ea0-16f2a59b57c8',
uid='profile-type-name',
profile_type_id='33f072dd-13b4-41e1-8ea0-16f2a59b57c8',
ne_attribute_id='33f072dd-13b4-41e1-8ea0-16f2a59b57c8',
order=0
)

```
[[Back to top]](#) 

