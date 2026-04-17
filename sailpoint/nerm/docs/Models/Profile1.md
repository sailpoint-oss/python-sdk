---
id: profile1
title: Profile1
pagination_label: Profile1
sidebar_label: Profile1
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Profile1', 'Profile1'] 
slug: /tools/sdk/python//models/profile1
tags: ['SDK', 'Software Development Kit', 'Profile1', 'Profile1']
---

# Profile1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The profile name. | [optional] 
**profile_type_id** | **str** | The profile type id. | [required]
**status** |  **Enum** [  'Active',    'Inactive',    'On Leave',    'Terminated' ] | The profile status. | [required]
**id_proofing_status** |  **Enum** [  'pending',    'pass',    'fail' ] | The id proofing status of the profile. | [optional] 
**archived** | **bool** | Describes whether the profile is archived or not. | [optional] [default to False]
**attributes** | **map[string]str** | The attributes associated with the profile. | [optional] 
}

## Example

```python
from sailpoint.nerm.models.profile1 import Profile1

profile1 = Profile1(
name='First Last',
profile_type_id='79ed1cb6-9977-4965-9bfe-f2bcc2424444',
status='Active',
id_proofing_status='pass',
archived=False,
attributes={text_attribute_uid=static text, date_attribute_uid=01/15/2020, profile_select_attribute_uid=79ed1cb6-9977-4965-9bfe-f2bcc242523e, multiple_profile_select_attribute_uid=59ed1cb6-9977-4965-9bfe-f2bcc242523e, 89ed1cb6-9977-4965-9bfe-f2bcc242523e, profile_search_attribute_uid=79ed1cb6-9977-4965-9bfe-f2bcc242523e, multiple_profile_search_attribute_uid=59ed1cb6-9977-4965-9bfe-f2bcc242523e, 89ed1cb6-9977-4965-9bfe-f2bcc242523e, contributor_select_attribute_uid=49ed1cb6-9977-4965-9bfe-f2bcc2425244, contributor_search_attribute_uid=49ed1cb6-9977-4965-9bfe-f2bcc2425244, multiple_contributor_search_attribute_uid=59ed1cb6-9977-4965-9bfe-f2bcc242523e, 89ed1cb6-9977-4965-9bfe-f2bcc242523e, owner_select_attribute_uid=79ed1cb6-9977-4965-9bfe-f2bcc242523e, owner_search_attribute_uid=79ed1cb6-9977-4965-9bfe-f2bcc242523e, dropdown_attribute_uid=yes, no, tags_attribute_uid=yes, no, checkbox_attribute_uid=yes, no, text_area_uid=static text, radio_attribute_uid=yes, no}
)

```
[[Back to top]](#) 

