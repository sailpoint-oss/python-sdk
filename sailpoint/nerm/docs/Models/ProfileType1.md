---
id: profile-type1
title: ProfileType1
pagination_label: ProfileType1
sidebar_label: ProfileType1
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'ProfileType1', 'ProfileType1'] 
slug: /tools/sdk/python//models/profile-type1
tags: ['SDK', 'Software Development Kit', 'ProfileType1', 'ProfileType1']
---

# ProfileType1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | This is the name of the profile type. | [optional] 
**category** |  **Enum** [  'employee',    'non-employee',    'organization',    'assignment',    'other' ] | This is the category the profile type falls into. | [optional] 
**bypass_dup_protection** | **bool** | Whether or not duplication protection is bypassed. | [optional] [default to False]
**archived** | **bool** | Whether or not the profile type is archived. | [optional] [default to False]
**permitted_role_ids** | **[]str** | The role ids that are permitted for this profile type. | [optional] 
**isc_synced** | **bool** | Is this profile type synced with ics | [optional] [default to False]
**profile_type_dup_attributes_attributes** | [**[]ProfileType1ProfileTypeDupAttributesAttributesInner**](profile-type1-profile-type-dup-attributes-attributes-inner) |  | [optional] 
**profile_type_namings_attributes** | [**[]ProfileType1ProfileTypeNamingsAttributesInner**](profile-type1-profile-type-namings-attributes-inner) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.profile_type1 import ProfileType1

profile_type1 = ProfileType1(
name='Worker',
category='employee',
bypass_dup_protection=False,
archived=False,
permitted_role_ids=[33f072dd-13b4-41e1-8ea0-16f2a59b57c8],
isc_synced=False,
profile_type_dup_attributes_attributes=[
                    sailpoint.nerm.models.profile_type_1_profile_type_dup_attributes_attributes_inner.ProfileType_1_profile_type_dup_attributes_attributes_inner(
                        ne_attribute_id = '33f072dd-13b4-41e1-8ea0-16f2a59b57c8', )
                    ],
profile_type_namings_attributes=[
                    sailpoint.nerm.models.profile_type_1_profile_type_namings_attributes_inner.ProfileType_1_profile_type_namings_attributes_inner(
                        ne_attribute_id = '33f072dd-13b4-41e1-8ea0-16f2a59b57c8', 
                        order = 0, )
                    ]
)

```
[[Back to top]](#) 

