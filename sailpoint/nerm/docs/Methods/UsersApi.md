---
id: users
title: Users
pagination_label: users
sidebar_label: users
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'users', 'users'] 
slug: /tools/sdk/python//methods/users
tags: ['SDK', 'Software Development Kit', 'users', 'users']
---

# sailpoint.nerm.UsersApi
   
All URIs are relative to *https://acmeco.nonemployee.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete-user**](#delete-user) | **DELETE** `/users/{id}` | Delete a user
[**get-user**](#get-user) | **GET** `/users/{id}` | Find user by id
[**get-user-avatar**](#get-user-avatar) | **GET** `/users/{id}/avatar` | Retrieves  URL user avatar
[**get-users**](#get-users) | **GET** `/users` | Get users
[**patch-user**](#patch-user) | **PATCH** `/users/{id}` | Update a user by id
[**patch-users**](#patch-users) | **PATCH** `/users` | Update multiple users
[**submit-user**](#submit-user) | **POST** `/user` | Create a new user
[**submit-user-avatar**](#submit-user-avatar) | **POST** `/users/{id}/avatar` | Uploads new user avatar
[**submit-users**](#submit-users) | **POST** `/users` | Create multiple new users


## delete-user
Delete a user
Delete a user

[API Spec](https://developer.sailpoint.com/docs/api//delete-user)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | id | **str** | True  | ID of the object to retrieve, update, or delete

### Return type
[**DeleteProfileTypeById200Response**](../models/delete-profile-type-by-id200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Info about the operation | DeleteProfileTypeById200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.users_api import UsersApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.delete_profile_type_by_id200_response import DeleteProfileTypeById200Response
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    id = '1246d8b3-ac29-4015-8154-dea4434a73fa' # str | ID of the object to retrieve, update, or delete # str | ID of the object to retrieve, update, or delete

    try:
        # Delete a user
        
        results = UsersApi(api_client).delete_user(id=id)
        # Below is a request that includes all optional parameters
        # results = UsersApi(api_client).delete_user(id)
        print("The response of UsersApi->delete_user:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling UsersApi->delete_user: %s\n" % e)
```



[[Back to top]](#) 

## get-user
Find user by id
Info for a specific user

[API Spec](https://developer.sailpoint.com/docs/api//get-user)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | id | **str** | True  | ID of the object to retrieve, update, or delete

### Return type
[**SubmitUser200Response**](../models/submit-user200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | SubmitUser200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.users_api import UsersApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.submit_user200_response import SubmitUser200Response
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    id = '1246d8b3-ac29-4015-8154-dea4434a73fa' # str | ID of the object to retrieve, update, or delete # str | ID of the object to retrieve, update, or delete

    try:
        # Find user by id
        
        results = UsersApi(api_client).get_user(id=id)
        # Below is a request that includes all optional parameters
        # results = UsersApi(api_client).get_user(id)
        print("The response of UsersApi->get_user:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling UsersApi->get_user: %s\n" % e)
```



[[Back to top]](#) 

## get-user-avatar
Retrieves  URL user avatar
Retrieves the URL of the user avatar

[API Spec](https://developer.sailpoint.com/docs/api//get-user-avatar)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | id | **str** | True  | ID of the object to retrieve, update, or delete

### Return type
[**Url**](../models/url)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | Url |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.users_api import UsersApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.url import Url
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    id = '1246d8b3-ac29-4015-8154-dea4434a73fa' # str | ID of the object to retrieve, update, or delete # str | ID of the object to retrieve, update, or delete

    try:
        # Retrieves  URL user avatar
        
        results = UsersApi(api_client).get_user_avatar(id=id)
        # Below is a request that includes all optional parameters
        # results = UsersApi(api_client).get_user_avatar(id)
        print("The response of UsersApi->get_user_avatar:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling UsersApi->get_user_avatar: %s\n" % e)
```



[[Back to top]](#) 

## get-users
Get users
This endpoint can retrieve users from Lifecycle or you can search for users using parameters

[API Spec](https://developer.sailpoint.com/docs/api//get-users)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
  Query | limit | **int** |   (optional) | The maximum number of items to return.
  Query | offset | **int** |   (optional) | The number of items to skip before starting to collect the result set.
  Query | order | **str** |   (optional) | The field to order results by.
  Query | name | **str** |   (optional) | object name for filtering
  Query | login | **str** |   (optional) | The user login to search by
  Query | title | **str** |   (optional) | The user title to search by
  Query | user_status | **str** |   (optional) | user status value for filtering
  Query | type | **str** |   (optional) | user type
  Query | email | **str** |   (optional) | The user email to search by
  Query | metadata | **bool** |   (optional) (default to False) | Returns batching metadata in the response. This includes `total` as the total quantity, `next` as the path of the following query url, `limit` and `after_id` (if requested) with the next following id (null if it is the last \"page\").
  Query | sailpoint_identity_id | **str** |   (optional) | SailPoint identity ID

### Return type
[**GetUsers200Response**](../models/get-users200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | GetUsers200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.users_api import UsersApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.get_users200_response import GetUsers200Response
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    limit = 5 # int | The maximum number of items to return. (optional) # int | The maximum number of items to return. (optional)
    offset = 5 # int | The number of items to skip before starting to collect the result set. (optional) # int | The number of items to skip before starting to collect the result set. (optional)
    order = 'created_at' # str | The field to order results by. (optional) # str | The field to order results by. (optional)
    name = 'name' # str | object name for filtering (optional) # str | object name for filtering (optional)
    login = 'jane.doe' # str | The user login to search by (optional) # str | The user login to search by (optional)
    title = 'Marketing Director' # str | The user title to search by (optional) # str | The user title to search by (optional)
    user_status = 'Active' # str | user status value for filtering (optional) # str | user status value for filtering (optional)
    type = 'NeprofileUser' # str | user type (optional) # str | user type (optional)
    email = 'support@sailpoint.com' # str | The user email to search by (optional) # str | The user email to search by (optional)
    metadata = False # bool | Returns batching metadata in the response. This includes `total` as the total quantity, `next` as the path of the following query url, `limit` and `after_id` (if requested) with the next following id (null if it is the last \"page\"). (optional) (default to False) # bool | Returns batching metadata in the response. This includes `total` as the total quantity, `next` as the path of the following query url, `limit` and `after_id` (if requested) with the next following id (null if it is the last \"page\"). (optional) (default to False)
    sailpoint_identity_id = '9496f8d6ddab49c0bef1e9ee6f1b835a' # str | SailPoint identity ID (optional) # str | SailPoint identity ID (optional)

    try:
        # Get users
        
        results = UsersApi(api_client).get_users()
        # Below is a request that includes all optional parameters
        # results = UsersApi(api_client).get_users(limit, offset, order, name, login, title, user_status, type, email, metadata, sailpoint_identity_id)
        print("The response of UsersApi->get_users:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling UsersApi->get_users: %s\n" % e)
```



[[Back to top]](#) 

## patch-user
Update a user by id
Update a user by id

[API Spec](https://developer.sailpoint.com/docs/api//patch-user)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | id | **str** | True  | ID of the object to retrieve, update, or delete
 Body  | submit_user_request | [**SubmitUserRequest**](../models/submit-user-request) | True  | 

### Return type
[**SubmitUser200Response**](../models/submit-user200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | SubmitUser200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.users_api import UsersApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.submit_user200_response import SubmitUser200Response
from sailpoint.nerm.models.submit_user_request import SubmitUserRequest
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    id = '1246d8b3-ac29-4015-8154-dea4434a73fa' # str | ID of the object to retrieve, update, or delete # str | ID of the object to retrieve, update, or delete
    submit_user_request = '''sailpoint.nerm.SubmitUserRequest()''' # SubmitUserRequest | 

    try:
        # Update a user by id
        new_submit_user_request = SubmitUserRequest.from_json(submit_user_request)
        results = UsersApi(api_client).patch_user(id=id, submit_user_request=new_submit_user_request)
        # Below is a request that includes all optional parameters
        # results = UsersApi(api_client).patch_user(id, new_submit_user_request)
        print("The response of UsersApi->patch_user:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling UsersApi->patch_user: %s\n" % e)
```



[[Back to top]](#) 

## patch-users
Update multiple users
Update multiple users

[API Spec](https://developer.sailpoint.com/docs/api//patch-users)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
 Body  | submit_users_request | [**SubmitUsersRequest**](../models/submit-users-request) | True  | 

### Return type
[**SubmitUsers200Response**](../models/submit-users200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | SubmitUsers200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.users_api import UsersApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.submit_users200_response import SubmitUsers200Response
from sailpoint.nerm.models.submit_users_request import SubmitUsersRequest
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    submit_users_request = '''sailpoint.nerm.SubmitUsersRequest()''' # SubmitUsersRequest | 

    try:
        # Update multiple users
        new_submit_users_request = SubmitUsersRequest.from_json(submit_users_request)
        results = UsersApi(api_client).patch_users(submit_users_request=new_submit_users_request)
        # Below is a request that includes all optional parameters
        # results = UsersApi(api_client).patch_users(new_submit_users_request)
        print("The response of UsersApi->patch_users:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling UsersApi->patch_users: %s\n" % e)
```



[[Back to top]](#) 

## submit-user
Create a new user
Create a new user

[API Spec](https://developer.sailpoint.com/docs/api//submit-user)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
 Body  | submit_user_request | [**SubmitUserRequest**](../models/submit-user-request) | True  | 

### Return type
[**SubmitUser200Response**](../models/submit-user200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | SubmitUser200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.users_api import UsersApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.submit_user200_response import SubmitUser200Response
from sailpoint.nerm.models.submit_user_request import SubmitUserRequest
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    submit_user_request = '''sailpoint.nerm.SubmitUserRequest()''' # SubmitUserRequest | 

    try:
        # Create a new user
        new_submit_user_request = SubmitUserRequest.from_json(submit_user_request)
        results = UsersApi(api_client).submit_user(submit_user_request=new_submit_user_request)
        # Below is a request that includes all optional parameters
        # results = UsersApi(api_client).submit_user(new_submit_user_request)
        print("The response of UsersApi->submit_user:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling UsersApi->submit_user: %s\n" % e)
```



[[Back to top]](#) 

## submit-user-avatar
Uploads new user avatar
Uploads a new user avatar

[API Spec](https://developer.sailpoint.com/docs/api//submit-user-avatar)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | id | **str** | True  | ID of the object to retrieve, update, or delete
   | file | **bytearray** |   (optional) | 

### Return type
[**Url**](../models/url)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | Url |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.users_api import UsersApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.url import Url
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    id = '1246d8b3-ac29-4015-8154-dea4434a73fa' # str | ID of the object to retrieve, update, or delete # str | ID of the object to retrieve, update, or delete
    file = None # bytearray |  (optional) # bytearray |  (optional)

    try:
        # Uploads new user avatar
        
        results = UsersApi(api_client).submit_user_avatar(id=id)
        # Below is a request that includes all optional parameters
        # results = UsersApi(api_client).submit_user_avatar(id, file)
        print("The response of UsersApi->submit_user_avatar:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling UsersApi->submit_user_avatar: %s\n" % e)
```



[[Back to top]](#) 

## submit-users
Create multiple new users
Create multiple new users

[API Spec](https://developer.sailpoint.com/docs/api//submit-users)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
 Body  | submit_users_request | [**SubmitUsersRequest**](../models/submit-users-request) | True  | 

### Return type
[**SubmitUsers200Response**](../models/submit-users200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | SubmitUsers200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.users_api import UsersApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.submit_users200_response import SubmitUsers200Response
from sailpoint.nerm.models.submit_users_request import SubmitUsersRequest
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    submit_users_request = '''sailpoint.nerm.SubmitUsersRequest()''' # SubmitUsersRequest | 

    try:
        # Create multiple new users
        new_submit_users_request = SubmitUsersRequest.from_json(submit_users_request)
        results = UsersApi(api_client).submit_users(submit_users_request=new_submit_users_request)
        # Below is a request that includes all optional parameters
        # results = UsersApi(api_client).submit_users(new_submit_users_request)
        print("The response of UsersApi->submit_users:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling UsersApi->submit_users: %s\n" % e)
```



[[Back to top]](#) 



