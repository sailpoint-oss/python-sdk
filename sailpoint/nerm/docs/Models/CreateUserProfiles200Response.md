---
id: create-user-profiles200-response
title: CreateUserProfiles200Response
pagination_label: CreateUserProfiles200Response
sidebar_label: CreateUserProfiles200Response
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'CreateUserProfiles200Response', 'CreateUserProfiles200Response'] 
slug: /tools/sdk/python//models/create-user-profiles200-response
tags: ['SDK', 'Software Development Kit', 'CreateUserProfiles200Response', 'CreateUserProfiles200Response']
---

# CreateUserProfiles200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_profiles** | [**[]UserProfile**](user-profile) |  | [optional] 
**info** | **str** |  | [optional] 
**job_status** | [**JobJobStatus**](job-job-status) |  | [optional] 
**status** | **int** |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.create_user_profiles200_response import CreateUserProfiles200Response

create_user_profiles200_response = CreateUserProfiles200Response(
user_profiles=[
                    sailpoint.nerm.models.user_profile.UserProfile(
                        id = '', 
                        uid = '', 
                        user_id = '', 
                        profile_id = '', 
                        ne_attribute_id = '', 
                        relationship_type = 'owner', )
                    ],
info='job has started',
job_status=sailpoint.nerm.models.job_job_status.Job_job_status(
                    job_id = '3ce88e47ad6dba2ddf349d21', 
                    status = 'queued', ),
status=200
)

```
[[Back to top]](#) 

