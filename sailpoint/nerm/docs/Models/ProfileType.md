---
id: profile-type
title: ProfileType
pagination_label: ProfileType
sidebar_label: ProfileType
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'ProfileType', 'ProfileType'] 
slug: /tools/sdk/python//models/profile-type
tags: ['SDK', 'Software Development Kit', 'ProfileType', 'ProfileType']
---

# ProfileType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The objects ID. | [optional] [readonly] 
**uid** | **str** | The objects UID. | [optional] [readonly] 
**name** | **str** | This is the name of the profile type. | [optional] 
**category** |  **Enum** [  'employee',    'non-employee',    'organization',    'assignment',    'other' ] | This is the category the profile type falls into. | [optional] 
**bypass_dup_protection** | **bool** | Whether or not duplication protection is bypassed. | [optional] 
**archived** | **bool** | Whether or not the profile type is archived. | [optional] 
**permitted_role_ids** | **[]str** | The role ids that are permitted for this profile type. | [optional] 
**isc_synced** | **bool** | Is this profile type synced with ics | [optional] 
**profile_type_dup_attributes** | [**[]ProfileTypeProfileTypeDupAttributesInner**](profile-type-profile-type-dup-attributes-inner) |  | [optional] 
**profile_type_namings** | [**[]ProfileTypeProfileTypeNamingsInner**](profile-type-profile-type-namings-inner) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.profile_type import ProfileType

profile_type = ProfileType(
id='33f072dd-13b4-41e1-8ea0-16f2a59b57c8',
uid='ptUid',
name='Worker',
category='employee',
bypass_dup_protection=False,
archived=False,
permitted_role_ids=[33f072dd-13b4-41e1-8ea0-16f2a59b57c8],
isc_synced=False,
profile_type_dup_attributes=[
                    sailpoint.nerm.models.profile_type_profile_type_dup_attributes_inner.ProfileType_profile_type_dup_attributes_inner(
                        id = '33f072dd-13b4-41e1-8ea0-16f2a59b57c8', 
                        uid = 'attribute-uid', 
                        profile_type_id = '33f072dd-13b4-41e1-8ea0-16f2a59b57c8', 
                        ne_attribute_id = '33f072dd-13b4-41e1-8ea0-16f2a59b57c8', )
                    ],
profile_type_namings=[
                    sailpoint.nerm.models.profile_type_profile_type_namings_inner.ProfileType_profile_type_namings_inner(
                        id = '33f072dd-13b4-41e1-8ea0-16f2a59b57c8', 
                        uid = 'profile-type-name', 
                        profile_type_id = '33f072dd-13b4-41e1-8ea0-16f2a59b57c8', 
                        ne_attribute_id = '33f072dd-13b4-41e1-8ea0-16f2a59b57c8', 
                        order = 0, )
                    ]
)

```
[[Back to top]](#) 

