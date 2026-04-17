---
id: delete-profiles200-response
title: DeleteProfiles200Response
pagination_label: DeleteProfiles200Response
sidebar_label: DeleteProfiles200Response
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'DeleteProfiles200Response', 'DeleteProfiles200Response'] 
slug: /tools/sdk/python//models/delete-profiles200-response
tags: ['SDK', 'Software Development Kit', 'DeleteProfiles200Response', 'DeleteProfiles200Response']
---

# DeleteProfiles200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profiles** | [**[]Profile**](profile) |  | [optional] 
**info** | **str** |  | [optional] 
**job_status** | [**JobJobStatus**](job-job-status) |  | [optional] 
**status** | **int** |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.delete_profiles200_response import DeleteProfiles200Response

delete_profiles200_response = DeleteProfiles200Response(
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
info='job has started',
job_status=sailpoint.nerm.models.job_job_status.Job_job_status(
                    job_id = '3ce88e47ad6dba2ddf349d21', 
                    status = 'queued', ),
status=200
)

```
[[Back to top]](#) 

