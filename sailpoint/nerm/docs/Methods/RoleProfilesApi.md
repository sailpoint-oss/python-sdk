---
id: role-profiles
title: Role_profiles
pagination_label: role_profiles
sidebar_label: role_profiles
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'role_profiles', 'role_profiles'] 
slug: /tools/sdk/python//methods/role-profiles
tags: ['SDK', 'Software Development Kit', 'role_profiles', 'role_profiles']
---

# sailpoint.nerm.RoleProfilesApi
   
All URIs are relative to *https://acmeco.nonemployee.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete-role-profile**](#delete-role-profile) | **DELETE** `/role_profile/{id}` | Delete a role profile assignment
[**get-role-profile**](#get-role-profile) | **GET** `/role_profiles/{id}` | Find role-profile contributor relationship
[**get-role-profiles**](#get-role-profiles) | **GET** `/role_profiles` | Get role-profile contributor relationships
[**patch-role-profile**](#patch-role-profile) | **PATCH** `/role_profiles/{id}` | Update a role-profile contributor relationship
[**patch-role-profiles**](#patch-role-profiles) | **PATCH** `/role_profiles` | Update multiple role-profile contributor relationships
[**submit-role-profile**](#submit-role-profile) | **POST** `/role_profile` | Create a role-profile contributor relationship
[**submit-role-profiles**](#submit-role-profiles) | **POST** `/role_profiles` | Create multiple role-profile contributor relationships


## delete-role-profile
Delete a role profile assignment
Delete a role profile assignment

[API Spec](https://developer.sailpoint.com/docs/api//delete-role-profile)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | id | **str** | True  | ID of the object to retrieve, update, or delete

### Return type
**object**

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Role profile was destroyed | object |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.role_profiles_api import RoleProfilesApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    id = '1246d8b3-ac29-4015-8154-dea4434a73fa' # str | ID of the object to retrieve, update, or delete # str | ID of the object to retrieve, update, or delete

    try:
        # Delete a role profile assignment
        
        results = RoleProfilesApi(api_client).delete_role_profile(id=id)
        # Below is a request that includes all optional parameters
        # results = RoleProfilesApi(api_client).delete_role_profile(id)
        print("The response of RoleProfilesApi->delete_role_profile:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling RoleProfilesApi->delete_role_profile: %s\n" % e)
```



[[Back to top]](#) 

## get-role-profile
Find role-profile contributor relationship
Find role-profile contributor relationship by id

[API Spec](https://developer.sailpoint.com/docs/api//get-role-profile)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | id | **str** | True  | ID of the object to retrieve, update, or delete

### Return type
[**SubmitRoleProfile200Response**](../models/submit-role-profile200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | SubmitRoleProfile200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.role_profiles_api import RoleProfilesApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.submit_role_profile200_response import SubmitRoleProfile200Response
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    id = '1246d8b3-ac29-4015-8154-dea4434a73fa' # str | ID of the object to retrieve, update, or delete # str | ID of the object to retrieve, update, or delete

    try:
        # Find role-profile contributor relationship
        
        results = RoleProfilesApi(api_client).get_role_profile(id=id)
        # Below is a request that includes all optional parameters
        # results = RoleProfilesApi(api_client).get_role_profile(id)
        print("The response of RoleProfilesApi->get_role_profile:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling RoleProfilesApi->get_role_profile: %s\n" % e)
```



[[Back to top]](#) 

## get-role-profiles
Get role-profile contributor relationships
Get role-profile contributor relationships

[API Spec](https://developer.sailpoint.com/docs/api//get-role-profiles)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
  Query | limit | **int** |   (optional) | The maximum number of items to return.
  Query | offset | **int** |   (optional) | The number of items to skip before starting to collect the result set.
  Query | order | **str** |   (optional) | The field to order results by.
  Query | role_id | **str** |   (optional) | The ID of a role for filtering
  Query | profile_id | **str** |   (optional) | Profile ID to filter by
  Query | metadata | **bool** |   (optional) (default to False) | Returns batching metadata in the response. This includes `total` as the total quantity, `next` as the path of the following query url, `limit` and `after_id` (if requested) with the next following id (null if it is the last \"page\").

### Return type
[**GetRoleProfiles200Response**](../models/get-role-profiles200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | GetRoleProfiles200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.role_profiles_api import RoleProfilesApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.get_role_profiles200_response import GetRoleProfiles200Response
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    limit = 5 # int | The maximum number of items to return. (optional) # int | The maximum number of items to return. (optional)
    offset = 5 # int | The number of items to skip before starting to collect the result set. (optional) # int | The number of items to skip before starting to collect the result set. (optional)
    order = 'created_at' # str | The field to order results by. (optional) # str | The field to order results by. (optional)
    role_id = 'c5e1dd38-7e29-464f-a0da-0c0d886d022a' # str | The ID of a role for filtering (optional) # str | The ID of a role for filtering (optional)
    profile_id = '4e480441-451d-47d9-87c2-9a0f0fe135eb' # str | Profile ID to filter by (optional) # str | Profile ID to filter by (optional)
    metadata = False # bool | Returns batching metadata in the response. This includes `total` as the total quantity, `next` as the path of the following query url, `limit` and `after_id` (if requested) with the next following id (null if it is the last \"page\"). (optional) (default to False) # bool | Returns batching metadata in the response. This includes `total` as the total quantity, `next` as the path of the following query url, `limit` and `after_id` (if requested) with the next following id (null if it is the last \"page\"). (optional) (default to False)

    try:
        # Get role-profile contributor relationships
        
        results = RoleProfilesApi(api_client).get_role_profiles()
        # Below is a request that includes all optional parameters
        # results = RoleProfilesApi(api_client).get_role_profiles(limit, offset, order, role_id, profile_id, metadata)
        print("The response of RoleProfilesApi->get_role_profiles:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling RoleProfilesApi->get_role_profiles: %s\n" % e)
```



[[Back to top]](#) 

## patch-role-profile
Update a role-profile contributor relationship
Update a role-profile contributor relationship by id

[API Spec](https://developer.sailpoint.com/docs/api//patch-role-profile)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | id | **str** | True  | ID of the object to retrieve, update, or delete
 Body  | submit_role_profile_request | [**SubmitRoleProfileRequest**](../models/submit-role-profile-request) | True  | 

### Return type
[**SubmitRoleProfile200Response**](../models/submit-role-profile200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | SubmitRoleProfile200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.role_profiles_api import RoleProfilesApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.submit_role_profile200_response import SubmitRoleProfile200Response
from sailpoint.nerm.models.submit_role_profile_request import SubmitRoleProfileRequest
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    id = '1246d8b3-ac29-4015-8154-dea4434a73fa' # str | ID of the object to retrieve, update, or delete # str | ID of the object to retrieve, update, or delete
    submit_role_profile_request = '''sailpoint.nerm.SubmitRoleProfileRequest()''' # SubmitRoleProfileRequest | 

    try:
        # Update a role-profile contributor relationship
        new_submit_role_profile_request = SubmitRoleProfileRequest.from_json(submit_role_profile_request)
        results = RoleProfilesApi(api_client).patch_role_profile(id=id, submit_role_profile_request=new_submit_role_profile_request)
        # Below is a request that includes all optional parameters
        # results = RoleProfilesApi(api_client).patch_role_profile(id, new_submit_role_profile_request)
        print("The response of RoleProfilesApi->patch_role_profile:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling RoleProfilesApi->patch_role_profile: %s\n" % e)
```



[[Back to top]](#) 

## patch-role-profiles
Update multiple role-profile contributor relationships
Update multiple role-profile contributor relationships

[API Spec](https://developer.sailpoint.com/docs/api//patch-role-profiles)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
 Body  | submit_role_profiles_request | [**SubmitRoleProfilesRequest**](../models/submit-role-profiles-request) | True  | 

### Return type
[**SubmitRoleProfiles200Response**](../models/submit-role-profiles200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | SubmitRoleProfiles200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.role_profiles_api import RoleProfilesApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.submit_role_profiles200_response import SubmitRoleProfiles200Response
from sailpoint.nerm.models.submit_role_profiles_request import SubmitRoleProfilesRequest
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    submit_role_profiles_request = '''sailpoint.nerm.SubmitRoleProfilesRequest()''' # SubmitRoleProfilesRequest | 

    try:
        # Update multiple role-profile contributor relationships
        new_submit_role_profiles_request = SubmitRoleProfilesRequest.from_json(submit_role_profiles_request)
        results = RoleProfilesApi(api_client).patch_role_profiles(submit_role_profiles_request=new_submit_role_profiles_request)
        # Below is a request that includes all optional parameters
        # results = RoleProfilesApi(api_client).patch_role_profiles(new_submit_role_profiles_request)
        print("The response of RoleProfilesApi->patch_role_profiles:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling RoleProfilesApi->patch_role_profiles: %s\n" % e)
```



[[Back to top]](#) 

## submit-role-profile
Create a role-profile contributor relationship
Create a role-profile contributor relationship

[API Spec](https://developer.sailpoint.com/docs/api//submit-role-profile)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
 Body  | submit_role_profile_request | [**SubmitRoleProfileRequest**](../models/submit-role-profile-request) | True  | 

### Return type
[**SubmitRoleProfile200Response**](../models/submit-role-profile200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | SubmitRoleProfile200Response |  -  |
405 | Invalid input |  |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.role_profiles_api import RoleProfilesApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.submit_role_profile200_response import SubmitRoleProfile200Response
from sailpoint.nerm.models.submit_role_profile_request import SubmitRoleProfileRequest
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    submit_role_profile_request = '''sailpoint.nerm.SubmitRoleProfileRequest()''' # SubmitRoleProfileRequest | 

    try:
        # Create a role-profile contributor relationship
        new_submit_role_profile_request = SubmitRoleProfileRequest.from_json(submit_role_profile_request)
        results = RoleProfilesApi(api_client).submit_role_profile(submit_role_profile_request=new_submit_role_profile_request)
        # Below is a request that includes all optional parameters
        # results = RoleProfilesApi(api_client).submit_role_profile(new_submit_role_profile_request)
        print("The response of RoleProfilesApi->submit_role_profile:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling RoleProfilesApi->submit_role_profile: %s\n" % e)
```



[[Back to top]](#) 

## submit-role-profiles
Create multiple role-profile contributor relationships
Create multiple role-profile contributor relationships

[API Spec](https://developer.sailpoint.com/docs/api//submit-role-profiles)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
 Body  | submit_role_profiles_request | [**SubmitRoleProfilesRequest**](../models/submit-role-profiles-request) | True  | 

### Return type
[**SubmitRoleProfiles200Response**](../models/submit-role-profiles200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | SubmitRoleProfiles200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.role_profiles_api import RoleProfilesApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.submit_role_profiles200_response import SubmitRoleProfiles200Response
from sailpoint.nerm.models.submit_role_profiles_request import SubmitRoleProfilesRequest
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    submit_role_profiles_request = '''sailpoint.nerm.SubmitRoleProfilesRequest()''' # SubmitRoleProfilesRequest | 

    try:
        # Create multiple role-profile contributor relationships
        new_submit_role_profiles_request = SubmitRoleProfilesRequest.from_json(submit_role_profiles_request)
        results = RoleProfilesApi(api_client).submit_role_profiles(submit_role_profiles_request=new_submit_role_profiles_request)
        # Below is a request that includes all optional parameters
        # results = RoleProfilesApi(api_client).submit_role_profiles(new_submit_role_profiles_request)
        print("The response of RoleProfilesApi->submit_role_profiles:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling RoleProfilesApi->submit_role_profiles: %s\n" % e)
```



[[Back to top]](#) 



