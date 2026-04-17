---
id: get-schema-mapped-profiles-collection200-response
title: GetSchemaMappedProfilesCollection200Response
pagination_label: GetSchemaMappedProfilesCollection200Response
sidebar_label: GetSchemaMappedProfilesCollection200Response
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'GetSchemaMappedProfilesCollection200Response', 'GetSchemaMappedProfilesCollection200Response'] 
slug: /tools/sdk/python//models/get-schema-mapped-profiles-collection200-response
tags: ['SDK', 'Software Development Kit', 'GetSchemaMappedProfilesCollection200Response', 'GetSchemaMappedProfilesCollection200Response']
---

# GetSchemaMappedProfilesCollection200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profiles** | [**[]Profile**](profile) |  | [optional] 
**metadata** | [**MetadataWithAfterId**](metadata-with-after-id) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.get_schema_mapped_profiles_collection200_response import GetSchemaMappedProfilesCollection200Response

get_schema_mapped_profiles_collection200_response = GetSchemaMappedProfilesCollection200Response(
profiles=[
                    sailpoint.nerm.models.profile.Profile(
                        id = '33f072dd-13b4-41e1-8ea0-16f2a59b57c8', 
                        uid = 'profileUid', 
                        name = 'Profile Name', 
                        profile_type_id = '33f072dd-13b4-41e1-8ea0-16f2a59b57c8', 
                        status = 'Active', 
                        id_proofing_status = 'pending', 
                        created_at = '2023-11-21T14:23:54.256-05:00', 
                        updated_at = '2023-11-21T14:23:54.256-05:00', 
                        attributes = {Non-Employee Profile ID=The Non-Employee Profile ID (will be returned for assignments, to be used during correlation configuration), text_attribute_uid=static text, date_attribute_uid=01/15/2020, profile_select_attribute_uid=Profile Name, profile_search_attribute_uid=Profile Name, multiple_profile_search_attribute_uid=Profile Name,Second Profile Name,Third Profile Name, multiple_profile_select_attribute_uid=Profile Name,Second Profile Name,Third Profile Name, contributor_select_attribute_uid=User Name (user_email@test.com), contributor_search_attribute_uid=User Name (user_email@test.com), multiple_contributor_search_attribute_uid=User Name (user_email@test.com),Second User Name (user_email@test.com),Third User Name (user_email@test.com), owner_select_attribute_uid=User Name (user_email@test.com), owner_search_attribute_uid=User Name (user_email@test.com), dropdown_attribute_uid=yes, no, tags_attribute_uid=yes, no, checkbox_attribute_uid=yes, no, text_area_uid=static text, radio_attribute_uid=yes, no}, )
                    ],
metadata=sailpoint.nerm.models.metadata_with_after_id.MetadataWithAfterId(
                    limit = 56, 
                    offset = 56, 
                    total = 56, 
                    next = '/endpoint?limit=10&offset=60', 
                    previous = '/endpoint?limit=10&offset=40', 
                    after_id = '4eaa719f-4312-4c5b-9264-d0eb04d4a02a', )
)

```
[[Back to top]](#) 

