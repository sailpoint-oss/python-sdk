---
id: permissions
title: Permissions
pagination_label: permissions
sidebar_label: permissions
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'permissions', 'permissions'] 
slug: /tools/sdk/python//methods/permissions
tags: ['SDK', 'Software Development Kit', 'permissions', 'permissions']
---

# sailpoint.nerm.PermissionsApi
   
All URIs are relative to *https://acmeco.nonemployee.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create-permission**](#create-permission) | **POST** `/permissions` | Create a permission


## create-permission
Create a permission
This endpoint can create permissions for Lifecycle, Consolidation, and Collaboration

[API Spec](https://developer.sailpoint.com/docs/api//create-permission)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
 Body  | create_permission_request | [**CreatePermissionRequest**](../models/create-permission-request) | True  | 

### Return type
[**CreatePermission200Response**](../models/create-permission200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | CreatePermission200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.permissions_api import PermissionsApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.create_permission200_response import CreatePermission200Response
from sailpoint.nerm.models.create_permission_request import CreatePermissionRequest
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    create_permission_request = '''sailpoint.nerm.CreatePermissionRequest()''' # CreatePermissionRequest | 

    try:
        # Create a permission
        new_create_permission_request = CreatePermissionRequest.from_json(create_permission_request)
        results = PermissionsApi(api_client).create_permission(create_permission_request=new_create_permission_request)
        # Below is a request that includes all optional parameters
        # results = PermissionsApi(api_client).create_permission(new_create_permission_request)
        print("The response of PermissionsApi->create_permission:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling PermissionsApi->create_permission: %s\n" % e)
```



[[Back to top]](#) 



