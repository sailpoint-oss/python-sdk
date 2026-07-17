---
id: auth-profile
title: Auth_Profile
pagination_label: Auth_Profile
sidebar_label: Auth_Profile
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Auth_Profile', 'Auth_Profile'] 
slug: /tools/sdk/python/auth-profile/methods/auth-profile
tags: ['SDK', 'Software Development Kit', 'Auth_Profile', 'Auth_Profile']
---

# sailpoint.auth_profile.AuthProfileApi
  Use this API to implement Auth Profile functionality. 
With this functionality in place, users can read authentication profiles and make changes to them. 

An authentication profile represents an identity profile&#39;s authentication configuration. 
When the identity profile is created, its authentication profile is also created. 
An authentication profile includes information like its authentication profile type (&#x60;BLOCK&#x60;, &#x60;MFA&#x60;, &#x60;NON_PTA&#x60;, PTA&#x60;) and settings controlling whether or not it blocks access from off network or untrusted geographies. 
 
All URIs are relative to *https://sailpoint.api.identitynow.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get-profile-config-list-v1**](#get-profile-config-list-v1) | **GET** `/auth-profiles/v1` | Get list of auth profiles
[**get-profile-config-v1**](#get-profile-config-v1) | **GET** `/auth-profiles/v1/{id}` | Get auth profile
[**patch-profile-config-v1**](#patch-profile-config-v1) | **PATCH** `/auth-profiles/v1/{id}` | Patch a specified auth profile


## get-profile-config-list-v1
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
Get list of auth profiles
This API returns a list of auth profiles.

[API Spec](https://developer.sailpoint.com/docs/api/get-profile-config-list-v-1)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
   | x_sail_point_experimental | **str** |   (optional) (default to 'true') | Use this header to enable this experimental API.

### Return type
[**List[AuthProfileSummary]**](../models/auth-profile-summary)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | List of Auth Profiles | List[AuthProfileSummary] |  -  |
400 | Client Error - Returned if the request body is invalid. | ErrorResponseDto |  -  |
401 | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. | GetProfileConfigListV1401Response |  -  |
403 | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. | ErrorResponseDto |  -  |
429 | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. | GetProfileConfigListV1429Response |  -  |
500 | Internal Server Error - Returned if there is an unexpected error. | ErrorResponseDto |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.auth_profile.api.auth_profile_api import AuthProfileApi
from sailpoint.auth_profile.api_client import ApiClient
from sailpoint.auth_profile.models.auth_profile_summary import AuthProfileSummary
from sailpoint.configuration import Configuration
configuration = Configuration()

configuration.experimental = True

with ApiClient(configuration) as api_client:
    x_sail_point_experimental = 'true' # str | Use this header to enable this experimental API. (optional) (default to 'true') # str | Use this header to enable this experimental API. (optional) (default to 'true')

    try:
        # Get list of auth profiles
        
        results = AuthProfileApi(api_client).get_profile_config_list_v1()
        # Below is a request that includes all optional parameters
        # results = AuthProfileApi(api_client).get_profile_config_list_v1(x_sail_point_experimental)
        print("The response of AuthProfileApi->get_profile_config_list_v1:\n")
        for item in results:
            print(item.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling AuthProfileApi->get_profile_config_list_v1: %s\n" % e)
```



[[Back to top]](#) 

## get-profile-config-v1
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
Get auth profile
This API returns auth profile information.

[API Spec](https://developer.sailpoint.com/docs/api/get-profile-config-v-1)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | id | **str** | True  | ID of the Auth Profile to patch.
   | x_sail_point_experimental | **str** |   (optional) (default to 'true') | Use this header to enable this experimental API.

### Return type
[**AuthProfile**](../models/auth-profile)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Auth Profile | AuthProfile |  -  |
400 | Client Error - Returned if the request body is invalid. | ErrorResponseDto |  -  |
401 | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. | GetProfileConfigListV1401Response |  -  |
403 | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. | ErrorResponseDto |  -  |
404 | Not Found - returned if the request URL refers to a resource or object that does not exist | ErrorResponseDto |  -  |
429 | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. | GetProfileConfigListV1429Response |  -  |
500 | Internal Server Error - Returned if there is an unexpected error. | ErrorResponseDto |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.auth_profile.api.auth_profile_api import AuthProfileApi
from sailpoint.auth_profile.api_client import ApiClient
from sailpoint.auth_profile.models.auth_profile import AuthProfile
from sailpoint.configuration import Configuration
configuration = Configuration()

configuration.experimental = True

with ApiClient(configuration) as api_client:
    id = '2c91808a7813090a017814121919ecca' # str | ID of the Auth Profile to patch. # str | ID of the Auth Profile to patch.
    x_sail_point_experimental = 'true' # str | Use this header to enable this experimental API. (optional) (default to 'true') # str | Use this header to enable this experimental API. (optional) (default to 'true')

    try:
        # Get auth profile
        
        results = AuthProfileApi(api_client).get_profile_config_v1(id=id)
        # Below is a request that includes all optional parameters
        # results = AuthProfileApi(api_client).get_profile_config_v1(id, x_sail_point_experimental)
        print("The response of AuthProfileApi->get_profile_config_v1:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling AuthProfileApi->get_profile_config_v1: %s\n" % e)
```



[[Back to top]](#) 

## patch-profile-config-v1
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
Patch a specified auth profile
This API updates an existing Auth Profile. The following fields are patchable:
**offNetwork**, **untrustedGeography**, **applicationId**, **applicationName**, **type**

[API Spec](https://developer.sailpoint.com/docs/api/patch-profile-config-v-1)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | id | **str** | True  | ID of the Auth Profile to patch.
 Body  | json_patch_operation | [**[]JsonPatchOperation**](../models/json-patch-operation) | True  | 
   | x_sail_point_experimental | **str** |   (optional) (default to 'true') | Use this header to enable this experimental API.

### Return type
[**AuthProfile**](../models/auth-profile)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Responds with the Auth Profile as updated. | AuthProfile |  -  |
400 | Client Error - Returned if the request body is invalid. | ErrorResponseDto |  -  |
401 | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. | GetProfileConfigListV1401Response |  -  |
403 | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. | ErrorResponseDto |  -  |
429 | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. | GetProfileConfigListV1429Response |  -  |
500 | Internal Server Error - Returned if there is an unexpected error. | ErrorResponseDto |  -  |

### HTTP request headers
 - **Content-Type**: application/json-patch+json
 - **Accept**: application/json

### Example

```python
from sailpoint.auth_profile.api.auth_profile_api import AuthProfileApi
from sailpoint.auth_profile.api_client import ApiClient
from sailpoint.auth_profile.models.auth_profile import AuthProfile
from sailpoint.auth_profile.models.json_patch_operation import JsonPatchOperation
from sailpoint.configuration import Configuration
configuration = Configuration()

configuration.experimental = True

with ApiClient(configuration) as api_client:
    id = '2c91808a7813090a017814121919ecca' # str | ID of the Auth Profile to patch. # str | ID of the Auth Profile to patch.
    json_patch_operation = '''[sailpoint.auth_profile.JsonPatchOperation()]''' # List[JsonPatchOperation] | 
    x_sail_point_experimental = 'true' # str | Use this header to enable this experimental API. (optional) (default to 'true') # str | Use this header to enable this experimental API. (optional) (default to 'true')

    try:
        # Patch a specified auth profile
        new_json_patch_operation = JsonPatchOperation.from_json(json_patch_operation)
        results = AuthProfileApi(api_client).patch_profile_config_v1(id=id, json_patch_operation=new_json_patch_operation)
        # Below is a request that includes all optional parameters
        # results = AuthProfileApi(api_client).patch_profile_config_v1(id, new_json_patch_operation, x_sail_point_experimental)
        print("The response of AuthProfileApi->patch_profile_config_v1:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling AuthProfileApi->patch_profile_config_v1: %s\n" % e)
```



[[Back to top]](#) 



