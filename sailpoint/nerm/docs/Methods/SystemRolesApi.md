---
id: system-roles
title: System_roles
pagination_label: system_roles
sidebar_label: system_roles
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'system_roles', 'system_roles'] 
slug: /tools/sdk/python//methods/system-roles
tags: ['SDK', 'Software Development Kit', 'system_roles', 'system_roles']
---

# sailpoint.nerm.SystemRolesApi
   
All URIs are relative to *https://acmeco.nonemployee.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get-system-roles**](#get-system-roles) | **GET** `/system_roles` | Get system roles


## get-system-roles
Get system roles
This endpoint can retrieve system roles from NERM. Optionally you can provide parameters to filter results.

[API Spec](https://developer.sailpoint.com/docs/api//get-system-roles)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
  Query | limit | **int** |   (optional) | The maximum number of items to return.
  Query | offset | **int** |   (optional) | The number of items to skip before starting to collect the result set.
  Query | order | **str** |   (optional) | The field to order results by.
  Query | metadata | **bool** |   (optional) (default to False) | Returns batching metadata in the response. This includes `total` as the total quantity, `next` as the path of the following query url, `limit` and `after_id` (if requested) with the next following id (null if it is the last \"page\").

### Return type
[**GetSystemRoles200Response**](../models/get-system-roles200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | GetSystemRoles200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.system_roles_api import SystemRolesApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.get_system_roles200_response import GetSystemRoles200Response
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    limit = 5 # int | The maximum number of items to return. (optional) # int | The maximum number of items to return. (optional)
    offset = 5 # int | The number of items to skip before starting to collect the result set. (optional) # int | The number of items to skip before starting to collect the result set. (optional)
    order = 'created_at' # str | The field to order results by. (optional) # str | The field to order results by. (optional)
    metadata = False # bool | Returns batching metadata in the response. This includes `total` as the total quantity, `next` as the path of the following query url, `limit` and `after_id` (if requested) with the next following id (null if it is the last \"page\"). (optional) (default to False) # bool | Returns batching metadata in the response. This includes `total` as the total quantity, `next` as the path of the following query url, `limit` and `after_id` (if requested) with the next following id (null if it is the last \"page\"). (optional) (default to False)

    try:
        # Get system roles
        
        results = SystemRolesApi(api_client).get_system_roles()
        # Below is a request that includes all optional parameters
        # results = SystemRolesApi(api_client).get_system_roles(limit, offset, order, metadata)
        print("The response of SystemRolesApi->get_system_roles:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling SystemRolesApi->get_system_roles: %s\n" % e)
```



[[Back to top]](#) 



