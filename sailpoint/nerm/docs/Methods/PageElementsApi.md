---
id: page-elements
title: Page_elements
pagination_label: page_elements
sidebar_label: page_elements
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'page_elements', 'page_elements'] 
slug: /tools/sdk/python//methods/page-elements
tags: ['SDK', 'Software Development Kit', 'page_elements', 'page_elements']
---

# sailpoint.nerm.PageElementsApi
   
All URIs are relative to *https://acmeco.nonemployee.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create-page-element**](#create-page-element) | **POST** `/page_elements` | Create a page element entry
[**delete-page-element-by-id**](#delete-page-element-by-id) | **DELETE** `/page_elements/{id}` | Delete page element
[**delete-page-element-by-uid**](#delete-page-element-by-uid) | **DELETE** `/page_elements/{uid}` | Delete page element
[**get-page-element-by-id**](#get-page-element-by-id) | **GET** `/page_elements/{id}` | Find a page element
[**get-page-element-by-uid**](#get-page-element-by-uid) | **GET** `/page_elements/{uid}` | Find page element
[**get-page-elements**](#get-page-elements) | **GET** `/page_elements` | Get page element data
[**update-page-element-by-id**](#update-page-element-by-id) | **PATCH** `/page_elements/{id}` | Update page element
[**update-page-element-by-uid**](#update-page-element-by-uid) | **PATCH** `/page_elements/{uid}` | Update page element


## create-page-element
Create a page element entry
Creates a page element.

[API Spec](https://developer.sailpoint.com/docs/api//create-page-element)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
 Body  | create_page_element_request | [**CreatePageElementRequest**](../models/create-page-element-request) | True  | 

### Return type
[**GetPageElements200Response**](../models/get-page-elements200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
201 | Expected response to a valid request | GetPageElements200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.page_elements_api import PageElementsApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.create_page_element_request import CreatePageElementRequest
from sailpoint.nerm.models.get_page_elements200_response import GetPageElements200Response
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    create_page_element_request = '''sailpoint.nerm.CreatePageElementRequest()''' # CreatePageElementRequest | 

    try:
        # Create a page element entry
        new_create_page_element_request = CreatePageElementRequest.from_json(create_page_element_request)
        results = PageElementsApi(api_client).create_page_element(create_page_element_request=new_create_page_element_request)
        # Below is a request that includes all optional parameters
        # results = PageElementsApi(api_client).create_page_element(new_create_page_element_request)
        print("The response of PageElementsApi->create_page_element:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling PageElementsApi->create_page_element: %s\n" % e)
```



[[Back to top]](#) 

## delete-page-element-by-id
Delete page element
Delete page element by id

[API Spec](https://developer.sailpoint.com/docs/api//delete-page-element-by-id)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | id | **str** | True  | ID of the object to retrieve, update, or delete

### Return type
[**GetPageElements200Response**](../models/get-page-elements200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | GetPageElements200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.page_elements_api import PageElementsApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.get_page_elements200_response import GetPageElements200Response
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    id = '1246d8b3-ac29-4015-8154-dea4434a73fa' # str | ID of the object to retrieve, update, or delete # str | ID of the object to retrieve, update, or delete

    try:
        # Delete page element
        
        results = PageElementsApi(api_client).delete_page_element_by_id(id=id)
        # Below is a request that includes all optional parameters
        # results = PageElementsApi(api_client).delete_page_element_by_id(id)
        print("The response of PageElementsApi->delete_page_element_by_id:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling PageElementsApi->delete_page_element_by_id: %s\n" % e)
```



[[Back to top]](#) 

## delete-page-element-by-uid
Delete page element
Delete page element by UID (user-specified identifier)

[API Spec](https://developer.sailpoint.com/docs/api//delete-page-element-by-uid)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | uid | **str** |   (optional) | UID of the object to retrieve, update, or delete.  A UID or \"specified identifier\" is a string typically in \"snake_case\" format that provides a human-readable description of the record.  They are commonly used to ensure sandbox, qa, staging and production tenants have the identical configuration items loaded.  Every record has a UID assigned when persisted. When not specified the system assigns one by default.  A default value looks like a 32 character string of random hexadecimal characters.

### Return type
[**GetPageElements200Response**](../models/get-page-elements200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | GetPageElements200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.page_elements_api import PageElementsApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.get_page_elements200_response import GetPageElements200Response
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    uid = 'middle_initial_attribute' # str | UID of the object to retrieve, update, or delete.  A UID or \"specified identifier\" is a string typically in \"snake_case\" format that provides a human-readable description of the record.  They are commonly used to ensure sandbox, qa, staging and production tenants have the identical configuration items loaded.  Every record has a UID assigned when persisted. When not specified the system assigns one by default.  A default value looks like a 32 character string of random hexadecimal characters. (optional) # str | UID of the object to retrieve, update, or delete.  A UID or \"specified identifier\" is a string typically in \"snake_case\" format that provides a human-readable description of the record.  They are commonly used to ensure sandbox, qa, staging and production tenants have the identical configuration items loaded.  Every record has a UID assigned when persisted. When not specified the system assigns one by default.  A default value looks like a 32 character string of random hexadecimal characters. (optional)

    try:
        # Delete page element
        
        results = PageElementsApi(api_client).delete_page_element_by_uid()
        # Below is a request that includes all optional parameters
        # results = PageElementsApi(api_client).delete_page_element_by_uid(uid)
        print("The response of PageElementsApi->delete_page_element_by_uid:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling PageElementsApi->delete_page_element_by_uid: %s\n" % e)
```



[[Back to top]](#) 

## get-page-element-by-id
Find a page element
Info for a specific page element record

[API Spec](https://developer.sailpoint.com/docs/api//get-page-element-by-id)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | id | **str** | True  | ID of the object to retrieve, update, or delete

### Return type
[**GetPageElements200Response**](../models/get-page-elements200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | GetPageElements200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.page_elements_api import PageElementsApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.get_page_elements200_response import GetPageElements200Response
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    id = '1246d8b3-ac29-4015-8154-dea4434a73fa' # str | ID of the object to retrieve, update, or delete # str | ID of the object to retrieve, update, or delete

    try:
        # Find a page element
        
        results = PageElementsApi(api_client).get_page_element_by_id(id=id)
        # Below is a request that includes all optional parameters
        # results = PageElementsApi(api_client).get_page_element_by_id(id)
        print("The response of PageElementsApi->get_page_element_by_id:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling PageElementsApi->get_page_element_by_id: %s\n" % e)
```



[[Back to top]](#) 

## get-page-element-by-uid
Find page element
Info for a specific page element record by UID (user-specified identifier)

[API Spec](https://developer.sailpoint.com/docs/api//get-page-element-by-uid)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | uid | **str** |   (optional) | UID of the object to retrieve, update, or delete.  A UID or \"specified identifier\" is a string typically in \"snake_case\" format that provides a human-readable description of the record.  They are commonly used to ensure sandbox, qa, staging and production tenants have the identical configuration items loaded.  Every record has a UID assigned when persisted. When not specified the system assigns one by default.  A default value looks like a 32 character string of random hexadecimal characters.

### Return type
[**GetPageElements200Response**](../models/get-page-elements200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | GetPageElements200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.page_elements_api import PageElementsApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.get_page_elements200_response import GetPageElements200Response
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    uid = 'middle_initial_attribute' # str | UID of the object to retrieve, update, or delete.  A UID or \"specified identifier\" is a string typically in \"snake_case\" format that provides a human-readable description of the record.  They are commonly used to ensure sandbox, qa, staging and production tenants have the identical configuration items loaded.  Every record has a UID assigned when persisted. When not specified the system assigns one by default.  A default value looks like a 32 character string of random hexadecimal characters. (optional) # str | UID of the object to retrieve, update, or delete.  A UID or \"specified identifier\" is a string typically in \"snake_case\" format that provides a human-readable description of the record.  They are commonly used to ensure sandbox, qa, staging and production tenants have the identical configuration items loaded.  Every record has a UID assigned when persisted. When not specified the system assigns one by default.  A default value looks like a 32 character string of random hexadecimal characters. (optional)

    try:
        # Find page element
        
        results = PageElementsApi(api_client).get_page_element_by_uid()
        # Below is a request that includes all optional parameters
        # results = PageElementsApi(api_client).get_page_element_by_uid(uid)
        print("The response of PageElementsApi->get_page_element_by_uid:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling PageElementsApi->get_page_element_by_uid: %s\n" % e)
```



[[Back to top]](#) 

## get-page-elements
Get page element data
Retrieves page elements data.

[API Spec](https://developer.sailpoint.com/docs/api//get-page-elements)

### Parameters 
This endpoint does not need any parameter. 

### Return type
[**GetPageElements200Response**](../models/get-page-elements200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | GetPageElements200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.page_elements_api import PageElementsApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.get_page_elements200_response import GetPageElements200Response
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:

    try:
        # Get page element data
        
        results = PageElementsApi(api_client).get_page_elements()
        # Below is a request that includes all optional parameters
        # results = PageElementsApi(api_client).get_page_elements()
        print("The response of PageElementsApi->get_page_elements:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling PageElementsApi->get_page_elements: %s\n" % e)
```



[[Back to top]](#) 

## update-page-element-by-id
Update page element
Update info for a specific page element record by id

[API Spec](https://developer.sailpoint.com/docs/api//update-page-element-by-id)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | id | **str** | True  | ID of the object to retrieve, update, or delete
 Body  | create_page_element_request | [**CreatePageElementRequest**](../models/create-page-element-request) | True  | 

### Return type
[**GetPageElements200Response**](../models/get-page-elements200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | GetPageElements200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
404 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.page_elements_api import PageElementsApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.create_page_element_request import CreatePageElementRequest
from sailpoint.nerm.models.get_page_elements200_response import GetPageElements200Response
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    id = '1246d8b3-ac29-4015-8154-dea4434a73fa' # str | ID of the object to retrieve, update, or delete # str | ID of the object to retrieve, update, or delete
    create_page_element_request = '''sailpoint.nerm.CreatePageElementRequest()''' # CreatePageElementRequest | 

    try:
        # Update page element
        new_create_page_element_request = CreatePageElementRequest.from_json(create_page_element_request)
        results = PageElementsApi(api_client).update_page_element_by_id(id=id, create_page_element_request=new_create_page_element_request)
        # Below is a request that includes all optional parameters
        # results = PageElementsApi(api_client).update_page_element_by_id(id, new_create_page_element_request)
        print("The response of PageElementsApi->update_page_element_by_id:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling PageElementsApi->update_page_element_by_id: %s\n" % e)
```



[[Back to top]](#) 

## update-page-element-by-uid
Update page element
Update info for a specific page element record by UID (user-specified identifier)

[API Spec](https://developer.sailpoint.com/docs/api//update-page-element-by-uid)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
 Body  | create_page_element_request | [**CreatePageElementRequest**](../models/create-page-element-request) | True  | 
Path   | uid | **str** |   (optional) | UID of the object to retrieve, update, or delete.  A UID or \"specified identifier\" is a string typically in \"snake_case\" format that provides a human-readable description of the record.  They are commonly used to ensure sandbox, qa, staging and production tenants have the identical configuration items loaded.  Every record has a UID assigned when persisted. When not specified the system assigns one by default.  A default value looks like a 32 character string of random hexadecimal characters.

### Return type
[**GetPageElements200Response**](../models/get-page-elements200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | GetPageElements200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
404 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.page_elements_api import PageElementsApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.create_page_element_request import CreatePageElementRequest
from sailpoint.nerm.models.get_page_elements200_response import GetPageElements200Response
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    create_page_element_request = '''sailpoint.nerm.CreatePageElementRequest()''' # CreatePageElementRequest | 
    uid = 'middle_initial_attribute' # str | UID of the object to retrieve, update, or delete.  A UID or \"specified identifier\" is a string typically in \"snake_case\" format that provides a human-readable description of the record.  They are commonly used to ensure sandbox, qa, staging and production tenants have the identical configuration items loaded.  Every record has a UID assigned when persisted. When not specified the system assigns one by default.  A default value looks like a 32 character string of random hexadecimal characters. (optional) # str | UID of the object to retrieve, update, or delete.  A UID or \"specified identifier\" is a string typically in \"snake_case\" format that provides a human-readable description of the record.  They are commonly used to ensure sandbox, qa, staging and production tenants have the identical configuration items loaded.  Every record has a UID assigned when persisted. When not specified the system assigns one by default.  A default value looks like a 32 character string of random hexadecimal characters. (optional)

    try:
        # Update page element
        new_create_page_element_request = CreatePageElementRequest.from_json(create_page_element_request)
        results = PageElementsApi(api_client).update_page_element_by_uid(create_page_element_request=new_create_page_element_request)
        # Below is a request that includes all optional parameters
        # results = PageElementsApi(api_client).update_page_element_by_uid(new_create_page_element_request, uid)
        print("The response of PageElementsApi->update_page_element_by_uid:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling PageElementsApi->update_page_element_by_uid: %s\n" % e)
```



[[Back to top]](#) 



