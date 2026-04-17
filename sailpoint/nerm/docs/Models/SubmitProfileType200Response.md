---
id: submit-profile-type200-response
title: SubmitProfileType200Response
pagination_label: SubmitProfileType200Response
sidebar_label: SubmitProfileType200Response
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'SubmitProfileType200Response', 'SubmitProfileType200Response'] 
slug: /tools/sdk/python//models/submit-profile-type200-response
tags: ['SDK', 'Software Development Kit', 'SubmitProfileType200Response', 'SubmitProfileType200Response']
---

# SubmitProfileType200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile_type** | [**ProfileType**](profile-type) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.submit_profile_type200_response import SubmitProfileType200Response

submit_profile_type200_response = SubmitProfileType200Response(
profile_type=sailpoint.nerm.models.profile_type.ProfileType(
                    id = '33f072dd-13b4-41e1-8ea0-16f2a59b57c8', 
                    uid = 'ptUid', 
                    name = 'Worker', 
                    category = 'employee', 
                    bypass_dup_protection = False, 
                    archived = False, 
                    permitted_role_ids = [33f072dd-13b4-41e1-8ea0-16f2a59b57c8], 
                    isc_synced = False, 
                    profile_type_dup_attributes = [
                        sailpoint.nerm.models.profile_type_profile_type_dup_attributes_inner.ProfileType_profile_type_dup_attributes_inner(
                            id = '33f072dd-13b4-41e1-8ea0-16f2a59b57c8', 
                            uid = 'attribute-uid', 
                            profile_type_id = '33f072dd-13b4-41e1-8ea0-16f2a59b57c8', 
                            ne_attribute_id = '33f072dd-13b4-41e1-8ea0-16f2a59b57c8', )
                        ], 
                    profile_type_namings = [
                        sailpoint.nerm.models.profile_type_profile_type_namings_inner.ProfileType_profile_type_namings_inner(
                            id = '33f072dd-13b4-41e1-8ea0-16f2a59b57c8', 
                            uid = 'profile-type-name', 
                            profile_type_id = '33f072dd-13b4-41e1-8ea0-16f2a59b57c8', 
                            ne_attribute_id = '33f072dd-13b4-41e1-8ea0-16f2a59b57c8', 
                            order = 0, )
                        ], )
)

```
[[Back to top]](#) 

