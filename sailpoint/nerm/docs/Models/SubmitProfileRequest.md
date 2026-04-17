---
id: submit-profile-request
title: SubmitProfileRequest
pagination_label: SubmitProfileRequest
sidebar_label: SubmitProfileRequest
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'SubmitProfileRequest', 'SubmitProfileRequest'] 
slug: /tools/sdk/python//models/submit-profile-request
tags: ['SDK', 'Software Development Kit', 'SubmitProfileRequest', 'SubmitProfileRequest']
---

# SubmitProfileRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile** | [**Profile1**](profile1) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.submit_profile_request import SubmitProfileRequest

submit_profile_request = SubmitProfileRequest(
profile=sailpoint.nerm.models.profile_1.Profile_1(
                    name = 'First Last', 
                    profile_type_id = '79ed1cb6-9977-4965-9bfe-f2bcc2424444', 
                    status = 'Active', 
                    id_proofing_status = 'pass', 
                    archived = False, 
                    attributes = {text_attribute_uid=static text, date_attribute_uid=01/15/2020, profile_select_attribute_uid=79ed1cb6-9977-4965-9bfe-f2bcc242523e, multiple_profile_select_attribute_uid=59ed1cb6-9977-4965-9bfe-f2bcc242523e, 89ed1cb6-9977-4965-9bfe-f2bcc242523e, profile_search_attribute_uid=79ed1cb6-9977-4965-9bfe-f2bcc242523e, multiple_profile_search_attribute_uid=59ed1cb6-9977-4965-9bfe-f2bcc242523e, 89ed1cb6-9977-4965-9bfe-f2bcc242523e, contributor_select_attribute_uid=49ed1cb6-9977-4965-9bfe-f2bcc2425244, contributor_search_attribute_uid=49ed1cb6-9977-4965-9bfe-f2bcc2425244, multiple_contributor_search_attribute_uid=59ed1cb6-9977-4965-9bfe-f2bcc242523e, 89ed1cb6-9977-4965-9bfe-f2bcc242523e, owner_select_attribute_uid=79ed1cb6-9977-4965-9bfe-f2bcc242523e, owner_search_attribute_uid=79ed1cb6-9977-4965-9bfe-f2bcc242523e, dropdown_attribute_uid=yes, no, tags_attribute_uid=yes, no, checkbox_attribute_uid=yes, no, text_area_uid=static text, radio_attribute_uid=yes, no}, )
)

```
[[Back to top]](#) 

