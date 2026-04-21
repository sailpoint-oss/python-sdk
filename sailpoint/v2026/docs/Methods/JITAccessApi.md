---
id: v2026-jit-access
title: JIT_Access
pagination_label: JIT_Access
sidebar_label: JIT_Access
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'JIT_Access', 'V2026JIT_Access'] 
slug: /tools/sdk/python/v2026/methods/jit-access
tags: ['SDK', 'Software Development Kit', 'JIT_Access', 'V2026JIT_Access']
---

# sailpoint.v2026.JITAccessApi
  Use these APIs to configure JIT provisioning activation policy for the tenant.
OAuth scopes: **idn:jit-policy:read** and **idn:jit-policy:manage** (get config), **idn:jit-policy:update** and **idn:jit-policy:manage** (update config). JIT activation workflow APIs use **idn:jit-activation-workflow:*** scopes (activate, extend, deactivate, manage, and **idn:jit-activation-workflow-internal:manage**).
For REST contract details, use the JIT Access operations in this specification and the [SailPoint API documentation](https://developer.sailpoint.com/idn/api/).
 
All URIs are relative to *https://sailpoint.api.identitynow.com/v2026*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get-jit-activation-config**](#get-jit-activation-config) | **GET** `/jit-activation-config/{configType}` | Get JIT activation policy configuration
[**patch-jit-activation-config**](#patch-jit-activation-config) | **PATCH** `/jit-activation-config/{configType}` | Update JIT activation policy configuration


## get-jit-activation-config
Get JIT activation policy configuration
Returns the tenant's current JIT activation policy configuration, including governed entitlement IDs, activation and extension time limits, default periods, notification settings, and whether the policy applies to future assignments.

The tenant comes from the authenticated request context (not the URL). Use **configType** to select which configuration to read. Returns **404** if that configuration has not been stored yet.

**User level:** POLICY_ADMIN (policy administrator).


[API Spec](https://developer.sailpoint.com/docs/api/v2026/get-jit-activation-config)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | config_type | **str** | True  | Configuration kind to read. Only **policy** (JIT activation policy) is supported today. 

### Return type
[**JITActivationConfigResponse**](../models/jit-activation-config-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Current JIT activation policy configuration, including limits, entitlements in scope, and notification-related fields. | JITActivationConfigResponse |  -  |
400 | Client Error - Returned if the request body is invalid. | ErrorResponseDto |  -  |
401 | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. | GetAccessRequestConfig401Response |  -  |
403 | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. | ErrorResponseDto |  -  |
404 | Not Found - returned if the request URL refers to a resource or object that does not exist | ErrorResponseDto |  -  |
429 | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. | GetAccessRequestConfig429Response |  -  |
500 | Internal Server Error - Returned if there is an unexpected error. | ErrorResponseDto |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.v2026.api.jit_access_api import JITAccessApi
from sailpoint.v2026.api_client import ApiClient
from sailpoint.v2026.models.jit_activation_config_response import JITActivationConfigResponse
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    config_type = 'policy' # str | Configuration kind to read. Only **policy** (JIT activation policy) is supported today.  # str | Configuration kind to read. Only **policy** (JIT activation policy) is supported today. 

    try:
        # Get JIT activation policy configuration
        
        results = JITAccessApi(api_client).get_jit_activation_config(config_type=config_type)
        # Below is a request that includes all optional parameters
        # results = JITAccessApi(api_client).get_jit_activation_config(config_type)
        print("The response of JITAccessApi->get_jit_activation_config:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling JITAccessApi->get_jit_activation_config: %s\n" % e)
```



[[Back to top]](#) 

## patch-jit-activation-config
Update JIT activation policy configuration
Updates the tenant's JIT activation policy configuration by applying one or more **replace** operations (same shape as JSON Patch: **op**, **path**, **value**). Use this to change entitlement lists, max/default activation and extension durations, notification recipients or template, and the apply-to-future-assignments flag.

The body must be a non-empty array. Only **replace** is supported; each **path** must be one of the values documented on the request item schema. The tenant is taken from the request context. **configType** selects which configuration to update. Returns **404** if the configuration does not exist, or **400** for an empty body, unknown **configType**, or invalid path/value.

**User level:** POLICY_ADMIN (policy administrator).


[API Spec](https://developer.sailpoint.com/docs/api/v2026/patch-jit-activation-config)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | config_type | **str** | True  | Configuration kind to update. Only **policy** (JIT activation policy) is supported today. 
 Body  | jit_access_operation_request | [**[]JitAccessOperationRequest**](../models/jit-access-operation-request) | True  | 

### Return type
[**JITActivationConfigResponse**](../models/jit-activation-config-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Full JIT activation policy configuration after applying all requested replace operations. | JITActivationConfigResponse |  -  |
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
from sailpoint.v2026.api.jit_access_api import JITAccessApi
from sailpoint.v2026.api_client import ApiClient
from sailpoint.v2026.models.jit_activation_config_response import JITActivationConfigResponse
from sailpoint.v2026.models.jit_access_operation_request import JitAccessOperationRequest
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    config_type = 'policy' # str | Configuration kind to update. Only **policy** (JIT activation policy) is supported today.  # str | Configuration kind to update. Only **policy** (JIT activation policy) is supported today. 
    jit_access_operation_request = '''[sailpoint.v2026.JitAccessOperationRequest()]''' # List[JitAccessOperationRequest] | 

    try:
        # Update JIT activation policy configuration
        new_jit_access_operation_request = JitAccessOperationRequest.from_json(jit_access_operation_request)
        results = JITAccessApi(api_client).patch_jit_activation_config(config_type=config_type, jit_access_operation_request=new_jit_access_operation_request)
        # Below is a request that includes all optional parameters
        # results = JITAccessApi(api_client).patch_jit_activation_config(config_type, new_jit_access_operation_request)
        print("The response of JITAccessApi->patch_jit_activation_config:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling JITAccessApi->patch_jit_activation_config: %s\n" % e)
```



[[Back to top]](#) 



