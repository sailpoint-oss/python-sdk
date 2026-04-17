---
id: user-managers
title: User_managers
pagination_label: user_managers
sidebar_label: user_managers
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'user_managers', 'user_managers'] 
slug: /tools/sdk/python//methods/user-managers
tags: ['SDK', 'Software Development Kit', 'user_managers', 'user_managers']
---

# sailpoint.nerm.UserManagersApi
   
All URIs are relative to *https://acmeco.nonemployee.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get-user-manager**](#get-user-manager) | **GET** `/user_managers/{id}` | Find user-manager relationship
[**get-user-managers**](#get-user-managers) | **GET** `/user_managers` | Get user-manager relationships
[**patch-user-manager**](#patch-user-manager) | **PATCH** `/user_managers/{id}` | Update a user-manager relationship
[**patch-user-managers**](#patch-user-managers) | **PATCH** `/user_managers` | Update multiple user-manager relationships
[**submit-user-manager**](#submit-user-manager) | **POST** `/user_manager` | Create a new user-manager relationship
[**submit-user-managers**](#submit-user-managers) | **POST** `/user_managers` | Create multiple new user-manager relationships


## get-user-manager
Find user-manager relationship
Info for a specific user-manager relationship

[API Spec](https://developer.sailpoint.com/docs/api//get-user-manager)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | id | **str** | True  | ID of the object to retrieve, update, or delete

### Return type
[**SubmitUserManager200Response**](../models/submit-user-manager200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | SubmitUserManager200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.user_managers_api import UserManagersApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.submit_user_manager200_response import SubmitUserManager200Response
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    id = '1246d8b3-ac29-4015-8154-dea4434a73fa' # str | ID of the object to retrieve, update, or delete # str | ID of the object to retrieve, update, or delete

    try:
        # Find user-manager relationship
        
        results = UserManagersApi(api_client).get_user_manager(id=id)
        # Below is a request that includes all optional parameters
        # results = UserManagersApi(api_client).get_user_manager(id)
        print("The response of UserManagersApi->get_user_manager:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling UserManagersApi->get_user_manager: %s\n" % e)
```



[[Back to top]](#) 

## get-user-managers
Get user-manager relationships
This endpoint can retrieve user-manager relationships from Lifecycle or you can search for user-manager relationships using parameters

[API Spec](https://developer.sailpoint.com/docs/api//get-user-managers)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
  Query | limit | **int** |   (optional) | The maximum number of items to return.
  Query | offset | **int** |   (optional) | The number of items to skip before starting to collect the result set.
  Query | order | **str** |   (optional) | The field to order results by.
  Query | user_id | **str** |   (optional) | The ID of a user for filtering
  Query | manager_id | **str** |   (optional) | The ID of a user for filtering
  Query | metadata | **bool** |   (optional) (default to False) | Returns batching metadata in the response. This includes `total` as the total quantity, `next` as the path of the following query url, `limit` and `after_id` (if requested) with the next following id (null if it is the last \"page\").

### Return type
[**GetUserManagers200Response**](../models/get-user-managers200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | GetUserManagers200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.user_managers_api import UserManagersApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.get_user_managers200_response import GetUserManagers200Response
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    limit = 5 # int | The maximum number of items to return. (optional) # int | The maximum number of items to return. (optional)
    offset = 5 # int | The number of items to skip before starting to collect the result set. (optional) # int | The number of items to skip before starting to collect the result set. (optional)
    order = 'created_at' # str | The field to order results by. (optional) # str | The field to order results by. (optional)
    user_id = 'bba9cfb2-96c1-4acb-ac79-a21732527265' # str | The ID of a user for filtering (optional) # str | The ID of a user for filtering (optional)
    manager_id = 'c5e1dd38-7e29-464f-a0da-0c0d886d022a' # str | The ID of a user for filtering (optional) # str | The ID of a user for filtering (optional)
    metadata = False # bool | Returns batching metadata in the response. This includes `total` as the total quantity, `next` as the path of the following query url, `limit` and `after_id` (if requested) with the next following id (null if it is the last \"page\"). (optional) (default to False) # bool | Returns batching metadata in the response. This includes `total` as the total quantity, `next` as the path of the following query url, `limit` and `after_id` (if requested) with the next following id (null if it is the last \"page\"). (optional) (default to False)

    try:
        # Get user-manager relationships
        
        results = UserManagersApi(api_client).get_user_managers()
        # Below is a request that includes all optional parameters
        # results = UserManagersApi(api_client).get_user_managers(limit, offset, order, user_id, manager_id, metadata)
        print("The response of UserManagersApi->get_user_managers:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling UserManagersApi->get_user_managers: %s\n" % e)
```



[[Back to top]](#) 

## patch-user-manager
Update a user-manager relationship
Update a user-manager relationship by id

[API Spec](https://developer.sailpoint.com/docs/api//patch-user-manager)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | id | **str** | True  | ID of the object to retrieve, update, or delete
 Body  | submit_user_manager_request | [**SubmitUserManagerRequest**](../models/submit-user-manager-request) | True  | 

### Return type
[**SubmitUserManager200Response**](../models/submit-user-manager200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | SubmitUserManager200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.user_managers_api import UserManagersApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.submit_user_manager200_response import SubmitUserManager200Response
from sailpoint.nerm.models.submit_user_manager_request import SubmitUserManagerRequest
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    id = '1246d8b3-ac29-4015-8154-dea4434a73fa' # str | ID of the object to retrieve, update, or delete # str | ID of the object to retrieve, update, or delete
    submit_user_manager_request = '''sailpoint.nerm.SubmitUserManagerRequest()''' # SubmitUserManagerRequest | 

    try:
        # Update a user-manager relationship
        new_submit_user_manager_request = SubmitUserManagerRequest.from_json(submit_user_manager_request)
        results = UserManagersApi(api_client).patch_user_manager(id=id, submit_user_manager_request=new_submit_user_manager_request)
        # Below is a request that includes all optional parameters
        # results = UserManagersApi(api_client).patch_user_manager(id, new_submit_user_manager_request)
        print("The response of UserManagersApi->patch_user_manager:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling UserManagersApi->patch_user_manager: %s\n" % e)
```



[[Back to top]](#) 

## patch-user-managers
Update multiple user-manager relationships
Update multiple user-manager relationships

[API Spec](https://developer.sailpoint.com/docs/api//patch-user-managers)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
 Body  | submit_user_managers_request | [**SubmitUserManagersRequest**](../models/submit-user-managers-request) | True  | 

### Return type
[**SubmitUserManagers200Response**](../models/submit-user-managers200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | SubmitUserManagers200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.user_managers_api import UserManagersApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.submit_user_managers200_response import SubmitUserManagers200Response
from sailpoint.nerm.models.submit_user_managers_request import SubmitUserManagersRequest
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    submit_user_managers_request = '''sailpoint.nerm.SubmitUserManagersRequest()''' # SubmitUserManagersRequest | 

    try:
        # Update multiple user-manager relationships
        new_submit_user_managers_request = SubmitUserManagersRequest.from_json(submit_user_managers_request)
        results = UserManagersApi(api_client).patch_user_managers(submit_user_managers_request=new_submit_user_managers_request)
        # Below is a request that includes all optional parameters
        # results = UserManagersApi(api_client).patch_user_managers(new_submit_user_managers_request)
        print("The response of UserManagersApi->patch_user_managers:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling UserManagersApi->patch_user_managers: %s\n" % e)
```



[[Back to top]](#) 

## submit-user-manager
Create a new user-manager relationship
Create a new user-manager relationship

[API Spec](https://developer.sailpoint.com/docs/api//submit-user-manager)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
 Body  | submit_user_manager_request | [**SubmitUserManagerRequest**](../models/submit-user-manager-request) | True  | 

### Return type
[**SubmitUserManager200Response**](../models/submit-user-manager200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | SubmitUserManager200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.user_managers_api import UserManagersApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.submit_user_manager200_response import SubmitUserManager200Response
from sailpoint.nerm.models.submit_user_manager_request import SubmitUserManagerRequest
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    submit_user_manager_request = '''sailpoint.nerm.SubmitUserManagerRequest()''' # SubmitUserManagerRequest | 

    try:
        # Create a new user-manager relationship
        new_submit_user_manager_request = SubmitUserManagerRequest.from_json(submit_user_manager_request)
        results = UserManagersApi(api_client).submit_user_manager(submit_user_manager_request=new_submit_user_manager_request)
        # Below is a request that includes all optional parameters
        # results = UserManagersApi(api_client).submit_user_manager(new_submit_user_manager_request)
        print("The response of UserManagersApi->submit_user_manager:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling UserManagersApi->submit_user_manager: %s\n" % e)
```



[[Back to top]](#) 

## submit-user-managers
Create multiple new user-manager relationships
Create multiple new user-manager relationships

[API Spec](https://developer.sailpoint.com/docs/api//submit-user-managers)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
 Body  | submit_user_managers_request | [**SubmitUserManagersRequest**](../models/submit-user-managers-request) | True  | 

### Return type
[**SubmitUserManagers200Response**](../models/submit-user-managers200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | SubmitUserManagers200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.user_managers_api import UserManagersApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.submit_user_managers200_response import SubmitUserManagers200Response
from sailpoint.nerm.models.submit_user_managers_request import SubmitUserManagersRequest
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    submit_user_managers_request = '''sailpoint.nerm.SubmitUserManagersRequest()''' # SubmitUserManagersRequest | 

    try:
        # Create multiple new user-manager relationships
        new_submit_user_managers_request = SubmitUserManagersRequest.from_json(submit_user_managers_request)
        results = UserManagersApi(api_client).submit_user_managers(submit_user_managers_request=new_submit_user_managers_request)
        # Below is a request that includes all optional parameters
        # results = UserManagersApi(api_client).submit_user_managers(new_submit_user_managers_request)
        print("The response of UserManagersApi->submit_user_managers:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling UserManagersApi->submit_user_managers: %s\n" % e)
```



[[Back to top]](#) 



