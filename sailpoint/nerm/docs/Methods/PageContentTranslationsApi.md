---
id: page-content-translations
title: Page_content_translations
pagination_label: page_content_translations
sidebar_label: page_content_translations
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'page_content_translations', 'page_content_translations'] 
slug: /tools/sdk/python//methods/page-content-translations
tags: ['SDK', 'Software Development Kit', 'page_content_translations', 'page_content_translations']
---

# sailpoint.nerm.PageContentTranslationsApi
   
All URIs are relative to *https://acmeco.nonemployee.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create-page-content-translation**](#create-page-content-translation) | **POST** `/page_content_translations` | Create page content translation
[**delete-page-content-translation-by-id**](#delete-page-content-translation-by-id) | **DELETE** `/page_content_translations/{id}` | Delete page content translation
[**delete-page-content-translation-by-uid**](#delete-page-content-translation-by-uid) | **DELETE** `/page_content_translations/{uid}` | Delete page content translation
[**get-page-content-translation**](#get-page-content-translation) | **GET** `/page_content_translations` | Get page contents translation
[**get-page-content-translation-by-id**](#get-page-content-translation-by-id) | **GET** `/page_content_translations/{id}` | Find page content translation
[**get-page-content-translation-by-uid**](#get-page-content-translation-by-uid) | **GET** `/page_content_translations/{uid}` | Find page content translation
[**update-page-content-translation-by-id**](#update-page-content-translation-by-id) | **PATCH** `/page_content_translations/{id}` | Update page content translation
[**update-page-content-translation-by-uid**](#update-page-content-translation-by-uid) | **PATCH** `/page_content_translations/{uid}` | Update page content translation


## create-page-content-translation
Create page content translation
Create a page content translation record.

[API Spec](https://developer.sailpoint.com/docs/api//create-page-content-translation)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
 Body  | create_page_content_translation_request | [**CreatePageContentTranslationRequest**](../models/create-page-content-translation-request) | True  | 

### Return type
[**GetPageContentTranslation200Response**](../models/get-page-content-translation200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
201 | Expected response to a valid request | GetPageContentTranslation200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.page_content_translations_api import PageContentTranslationsApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.create_page_content_translation_request import CreatePageContentTranslationRequest
from sailpoint.nerm.models.get_page_content_translation200_response import GetPageContentTranslation200Response
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    create_page_content_translation_request = '''sailpoint.nerm.CreatePageContentTranslationRequest()''' # CreatePageContentTranslationRequest | 

    try:
        # Create page content translation
        new_create_page_content_translation_request = CreatePageContentTranslationRequest.from_json(create_page_content_translation_request)
        results = PageContentTranslationsApi(api_client).create_page_content_translation(create_page_content_translation_request=new_create_page_content_translation_request)
        # Below is a request that includes all optional parameters
        # results = PageContentTranslationsApi(api_client).create_page_content_translation(new_create_page_content_translation_request)
        print("The response of PageContentTranslationsApi->create_page_content_translation:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling PageContentTranslationsApi->create_page_content_translation: %s\n" % e)
```



[[Back to top]](#) 

## delete-page-content-translation-by-id
Delete page content translation
Delete page content translation by id

[API Spec](https://developer.sailpoint.com/docs/api//delete-page-content-translation-by-id)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | id | **str** | True  | ID of the object to retrieve, update, or delete

### Return type
[**GetPageContentTranslation200Response**](../models/get-page-content-translation200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | GetPageContentTranslation200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.page_content_translations_api import PageContentTranslationsApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.get_page_content_translation200_response import GetPageContentTranslation200Response
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    id = '1246d8b3-ac29-4015-8154-dea4434a73fa' # str | ID of the object to retrieve, update, or delete # str | ID of the object to retrieve, update, or delete

    try:
        # Delete page content translation
        
        results = PageContentTranslationsApi(api_client).delete_page_content_translation_by_id(id=id)
        # Below is a request that includes all optional parameters
        # results = PageContentTranslationsApi(api_client).delete_page_content_translation_by_id(id)
        print("The response of PageContentTranslationsApi->delete_page_content_translation_by_id:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling PageContentTranslationsApi->delete_page_content_translation_by_id: %s\n" % e)
```



[[Back to top]](#) 

## delete-page-content-translation-by-uid
Delete page content translation
Delete page content translation by UID (user-specified identifier)

[API Spec](https://developer.sailpoint.com/docs/api//delete-page-content-translation-by-uid)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | id | **str** | True  | ID of the object to retrieve, update, or delete

### Return type
[**GetPageContentTranslation200Response**](../models/get-page-content-translation200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | GetPageContentTranslation200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.page_content_translations_api import PageContentTranslationsApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.get_page_content_translation200_response import GetPageContentTranslation200Response
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    id = '1246d8b3-ac29-4015-8154-dea4434a73fa' # str | ID of the object to retrieve, update, or delete # str | ID of the object to retrieve, update, or delete

    try:
        # Delete page content translation
        
        results = PageContentTranslationsApi(api_client).delete_page_content_translation_by_uid(id=id)
        # Below is a request that includes all optional parameters
        # results = PageContentTranslationsApi(api_client).delete_page_content_translation_by_uid(id)
        print("The response of PageContentTranslationsApi->delete_page_content_translation_by_uid:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling PageContentTranslationsApi->delete_page_content_translation_by_uid: %s\n" % e)
```



[[Back to top]](#) 

## get-page-content-translation
Get page contents translation
This endpoint can retrieve page content translation data.

[API Spec](https://developer.sailpoint.com/docs/api//get-page-content-translation)

### Parameters 
This endpoint does not need any parameter. 

### Return type
[**GetPageContentTranslation200Response**](../models/get-page-content-translation200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | GetPageContentTranslation200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.page_content_translations_api import PageContentTranslationsApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.get_page_content_translation200_response import GetPageContentTranslation200Response
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:

    try:
        # Get page contents translation
        
        results = PageContentTranslationsApi(api_client).get_page_content_translation()
        # Below is a request that includes all optional parameters
        # results = PageContentTranslationsApi(api_client).get_page_content_translation()
        print("The response of PageContentTranslationsApi->get_page_content_translation:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling PageContentTranslationsApi->get_page_content_translation: %s\n" % e)
```



[[Back to top]](#) 

## get-page-content-translation-by-id
Find page content translation
Info for a specific page content translation record by Id

[API Spec](https://developer.sailpoint.com/docs/api//get-page-content-translation-by-id)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | id | **str** | True  | ID of the object to retrieve, update, or delete

### Return type
[**GetPageContentTranslation200Response**](../models/get-page-content-translation200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | GetPageContentTranslation200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.page_content_translations_api import PageContentTranslationsApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.get_page_content_translation200_response import GetPageContentTranslation200Response
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    id = '1246d8b3-ac29-4015-8154-dea4434a73fa' # str | ID of the object to retrieve, update, or delete # str | ID of the object to retrieve, update, or delete

    try:
        # Find page content translation
        
        results = PageContentTranslationsApi(api_client).get_page_content_translation_by_id(id=id)
        # Below is a request that includes all optional parameters
        # results = PageContentTranslationsApi(api_client).get_page_content_translation_by_id(id)
        print("The response of PageContentTranslationsApi->get_page_content_translation_by_id:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling PageContentTranslationsApi->get_page_content_translation_by_id: %s\n" % e)
```



[[Back to top]](#) 

## get-page-content-translation-by-uid
Find page content translation
Info for a specific page content translation record by UID (user-specified identifier)

[API Spec](https://developer.sailpoint.com/docs/api//get-page-content-translation-by-uid)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | uid | **str** |   (optional) | UID of the object to retrieve, update, or delete.  A UID or \"specified identifier\" is a string typically in \"snake_case\" format that provides a human-readable description of the record.  They are commonly used to ensure sandbox, qa, staging and production tenants have the identical configuration items loaded.  Every record has a UID assigned when persisted. When not specified the system assigns one by default.  A default value looks like a 32 character string of random hexadecimal characters.

### Return type
[**GetPageContentTranslation200Response**](../models/get-page-content-translation200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | GetPageContentTranslation200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.page_content_translations_api import PageContentTranslationsApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.get_page_content_translation200_response import GetPageContentTranslation200Response
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    uid = 'middle_initial_attribute' # str | UID of the object to retrieve, update, or delete.  A UID or \"specified identifier\" is a string typically in \"snake_case\" format that provides a human-readable description of the record.  They are commonly used to ensure sandbox, qa, staging and production tenants have the identical configuration items loaded.  Every record has a UID assigned when persisted. When not specified the system assigns one by default.  A default value looks like a 32 character string of random hexadecimal characters. (optional) # str | UID of the object to retrieve, update, or delete.  A UID or \"specified identifier\" is a string typically in \"snake_case\" format that provides a human-readable description of the record.  They are commonly used to ensure sandbox, qa, staging and production tenants have the identical configuration items loaded.  Every record has a UID assigned when persisted. When not specified the system assigns one by default.  A default value looks like a 32 character string of random hexadecimal characters. (optional)

    try:
        # Find page content translation
        
        results = PageContentTranslationsApi(api_client).get_page_content_translation_by_uid()
        # Below is a request that includes all optional parameters
        # results = PageContentTranslationsApi(api_client).get_page_content_translation_by_uid(uid)
        print("The response of PageContentTranslationsApi->get_page_content_translation_by_uid:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling PageContentTranslationsApi->get_page_content_translation_by_uid: %s\n" % e)
```



[[Back to top]](#) 

## update-page-content-translation-by-id
Update page content translation
Update info for a specific page content translation record by id

[API Spec](https://developer.sailpoint.com/docs/api//update-page-content-translation-by-id)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | id | **str** | True  | ID of the object to retrieve, update, or delete
 Body  | update_page_content_translation_by_id_request | [**UpdatePageContentTranslationByIdRequest**](../models/update-page-content-translation-by-id-request) | True  | 

### Return type
[**GetPageContentTranslation200Response**](../models/get-page-content-translation200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | GetPageContentTranslation200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
404 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.page_content_translations_api import PageContentTranslationsApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.get_page_content_translation200_response import GetPageContentTranslation200Response
from sailpoint.nerm.models.update_page_content_translation_by_id_request import UpdatePageContentTranslationByIdRequest
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    id = '1246d8b3-ac29-4015-8154-dea4434a73fa' # str | ID of the object to retrieve, update, or delete # str | ID of the object to retrieve, update, or delete
    update_page_content_translation_by_id_request = '''sailpoint.nerm.UpdatePageContentTranslationByIdRequest()''' # UpdatePageContentTranslationByIdRequest | 

    try:
        # Update page content translation
        new_update_page_content_translation_by_id_request = UpdatePageContentTranslationByIdRequest.from_json(update_page_content_translation_by_id_request)
        results = PageContentTranslationsApi(api_client).update_page_content_translation_by_id(id=id, update_page_content_translation_by_id_request=new_update_page_content_translation_by_id_request)
        # Below is a request that includes all optional parameters
        # results = PageContentTranslationsApi(api_client).update_page_content_translation_by_id(id, new_update_page_content_translation_by_id_request)
        print("The response of PageContentTranslationsApi->update_page_content_translation_by_id:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling PageContentTranslationsApi->update_page_content_translation_by_id: %s\n" % e)
```



[[Back to top]](#) 

## update-page-content-translation-by-uid
Update page content translation
Update info for a specific page content translation record by UID (user-specified identifier)

[API Spec](https://developer.sailpoint.com/docs/api//update-page-content-translation-by-uid)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
 Body  | update_page_content_translation_by_id_request | [**UpdatePageContentTranslationByIdRequest**](../models/update-page-content-translation-by-id-request) | True  | 
Path   | uid | **str** |   (optional) | UID of the object to retrieve, update, or delete.  A UID or \"specified identifier\" is a string typically in \"snake_case\" format that provides a human-readable description of the record.  They are commonly used to ensure sandbox, qa, staging and production tenants have the identical configuration items loaded.  Every record has a UID assigned when persisted. When not specified the system assigns one by default.  A default value looks like a 32 character string of random hexadecimal characters.

### Return type
[**GetPageContentTranslation200Response**](../models/get-page-content-translation200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | GetPageContentTranslation200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
404 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.page_content_translations_api import PageContentTranslationsApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.get_page_content_translation200_response import GetPageContentTranslation200Response
from sailpoint.nerm.models.update_page_content_translation_by_id_request import UpdatePageContentTranslationByIdRequest
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    update_page_content_translation_by_id_request = '''sailpoint.nerm.UpdatePageContentTranslationByIdRequest()''' # UpdatePageContentTranslationByIdRequest | 
    uid = 'middle_initial_attribute' # str | UID of the object to retrieve, update, or delete.  A UID or \"specified identifier\" is a string typically in \"snake_case\" format that provides a human-readable description of the record.  They are commonly used to ensure sandbox, qa, staging and production tenants have the identical configuration items loaded.  Every record has a UID assigned when persisted. When not specified the system assigns one by default.  A default value looks like a 32 character string of random hexadecimal characters. (optional) # str | UID of the object to retrieve, update, or delete.  A UID or \"specified identifier\" is a string typically in \"snake_case\" format that provides a human-readable description of the record.  They are commonly used to ensure sandbox, qa, staging and production tenants have the identical configuration items loaded.  Every record has a UID assigned when persisted. When not specified the system assigns one by default.  A default value looks like a 32 character string of random hexadecimal characters. (optional)

    try:
        # Update page content translation
        new_update_page_content_translation_by_id_request = UpdatePageContentTranslationByIdRequest.from_json(update_page_content_translation_by_id_request)
        results = PageContentTranslationsApi(api_client).update_page_content_translation_by_uid(update_page_content_translation_by_id_request=new_update_page_content_translation_by_id_request)
        # Below is a request that includes all optional parameters
        # results = PageContentTranslationsApi(api_client).update_page_content_translation_by_uid(new_update_page_content_translation_by_id_request, uid)
        print("The response of PageContentTranslationsApi->update_page_content_translation_by_uid:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling PageContentTranslationsApi->update_page_content_translation_by_uid: %s\n" % e)
```



[[Back to top]](#) 



