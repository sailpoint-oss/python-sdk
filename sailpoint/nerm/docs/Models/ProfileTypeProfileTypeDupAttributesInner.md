---
id: profile-type-profile-type-dup-attributes-inner
title: ProfileTypeProfileTypeDupAttributesInner
pagination_label: ProfileTypeProfileTypeDupAttributesInner
sidebar_label: ProfileTypeProfileTypeDupAttributesInner
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'ProfileTypeProfileTypeDupAttributesInner', 'ProfileTypeProfileTypeDupAttributesInner'] 
slug: /tools/sdk/python//models/profile-type-profile-type-dup-attributes-inner
tags: ['SDK', 'Software Development Kit', 'ProfileTypeProfileTypeDupAttributesInner', 'ProfileTypeProfileTypeDupAttributesInner']
---

# ProfileTypeProfileTypeDupAttributesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the properties that are used for duplication protection. | [optional] 
**uid** | **str** | The user-specified identifier of the properties that are used for duplication protection. | [optional] 
**profile_type_id** | **str** | The ID of the profile type. | [optional] 
**ne_attribute_id** | **str** | The ID of the ne attribute. | [optional] 
}

## Example

```python
from sailpoint.nerm.models.profile_type_profile_type_dup_attributes_inner import ProfileTypeProfileTypeDupAttributesInner

profile_type_profile_type_dup_attributes_inner = ProfileTypeProfileTypeDupAttributesInner(
id='33f072dd-13b4-41e1-8ea0-16f2a59b57c8',
uid='attribute-uid',
profile_type_id='33f072dd-13b4-41e1-8ea0-16f2a59b57c8',
ne_attribute_id='33f072dd-13b4-41e1-8ea0-16f2a59b57c8'
)

```
[[Back to top]](#) 

