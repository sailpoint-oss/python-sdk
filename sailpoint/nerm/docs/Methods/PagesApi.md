---
id: pages
title: Pages
pagination_label: pages
sidebar_label: pages
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'pages', 'pages'] 
slug: /tools/sdk/python//methods/pages
tags: ['SDK', 'Software Development Kit', 'pages', 'pages']
---

# sailpoint.nerm.PagesApi
   
All URIs are relative to *https://acmeco.nonemployee.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create-profile-page**](#create-profile-page) | **POST** `/pages/profile_pages` | Create a profile page
[**create-workflow-page**](#create-workflow-page) | **POST** `/pages/workflow_pages` | Create a workflow page


## create-profile-page
Create a profile page
Create a profile page

[API Spec](https://developer.sailpoint.com/docs/api//create-profile-page)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
 Body  | create_profile_page_request | [**CreateProfilePageRequest**](../models/create-profile-page-request) | True  | 

### Return type
[**CreateProfilePage200Response**](../models/create-profile-page200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | CreateProfilePage200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.pages_api import PagesApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.create_profile_page200_response import CreateProfilePage200Response
from sailpoint.nerm.models.create_profile_page_request import CreateProfilePageRequest
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    create_profile_page_request = '''sailpoint.nerm.CreateProfilePageRequest()''' # CreateProfilePageRequest | 

    try:
        # Create a profile page
        new_create_profile_page_request = CreateProfilePageRequest.from_json(create_profile_page_request)
        results = PagesApi(api_client).create_profile_page(create_profile_page_request=new_create_profile_page_request)
        # Below is a request that includes all optional parameters
        # results = PagesApi(api_client).create_profile_page(new_create_profile_page_request)
        print("The response of PagesApi->create_profile_page:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling PagesApi->create_profile_page: %s\n" % e)
```



[[Back to top]](#) 

## create-workflow-page
Create a workflow page
Create a workflow page

[API Spec](https://developer.sailpoint.com/docs/api//create-workflow-page)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
 Body  | create_workflow_page_request | [**CreateWorkflowPageRequest**](../models/create-workflow-page-request) | True  | 

### Return type
[**CreateProfilePage200Response**](../models/create-profile-page200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | CreateProfilePage200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.pages_api import PagesApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.create_profile_page200_response import CreateProfilePage200Response
from sailpoint.nerm.models.create_workflow_page_request import CreateWorkflowPageRequest
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    create_workflow_page_request = '''sailpoint.nerm.CreateWorkflowPageRequest()''' # CreateWorkflowPageRequest | 

    try:
        # Create a workflow page
        new_create_workflow_page_request = CreateWorkflowPageRequest.from_json(create_workflow_page_request)
        results = PagesApi(api_client).create_workflow_page(create_workflow_page_request=new_create_workflow_page_request)
        # Below is a request that includes all optional parameters
        # results = PagesApi(api_client).create_workflow_page(new_create_workflow_page_request)
        print("The response of PagesApi->create_workflow_page:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling PagesApi->create_workflow_page: %s\n" % e)
```



[[Back to top]](#) 



