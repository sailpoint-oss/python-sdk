---
id: submit-roles200-response
title: SubmitRoles200Response
pagination_label: SubmitRoles200Response
sidebar_label: SubmitRoles200Response
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'SubmitRoles200Response', 'SubmitRoles200Response'] 
slug: /tools/sdk/python//models/submit-roles200-response
tags: ['SDK', 'Software Development Kit', 'SubmitRoles200Response', 'SubmitRoles200Response']
---

# SubmitRoles200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**roles** | [**[]Role**](role) |  | [optional] 
**info** | **str** |  | [optional] 
**job_status** | [**JobJobStatus**](job-job-status) |  | [optional] 
**status** | **int** |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.submit_roles200_response import SubmitRoles200Response

submit_roles200_response = SubmitRoles200Response(
roles=[
                    sailpoint.nerm.models.role.Role(
                        id = '', 
                        uid = 'sponsors_role', 
                        name = 'Sponsors', 
                        groups = [
                            'ad_group_name'
                            ], )
                    ],
info='job has started',
job_status=sailpoint.nerm.models.job_job_status.Job_job_status(
                    job_id = '3ce88e47ad6dba2ddf349d21', 
                    status = 'queued', ),
status=200
)

```
[[Back to top]](#) 

