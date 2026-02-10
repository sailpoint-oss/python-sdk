---
id: v2025-role-propagation
title: Role_Propagation
pagination_label: Role_Propagation
sidebar_label: Role_Propagation
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Role_Propagation', 'V2025Role_Propagation'] 
slug: /tools/sdk/python/v2025/methods/role-propagation
tags: ['SDK', 'Software Development Kit', 'Role_Propagation', 'V2025Role_Propagation']
---

# sailpoint.v2025.RolePropagationApi
  Role Change Propagation ensures that any changes to the composition of a role’s access objects 
(entitlements, access profiles, or dimensions) are applied to all member identities. 
For example: If an entitlement is removed from a role, all identities assigned to that role 
should lose access to that entitlement as part of this process.
 
All URIs are relative to *https://sailpoint.api.identitynow.com/v2025*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel-role-propagation**](#cancel-role-propagation) | **POST** `/role-propagation/terminate` | Terminate Role Propagation process
[**get-ongoing-role-propagation**](#get-ongoing-role-propagation) | **GET** `/role-propagation/is-running` | Get ongoing Role Propagation process
[**get-role-propagation-status**](#get-role-propagation-status) | **GET** `/role-propagation/{rolePropagationId}/status` | Get status of Role-Propagation process
[**start-role-propagation**](#start-role-propagation) | **POST** `/role-propagation` | Initiate Role Propagation process


## cancel-role-propagation
:::warning experimental 
This API is currently in an experimental state. The API is subject to change based on feedback and further testing. You must include the X-SailPoint-Experimental header and set it to `true` to use this endpoint.
:::
:::tip setting x-sailpoint-experimental header
 on the configuration object you can set the `x-sailpoint-experimental` header to `true' to enable all experimantl endpoints within the SDK.
 Example:
 ```python
   configuration = Configuration()
   configuration.experimental = True
 ```
:::
Terminate Role Propagation process
This endpoint terminates the ongoing role change propagation process for a tenant.

[API Spec](https://developer.sailpoint.com/docs/api/v2025/cancel-role-propagation)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
   | x_sail_point_experimental | **str** | True  (default to 'true') | Use this header to enable this experimental API.

### Return type
 (empty response body)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
204 | Role Propagation has been successfully terminated. |  |  -  |
400 | Client Error - Returned if the request body is invalid. | ErrorResponseDto |  -  |
401 | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. | ListAccessProfiles401Response |  -  |
403 | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. | ErrorResponseDto |  -  |
429 | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. | ListAccessProfiles429Response |  -  |
500 | Internal Server Error - Returned if there is an unexpected error. | ErrorResponseDto |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.v2025.api.role_propagation_api import RolePropagationApi
from sailpoint.v2025.api_client import ApiClient
from sailpoint.configuration import Configuration
configuration = Configuration()

configuration.experimental = True

with ApiClient(configuration) as api_client:
    x_sail_point_experimental = 'true' # str | Use this header to enable this experimental API. (default to 'true') # str | Use this header to enable this experimental API. (default to 'true')

    try:
        # Terminate Role Propagation process
        
        RolePropagationApi(api_client).cancel_role_propagation(x_sail_point_experimental=x_sail_point_experimental)
        # Below is a request that includes all optional parameters
        # RolePropagationApi(api_client).cancel_role_propagation(x_sail_point_experimental)
    except Exception as e:
        print("Exception when calling RolePropagationApi->cancel_role_propagation: %s\n" % e)
```



[[Back to top]](#) 

## get-ongoing-role-propagation
:::warning experimental 
This API is currently in an experimental state. The API is subject to change based on feedback and further testing. You must include the X-SailPoint-Experimental header and set it to `true` to use this endpoint.
:::
:::tip setting x-sailpoint-experimental header
 on the configuration object you can set the `x-sailpoint-experimental` header to `true' to enable all experimantl endpoints within the SDK.
 Example:
 ```python
   configuration = Configuration()
   configuration.experimental = True
 ```
:::
Get ongoing Role Propagation process
This endpoint returns the information of ongoing role change propagation process for a tenant. It returns the information whether the role propagation process is currently running or not, If it is running it returns the details of the ongoing role propagation process. The execution stage of the role propagation process can be one of the following: - PENDING - The role propagation process is queued to be executed. - DATA_AGGREGATION_RUNNING - The role propagation process is currently aggregating data. - LAUNCH_PROVISIONING - The role propagation process has started to provision the access to the identities. - SUCCEEDED - The role propagation process has successfully completed. - FAILED - The role propagation process has failed. - TERMINATED - The role propagation process was externally terminated.

[API Spec](https://developer.sailpoint.com/docs/api/v2025/get-ongoing-role-propagation)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
   | x_sail_point_experimental | **str** | True  (default to 'true') | Use this header to enable this experimental API.

### Return type
[**RolePropagationOngoingResponse**](../models/role-propagation-ongoing-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Information of ongoing role propagation process. | RolePropagationOngoingResponse |  -  |
400 | Client Error - Returned if the request body is invalid. | ErrorResponseDto |  -  |
401 | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. | ListAccessProfiles401Response |  -  |
403 | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. | ErrorResponseDto |  -  |
429 | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. | ListAccessProfiles429Response |  -  |
500 | Internal Server Error - Returned if there is an unexpected error. | ErrorResponseDto |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.v2025.api.role_propagation_api import RolePropagationApi
from sailpoint.v2025.api_client import ApiClient
from sailpoint.v2025.models.role_propagation_ongoing_response import RolePropagationOngoingResponse
from sailpoint.configuration import Configuration
configuration = Configuration()

configuration.experimental = True

with ApiClient(configuration) as api_client:
    x_sail_point_experimental = 'true' # str | Use this header to enable this experimental API. (default to 'true') # str | Use this header to enable this experimental API. (default to 'true')

    try:
        # Get ongoing Role Propagation process
        
        results = RolePropagationApi(api_client).get_ongoing_role_propagation(x_sail_point_experimental=x_sail_point_experimental)
        # Below is a request that includes all optional parameters
        # results = RolePropagationApi(api_client).get_ongoing_role_propagation(x_sail_point_experimental)
        print("The response of RolePropagationApi->get_ongoing_role_propagation:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling RolePropagationApi->get_ongoing_role_propagation: %s\n" % e)
```



[[Back to top]](#) 

## get-role-propagation-status
:::warning experimental 
This API is currently in an experimental state. The API is subject to change based on feedback and further testing. You must include the X-SailPoint-Experimental header and set it to `true` to use this endpoint.
:::
:::tip setting x-sailpoint-experimental header
 on the configuration object you can set the `x-sailpoint-experimental` header to `true' to enable all experimantl endpoints within the SDK.
 Example:
 ```python
   configuration = Configuration()
   configuration.experimental = True
 ```
:::
Get status of Role-Propagation process
This endpoint returns the information of the specified role change propagation process. The execution stage of the role propagation process can be one of the following:
    - PENDING - The role propagation process is queued to be executed.
    - DATA_AGGREGATION_RUNNING - The role propagation process is currently aggregating data.
    - LAUNCH_PROVISIONING - The role propagation process has started to provision the access to the identities.
    - SUCCEEDED - The role propagation process has successfully completed.
    - FAILED - The role propagation process has failed.
    - TERMINATED - The role propagation process was externally terminated.

[API Spec](https://developer.sailpoint.com/docs/api/v2025/get-role-propagation-status)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
   | x_sail_point_experimental | **str** | True  (default to 'true') | Use this header to enable this experimental API.
Path   | role_propagation_id | **str** | True  | The ID of the role propagation process to retrieve the status for.

### Return type
[**RolePropagationStatusResponse**](../models/role-propagation-status-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Information of the role propagation process. | RolePropagationStatusResponse |  -  |
400 | Client Error - Returned if the request body is invalid. | ErrorResponseDto |  -  |
401 | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. | ListAccessProfiles401Response |  -  |
403 | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. | ErrorResponseDto |  -  |
404 | Not Found - returned if the request URL refers to a resource or object that does not exist | ErrorResponseDto |  -  |
429 | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. | ListAccessProfiles429Response |  -  |
500 | Internal Server Error - Returned if there is an unexpected error. | ErrorResponseDto |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.v2025.api.role_propagation_api import RolePropagationApi
from sailpoint.v2025.api_client import ApiClient
from sailpoint.v2025.models.role_propagation_status_response import RolePropagationStatusResponse
from sailpoint.configuration import Configuration
configuration = Configuration()

configuration.experimental = True

with ApiClient(configuration) as api_client:
    x_sail_point_experimental = 'true' # str | Use this header to enable this experimental API. (default to 'true') # str | Use this header to enable this experimental API. (default to 'true')
    role_propagation_id = '47b9fb02-e12e-42ba-8bfe-1860d78c88eb' # str | The ID of the role propagation process to retrieve the status for. # str | The ID of the role propagation process to retrieve the status for.

    try:
        # Get status of Role-Propagation process
        
        results = RolePropagationApi(api_client).get_role_propagation_status(x_sail_point_experimental=x_sail_point_experimental, role_propagation_id=role_propagation_id)
        # Below is a request that includes all optional parameters
        # results = RolePropagationApi(api_client).get_role_propagation_status(x_sail_point_experimental, role_propagation_id)
        print("The response of RolePropagationApi->get_role_propagation_status:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling RolePropagationApi->get_role_propagation_status: %s\n" % e)
```



[[Back to top]](#) 

## start-role-propagation
:::warning experimental 
This API is currently in an experimental state. The API is subject to change based on feedback and further testing. You must include the X-SailPoint-Experimental header and set it to `true` to use this endpoint.
:::
:::tip setting x-sailpoint-experimental header
 on the configuration object you can set the `x-sailpoint-experimental` header to `true' to enable all experimantl endpoints within the SDK.
 Example:
 ```python
   configuration = Configuration()
   configuration.experimental = True
 ```
:::
Initiate Role Propagation process
This endpoint initiates a role change propagation process for a tenant asynchronously.  If all preconditions are met, the request is accepted and a rolePropagationId is returned which  can be used to view the status.
API throws 4xx if any of the following conditions are met - Role propagation feature is disabled  - There is an ongoing role propagation for the tenant - Role refresh needs to be kicked off as part of the role propagation (skipRoleRefresh=false) and there is an ongoing refresh for the tenant

[API Spec](https://developer.sailpoint.com/docs/api/v2025/start-role-propagation)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
   | x_sail_point_experimental | **str** | True  (default to 'true') | Use this header to enable this experimental API.
  Query | skip_role_refresh | **bool** |   (optional) (default to False) | When true, the role refresh is not performed. Keeping it false is recommended.

### Return type
[**RolePropagationResponse**](../models/role-propagation-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
202 | Role Propagation has sucessfully started. | RolePropagationResponse |  -  |
400 | Client Error - Returned if the request body is invalid. | ErrorResponseDto |  -  |
401 | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. | ListAccessProfiles401Response |  -  |
403 | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. | ErrorResponseDto |  -  |
429 | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. | ListAccessProfiles429Response |  -  |
500 | Internal Server Error - Returned if there is an unexpected error. | ErrorResponseDto |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.v2025.api.role_propagation_api import RolePropagationApi
from sailpoint.v2025.api_client import ApiClient
from sailpoint.v2025.models.role_propagation_response import RolePropagationResponse
from sailpoint.configuration import Configuration
configuration = Configuration()

configuration.experimental = True

with ApiClient(configuration) as api_client:
    x_sail_point_experimental = 'true' # str | Use this header to enable this experimental API. (default to 'true') # str | Use this header to enable this experimental API. (default to 'true')
    skip_role_refresh = False # bool | When true, the role refresh is not performed. Keeping it false is recommended. (optional) (default to False) # bool | When true, the role refresh is not performed. Keeping it false is recommended. (optional) (default to False)

    try:
        # Initiate Role Propagation process
        
        results = RolePropagationApi(api_client).start_role_propagation(x_sail_point_experimental=x_sail_point_experimental)
        # Below is a request that includes all optional parameters
        # results = RolePropagationApi(api_client).start_role_propagation(x_sail_point_experimental, skip_role_refresh)
        print("The response of RolePropagationApi->start_role_propagation:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling RolePropagationApi->start_role_propagation: %s\n" % e)
```



[[Back to top]](#) 



