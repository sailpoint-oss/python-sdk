---
id: v2026-machine-account-subtypes
title: Machine_Account_Subtypes
pagination_label: Machine_Account_Subtypes
sidebar_label: Machine_Account_Subtypes
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Machine_Account_Subtypes', 'V2026Machine_Account_Subtypes'] 
slug: /tools/sdk/python/v2026/methods/machine-account-subtypes
tags: ['SDK', 'Software Development Kit', 'Machine_Account_Subtypes', 'V2026Machine_Account_Subtypes']
---

# sailpoint.v2026.MachineAccountSubtypesApi
  Use this API to get, update, and delete machine account subtype for sources.
 
All URIs are relative to *https://sailpoint.api.identitynow.com/v2026*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete-machine-account-subtype**](#delete-machine-account-subtype) | **DELETE** `/source-subtypes/{subtypeId}` | Delete subtype by ID
[**get-source-subtype-by-id**](#get-source-subtype-by-id) | **GET** `/source-subtypes/{subtypeId}` | Get subtype by ID
[**patch-machine-account-subtype**](#patch-machine-account-subtype) | **PATCH** `/source-subtypes/{subtypeId}` | Patch subtype by ID


## delete-machine-account-subtype
Delete subtype by ID
Delete a machine account subtype by subtype ID.

Note: If subtype has approval settings or entitlement for machine account creation enablement then it'll be also deleted.

[API Spec](https://developer.sailpoint.com/docs/api/v2026/delete-machine-account-subtype)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | subtype_id | **str** | True  | The ID of the subtype.

### Return type
 (empty response body)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
204 | Subtype deleted successfully. |  |  -  |
400 | Client Error - Returned if the request body is invalid. | ErrorResponseDto |  -  |
401 | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. | GetAccessRequestConfig401Response |  -  |
403 | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. | ErrorResponseDto |  -  |
429 | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. | GetAccessRequestConfig429Response |  -  |
500 | Internal Server Error - Returned if there is an unexpected error. | ErrorResponseDto |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.v2026.api.machine_account_subtypes_api import MachineAccountSubtypesApi
from sailpoint.v2026.api_client import ApiClient
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    subtype_id = '6d28b7c1-620c-49c6-b6d5-cbf81eb4b5fa' # str | The ID of the subtype. # str | The ID of the subtype.

    try:
        # Delete subtype by ID
        
        MachineAccountSubtypesApi(api_client).delete_machine_account_subtype(subtype_id=subtype_id)
        # Below is a request that includes all optional parameters
        # MachineAccountSubtypesApi(api_client).delete_machine_account_subtype(subtype_id)
    except Exception as e:
        print("Exception when calling MachineAccountSubtypesApi->delete_machine_account_subtype: %s\n" % e)
```



[[Back to top]](#) 

## get-source-subtype-by-id
Get subtype by ID
Get a machine account subtype by subtype ID.

[API Spec](https://developer.sailpoint.com/docs/api/v2026/get-source-subtype-by-id)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | subtype_id | **str** | True  | The ID of the subtype.

### Return type
[**SourceSubtypeWithSource**](../models/source-subtype-with-source)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Machine account subtype object. | SourceSubtypeWithSource |  -  |
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
from sailpoint.v2026.api.machine_account_subtypes_api import MachineAccountSubtypesApi
from sailpoint.v2026.api_client import ApiClient
from sailpoint.v2026.models.source_subtype_with_source import SourceSubtypeWithSource
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    subtype_id = '6d28b7c1-620c-49c6-b6d5-cbf81eb4b5fa' # str | The ID of the subtype. # str | The ID of the subtype.

    try:
        # Get subtype by ID
        
        results = MachineAccountSubtypesApi(api_client).get_source_subtype_by_id(subtype_id=subtype_id)
        # Below is a request that includes all optional parameters
        # results = MachineAccountSubtypesApi(api_client).get_source_subtype_by_id(subtype_id)
        print("The response of MachineAccountSubtypesApi->get_source_subtype_by_id:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling MachineAccountSubtypesApi->get_source_subtype_by_id: %s\n" % e)
```



[[Back to top]](#) 

## patch-machine-account-subtype
Patch subtype by ID
Update fields of a machine account subtype by subtype ID.
Patchable fields only include: `displayName`, `description`.

[API Spec](https://developer.sailpoint.com/docs/api/v2026/patch-machine-account-subtype)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | subtype_id | **str** | True  | The ID of the subtype.
 Body  | request_body | **[]object** | True  | A JSON of updated values [JSON Patch](https://tools.ietf.org/html/rfc6902) standard.

### Return type
[**SourceSubtypeWithSource**](../models/source-subtype-with-source)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Updated machine account subtype. | SourceSubtypeWithSource |  -  |
400 | Client Error - Returned if the request body is invalid. | ErrorResponseDto |  -  |
401 | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. | GetAccessRequestConfig401Response |  -  |
403 | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. | ErrorResponseDto |  -  |
429 | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. | GetAccessRequestConfig429Response |  -  |
500 | Internal Server Error - Returned if there is an unexpected error. | ErrorResponseDto |  -  |

### HTTP request headers
 - **Content-Type**: application/json-patch+json
 - **Accept**: application/json

### Example

```python
from sailpoint.v2026.api.machine_account_subtypes_api import MachineAccountSubtypesApi
from sailpoint.v2026.api_client import ApiClient
from sailpoint.v2026.models.source_subtype_with_source import SourceSubtypeWithSource
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    subtype_id = '6d28b7c1-620c-49c6-b6d5-cbf81eb4b5fa' # str | The ID of the subtype. # str | The ID of the subtype.
    request_body = '''[{op=replace, path=/displayName, value=Test New DisplayName}]''' # List[object] | A JSON of updated values [JSON Patch](https://tools.ietf.org/html/rfc6902) standard.

    try:
        # Patch subtype by ID
        new_request_body = RequestBody.from_json(request_body)
        results = MachineAccountSubtypesApi(api_client).patch_machine_account_subtype(subtype_id=subtype_id, request_body=new_request_body)
        # Below is a request that includes all optional parameters
        # results = MachineAccountSubtypesApi(api_client).patch_machine_account_subtype(subtype_id, new_request_body)
        print("The response of MachineAccountSubtypesApi->patch_machine_account_subtype:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling MachineAccountSubtypesApi->patch_machine_account_subtype: %s\n" % e)
```



[[Back to top]](#) 



