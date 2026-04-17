---
id: submit-user-roles200-response
title: SubmitUserRoles200Response
pagination_label: SubmitUserRoles200Response
sidebar_label: SubmitUserRoles200Response
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'SubmitUserRoles200Response', 'SubmitUserRoles200Response'] 
slug: /tools/sdk/python//models/submit-user-roles200-response
tags: ['SDK', 'Software Development Kit', 'SubmitUserRoles200Response', 'SubmitUserRoles200Response']
---

# SubmitUserRoles200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_roles** | [**[]UserRole**](user-role) |  | [optional] 
**info** | **str** |  | [optional] 
**job_status** | [**JobJobStatus**](job-job-status) |  | [optional] 
**status** | **int** |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.submit_user_roles200_response import SubmitUserRoles200Response

submit_user_roles200_response = SubmitUserRoles200Response(
user_roles=[
                    sailpoint.nerm.models.user_role.UserRole(
                        id = '', 
                        uid = '', 
                        user_id = '', 
                        role_id = '', )
                    ],
info='job has started',
job_status=sailpoint.nerm.models.job_job_status.Job_job_status(
                    job_id = '3ce88e47ad6dba2ddf349d21', 
                    status = 'queued', ),
status=200
)

```
[[Back to top]](#) 

