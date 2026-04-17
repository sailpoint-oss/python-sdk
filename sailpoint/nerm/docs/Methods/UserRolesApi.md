---
id: user-roles
title: User_roles
pagination_label: user_roles
sidebar_label: user_roles
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'user_roles', 'user_roles'] 
slug: /tools/sdk/python//methods/user-roles
tags: ['SDK', 'Software Development Kit', 'user_roles', 'user_roles']
---

# sailpoint.nerm.UserRolesApi
   
All URIs are relative to *https://acmeco.nonemployee.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete-user-role**](#delete-user-role) | **DELETE** `/user_role/{id}` | Delete a user role assignment
[**get-user-role**](#get-user-role) | **GET** `/user_roles/{id}` | Find user role pairing
[**get-user-roles**](#get-user-roles) | **GET** `/user_roles` | Get user role pairings
[**patch-user-role**](#patch-user-role) | **PATCH** `/user_roles/{id}` | Update a user role pairing
[**patch-user-roles**](#patch-user-roles) | **PATCH** `/user_roles` | Update multiple user role pairings
[**submit-user-role**](#submit-user-role) | **POST** `/user_role` | Assign new role to user
[**submit-user-roles**](#submit-user-roles) | **POST** `/user_roles` | Create new user role pairings


## delete-user-role
Delete a user role assignment
Delete a user role assignment

[API Spec](https://developer.sailpoint.com/docs/api//delete-user-role)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | id | **str** | True  | ID of the object to retrieve, update, or delete

### Return type
**object**

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | User role was destroyed | object |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.user_roles_api import UserRolesApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    id = '1246d8b3-ac29-4015-8154-dea4434a73fa' # str | ID of the object to retrieve, update, or delete # str | ID of the object to retrieve, update, or delete

    try:
        # Delete a user role assignment
        
        results = UserRolesApi(api_client).delete_user_role(id=id)
        # Below is a request that includes all optional parameters
        # results = UserRolesApi(api_client).delete_user_role(id)
        print("The response of UserRolesApi->delete_user_role:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling UserRolesApi->delete_user_role: %s\n" % e)
```



[[Back to top]](#) 

## get-user-role
Find user role pairing
Info for a specific user role pairing

[API Spec](https://developer.sailpoint.com/docs/api//get-user-role)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | id | **str** | True  | ID of the object to retrieve, update, or delete

### Return type
[**SubmitUserRole200Response**](../models/submit-user-role200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | SubmitUserRole200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.user_roles_api import UserRolesApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.submit_user_role200_response import SubmitUserRole200Response
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    id = '1246d8b3-ac29-4015-8154-dea4434a73fa' # str | ID of the object to retrieve, update, or delete # str | ID of the object to retrieve, update, or delete

    try:
        # Find user role pairing
        
        results = UserRolesApi(api_client).get_user_role(id=id)
        # Below is a request that includes all optional parameters
        # results = UserRolesApi(api_client).get_user_role(id)
        print("The response of UserRolesApi->get_user_role:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling UserRolesApi->get_user_role: %s\n" % e)
```



[[Back to top]](#) 

## get-user-roles
Get user role pairings
This endpoint can retrieve user role pairings from Lifecycle or you can search for user role pairings using parameters

[API Spec](https://developer.sailpoint.com/docs/api//get-user-roles)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
  Query | limit | **int** |   (optional) | The maximum number of items to return.
  Query | offset | **int** |   (optional) | The number of items to skip before starting to collect the result set.
  Query | order | **str** |   (optional) | The field to order results by.
  Query | user_id | **str** |   (optional) | The ID of a user for filtering
  Query | role_id | **str** |   (optional) | The ID of a role for filtering
  Query | metadata | **bool** |   (optional) (default to False) | Returns batching metadata in the response. This includes `total` as the total quantity, `next` as the path of the following query url, `limit` and `after_id` (if requested) with the next following id (null if it is the last \"page\").

### Return type
[**GetUserRoles200Response**](../models/get-user-roles200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | GetUserRoles200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.user_roles_api import UserRolesApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.get_user_roles200_response import GetUserRoles200Response
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    limit = 5 # int | The maximum number of items to return. (optional) # int | The maximum number of items to return. (optional)
    offset = 5 # int | The number of items to skip before starting to collect the result set. (optional) # int | The number of items to skip before starting to collect the result set. (optional)
    order = 'created_at' # str | The field to order results by. (optional) # str | The field to order results by. (optional)
    user_id = 'bba9cfb2-96c1-4acb-ac79-a21732527265' # str | The ID of a user for filtering (optional) # str | The ID of a user for filtering (optional)
    role_id = 'c5e1dd38-7e29-464f-a0da-0c0d886d022a' # str | The ID of a role for filtering (optional) # str | The ID of a role for filtering (optional)
    metadata = False # bool | Returns batching metadata in the response. This includes `total` as the total quantity, `next` as the path of the following query url, `limit` and `after_id` (if requested) with the next following id (null if it is the last \"page\"). (optional) (default to False) # bool | Returns batching metadata in the response. This includes `total` as the total quantity, `next` as the path of the following query url, `limit` and `after_id` (if requested) with the next following id (null if it is the last \"page\"). (optional) (default to False)

    try:
        # Get user role pairings
        
        results = UserRolesApi(api_client).get_user_roles()
        # Below is a request that includes all optional parameters
        # results = UserRolesApi(api_client).get_user_roles(limit, offset, order, user_id, role_id, metadata)
        print("The response of UserRolesApi->get_user_roles:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling UserRolesApi->get_user_roles: %s\n" % e)
```



[[Back to top]](#) 

## patch-user-role
Update a user role pairing
Update a user role pairing by id

[API Spec](https://developer.sailpoint.com/docs/api//patch-user-role)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | id | **str** | True  | ID of the object to retrieve, update, or delete
 Body  | submit_user_role_request | [**SubmitUserRoleRequest**](../models/submit-user-role-request) | True  | 

### Return type
[**SubmitUserRole200Response**](../models/submit-user-role200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | SubmitUserRole200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.user_roles_api import UserRolesApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.submit_user_role200_response import SubmitUserRole200Response
from sailpoint.nerm.models.submit_user_role_request import SubmitUserRoleRequest
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    id = '1246d8b3-ac29-4015-8154-dea4434a73fa' # str | ID of the object to retrieve, update, or delete # str | ID of the object to retrieve, update, or delete
    submit_user_role_request = '''sailpoint.nerm.SubmitUserRoleRequest()''' # SubmitUserRoleRequest | 

    try:
        # Update a user role pairing
        new_submit_user_role_request = SubmitUserRoleRequest.from_json(submit_user_role_request)
        results = UserRolesApi(api_client).patch_user_role(id=id, submit_user_role_request=new_submit_user_role_request)
        # Below is a request that includes all optional parameters
        # results = UserRolesApi(api_client).patch_user_role(id, new_submit_user_role_request)
        print("The response of UserRolesApi->patch_user_role:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling UserRolesApi->patch_user_role: %s\n" % e)
```



[[Back to top]](#) 

## patch-user-roles
Update multiple user role pairings
Update multiple user role pairings

[API Spec](https://developer.sailpoint.com/docs/api//patch-user-roles)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
 Body  | submit_user_roles_request | [**SubmitUserRolesRequest**](../models/submit-user-roles-request) | True  | 

### Return type
[**SubmitUserRoles200Response**](../models/submit-user-roles200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | SubmitUserRoles200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.user_roles_api import UserRolesApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.submit_user_roles200_response import SubmitUserRoles200Response
from sailpoint.nerm.models.submit_user_roles_request import SubmitUserRolesRequest
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    submit_user_roles_request = '''sailpoint.nerm.SubmitUserRolesRequest()''' # SubmitUserRolesRequest | 

    try:
        # Update multiple user role pairings
        new_submit_user_roles_request = SubmitUserRolesRequest.from_json(submit_user_roles_request)
        results = UserRolesApi(api_client).patch_user_roles(submit_user_roles_request=new_submit_user_roles_request)
        # Below is a request that includes all optional parameters
        # results = UserRolesApi(api_client).patch_user_roles(new_submit_user_roles_request)
        print("The response of UserRolesApi->patch_user_roles:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling UserRolesApi->patch_user_roles: %s\n" % e)
```



[[Back to top]](#) 

## submit-user-role
Assign new role to user
Assign a new role to a user

[API Spec](https://developer.sailpoint.com/docs/api//submit-user-role)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
 Body  | submit_user_role_request | [**SubmitUserRoleRequest**](../models/submit-user-role-request) | True  | 

### Return type
[**SubmitUserRole200Response**](../models/submit-user-role200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | SubmitUserRole200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.user_roles_api import UserRolesApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.submit_user_role200_response import SubmitUserRole200Response
from sailpoint.nerm.models.submit_user_role_request import SubmitUserRoleRequest
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    submit_user_role_request = '''sailpoint.nerm.SubmitUserRoleRequest()''' # SubmitUserRoleRequest | 

    try:
        # Assign new role to user
        new_submit_user_role_request = SubmitUserRoleRequest.from_json(submit_user_role_request)
        results = UserRolesApi(api_client).submit_user_role(submit_user_role_request=new_submit_user_role_request)
        # Below is a request that includes all optional parameters
        # results = UserRolesApi(api_client).submit_user_role(new_submit_user_role_request)
        print("The response of UserRolesApi->submit_user_role:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling UserRolesApi->submit_user_role: %s\n" % e)
```



[[Back to top]](#) 

## submit-user-roles
Create new user role pairings
Create multiple new user role pairings

[API Spec](https://developer.sailpoint.com/docs/api//submit-user-roles)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
 Body  | submit_user_roles_request | [**SubmitUserRolesRequest**](../models/submit-user-roles-request) | True  | 

### Return type
[**SubmitUserRoles200Response**](../models/submit-user-roles200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | SubmitUserRoles200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.user_roles_api import UserRolesApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.submit_user_roles200_response import SubmitUserRoles200Response
from sailpoint.nerm.models.submit_user_roles_request import SubmitUserRolesRequest
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    submit_user_roles_request = '''sailpoint.nerm.SubmitUserRolesRequest()''' # SubmitUserRolesRequest | 

    try:
        # Create new user role pairings
        new_submit_user_roles_request = SubmitUserRolesRequest.from_json(submit_user_roles_request)
        results = UserRolesApi(api_client).submit_user_roles(submit_user_roles_request=new_submit_user_roles_request)
        # Below is a request that includes all optional parameters
        # results = UserRolesApi(api_client).submit_user_roles(new_submit_user_roles_request)
        print("The response of UserRolesApi->submit_user_roles:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling UserRolesApi->submit_user_roles: %s\n" % e)
```



[[Back to top]](#) 



