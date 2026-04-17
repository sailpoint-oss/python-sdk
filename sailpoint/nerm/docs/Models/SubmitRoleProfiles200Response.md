---
id: submit-role-profiles200-response
title: SubmitRoleProfiles200Response
pagination_label: SubmitRoleProfiles200Response
sidebar_label: SubmitRoleProfiles200Response
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'SubmitRoleProfiles200Response', 'SubmitRoleProfiles200Response'] 
slug: /tools/sdk/python//models/submit-role-profiles200-response
tags: ['SDK', 'Software Development Kit', 'SubmitRoleProfiles200Response', 'SubmitRoleProfiles200Response']
---

# SubmitRoleProfiles200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role_profiles** | [**[]RoleProfile**](role-profile) |  | [optional] 
**info** | **str** |  | [optional] 
**job_status** | [**JobJobStatus**](job-job-status) |  | [optional] 
**status** | **int** |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.submit_role_profiles200_response import SubmitRoleProfiles200Response

submit_role_profiles200_response = SubmitRoleProfiles200Response(
role_profiles=[
                    sailpoint.nerm.models.role_profile.RoleProfile(
                        id = '', 
                        uid = '', 
                        role_id = '', 
                        profile_id = '', )
                    ],
info='job has started',
job_status=sailpoint.nerm.models.job_job_status.Job_job_status(
                    job_id = '3ce88e47ad6dba2ddf349d21', 
                    status = 'queued', ),
status=200
)

```
[[Back to top]](#) 

