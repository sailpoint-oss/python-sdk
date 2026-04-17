---
id: submit-profile-type-request
title: SubmitProfileTypeRequest
pagination_label: SubmitProfileTypeRequest
sidebar_label: SubmitProfileTypeRequest
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'SubmitProfileTypeRequest', 'SubmitProfileTypeRequest'] 
slug: /tools/sdk/python//models/submit-profile-type-request
tags: ['SDK', 'Software Development Kit', 'SubmitProfileTypeRequest', 'SubmitProfileTypeRequest']
---

# SubmitProfileTypeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile_type** | [**ProfileType1**](profile-type1) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.submit_profile_type_request import SubmitProfileTypeRequest

submit_profile_type_request = SubmitProfileTypeRequest(
profile_type=sailpoint.nerm.models.profile_type_1.ProfileType_1(
                    name = 'Worker', 
                    category = 'employee', 
                    bypass_dup_protection = False, 
                    archived = False, 
                    permitted_role_ids = [33f072dd-13b4-41e1-8ea0-16f2a59b57c8], 
                    isc_synced = False, 
                    profile_type_dup_attributes_attributes = [
                        sailpoint.nerm.models.profile_type_1_profile_type_dup_attributes_attributes_inner.ProfileType_1_profile_type_dup_attributes_attributes_inner(
                            ne_attribute_id = '33f072dd-13b4-41e1-8ea0-16f2a59b57c8', )
                        ], 
                    profile_type_namings_attributes = [
                        sailpoint.nerm.models.profile_type_1_profile_type_namings_attributes_inner.ProfileType_1_profile_type_namings_attributes_inner(
                            ne_attribute_id = '33f072dd-13b4-41e1-8ea0-16f2a59b57c8', 
                            order = 0, )
                        ], )
)

```
[[Back to top]](#) 

