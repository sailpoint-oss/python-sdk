---
id: profile--type-roles
title: Profile__type_roles
pagination_label: profile__type_roles
sidebar_label: profile__type_roles
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'profile__type_roles', 'profile__type_roles'] 
slug: /tools/sdk/python//methods/profile--type-roles
tags: ['SDK', 'Software Development Kit', 'profile__type_roles', 'profile__type_roles']
---

# sailpoint.nerm.ProfileTypeRolesApi
   
All URIs are relative to *https://acmeco.nonemployee.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create-profile-type-role**](#create-profile-type-role) | **POST** `/profile_type_roles` | Create a profile type role


## create-profile-type-role
Create a profile type role
This endpoint can create a profile type role. NOTE- The ability to toggle Allow/Block is done through the Profile Type

[API Spec](https://developer.sailpoint.com/docs/api//create-profile-type-role)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
 Body  | create_profile_type_role_request | [**CreateProfileTypeRoleRequest**](../models/create-profile-type-role-request) | True  | 

### Return type
[**CreateProfileTypeRole200Response**](../models/create-profile-type-role200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | CreateProfileTypeRole200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.profile_type_roles_api import ProfileTypeRolesApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.create_profile_type_role200_response import CreateProfileTypeRole200Response
from sailpoint.nerm.models.create_profile_type_role_request import CreateProfileTypeRoleRequest
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    create_profile_type_role_request = '''sailpoint.nerm.CreateProfileTypeRoleRequest()''' # CreateProfileTypeRoleRequest | 

    try:
        # Create a profile type role
        new_create_profile_type_role_request = CreateProfileTypeRoleRequest.from_json(create_profile_type_role_request)
        results = ProfileTypeRolesApi(api_client).create_profile_type_role(create_profile_type_role_request=new_create_profile_type_role_request)
        # Below is a request that includes all optional parameters
        # results = ProfileTypeRolesApi(api_client).create_profile_type_role(new_create_profile_type_role_request)
        print("The response of ProfileTypeRolesApi->create_profile_type_role:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling ProfileTypeRolesApi->create_profile_type_role: %s\n" % e)
```



[[Back to top]](#) 



