---
id: page-contents
title: Page_contents
pagination_label: page_contents
sidebar_label: page_contents
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'page_contents', 'page_contents'] 
slug: /tools/sdk/python//methods/page-contents
tags: ['SDK', 'Software Development Kit', 'page_contents', 'page_contents']
---

# sailpoint.nerm.PageContentsApi
   
All URIs are relative to *https://acmeco.nonemployee.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create-page-content**](#create-page-content) | **POST** `/page_contents` | Create a page content entry
[**delete-page-content-by-id**](#delete-page-content-by-id) | **DELETE** `/page_contents/{id}` | Delete page content record
[**delete-page-content-by-uid**](#delete-page-content-by-uid) | **DELETE** `/page_contents/{uid}` | Delete page content record
[**get-page-content-by-id**](#get-page-content-by-id) | **GET** `/page_contents/{id}` | Find page content record
[**get-page-content-by-uid**](#get-page-content-by-uid) | **GET** `/page_contents/{uid}` | Find a page content record
[**get-page-contents**](#get-page-contents) | **GET** `/page_contents` | Get page contents data
[**update-page-content-by-id**](#update-page-content-by-id) | **PATCH** `/page_contents/{id}` | Update page content record
[**update-page-content-by-uid**](#update-page-content-by-uid) | **PATCH** `/page_contents/{uid}` | Update page content record


## create-page-content
Create a page content entry
This endpoint can create page content

[API Spec](https://developer.sailpoint.com/docs/api//create-page-content)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
 Body  | create_page_content_request | [**CreatePageContentRequest**](../models/create-page-content-request) | True  | 

### Return type
[**GetPageContents200Response**](../models/get-page-contents200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
201 | Expected response to a valid request | GetPageContents200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.page_contents_api import PageContentsApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.create_page_content_request import CreatePageContentRequest
from sailpoint.nerm.models.get_page_contents200_response import GetPageContents200Response
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    create_page_content_request = '''sailpoint.nerm.CreatePageContentRequest()''' # CreatePageContentRequest | 

    try:
        # Create a page content entry
        new_create_page_content_request = CreatePageContentRequest.from_json(create_page_content_request)
        results = PageContentsApi(api_client).create_page_content(create_page_content_request=new_create_page_content_request)
        # Below is a request that includes all optional parameters
        # results = PageContentsApi(api_client).create_page_content(new_create_page_content_request)
        print("The response of PageContentsApi->create_page_content:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling PageContentsApi->create_page_content: %s\n" % e)
```



[[Back to top]](#) 

## delete-page-content-by-id
Delete page content record
Delete page content by id

[API Spec](https://developer.sailpoint.com/docs/api//delete-page-content-by-id)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | id | **str** | True  | ID of the object to retrieve, update, or delete

### Return type
[**GetPageContents200Response**](../models/get-page-contents200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | GetPageContents200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.page_contents_api import PageContentsApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.get_page_contents200_response import GetPageContents200Response
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    id = '1246d8b3-ac29-4015-8154-dea4434a73fa' # str | ID of the object to retrieve, update, or delete # str | ID of the object to retrieve, update, or delete

    try:
        # Delete page content record
        
        results = PageContentsApi(api_client).delete_page_content_by_id(id=id)
        # Below is a request that includes all optional parameters
        # results = PageContentsApi(api_client).delete_page_content_by_id(id)
        print("The response of PageContentsApi->delete_page_content_by_id:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling PageContentsApi->delete_page_content_by_id: %s\n" % e)
```



[[Back to top]](#) 

## delete-page-content-by-uid
Delete page content record
Delete page content by by UID (user-specified identifier)

[API Spec](https://developer.sailpoint.com/docs/api//delete-page-content-by-uid)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | id | **str** | True  | ID of the object to retrieve, update, or delete

### Return type
[**GetPageContents200Response**](../models/get-page-contents200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | GetPageContents200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
404 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.page_contents_api import PageContentsApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.get_page_contents200_response import GetPageContents200Response
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    id = '1246d8b3-ac29-4015-8154-dea4434a73fa' # str | ID of the object to retrieve, update, or delete # str | ID of the object to retrieve, update, or delete

    try:
        # Delete page content record
        
        results = PageContentsApi(api_client).delete_page_content_by_uid(id=id)
        # Below is a request that includes all optional parameters
        # results = PageContentsApi(api_client).delete_page_content_by_uid(id)
        print("The response of PageContentsApi->delete_page_content_by_uid:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling PageContentsApi->delete_page_content_by_uid: %s\n" % e)
```



[[Back to top]](#) 

## get-page-content-by-id
Find page content record
Info for a specific page content record

[API Spec](https://developer.sailpoint.com/docs/api//get-page-content-by-id)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | id | **str** | True  | ID of the object to retrieve, update, or delete

### Return type
[**GetPageContents200Response**](../models/get-page-contents200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | GetPageContents200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.page_contents_api import PageContentsApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.get_page_contents200_response import GetPageContents200Response
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    id = '1246d8b3-ac29-4015-8154-dea4434a73fa' # str | ID of the object to retrieve, update, or delete # str | ID of the object to retrieve, update, or delete

    try:
        # Find page content record
        
        results = PageContentsApi(api_client).get_page_content_by_id(id=id)
        # Below is a request that includes all optional parameters
        # results = PageContentsApi(api_client).get_page_content_by_id(id)
        print("The response of PageContentsApi->get_page_content_by_id:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling PageContentsApi->get_page_content_by_id: %s\n" % e)
```



[[Back to top]](#) 

## get-page-content-by-uid
Find a page content record
Info for a specific page content record by UID (user-specified identifier)

[API Spec](https://developer.sailpoint.com/docs/api//get-page-content-by-uid)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | uid | **str** |   (optional) | UID of the object to retrieve, update, or delete.  A UID or \"specified identifier\" is a string typically in \"snake_case\" format that provides a human-readable description of the record.  They are commonly used to ensure sandbox, qa, staging and production tenants have the identical configuration items loaded.  Every record has a UID assigned when persisted. When not specified the system assigns one by default.  A default value looks like a 32 character string of random hexadecimal characters.

### Return type
[**GetPageContents200Response**](../models/get-page-contents200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | GetPageContents200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.page_contents_api import PageContentsApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.get_page_contents200_response import GetPageContents200Response
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    uid = 'middle_initial_attribute' # str | UID of the object to retrieve, update, or delete.  A UID or \"specified identifier\" is a string typically in \"snake_case\" format that provides a human-readable description of the record.  They are commonly used to ensure sandbox, qa, staging and production tenants have the identical configuration items loaded.  Every record has a UID assigned when persisted. When not specified the system assigns one by default.  A default value looks like a 32 character string of random hexadecimal characters. (optional) # str | UID of the object to retrieve, update, or delete.  A UID or \"specified identifier\" is a string typically in \"snake_case\" format that provides a human-readable description of the record.  They are commonly used to ensure sandbox, qa, staging and production tenants have the identical configuration items loaded.  Every record has a UID assigned when persisted. When not specified the system assigns one by default.  A default value looks like a 32 character string of random hexadecimal characters. (optional)

    try:
        # Find a page content record
        
        results = PageContentsApi(api_client).get_page_content_by_uid()
        # Below is a request that includes all optional parameters
        # results = PageContentsApi(api_client).get_page_content_by_uid(uid)
        print("The response of PageContentsApi->get_page_content_by_uid:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling PageContentsApi->get_page_content_by_uid: %s\n" % e)
```



[[Back to top]](#) 

## get-page-contents
Get page contents data
This endpoint can retrieve page content data.

[API Spec](https://developer.sailpoint.com/docs/api//get-page-contents)

### Parameters 
This endpoint does not need any parameter. 

### Return type
[**GetPageContents200Response**](../models/get-page-contents200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | GetPageContents200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.page_contents_api import PageContentsApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.get_page_contents200_response import GetPageContents200Response
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:

    try:
        # Get page contents data
        
        results = PageContentsApi(api_client).get_page_contents()
        # Below is a request that includes all optional parameters
        # results = PageContentsApi(api_client).get_page_contents()
        print("The response of PageContentsApi->get_page_contents:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling PageContentsApi->get_page_contents: %s\n" % e)
```



[[Back to top]](#) 

## update-page-content-by-id
Update page content record
Update info for a specific page content record by id

[API Spec](https://developer.sailpoint.com/docs/api//update-page-content-by-id)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | id | **str** | True  | ID of the object to retrieve, update, or delete
 Body  | create_page_content_request | [**CreatePageContentRequest**](../models/create-page-content-request) | True  | 

### Return type
[**GetPageContents200Response**](../models/get-page-contents200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | GetPageContents200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
404 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.page_contents_api import PageContentsApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.create_page_content_request import CreatePageContentRequest
from sailpoint.nerm.models.get_page_contents200_response import GetPageContents200Response
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    id = '1246d8b3-ac29-4015-8154-dea4434a73fa' # str | ID of the object to retrieve, update, or delete # str | ID of the object to retrieve, update, or delete
    create_page_content_request = '''sailpoint.nerm.CreatePageContentRequest()''' # CreatePageContentRequest | 

    try:
        # Update page content record
        new_create_page_content_request = CreatePageContentRequest.from_json(create_page_content_request)
        results = PageContentsApi(api_client).update_page_content_by_id(id=id, create_page_content_request=new_create_page_content_request)
        # Below is a request that includes all optional parameters
        # results = PageContentsApi(api_client).update_page_content_by_id(id, new_create_page_content_request)
        print("The response of PageContentsApi->update_page_content_by_id:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling PageContentsApi->update_page_content_by_id: %s\n" % e)
```



[[Back to top]](#) 

## update-page-content-by-uid
Update page content record
Update info for a specific page content record by UID (user-specified identifier)

[API Spec](https://developer.sailpoint.com/docs/api//update-page-content-by-uid)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
 Body  | create_page_content_request | [**CreatePageContentRequest**](../models/create-page-content-request) | True  | 
Path   | uid | **str** |   (optional) | UID of the object to retrieve, update, or delete.  A UID or \"specified identifier\" is a string typically in \"snake_case\" format that provides a human-readable description of the record.  They are commonly used to ensure sandbox, qa, staging and production tenants have the identical configuration items loaded.  Every record has a UID assigned when persisted. When not specified the system assigns one by default.  A default value looks like a 32 character string of random hexadecimal characters.

### Return type
[**GetPageContents200Response**](../models/get-page-contents200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | GetPageContents200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
404 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.page_contents_api import PageContentsApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.create_page_content_request import CreatePageContentRequest
from sailpoint.nerm.models.get_page_contents200_response import GetPageContents200Response
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    create_page_content_request = '''sailpoint.nerm.CreatePageContentRequest()''' # CreatePageContentRequest | 
    uid = 'middle_initial_attribute' # str | UID of the object to retrieve, update, or delete.  A UID or \"specified identifier\" is a string typically in \"snake_case\" format that provides a human-readable description of the record.  They are commonly used to ensure sandbox, qa, staging and production tenants have the identical configuration items loaded.  Every record has a UID assigned when persisted. When not specified the system assigns one by default.  A default value looks like a 32 character string of random hexadecimal characters. (optional) # str | UID of the object to retrieve, update, or delete.  A UID or \"specified identifier\" is a string typically in \"snake_case\" format that provides a human-readable description of the record.  They are commonly used to ensure sandbox, qa, staging and production tenants have the identical configuration items loaded.  Every record has a UID assigned when persisted. When not specified the system assigns one by default.  A default value looks like a 32 character string of random hexadecimal characters. (optional)

    try:
        # Update page content record
        new_create_page_content_request = CreatePageContentRequest.from_json(create_page_content_request)
        results = PageContentsApi(api_client).update_page_content_by_uid(create_page_content_request=new_create_page_content_request)
        # Below is a request that includes all optional parameters
        # results = PageContentsApi(api_client).update_page_content_by_uid(new_create_page_content_request, uid)
        print("The response of PageContentsApi->update_page_content_by_uid:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling PageContentsApi->update_page_content_by_uid: %s\n" % e)
```



[[Back to top]](#) 



