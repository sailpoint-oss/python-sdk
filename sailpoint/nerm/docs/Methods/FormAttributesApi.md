---
id: form-attributes
title: Form_attributes
pagination_label: form_attributes
sidebar_label: form_attributes
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'form_attributes', 'form_attributes'] 
slug: /tools/sdk/python//methods/form-attributes
tags: ['SDK', 'Software Development Kit', 'form_attributes', 'form_attributes']
---

# sailpoint.nerm.FormAttributesApi
   
All URIs are relative to *https://acmeco.nonemployee.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create-form-attribute**](#create-form-attribute) | **POST** `/form_attributes` | Create a form attribute
[**delete-form-attribute-by-id**](#delete-form-attribute-by-id) | **DELETE** `/form_attributes/{id}` | Delete form attribute
[**delete-form-attribute-by-uid**](#delete-form-attribute-by-uid) | **DELETE** `/form_attributes/{uid}` | Delete form attribute
[**get-form-attribute-by-id**](#get-form-attribute-by-id) | **GET** `/form_attributes/{id}` | Get form attribute data
[**get-form-attribute-by-uid**](#get-form-attribute-by-uid) | **GET** `/form_attributes/{uid}` | Get form attribute data
[**get-form-attributes**](#get-form-attributes) | **GET** `/form_attributes` | Get form attributes
[**update-form-attribute-by-id**](#update-form-attribute-by-id) | **PATCH** `/form_attributes/{id}` | Update form attribute data
[**update-form-attribute-by-uid**](#update-form-attribute-by-uid) | **PATCH** `/form_attributes/{uid}` | Update form attribute data


## create-form-attribute
Create a form attribute
This endpoint can create a form attribute

[API Spec](https://developer.sailpoint.com/docs/api//create-form-attribute)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
 Body  | create_form_attribute_request | [**CreateFormAttributeRequest**](../models/create-form-attribute-request) | True  | 

### Return type
[**GetFormAttributes200Response**](../models/get-form-attributes200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | GetFormAttributes200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.form_attributes_api import FormAttributesApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.create_form_attribute_request import CreateFormAttributeRequest
from sailpoint.nerm.models.get_form_attributes200_response import GetFormAttributes200Response
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    create_form_attribute_request = '''sailpoint.nerm.CreateFormAttributeRequest()''' # CreateFormAttributeRequest | 

    try:
        # Create a form attribute
        new_create_form_attribute_request = CreateFormAttributeRequest.from_json(create_form_attribute_request)
        results = FormAttributesApi(api_client).create_form_attribute(create_form_attribute_request=new_create_form_attribute_request)
        # Below is a request that includes all optional parameters
        # results = FormAttributesApi(api_client).create_form_attribute(new_create_form_attribute_request)
        print("The response of FormAttributesApi->create_form_attribute:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling FormAttributesApi->create_form_attribute: %s\n" % e)
```



[[Back to top]](#) 

## delete-form-attribute-by-id
Delete form attribute
Delete form attribute by id

[API Spec](https://developer.sailpoint.com/docs/api//delete-form-attribute-by-id)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | id | **str** | True  | ID of the object to retrieve, update, or delete

### Return type
[**GetFormAttributes200Response**](../models/get-form-attributes200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | GetFormAttributes200Response |  -  |
404 | Record Not Found | DelegationsPost404Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.form_attributes_api import FormAttributesApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.get_form_attributes200_response import GetFormAttributes200Response
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    id = '1246d8b3-ac29-4015-8154-dea4434a73fa' # str | ID of the object to retrieve, update, or delete # str | ID of the object to retrieve, update, or delete

    try:
        # Delete form attribute
        
        results = FormAttributesApi(api_client).delete_form_attribute_by_id(id=id)
        # Below is a request that includes all optional parameters
        # results = FormAttributesApi(api_client).delete_form_attribute_by_id(id)
        print("The response of FormAttributesApi->delete_form_attribute_by_id:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling FormAttributesApi->delete_form_attribute_by_id: %s\n" % e)
```



[[Back to top]](#) 

## delete-form-attribute-by-uid
Delete form attribute
Delete form attribute by UID

[API Spec](https://developer.sailpoint.com/docs/api//delete-form-attribute-by-uid)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | uid | **str** |   (optional) | UID of the object to retrieve, update, or delete.  A UID or \"specified identifier\" is a string typically in \"snake_case\" format that provides a human-readable description of the record.  They are commonly used to ensure sandbox, qa, staging and production tenants have the identical configuration items loaded.  Every record has a UID assigned when persisted. When not specified the system assigns one by default.  A default value looks like a 32 character string of random hexadecimal characters.

### Return type
[**GetFormAttributes200Response**](../models/get-form-attributes200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | GetFormAttributes200Response |  -  |
404 | Record Not Found | DelegationsPost404Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.form_attributes_api import FormAttributesApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.get_form_attributes200_response import GetFormAttributes200Response
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    uid = 'middle_initial_attribute' # str | UID of the object to retrieve, update, or delete.  A UID or \"specified identifier\" is a string typically in \"snake_case\" format that provides a human-readable description of the record.  They are commonly used to ensure sandbox, qa, staging and production tenants have the identical configuration items loaded.  Every record has a UID assigned when persisted. When not specified the system assigns one by default.  A default value looks like a 32 character string of random hexadecimal characters. (optional) # str | UID of the object to retrieve, update, or delete.  A UID or \"specified identifier\" is a string typically in \"snake_case\" format that provides a human-readable description of the record.  They are commonly used to ensure sandbox, qa, staging and production tenants have the identical configuration items loaded.  Every record has a UID assigned when persisted. When not specified the system assigns one by default.  A default value looks like a 32 character string of random hexadecimal characters. (optional)

    try:
        # Delete form attribute
        
        results = FormAttributesApi(api_client).delete_form_attribute_by_uid()
        # Below is a request that includes all optional parameters
        # results = FormAttributesApi(api_client).delete_form_attribute_by_uid(uid)
        print("The response of FormAttributesApi->delete_form_attribute_by_uid:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling FormAttributesApi->delete_form_attribute_by_uid: %s\n" % e)
```



[[Back to top]](#) 

## get-form-attribute-by-id
Get form attribute data
Gets info for a specific form attribute by ID

[API Spec](https://developer.sailpoint.com/docs/api//get-form-attribute-by-id)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | id | **str** | True  | ID of the object to retrieve, update, or delete

### Return type
[**GetFormAttributes200Response**](../models/get-form-attributes200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | GetFormAttributes200Response |  -  |
404 | Record Not Found | DelegationsPost404Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.form_attributes_api import FormAttributesApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.get_form_attributes200_response import GetFormAttributes200Response
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    id = '1246d8b3-ac29-4015-8154-dea4434a73fa' # str | ID of the object to retrieve, update, or delete # str | ID of the object to retrieve, update, or delete

    try:
        # Get form attribute data
        
        results = FormAttributesApi(api_client).get_form_attribute_by_id(id=id)
        # Below is a request that includes all optional parameters
        # results = FormAttributesApi(api_client).get_form_attribute_by_id(id)
        print("The response of FormAttributesApi->get_form_attribute_by_id:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling FormAttributesApi->get_form_attribute_by_id: %s\n" % e)
```



[[Back to top]](#) 

## get-form-attribute-by-uid
Get form attribute data
Get info for a specific form attribute by UID

[API Spec](https://developer.sailpoint.com/docs/api//get-form-attribute-by-uid)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | uid | **str** |   (optional) | UID of the object to retrieve, update, or delete.  A UID or \"specified identifier\" is a string typically in \"snake_case\" format that provides a human-readable description of the record.  They are commonly used to ensure sandbox, qa, staging and production tenants have the identical configuration items loaded.  Every record has a UID assigned when persisted. When not specified the system assigns one by default.  A default value looks like a 32 character string of random hexadecimal characters.

### Return type
[**GetFormAttributes200Response**](../models/get-form-attributes200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | GetFormAttributes200Response |  -  |
404 | Record Not Found | DelegationsPost404Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.form_attributes_api import FormAttributesApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.get_form_attributes200_response import GetFormAttributes200Response
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    uid = 'middle_initial_attribute' # str | UID of the object to retrieve, update, or delete.  A UID or \"specified identifier\" is a string typically in \"snake_case\" format that provides a human-readable description of the record.  They are commonly used to ensure sandbox, qa, staging and production tenants have the identical configuration items loaded.  Every record has a UID assigned when persisted. When not specified the system assigns one by default.  A default value looks like a 32 character string of random hexadecimal characters. (optional) # str | UID of the object to retrieve, update, or delete.  A UID or \"specified identifier\" is a string typically in \"snake_case\" format that provides a human-readable description of the record.  They are commonly used to ensure sandbox, qa, staging and production tenants have the identical configuration items loaded.  Every record has a UID assigned when persisted. When not specified the system assigns one by default.  A default value looks like a 32 character string of random hexadecimal characters. (optional)

    try:
        # Get form attribute data
        
        results = FormAttributesApi(api_client).get_form_attribute_by_uid()
        # Below is a request that includes all optional parameters
        # results = FormAttributesApi(api_client).get_form_attribute_by_uid(uid)
        print("The response of FormAttributesApi->get_form_attribute_by_uid:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling FormAttributesApi->get_form_attribute_by_uid: %s\n" % e)
```



[[Back to top]](#) 

## get-form-attributes
Get form attributes
Get defined form attribute in the system

[API Spec](https://developer.sailpoint.com/docs/api//get-form-attributes)

### Parameters 
This endpoint does not need any parameter. 

### Return type
[**GetFormAttributes200Response**](../models/get-form-attributes200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | GetFormAttributes200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
404 | Record Not Found | DelegationsPost404Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.form_attributes_api import FormAttributesApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.get_form_attributes200_response import GetFormAttributes200Response
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:

    try:
        # Get form attributes
        
        results = FormAttributesApi(api_client).get_form_attributes()
        # Below is a request that includes all optional parameters
        # results = FormAttributesApi(api_client).get_form_attributes()
        print("The response of FormAttributesApi->get_form_attributes:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling FormAttributesApi->get_form_attributes: %s\n" % e)
```



[[Back to top]](#) 

## update-form-attribute-by-id
Update form attribute data
Update info for a specific form attribute by ID

[API Spec](https://developer.sailpoint.com/docs/api//update-form-attribute-by-id)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | id | **str** | True  | ID of the object to retrieve, update, or delete
 Body  | create_form_attribute_request | [**CreateFormAttributeRequest**](../models/create-form-attribute-request) | True  | 

### Return type
[**GetFormAttributes200Response**](../models/get-form-attributes200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | GetFormAttributes200Response |  -  |
404 | Record Not Found | DelegationsPost404Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.form_attributes_api import FormAttributesApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.create_form_attribute_request import CreateFormAttributeRequest
from sailpoint.nerm.models.get_form_attributes200_response import GetFormAttributes200Response
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    id = '1246d8b3-ac29-4015-8154-dea4434a73fa' # str | ID of the object to retrieve, update, or delete # str | ID of the object to retrieve, update, or delete
    create_form_attribute_request = '''sailpoint.nerm.CreateFormAttributeRequest()''' # CreateFormAttributeRequest | 

    try:
        # Update form attribute data
        new_create_form_attribute_request = CreateFormAttributeRequest.from_json(create_form_attribute_request)
        results = FormAttributesApi(api_client).update_form_attribute_by_id(id=id, create_form_attribute_request=new_create_form_attribute_request)
        # Below is a request that includes all optional parameters
        # results = FormAttributesApi(api_client).update_form_attribute_by_id(id, new_create_form_attribute_request)
        print("The response of FormAttributesApi->update_form_attribute_by_id:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling FormAttributesApi->update_form_attribute_by_id: %s\n" % e)
```



[[Back to top]](#) 

## update-form-attribute-by-uid
Update form attribute data
Update info for a specific form attribute by UID

[API Spec](https://developer.sailpoint.com/docs/api//update-form-attribute-by-uid)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
 Body  | create_form_attribute_request | [**CreateFormAttributeRequest**](../models/create-form-attribute-request) | True  | 
Path   | uid | **str** |   (optional) | UID of the object to retrieve, update, or delete.  A UID or \"specified identifier\" is a string typically in \"snake_case\" format that provides a human-readable description of the record.  They are commonly used to ensure sandbox, qa, staging and production tenants have the identical configuration items loaded.  Every record has a UID assigned when persisted. When not specified the system assigns one by default.  A default value looks like a 32 character string of random hexadecimal characters.

### Return type
[**GetFormAttributes200Response**](../models/get-form-attributes200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | GetFormAttributes200Response |  -  |
404 | Record Not Found | DelegationsPost404Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.form_attributes_api import FormAttributesApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.create_form_attribute_request import CreateFormAttributeRequest
from sailpoint.nerm.models.get_form_attributes200_response import GetFormAttributes200Response
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    create_form_attribute_request = '''sailpoint.nerm.CreateFormAttributeRequest()''' # CreateFormAttributeRequest | 
    uid = 'middle_initial_attribute' # str | UID of the object to retrieve, update, or delete.  A UID or \"specified identifier\" is a string typically in \"snake_case\" format that provides a human-readable description of the record.  They are commonly used to ensure sandbox, qa, staging and production tenants have the identical configuration items loaded.  Every record has a UID assigned when persisted. When not specified the system assigns one by default.  A default value looks like a 32 character string of random hexadecimal characters. (optional) # str | UID of the object to retrieve, update, or delete.  A UID or \"specified identifier\" is a string typically in \"snake_case\" format that provides a human-readable description of the record.  They are commonly used to ensure sandbox, qa, staging and production tenants have the identical configuration items loaded.  Every record has a UID assigned when persisted. When not specified the system assigns one by default.  A default value looks like a 32 character string of random hexadecimal characters. (optional)

    try:
        # Update form attribute data
        new_create_form_attribute_request = CreateFormAttributeRequest.from_json(create_form_attribute_request)
        results = FormAttributesApi(api_client).update_form_attribute_by_uid(create_form_attribute_request=new_create_form_attribute_request)
        # Below is a request that includes all optional parameters
        # results = FormAttributesApi(api_client).update_form_attribute_by_uid(new_create_form_attribute_request, uid)
        print("The response of FormAttributesApi->update_form_attribute_by_uid:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling FormAttributesApi->update_form_attribute_by_uid: %s\n" % e)
```



[[Back to top]](#) 



