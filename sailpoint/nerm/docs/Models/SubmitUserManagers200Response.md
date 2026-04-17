---
id: submit-user-managers200-response
title: SubmitUserManagers200Response
pagination_label: SubmitUserManagers200Response
sidebar_label: SubmitUserManagers200Response
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'SubmitUserManagers200Response', 'SubmitUserManagers200Response'] 
slug: /tools/sdk/python//models/submit-user-managers200-response
tags: ['SDK', 'Software Development Kit', 'SubmitUserManagers200Response', 'SubmitUserManagers200Response']
---

# SubmitUserManagers200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **str** |  | [optional] 
**job_status** | [**JobJobStatus**](job-job-status) |  | [optional] 
**status** | **int** |  | [optional] 
**user_managers** | [**[]UserManager**](user-manager) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.submit_user_managers200_response import SubmitUserManagers200Response

submit_user_managers200_response = SubmitUserManagers200Response(
info='job has started',
job_status=sailpoint.nerm.models.job_job_status.Job_job_status(
                    job_id = '3ce88e47ad6dba2ddf349d21', 
                    status = 'queued', ),
status=200,
user_managers=[
                    sailpoint.nerm.models.user_manager.UserManager(
                        id = '', 
                        uid = '', 
                        user_id = '', 
                        manager_id = '', )
                    ]
)

```
[[Back to top]](#) 

