---
id: get-job-status200-response-job-data-inner
title: GetJobStatus200ResponseJobDataInner
pagination_label: GetJobStatus200ResponseJobDataInner
sidebar_label: GetJobStatus200ResponseJobDataInner
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'GetJobStatus200ResponseJobDataInner', 'GetJobStatus200ResponseJobDataInner'] 
slug: /tools/sdk/python//models/get-job-status200-response-job-data-inner
tags: ['SDK', 'Software Development Kit', 'GetJobStatus200ResponseJobDataInner', 'GetJobStatus200ResponseJobDataInner']
---

# GetJobStatus200ResponseJobDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | [optional] 
**manager_id** | **str** |  | [optional] 
**errors** | **[]str** |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.get_job_status200_response_job_data_inner import GetJobStatus200ResponseJobDataInner

get_job_status200_response_job_data_inner = GetJobStatus200ResponseJobDataInner(
user_id='',
manager_id='',
errors=[
                    'Validation error for record in job'
                    ]
)

```
[[Back to top]](#) 

