---
id: get-profile-types200-response
title: GetProfileTypes200Response
pagination_label: GetProfileTypes200Response
sidebar_label: GetProfileTypes200Response
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'GetProfileTypes200Response', 'GetProfileTypes200Response'] 
slug: /tools/sdk/python//models/get-profile-types200-response
tags: ['SDK', 'Software Development Kit', 'GetProfileTypes200Response', 'GetProfileTypes200Response']
---

# GetProfileTypes200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile_types** | [**[]ProfileType**](profile-type) |  | [optional] 
**metadata** | [**Metadata**](metadata) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.get_profile_types200_response import GetProfileTypes200Response

get_profile_types200_response = GetProfileTypes200Response(
profile_types=[
                    sailpoint.nerm.models.profile_type.ProfileType(
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
                    ],
metadata=sailpoint.nerm.models.metadata.Metadata(
                    limit = 56, 
                    offset = 56, 
                    total = 56, 
                    next = '/endpoint?limit=10&offset=60', 
                    previous = '/endpoint?limit=10&offset=40', )
)

```
[[Back to top]](#) 

