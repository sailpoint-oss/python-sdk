---
id: machine-account-subtypes
title: Machine_Account_Subtypes
pagination_label: Machine_Account_Subtypes
sidebar_label: Machine_Account_Subtypes
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Machine_Account_Subtypes', 'Machine_Account_Subtypes'] 
slug: /tools/sdk/python/v1/methods/machine-account-subtypes
tags: ['SDK', 'Software Development Kit', 'Machine_Account_Subtypes', 'Machine_Account_Subtypes']
---

# sailpoint.machine_account_subtypes_v1.MachineAccountSubtypesV1Api
  Use this API to get, update, and delete machine account subtype for sources.
 
All URIs are relative to *https://sailpoint.api.identitynow.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete-machine-account-subtype-v1**](#delete-machine-account-subtype-v1) | **DELETE** `/source-subtypes/v1/{subtypeId}` | Delete subtype by ID
[**get-source-subtype-by-id-v1**](#get-source-subtype-by-id-v1) | **GET** `/source-subtypes/v1/{subtypeId}` | Get subtype by ID
[**patch-machine-account-subtype-v1**](#patch-machine-account-subtype-v1) | **PATCH** `/source-subtypes/v1/{subtypeId}` | Patch subtype by ID


## delete-machine-account-subtype-v1
Delete subtype by ID
Delete a machine account subtype by subtype ID.

Note: If subtype has approval settings or entitlement for machine account creation enablement then it'll be also deleted.

[API Spec](https://developer.sailpoint.com/docs/api/v1/delete-machine-account-subtype-v1)

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
400 | Client Error - Returned if the request body is invalid. | Errorresponsedto |  -  |
401 | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. | GetSourceSubtypeByIdV1401Response |  -  |
403 | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. | Errorresponsedto |  -  |
429 | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. | GetSourceSubtypeByIdV1429Response |  -  |
500 | Internal Server Error - Returned if there is an unexpected error. | Errorresponsedto |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.machine_account_subtypes_v1.api.machine_account_subtypes_v1_api import MachineAccountSubtypesV1Api
from sailpoint.machine_account_subtypes_v1.api_client import ApiClient
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    subtype_id = '6d28b7c1-620c-49c6-b6d5-cbf81eb4b5fa' # str | The ID of the subtype. # str | The ID of the subtype.

    try:
        # Delete subtype by ID
        
        MachineAccountSubtypesV1Api(api_client).delete_machine_account_subtype_v1(subtype_id=subtype_id)
        # Below is a request that includes all optional parameters
        # MachineAccountSubtypesV1Api(api_client).delete_machine_account_subtype_v1(subtype_id)
    except Exception as e:
        print("Exception when calling MachineAccountSubtypesV1Api->delete_machine_account_subtype_v1: %s\n" % e)
```



[[Back to top]](#) 

## get-source-subtype-by-id-v1
Get subtype by ID
Get a machine account subtype by subtype ID.

[API Spec](https://developer.sailpoint.com/docs/api/v1/get-source-subtype-by-id-v1)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | subtype_id | **str** | True  | The ID of the subtype.

### Return type
[**Sourcesubtypewithsource**](../models/sourcesubtypewithsource)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Machine account subtype object. | Sourcesubtypewithsource |  -  |
400 | Client Error - Returned if the request body is invalid. | Errorresponsedto |  -  |
401 | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. | GetSourceSubtypeByIdV1401Response |  -  |
403 | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. | Errorresponsedto |  -  |
404 | Not Found - returned if the request URL refers to a resource or object that does not exist | Errorresponsedto |  -  |
429 | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. | GetSourceSubtypeByIdV1429Response |  -  |
500 | Internal Server Error - Returned if there is an unexpected error. | Errorresponsedto |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.machine_account_subtypes_v1.api.machine_account_subtypes_v1_api import MachineAccountSubtypesV1Api
from sailpoint.machine_account_subtypes_v1.api_client import ApiClient
from sailpoint.machine_account_subtypes_v1.models.sourcesubtypewithsource import Sourcesubtypewithsource
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    subtype_id = '6d28b7c1-620c-49c6-b6d5-cbf81eb4b5fa' # str | The ID of the subtype. # str | The ID of the subtype.

    try:
        # Get subtype by ID
        
        results = MachineAccountSubtypesV1Api(api_client).get_source_subtype_by_id_v1(subtype_id=subtype_id)
        # Below is a request that includes all optional parameters
        # results = MachineAccountSubtypesV1Api(api_client).get_source_subtype_by_id_v1(subtype_id)
        print("The response of MachineAccountSubtypesV1Api->get_source_subtype_by_id_v1:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling MachineAccountSubtypesV1Api->get_source_subtype_by_id_v1: %s\n" % e)
```



[[Back to top]](#) 

## patch-machine-account-subtype-v1
Patch subtype by ID
Update fields of a machine account subtype by subtype ID.
Patchable fields only include: `displayName`, `description`.

[API Spec](https://developer.sailpoint.com/docs/api/v1/patch-machine-account-subtype-v1)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | subtype_id | **str** | True  | The ID of the subtype.
 Body  | request_body | **[]object** | True  | A JSON of updated values [JSON Patch](https://tools.ietf.org/html/rfc6902) standard.

### Return type
[**Sourcesubtypewithsource**](../models/sourcesubtypewithsource)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Updated machine account subtype. | Sourcesubtypewithsource |  -  |
400 | Client Error - Returned if the request body is invalid. | Errorresponsedto |  -  |
401 | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. | GetSourceSubtypeByIdV1401Response |  -  |
403 | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. | Errorresponsedto |  -  |
429 | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. | GetSourceSubtypeByIdV1429Response |  -  |
500 | Internal Server Error - Returned if there is an unexpected error. | Errorresponsedto |  -  |

### HTTP request headers
 - **Content-Type**: application/json-patch+json
 - **Accept**: application/json

### Example

```python
from sailpoint.machine_account_subtypes_v1.api.machine_account_subtypes_v1_api import MachineAccountSubtypesV1Api
from sailpoint.machine_account_subtypes_v1.api_client import ApiClient
from sailpoint.machine_account_subtypes_v1.models.sourcesubtypewithsource import Sourcesubtypewithsource
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    subtype_id = '6d28b7c1-620c-49c6-b6d5-cbf81eb4b5fa' # str | The ID of the subtype. # str | The ID of the subtype.
    request_body = '''[{"op":"replace","path":"/displayName","value":"Test New DisplayName"}]''' # List[object] | A JSON of updated values [JSON Patch](https://tools.ietf.org/html/rfc6902) standard.

    try:
        # Patch subtype by ID
        new_request_body = RequestBody.from_json(request_body)
        results = MachineAccountSubtypesV1Api(api_client).patch_machine_account_subtype_v1(subtype_id=subtype_id, request_body=new_request_body)
        # Below is a request that includes all optional parameters
        # results = MachineAccountSubtypesV1Api(api_client).patch_machine_account_subtype_v1(subtype_id, new_request_body)
        print("The response of MachineAccountSubtypesV1Api->patch_machine_account_subtype_v1:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling MachineAccountSubtypesV1Api->patch_machine_account_subtype_v1: %s\n" % e)
```



[[Back to top]](#) 



