---
id: create-profiles-request
title: CreateProfilesRequest
pagination_label: CreateProfilesRequest
sidebar_label: CreateProfilesRequest
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'CreateProfilesRequest', 'CreateProfilesRequest'] 
slug: /tools/sdk/python//models/create-profiles-request
tags: ['SDK', 'Software Development Kit', 'CreateProfilesRequest', 'CreateProfilesRequest']
---

# CreateProfilesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profiles** | [**[]Profile1**](profile1) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.create_profiles_request import CreateProfilesRequest

create_profiles_request = CreateProfilesRequest(
profiles=[
                    sailpoint.nerm.models.profile_1.Profile_1(
                        name = 'First Last', 
                        profile_type_id = '79ed1cb6-9977-4965-9bfe-f2bcc2424444', 
                        status = 'Active', 
                        id_proofing_status = 'pass', 
                        archived = False, 
                        attributes = {text_attribute_uid=static text, date_attribute_uid=01/15/2020, profile_select_attribute_uid=79ed1cb6-9977-4965-9bfe-f2bcc242523e, multiple_profile_select_attribute_uid=59ed1cb6-9977-4965-9bfe-f2bcc242523e, 89ed1cb6-9977-4965-9bfe-f2bcc242523e, profile_search_attribute_uid=79ed1cb6-9977-4965-9bfe-f2bcc242523e, multiple_profile_search_attribute_uid=59ed1cb6-9977-4965-9bfe-f2bcc242523e, 89ed1cb6-9977-4965-9bfe-f2bcc242523e, contributor_select_attribute_uid=49ed1cb6-9977-4965-9bfe-f2bcc2425244, contributor_search_attribute_uid=49ed1cb6-9977-4965-9bfe-f2bcc2425244, multiple_contributor_search_attribute_uid=59ed1cb6-9977-4965-9bfe-f2bcc242523e, 89ed1cb6-9977-4965-9bfe-f2bcc242523e, owner_select_attribute_uid=79ed1cb6-9977-4965-9bfe-f2bcc242523e, owner_search_attribute_uid=79ed1cb6-9977-4965-9bfe-f2bcc242523e, dropdown_attribute_uid=yes, no, tags_attribute_uid=yes, no, checkbox_attribute_uid=yes, no, text_area_uid=static text, radio_attribute_uid=yes, no}, )
                    ]
)

```
[[Back to top]](#) 

