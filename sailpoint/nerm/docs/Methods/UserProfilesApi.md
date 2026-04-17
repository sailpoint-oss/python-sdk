---
id: user-profiles
title: User_profiles
pagination_label: user_profiles
sidebar_label: user_profiles
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'user_profiles', 'user_profiles'] 
slug: /tools/sdk/python//methods/user-profiles
tags: ['SDK', 'Software Development Kit', 'user_profiles', 'user_profiles']
---

# sailpoint.nerm.UserProfilesApi
   
All URIs are relative to *https://acmeco.nonemployee.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create-user-profiles**](#create-user-profiles) | **POST** `/user_profiles` | Create multiple user-profile contributor relationships
[**delete-user-profile**](#delete-user-profile) | **DELETE** `/user_profile/{id}` | Delete a user profile assignment
[**delete-user-profiles**](#delete-user-profiles) | **DELETE** `/user_profiles` | Delete multiple user-profile contributor relationships
[**get-user-profile**](#get-user-profile) | **GET** `/user_profiles/{id}` | Find user-profile contributor relationship
[**get-user-profiles**](#get-user-profiles) | **GET** `/user_profiles` | Get user-profile contributor relationships
[**patch-user-profile**](#patch-user-profile) | **PATCH** `/user_profiles/{id}` | Update a user-profile contributor relationship
[**patch-user-profiles**](#patch-user-profiles) | **PATCH** `/user_profiles` | Update multiple user-profile contributor relationships
[**submit-user-profile**](#submit-user-profile) | **POST** `/user_profile` | Create a user-profile contributor relationship


## create-user-profiles
Create multiple user-profile contributor relationships
Create multiple user-profile contributor relationships

[API Spec](https://developer.sailpoint.com/docs/api//create-user-profiles)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
 Body  | create_user_profiles_request | [**CreateUserProfilesRequest**](../models/create-user-profiles-request) | True  | 

### Return type
[**CreateUserProfiles200Response**](../models/create-user-profiles200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | CreateUserProfiles200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.user_profiles_api import UserProfilesApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.create_user_profiles200_response import CreateUserProfiles200Response
from sailpoint.nerm.models.create_user_profiles_request import CreateUserProfilesRequest
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    create_user_profiles_request = '''sailpoint.nerm.CreateUserProfilesRequest()''' # CreateUserProfilesRequest | 

    try:
        # Create multiple user-profile contributor relationships
        new_create_user_profiles_request = CreateUserProfilesRequest.from_json(create_user_profiles_request)
        results = UserProfilesApi(api_client).create_user_profiles(create_user_profiles_request=new_create_user_profiles_request)
        # Below is a request that includes all optional parameters
        # results = UserProfilesApi(api_client).create_user_profiles(new_create_user_profiles_request)
        print("The response of UserProfilesApi->create_user_profiles:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling UserProfilesApi->create_user_profiles: %s\n" % e)
```



[[Back to top]](#) 

## delete-user-profile
Delete a user profile assignment
Delete a user profile assignment

[API Spec](https://developer.sailpoint.com/docs/api//delete-user-profile)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | id | **str** | True  | ID of the object to retrieve, update, or delete

### Return type
**object**

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | User profile was destroyed | object |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.user_profiles_api import UserProfilesApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    id = '1246d8b3-ac29-4015-8154-dea4434a73fa' # str | ID of the object to retrieve, update, or delete # str | ID of the object to retrieve, update, or delete

    try:
        # Delete a user profile assignment
        
        results = UserProfilesApi(api_client).delete_user_profile(id=id)
        # Below is a request that includes all optional parameters
        # results = UserProfilesApi(api_client).delete_user_profile(id)
        print("The response of UserProfilesApi->delete_user_profile:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling UserProfilesApi->delete_user_profile: %s\n" % e)
```



[[Back to top]](#) 

## delete-user-profiles
Delete multiple user-profile contributor relationships
Delete multiple user-profile contributor relationships

[API Spec](https://developer.sailpoint.com/docs/api//delete-user-profiles)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
 Body  | create_user_profiles_request | [**CreateUserProfilesRequest**](../models/create-user-profiles-request) | True  | 

### Return type
[**CreateUserProfiles200Response**](../models/create-user-profiles200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | CreateUserProfiles200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.user_profiles_api import UserProfilesApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.create_user_profiles200_response import CreateUserProfiles200Response
from sailpoint.nerm.models.create_user_profiles_request import CreateUserProfilesRequest
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    create_user_profiles_request = '''sailpoint.nerm.CreateUserProfilesRequest()''' # CreateUserProfilesRequest | 

    try:
        # Delete multiple user-profile contributor relationships
        new_create_user_profiles_request = CreateUserProfilesRequest.from_json(create_user_profiles_request)
        results = UserProfilesApi(api_client).delete_user_profiles(create_user_profiles_request=new_create_user_profiles_request)
        # Below is a request that includes all optional parameters
        # results = UserProfilesApi(api_client).delete_user_profiles(new_create_user_profiles_request)
        print("The response of UserProfilesApi->delete_user_profiles:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling UserProfilesApi->delete_user_profiles: %s\n" % e)
```



[[Back to top]](#) 

## get-user-profile
Find user-profile contributor relationship
Find user-profile contributor relationship by id

[API Spec](https://developer.sailpoint.com/docs/api//get-user-profile)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | id | **str** | True  | ID of the object to retrieve, update, or delete

### Return type
[**SubmitUserProfile200Response**](../models/submit-user-profile200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | SubmitUserProfile200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.user_profiles_api import UserProfilesApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.submit_user_profile200_response import SubmitUserProfile200Response
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    id = '1246d8b3-ac29-4015-8154-dea4434a73fa' # str | ID of the object to retrieve, update, or delete # str | ID of the object to retrieve, update, or delete

    try:
        # Find user-profile contributor relationship
        
        results = UserProfilesApi(api_client).get_user_profile(id=id)
        # Below is a request that includes all optional parameters
        # results = UserProfilesApi(api_client).get_user_profile(id)
        print("The response of UserProfilesApi->get_user_profile:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling UserProfilesApi->get_user_profile: %s\n" % e)
```



[[Back to top]](#) 

## get-user-profiles
Get user-profile contributor relationships
Get user-profile contributor relationships

[API Spec](https://developer.sailpoint.com/docs/api//get-user-profiles)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
  Query | limit | **int** |   (optional) | The maximum number of items to return.
  Query | offset | **int** |   (optional) | The number of items to skip before starting to collect the result set.
  Query | order | **str** |   (optional) | The field to order results by.
  Query | user_id | **str** |   (optional) | The ID of a user for filtering
  Query | ne_attribute_id | **str** |   (optional) | ID of an attribute for filtering
  Query | profile_id | **str** |   (optional) | Profile ID to filter by
  Query | relationship_type | **str** |   (optional) | Type of user contributor relationship to filter by
  Query | metadata | **bool** |   (optional) (default to False) | Returns batching metadata in the response. This includes `total` as the total quantity, `next` as the path of the following query url, `limit` and `after_id` (if requested) with the next following id (null if it is the last \"page\").

### Return type
[**GetUserProfiles200Response**](../models/get-user-profiles200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | GetUserProfiles200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.user_profiles_api import UserProfilesApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.get_user_profiles200_response import GetUserProfiles200Response
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    limit = 5 # int | The maximum number of items to return. (optional) # int | The maximum number of items to return. (optional)
    offset = 5 # int | The number of items to skip before starting to collect the result set. (optional) # int | The number of items to skip before starting to collect the result set. (optional)
    order = 'created_at' # str | The field to order results by. (optional) # str | The field to order results by. (optional)
    user_id = 'bba9cfb2-96c1-4acb-ac79-a21732527265' # str | The ID of a user for filtering (optional) # str | The ID of a user for filtering (optional)
    ne_attribute_id = '33f072dd-13b4-41e1-8ea0-16f2a59b57c8' # str | ID of an attribute for filtering (optional) # str | ID of an attribute for filtering (optional)
    profile_id = '4e480441-451d-47d9-87c2-9a0f0fe135eb' # str | Profile ID to filter by (optional) # str | Profile ID to filter by (optional)
    relationship_type = 'contributor' # str | Type of user contributor relationship to filter by (optional) # str | Type of user contributor relationship to filter by (optional)
    metadata = False # bool | Returns batching metadata in the response. This includes `total` as the total quantity, `next` as the path of the following query url, `limit` and `after_id` (if requested) with the next following id (null if it is the last \"page\"). (optional) (default to False) # bool | Returns batching metadata in the response. This includes `total` as the total quantity, `next` as the path of the following query url, `limit` and `after_id` (if requested) with the next following id (null if it is the last \"page\"). (optional) (default to False)

    try:
        # Get user-profile contributor relationships
        
        results = UserProfilesApi(api_client).get_user_profiles()
        # Below is a request that includes all optional parameters
        # results = UserProfilesApi(api_client).get_user_profiles(limit, offset, order, user_id, ne_attribute_id, profile_id, relationship_type, metadata)
        print("The response of UserProfilesApi->get_user_profiles:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling UserProfilesApi->get_user_profiles: %s\n" % e)
```



[[Back to top]](#) 

## patch-user-profile
Update a user-profile contributor relationship
Update a user-profile contributor relationship by id

[API Spec](https://developer.sailpoint.com/docs/api//patch-user-profile)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | id | **str** | True  | ID of the object to retrieve, update, or delete
 Body  | submit_user_profile_request | [**SubmitUserProfileRequest**](../models/submit-user-profile-request) | True  | 

### Return type
[**SubmitUserProfile200Response**](../models/submit-user-profile200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | SubmitUserProfile200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.user_profiles_api import UserProfilesApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.submit_user_profile200_response import SubmitUserProfile200Response
from sailpoint.nerm.models.submit_user_profile_request import SubmitUserProfileRequest
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    id = '1246d8b3-ac29-4015-8154-dea4434a73fa' # str | ID of the object to retrieve, update, or delete # str | ID of the object to retrieve, update, or delete
    submit_user_profile_request = '''sailpoint.nerm.SubmitUserProfileRequest()''' # SubmitUserProfileRequest | 

    try:
        # Update a user-profile contributor relationship
        new_submit_user_profile_request = SubmitUserProfileRequest.from_json(submit_user_profile_request)
        results = UserProfilesApi(api_client).patch_user_profile(id=id, submit_user_profile_request=new_submit_user_profile_request)
        # Below is a request that includes all optional parameters
        # results = UserProfilesApi(api_client).patch_user_profile(id, new_submit_user_profile_request)
        print("The response of UserProfilesApi->patch_user_profile:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling UserProfilesApi->patch_user_profile: %s\n" % e)
```



[[Back to top]](#) 

## patch-user-profiles
Update multiple user-profile contributor relationships
Update multiple user-profile contributor relationships

[API Spec](https://developer.sailpoint.com/docs/api//patch-user-profiles)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
 Body  | create_user_profiles_request | [**CreateUserProfilesRequest**](../models/create-user-profiles-request) | True  | 

### Return type
[**CreateUserProfiles200Response**](../models/create-user-profiles200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | CreateUserProfiles200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.user_profiles_api import UserProfilesApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.create_user_profiles200_response import CreateUserProfiles200Response
from sailpoint.nerm.models.create_user_profiles_request import CreateUserProfilesRequest
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    create_user_profiles_request = '''sailpoint.nerm.CreateUserProfilesRequest()''' # CreateUserProfilesRequest | 

    try:
        # Update multiple user-profile contributor relationships
        new_create_user_profiles_request = CreateUserProfilesRequest.from_json(create_user_profiles_request)
        results = UserProfilesApi(api_client).patch_user_profiles(create_user_profiles_request=new_create_user_profiles_request)
        # Below is a request that includes all optional parameters
        # results = UserProfilesApi(api_client).patch_user_profiles(new_create_user_profiles_request)
        print("The response of UserProfilesApi->patch_user_profiles:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling UserProfilesApi->patch_user_profiles: %s\n" % e)
```



[[Back to top]](#) 

## submit-user-profile
Create a user-profile contributor relationship
Create a user-profile contributor relationship

[API Spec](https://developer.sailpoint.com/docs/api//submit-user-profile)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
 Body  | submit_user_profile_request | [**SubmitUserProfileRequest**](../models/submit-user-profile-request) | True  | 

### Return type
[**SubmitUserProfile200Response**](../models/submit-user-profile200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | SubmitUserProfile200Response |  -  |
405 | Invalid input |  |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.user_profiles_api import UserProfilesApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.submit_user_profile200_response import SubmitUserProfile200Response
from sailpoint.nerm.models.submit_user_profile_request import SubmitUserProfileRequest
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    submit_user_profile_request = '''sailpoint.nerm.SubmitUserProfileRequest()''' # SubmitUserProfileRequest | 

    try:
        # Create a user-profile contributor relationship
        new_submit_user_profile_request = SubmitUserProfileRequest.from_json(submit_user_profile_request)
        results = UserProfilesApi(api_client).submit_user_profile(submit_user_profile_request=new_submit_user_profile_request)
        # Below is a request that includes all optional parameters
        # results = UserProfilesApi(api_client).submit_user_profile(new_submit_user_profile_request)
        print("The response of UserProfilesApi->submit_user_profile:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling UserProfilesApi->submit_user_profile: %s\n" % e)
```



[[Back to top]](#) 



