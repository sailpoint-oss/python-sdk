---
id: v2026-jit-activations
title: JIT_Activations
pagination_label: JIT_Activations
sidebar_label: JIT_Activations
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'JIT_Activations', 'V2026JIT_Activations'] 
slug: /tools/sdk/python/v2026/methods/jit-activations
tags: ['SDK', 'Software Development Kit', 'JIT_Activations', 'V2026JIT_Activations']
---

# sailpoint.v2026.JITActivationsApi
  Use this API to start and manage Just-In-Time (JIT) Privileged activation workflows for entitlement connections.
 
All URIs are relative to *https://sailpoint.api.identitynow.com/v2026*

Method | HTTP request | Description
------------- | ------------- | -------------
[**start-activate-workflow**](#start-activate-workflow) | **POST** `/jit-activations/activate` | Start JIT activation workflow
[**start-deactivate-workflow**](#start-deactivate-workflow) | **POST** `/jit-activations/deactivate` | Deactivate JIT activation workflow
[**start-extend-workflow**](#start-extend-workflow) | **POST** `/jit-activations/extend` | Extend JIT activation workflow


## start-activate-workflow
Start JIT activation workflow
Starts a JIT Privileged (JIT P) activation workflow for the given entitlement connection and duration.
The service performs quick validation; the workflow performs additional validation.

The response is returned with HTTP 202 Accepted while the workflow initializes.


[API Spec](https://developer.sailpoint.com/docs/api/v2026/start-activate-workflow)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
 Body  | jit_activation_activate_request | [**JitActivationActivateRequest**](../models/jit-activation-activate-request) | True  | 

### Return type
[**JitActivationActivateResponse**](../models/jit-activation-activate-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
202 | Accepted. The activation workflow was accepted and is running.  | JitActivationActivateResponse |  -  |
400 | Client Error - Returned if the request body is invalid. | ErrorResponseDto |  -  |
401 | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. | GetAccessRequestConfig401Response |  -  |
403 | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. | ErrorResponseDto |  -  |
429 | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. | GetAccessRequestConfig429Response |  -  |
500 | Internal Server Error - Returned if there is an unexpected error. | ErrorResponseDto |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.v2026.api.jit_activations_api import JITActivationsApi
from sailpoint.v2026.api_client import ApiClient
from sailpoint.v2026.models.jit_activation_activate_request import JitActivationActivateRequest
from sailpoint.v2026.models.jit_activation_activate_response import JitActivationActivateResponse
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    jit_activation_activate_request = '''{
          "activationPeriodMins" : 120,
          "connectionId" : "757fb803-9024-5861-e510-83a56e4c5bd3"
        }''' # JitActivationActivateRequest | 

    try:
        # Start JIT activation workflow
        new_jit_activation_activate_request = JitActivationActivateRequest.from_json(jit_activation_activate_request)
        results = JITActivationsApi(api_client).start_activate_workflow(jit_activation_activate_request=new_jit_activation_activate_request)
        # Below is a request that includes all optional parameters
        # results = JITActivationsApi(api_client).start_activate_workflow(new_jit_activation_activate_request)
        print("The response of JITActivationsApi->start_activate_workflow:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling JITActivationsApi->start_activate_workflow: %s\n" % e)
```



[[Back to top]](#) 

## start-deactivate-workflow
Deactivate JIT activation workflow
Sends a signal to a running JIT Privileged (JIT P) activation workflow to deactivate.

This request cannot be applied to a workflow that does not exist or whose execution has already completed.
The client receives an error response in those cases.

The response is returned with HTTP 202 Accepted after the signal is sent.


[API Spec](https://developer.sailpoint.com/docs/api/v2026/start-deactivate-workflow)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
 Body  | jit_activation_deactivate_request | [**JitActivationDeactivateRequest**](../models/jit-activation-deactivate-request) | True  | 

### Return type
[**JitActivationDeactivateResponse**](../models/jit-activation-deactivate-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
202 | Accepted. The deactivation signal was sent to the workflow.  | JitActivationDeactivateResponse |  -  |
400 | Client Error - Returned if the request body is invalid. | ErrorResponseDto |  -  |
401 | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. | GetAccessRequestConfig401Response |  -  |
403 | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. | ErrorResponseDto |  -  |
404 | Not Found - returned if the request URL refers to a resource or object that does not exist | ErrorResponseDto |  -  |
429 | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. | GetAccessRequestConfig429Response |  -  |
500 | Internal Server Error - Returned if there is an unexpected error. | ErrorResponseDto |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.v2026.api.jit_activations_api import JITActivationsApi
from sailpoint.v2026.api_client import ApiClient
from sailpoint.v2026.models.jit_activation_deactivate_request import JitActivationDeactivateRequest
from sailpoint.v2026.models.jit_activation_deactivate_response import JitActivationDeactivateResponse
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    jit_activation_deactivate_request = '''{
          "connectionId" : "757fb803-9024-5861-e510-83a56e4c5bd3"
        }''' # JitActivationDeactivateRequest | 

    try:
        # Deactivate JIT activation workflow
        new_jit_activation_deactivate_request = JitActivationDeactivateRequest.from_json(jit_activation_deactivate_request)
        results = JITActivationsApi(api_client).start_deactivate_workflow(jit_activation_deactivate_request=new_jit_activation_deactivate_request)
        # Below is a request that includes all optional parameters
        # results = JITActivationsApi(api_client).start_deactivate_workflow(new_jit_activation_deactivate_request)
        print("The response of JITActivationsApi->start_deactivate_workflow:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling JITActivationsApi->start_deactivate_workflow: %s\n" % e)
```



[[Back to top]](#) 

## start-extend-workflow
Extend JIT activation workflow
Sends a signal to a running JIT Privileged (JIT P) activation workflow to extend the activation period
by the requested number of minutes.

This request cannot be applied to a workflow that does not exist or whose execution has already completed.
The client receives an error response in those cases.

The response is returned with HTTP 202 Accepted after the signal is sent.


[API Spec](https://developer.sailpoint.com/docs/api/v2026/start-extend-workflow)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
 Body  | jit_activation_extend_request | [**JitActivationExtendRequest**](../models/jit-activation-extend-request) | True  | 

### Return type
[**JitActivationExtendResponse**](../models/jit-activation-extend-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
202 | Accepted. The extend signal was sent to the workflow.  | JitActivationExtendResponse |  -  |
400 | Client Error - Returned if the request body is invalid. | ErrorResponseDto |  -  |
401 | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. | GetAccessRequestConfig401Response |  -  |
403 | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. | ErrorResponseDto |  -  |
404 | Not Found - returned if the request URL refers to a resource or object that does not exist | ErrorResponseDto |  -  |
429 | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. | GetAccessRequestConfig429Response |  -  |
500 | Internal Server Error - Returned if there is an unexpected error. | ErrorResponseDto |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.v2026.api.jit_activations_api import JITActivationsApi
from sailpoint.v2026.api_client import ApiClient
from sailpoint.v2026.models.jit_activation_extend_request import JitActivationExtendRequest
from sailpoint.v2026.models.jit_activation_extend_response import JitActivationExtendResponse
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    jit_activation_extend_request = '''{
          "activationPeriodExtensionMins" : 120,
          "connectionId" : "757fb803-9024-5861-e510-83a56e4c5bd3"
        }''' # JitActivationExtendRequest | 

    try:
        # Extend JIT activation workflow
        new_jit_activation_extend_request = JitActivationExtendRequest.from_json(jit_activation_extend_request)
        results = JITActivationsApi(api_client).start_extend_workflow(jit_activation_extend_request=new_jit_activation_extend_request)
        # Below is a request that includes all optional parameters
        # results = JITActivationsApi(api_client).start_extend_workflow(new_jit_activation_extend_request)
        print("The response of JITActivationsApi->start_extend_workflow:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling JITActivationsApi->start_extend_workflow: %s\n" % e)
```



[[Back to top]](#) 



