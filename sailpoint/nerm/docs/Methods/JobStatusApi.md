---
id: job-status
title: Job_status
pagination_label: job_status
sidebar_label: job_status
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'job_status', 'job_status'] 
slug: /tools/sdk/python//methods/job-status
tags: ['SDK', 'Software Development Kit', 'job_status', 'job_status']
---

# sailpoint.nerm.JobStatusApi
   
All URIs are relative to *https://acmeco.nonemployee.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get-job-status**](#get-job-status) | **GET** `/job_status` | Get bulk job status


## get-job-status
Get bulk job status
Retrieve the status of a bulk job

[API Spec](https://developer.sailpoint.com/docs/api//get-job-status)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
  Query | job_id | **str** | True  | The id of the job returned from a POST or PATCH endpoint that resulted in a job being created

### Return type
[**GetJobStatus200Response**](../models/get-job-status200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | GetJobStatus200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.job_status_api import JobStatusApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.get_job_status200_response import GetJobStatus200Response
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    job_id = 'c5e1dd38-7e29-464f-a0da-0c0d886d022a' # str | The id of the job returned from a POST or PATCH endpoint that resulted in a job being created # str | The id of the job returned from a POST or PATCH endpoint that resulted in a job being created

    try:
        # Get bulk job status
        
        results = JobStatusApi(api_client).get_job_status(job_id=job_id)
        # Below is a request that includes all optional parameters
        # results = JobStatusApi(api_client).get_job_status(job_id)
        print("The response of JobStatusApi->get_job_status:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling JobStatusApi->get_job_status: %s\n" % e)
```



[[Back to top]](#) 



