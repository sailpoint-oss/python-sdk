---
id: system-role-permissions
title: System_role_permissions
pagination_label: system_role_permissions
sidebar_label: system_role_permissions
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'system_role_permissions', 'system_role_permissions'] 
slug: /tools/sdk/python//methods/system-role-permissions
tags: ['SDK', 'Software Development Kit', 'system_role_permissions', 'system_role_permissions']
---

# sailpoint.nerm.SystemRolePermissionsApi
   
All URIs are relative to *https://acmeco.nonemployee.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create-system-role-permission**](#create-system-role-permission) | **POST** `/system_role_permissions` | Create a system role permission


## create-system-role-permission
Create a system role permission
This endpoint can create system role permissions for Lifecycle System Roles

[API Spec](https://developer.sailpoint.com/docs/api//create-system-role-permission)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
 Body  | create_system_role_permission_request | [**CreateSystemRolePermissionRequest**](../models/create-system-role-permission-request) | True  | 

### Return type
[**CreateSystemRolePermission200Response**](../models/create-system-role-permission200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | CreateSystemRolePermission200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.system_role_permissions_api import SystemRolePermissionsApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.create_system_role_permission200_response import CreateSystemRolePermission200Response
from sailpoint.nerm.models.create_system_role_permission_request import CreateSystemRolePermissionRequest
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    create_system_role_permission_request = '''sailpoint.nerm.CreateSystemRolePermissionRequest()''' # CreateSystemRolePermissionRequest | 

    try:
        # Create a system role permission
        new_create_system_role_permission_request = CreateSystemRolePermissionRequest.from_json(create_system_role_permission_request)
        results = SystemRolePermissionsApi(api_client).create_system_role_permission(create_system_role_permission_request=new_create_system_role_permission_request)
        # Below is a request that includes all optional parameters
        # results = SystemRolePermissionsApi(api_client).create_system_role_permission(new_create_system_role_permission_request)
        print("The response of SystemRolePermissionsApi->create_system_role_permission:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling SystemRolePermissionsApi->create_system_role_permission: %s\n" % e)
```



[[Back to top]](#) 



