---
id: roles
title: Roles
pagination_label: roles
sidebar_label: roles
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'roles', 'roles'] 
slug: /tools/sdk/python//methods/roles
tags: ['SDK', 'Software Development Kit', 'roles', 'roles']
---

# sailpoint.nerm.RolesApi
   
All URIs are relative to *https://acmeco.nonemployee.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get-role**](#get-role) | **GET** `/roles/{id}` | Find role by id
[**get-roles**](#get-roles) | **GET** `/roles` | Get roles
[**patch-role**](#patch-role) | **PATCH** `/roles/{id}` | Update an existing role
[**patch-roles**](#patch-roles) | **PATCH** `/roles` | Update multiple roles
[**submit-role**](#submit-role) | **POST** `/role` | Create a new role
[**submit-roles**](#submit-roles) | **POST** `/roles` | Create multiple new roles


## get-role
Find role by id
Info for a specific user role

[API Spec](https://developer.sailpoint.com/docs/api//get-role)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | id | **str** | True  | ID of the object to retrieve, update, or delete

### Return type
[**SubmitRole200Response**](../models/submit-role200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | SubmitRole200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.roles_api import RolesApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.submit_role200_response import SubmitRole200Response
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    id = '1246d8b3-ac29-4015-8154-dea4434a73fa' # str | ID of the object to retrieve, update, or delete # str | ID of the object to retrieve, update, or delete

    try:
        # Find role by id
        
        results = RolesApi(api_client).get_role(id=id)
        # Below is a request that includes all optional parameters
        # results = RolesApi(api_client).get_role(id)
        print("The response of RolesApi->get_role:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling RolesApi->get_role: %s\n" % e)
```



[[Back to top]](#) 

## get-roles
Get roles
This endpoint can retrieve roles from NERM. Optionally you can provide parameters to filter results.

[API Spec](https://developer.sailpoint.com/docs/api//get-roles)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
  Query | limit | **int** |   (optional) | The maximum number of items to return.
  Query | offset | **int** |   (optional) | The number of items to skip before starting to collect the result set.
  Query | order | **str** |   (optional) | The field to order results by.
  Query | metadata | **bool** |   (optional) (default to False) | Returns batching metadata in the response. This includes `total` as the total quantity, `next` as the path of the following query url, `limit` and `after_id` (if requested) with the next following id (null if it is the last \"page\").
  Query | type | **str** |   (optional) | Filter roles by type.

### Return type
[**GetRoles200Response**](../models/get-roles200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | GetRoles200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.roles_api import RolesApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.get_roles200_response import GetRoles200Response
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    limit = 5 # int | The maximum number of items to return. (optional) # int | The maximum number of items to return. (optional)
    offset = 5 # int | The number of items to skip before starting to collect the result set. (optional) # int | The number of items to skip before starting to collect the result set. (optional)
    order = 'created_at' # str | The field to order results by. (optional) # str | The field to order results by. (optional)
    metadata = False # bool | Returns batching metadata in the response. This includes `total` as the total quantity, `next` as the path of the following query url, `limit` and `after_id` (if requested) with the next following id (null if it is the last \"page\"). (optional) (default to False) # bool | Returns batching metadata in the response. This includes `total` as the total quantity, `next` as the path of the following query url, `limit` and `after_id` (if requested) with the next following id (null if it is the last \"page\"). (optional) (default to False)
    type = 'NeprofileRole' # str | Filter roles by type. (optional) # str | Filter roles by type. (optional)

    try:
        # Get roles
        
        results = RolesApi(api_client).get_roles()
        # Below is a request that includes all optional parameters
        # results = RolesApi(api_client).get_roles(limit, offset, order, metadata, type)
        print("The response of RolesApi->get_roles:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling RolesApi->get_roles: %s\n" % e)
```



[[Back to top]](#) 

## patch-role
Update an existing role
Update an existing role

[API Spec](https://developer.sailpoint.com/docs/api//patch-role)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | id | **str** | True  | ID of the object to retrieve, update, or delete
 Body  | submit_role_request | [**SubmitRoleRequest**](../models/submit-role-request) | True  | 

### Return type
[**SubmitRole200Response**](../models/submit-role200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | SubmitRole200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.roles_api import RolesApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.submit_role200_response import SubmitRole200Response
from sailpoint.nerm.models.submit_role_request import SubmitRoleRequest
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    id = '1246d8b3-ac29-4015-8154-dea4434a73fa' # str | ID of the object to retrieve, update, or delete # str | ID of the object to retrieve, update, or delete
    submit_role_request = '''sailpoint.nerm.SubmitRoleRequest()''' # SubmitRoleRequest | 

    try:
        # Update an existing role
        new_submit_role_request = SubmitRoleRequest.from_json(submit_role_request)
        results = RolesApi(api_client).patch_role(id=id, submit_role_request=new_submit_role_request)
        # Below is a request that includes all optional parameters
        # results = RolesApi(api_client).patch_role(id, new_submit_role_request)
        print("The response of RolesApi->patch_role:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling RolesApi->patch_role: %s\n" % e)
```



[[Back to top]](#) 

## patch-roles
Update multiple roles
Update multiple users

[API Spec](https://developer.sailpoint.com/docs/api//patch-roles)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
 Body  | submit_roles_request | [**SubmitRolesRequest**](../models/submit-roles-request) | True  | 

### Return type
[**SubmitRoles200Response**](../models/submit-roles200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | SubmitRoles200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.roles_api import RolesApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.submit_roles200_response import SubmitRoles200Response
from sailpoint.nerm.models.submit_roles_request import SubmitRolesRequest
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    submit_roles_request = '''sailpoint.nerm.SubmitRolesRequest()''' # SubmitRolesRequest | 

    try:
        # Update multiple roles
        new_submit_roles_request = SubmitRolesRequest.from_json(submit_roles_request)
        results = RolesApi(api_client).patch_roles(submit_roles_request=new_submit_roles_request)
        # Below is a request that includes all optional parameters
        # results = RolesApi(api_client).patch_roles(new_submit_roles_request)
        print("The response of RolesApi->patch_roles:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling RolesApi->patch_roles: %s\n" % e)
```



[[Back to top]](#) 

## submit-role
Create a new role
Create a new role

[API Spec](https://developer.sailpoint.com/docs/api//submit-role)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
 Body  | submit_role_request | [**SubmitRoleRequest**](../models/submit-role-request) | True  | 

### Return type
[**SubmitRole200Response**](../models/submit-role200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | SubmitRole200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.roles_api import RolesApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.submit_role200_response import SubmitRole200Response
from sailpoint.nerm.models.submit_role_request import SubmitRoleRequest
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    submit_role_request = '''sailpoint.nerm.SubmitRoleRequest()''' # SubmitRoleRequest | 

    try:
        # Create a new role
        new_submit_role_request = SubmitRoleRequest.from_json(submit_role_request)
        results = RolesApi(api_client).submit_role(submit_role_request=new_submit_role_request)
        # Below is a request that includes all optional parameters
        # results = RolesApi(api_client).submit_role(new_submit_role_request)
        print("The response of RolesApi->submit_role:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling RolesApi->submit_role: %s\n" % e)
```



[[Back to top]](#) 

## submit-roles
Create multiple new roles
Create multiple new users

[API Spec](https://developer.sailpoint.com/docs/api//submit-roles)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
 Body  | submit_roles_request | [**SubmitRolesRequest**](../models/submit-roles-request) | True  | 

### Return type
[**SubmitRoles200Response**](../models/submit-roles200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | SubmitRoles200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.roles_api import RolesApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.submit_roles200_response import SubmitRoles200Response
from sailpoint.nerm.models.submit_roles_request import SubmitRolesRequest
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    submit_roles_request = '''sailpoint.nerm.SubmitRolesRequest()''' # SubmitRolesRequest | 

    try:
        # Create multiple new roles
        new_submit_roles_request = SubmitRolesRequest.from_json(submit_roles_request)
        results = RolesApi(api_client).submit_roles(submit_roles_request=new_submit_roles_request)
        # Below is a request that includes all optional parameters
        # results = RolesApi(api_client).submit_roles(new_submit_roles_request)
        print("The response of RolesApi->submit_roles:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling RolesApi->submit_roles: %s\n" % e)
```



[[Back to top]](#) 



