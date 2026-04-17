---
id: get-job-status200-response
title: GetJobStatus200Response
pagination_label: GetJobStatus200Response
sidebar_label: GetJobStatus200Response
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'GetJobStatus200Response', 'GetJobStatus200Response'] 
slug: /tools/sdk/python//models/get-job-status200-response
tags: ['SDK', 'Software Development Kit', 'GetJobStatus200Response', 'GetJobStatus200Response']
---

# GetJobStatus200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uid** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**job_type** | **str** |  | [optional] 
**job_data** | [**[]GetJobStatus200ResponseJobDataInner**](get-job-status200-response-job-data-inner) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.get_job_status200_response import GetJobStatus200Response

get_job_status200_response = GetJobStatus200Response(
uid='',
status='complete',
job_type='import',
job_data=[
                    sailpoint.nerm.models.get_job_status_200_response_job_data_inner.getJobStatus_200_response_job_data_inner(
                        user_id = '', 
                        manager_id = '', 
                        errors = [
                            'Validation error for record in job'
                            ], )
                    ]
)

```
[[Back to top]](#) 

