---
id: attribute-options
title: Attribute_options
pagination_label: attribute_options
sidebar_label: attribute_options
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'attribute_options', 'attribute_options'] 
slug: /tools/sdk/python//methods/attribute-options
tags: ['SDK', 'Software Development Kit', 'attribute_options', 'attribute_options']
---

# sailpoint.nerm.AttributeOptionsApi
   
All URIs are relative to *https://acmeco.nonemployee.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete-attribute-option-by-id**](#delete-attribute-option-by-id) | **DELETE** `/ne_attribute_options/{id}` | Delete option based attribute value
[**delete-attribute-option-by-uid**](#delete-attribute-option-by-uid) | **DELETE** `/ne_attribute_options/{uid}` | Delete option value
[**get-attribute-option-by-id**](#get-attribute-option-by-id) | **GET** `/ne_attribute_options/{id}` | Find option based attribute value
[**get-attribute-option-by-uid**](#get-attribute-option-by-uid) | **GET** `/ne_attribute_options/{uid}` | Find option attribute value
[**get-attribute-options**](#get-attribute-options) | **GET** `/ne_attribute_options` | Get option based attribute values
[**patch-attribute-option-by-id**](#patch-attribute-option-by-id) | **PATCH** `/ne_attribute_options/{id}` | Update option based attribute value
[**patch-attribute-option-by-uid**](#patch-attribute-option-by-uid) | **PATCH** `/ne_attribute_options/{uid}` | Update option value
[**patch-attribute-options**](#patch-attribute-options) | **PATCH** `/ne_attribute_options` | Update multiple option values
[**submit-attribute-option**](#submit-attribute-option) | **POST** `/ne_attribute_option` | Add value to option
[**submit-attribute-options**](#submit-attribute-options) | **POST** `/ne_attribute_options` | Create multiple option values


## delete-attribute-option-by-id
Delete option based attribute value
Delete a option based attribute value by id

[API Spec](https://developer.sailpoint.com/docs/api//delete-attribute-option-by-id)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | id | **str** | True  | ID of the object to retrieve, update, or delete

### Return type
[**DeleteAttributeOptionById200Response**](../models/delete-attribute-option-by-id200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Confirmation of a deleted object | DeleteAttributeOptionById200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.attribute_options_api import AttributeOptionsApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.delete_attribute_option_by_id200_response import DeleteAttributeOptionById200Response
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    id = '1246d8b3-ac29-4015-8154-dea4434a73fa' # str | ID of the object to retrieve, update, or delete # str | ID of the object to retrieve, update, or delete

    try:
        # Delete option based attribute value
        
        results = AttributeOptionsApi(api_client).delete_attribute_option_by_id(id=id)
        # Below is a request that includes all optional parameters
        # results = AttributeOptionsApi(api_client).delete_attribute_option_by_id(id)
        print("The response of AttributeOptionsApi->delete_attribute_option_by_id:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling AttributeOptionsApi->delete_attribute_option_by_id: %s\n" % e)
```



[[Back to top]](#) 

## delete-attribute-option-by-uid
Delete option value
Delete a option based attribute value by UID (user-specified identifier)

[API Spec](https://developer.sailpoint.com/docs/api//delete-attribute-option-by-uid)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | uid | **str** |   (optional) | UID of the object to retrieve, update, or delete.  A UID or \"specified identifier\" is a string typically in \"snake_case\" format that provides a human-readable description of the record.  They are commonly used to ensure sandbox, qa, staging and production tenants have the identical configuration items loaded.  Every record has a UID assigned when persisted. When not specified the system assigns one by default.  A default value looks like a 32 character string of random hexadecimal characters.

### Return type
[**DeleteAttributeOptionById200Response**](../models/delete-attribute-option-by-id200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Confirmation of a deleted object | DeleteAttributeOptionById200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.attribute_options_api import AttributeOptionsApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.delete_attribute_option_by_id200_response import DeleteAttributeOptionById200Response
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    uid = 'middle_initial_attribute' # str | UID of the object to retrieve, update, or delete.  A UID or \"specified identifier\" is a string typically in \"snake_case\" format that provides a human-readable description of the record.  They are commonly used to ensure sandbox, qa, staging and production tenants have the identical configuration items loaded.  Every record has a UID assigned when persisted. When not specified the system assigns one by default.  A default value looks like a 32 character string of random hexadecimal characters. (optional) # str | UID of the object to retrieve, update, or delete.  A UID or \"specified identifier\" is a string typically in \"snake_case\" format that provides a human-readable description of the record.  They are commonly used to ensure sandbox, qa, staging and production tenants have the identical configuration items loaded.  Every record has a UID assigned when persisted. When not specified the system assigns one by default.  A default value looks like a 32 character string of random hexadecimal characters. (optional)

    try:
        # Delete option value
        
        results = AttributeOptionsApi(api_client).delete_attribute_option_by_uid()
        # Below is a request that includes all optional parameters
        # results = AttributeOptionsApi(api_client).delete_attribute_option_by_uid(uid)
        print("The response of AttributeOptionsApi->delete_attribute_option_by_uid:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling AttributeOptionsApi->delete_attribute_option_by_uid: %s\n" % e)
```



[[Back to top]](#) 

## get-attribute-option-by-id
Find option based attribute value
Info for a specific option based attribute value by id

[API Spec](https://developer.sailpoint.com/docs/api//get-attribute-option-by-id)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | id | **str** | True  | ID of the object to retrieve, update, or delete

### Return type
[**SubmitAttributeOption200Response**](../models/submit-attribute-option200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | SubmitAttributeOption200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.attribute_options_api import AttributeOptionsApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.submit_attribute_option200_response import SubmitAttributeOption200Response
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    id = '1246d8b3-ac29-4015-8154-dea4434a73fa' # str | ID of the object to retrieve, update, or delete # str | ID of the object to retrieve, update, or delete

    try:
        # Find option based attribute value
        
        results = AttributeOptionsApi(api_client).get_attribute_option_by_id(id=id)
        # Below is a request that includes all optional parameters
        # results = AttributeOptionsApi(api_client).get_attribute_option_by_id(id)
        print("The response of AttributeOptionsApi->get_attribute_option_by_id:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling AttributeOptionsApi->get_attribute_option_by_id: %s\n" % e)
```



[[Back to top]](#) 

## get-attribute-option-by-uid
Find option attribute value
Get a specific option based attribute value by UID (user-specified identifier)

[API Spec](https://developer.sailpoint.com/docs/api//get-attribute-option-by-uid)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | uid | **str** |   (optional) | UID of the object to retrieve, update, or delete.  A UID or \"specified identifier\" is a string typically in \"snake_case\" format that provides a human-readable description of the record.  They are commonly used to ensure sandbox, qa, staging and production tenants have the identical configuration items loaded.  Every record has a UID assigned when persisted. When not specified the system assigns one by default.  A default value looks like a 32 character string of random hexadecimal characters.

### Return type
[**SubmitAttributeOption200Response**](../models/submit-attribute-option200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | SubmitAttributeOption200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.attribute_options_api import AttributeOptionsApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.submit_attribute_option200_response import SubmitAttributeOption200Response
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    uid = 'middle_initial_attribute' # str | UID of the object to retrieve, update, or delete.  A UID or \"specified identifier\" is a string typically in \"snake_case\" format that provides a human-readable description of the record.  They are commonly used to ensure sandbox, qa, staging and production tenants have the identical configuration items loaded.  Every record has a UID assigned when persisted. When not specified the system assigns one by default.  A default value looks like a 32 character string of random hexadecimal characters. (optional) # str | UID of the object to retrieve, update, or delete.  A UID or \"specified identifier\" is a string typically in \"snake_case\" format that provides a human-readable description of the record.  They are commonly used to ensure sandbox, qa, staging and production tenants have the identical configuration items loaded.  Every record has a UID assigned when persisted. When not specified the system assigns one by default.  A default value looks like a 32 character string of random hexadecimal characters. (optional)

    try:
        # Find option attribute value
        
        results = AttributeOptionsApi(api_client).get_attribute_option_by_uid()
        # Below is a request that includes all optional parameters
        # results = AttributeOptionsApi(api_client).get_attribute_option_by_uid(uid)
        print("The response of AttributeOptionsApi->get_attribute_option_by_uid:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling AttributeOptionsApi->get_attribute_option_by_uid: %s\n" % e)
```



[[Back to top]](#) 

## get-attribute-options
Get option based attribute values
Get option based attribute values

[API Spec](https://developer.sailpoint.com/docs/api//get-attribute-options)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
  Query | limit | **int** |   (optional) | The maximum number of items to return.
  Query | offset | **int** |   (optional) | The number of items to skip before starting to collect the result set.
  Query | order | **str** |   (optional) | The field to order results by.
  Query | ne_attribute_id | **str** |   (optional) | ID of an attribute for filtering
  Query | metadata | **bool** |   (optional) (default to False) | Returns batching metadata in the response. This includes `total` as the total quantity, `next` as the path of the following query url, `limit` and `after_id` (if requested) with the next following id (null if it is the last \"page\").

### Return type
[**GetAttributeOptions200Response**](../models/get-attribute-options200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | GetAttributeOptions200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.attribute_options_api import AttributeOptionsApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.get_attribute_options200_response import GetAttributeOptions200Response
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    limit = 5 # int | The maximum number of items to return. (optional) # int | The maximum number of items to return. (optional)
    offset = 5 # int | The number of items to skip before starting to collect the result set. (optional) # int | The number of items to skip before starting to collect the result set. (optional)
    order = 'created_at' # str | The field to order results by. (optional) # str | The field to order results by. (optional)
    ne_attribute_id = '33f072dd-13b4-41e1-8ea0-16f2a59b57c8' # str | ID of an attribute for filtering (optional) # str | ID of an attribute for filtering (optional)
    metadata = False # bool | Returns batching metadata in the response. This includes `total` as the total quantity, `next` as the path of the following query url, `limit` and `after_id` (if requested) with the next following id (null if it is the last \"page\"). (optional) (default to False) # bool | Returns batching metadata in the response. This includes `total` as the total quantity, `next` as the path of the following query url, `limit` and `after_id` (if requested) with the next following id (null if it is the last \"page\"). (optional) (default to False)

    try:
        # Get option based attribute values
        
        results = AttributeOptionsApi(api_client).get_attribute_options()
        # Below is a request that includes all optional parameters
        # results = AttributeOptionsApi(api_client).get_attribute_options(limit, offset, order, ne_attribute_id, metadata)
        print("The response of AttributeOptionsApi->get_attribute_options:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling AttributeOptionsApi->get_attribute_options: %s\n" % e)
```



[[Back to top]](#) 

## patch-attribute-option-by-id
Update option based attribute value
Update a option based attribute value by id

[API Spec](https://developer.sailpoint.com/docs/api//patch-attribute-option-by-id)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | id | **str** | True  | ID of the object to retrieve, update, or delete
 Body  | submit_attribute_option_request | [**SubmitAttributeOptionRequest**](../models/submit-attribute-option-request) | True  | 

### Return type
[**SubmitAttributeOption200Response**](../models/submit-attribute-option200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | SubmitAttributeOption200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.attribute_options_api import AttributeOptionsApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.submit_attribute_option200_response import SubmitAttributeOption200Response
from sailpoint.nerm.models.submit_attribute_option_request import SubmitAttributeOptionRequest
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    id = '1246d8b3-ac29-4015-8154-dea4434a73fa' # str | ID of the object to retrieve, update, or delete # str | ID of the object to retrieve, update, or delete
    submit_attribute_option_request = '''sailpoint.nerm.SubmitAttributeOptionRequest()''' # SubmitAttributeOptionRequest | 

    try:
        # Update option based attribute value
        new_submit_attribute_option_request = SubmitAttributeOptionRequest.from_json(submit_attribute_option_request)
        results = AttributeOptionsApi(api_client).patch_attribute_option_by_id(id=id, submit_attribute_option_request=new_submit_attribute_option_request)
        # Below is a request that includes all optional parameters
        # results = AttributeOptionsApi(api_client).patch_attribute_option_by_id(id, new_submit_attribute_option_request)
        print("The response of AttributeOptionsApi->patch_attribute_option_by_id:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling AttributeOptionsApi->patch_attribute_option_by_id: %s\n" % e)
```



[[Back to top]](#) 

## patch-attribute-option-by-uid
Update option value
Update a option based attribute value by UID (user-specified identifier)

[API Spec](https://developer.sailpoint.com/docs/api//patch-attribute-option-by-uid)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
 Body  | submit_attribute_option_request | [**SubmitAttributeOptionRequest**](../models/submit-attribute-option-request) | True  | 
Path   | uid | **str** |   (optional) | UID of the object to retrieve, update, or delete.  A UID or \"specified identifier\" is a string typically in \"snake_case\" format that provides a human-readable description of the record.  They are commonly used to ensure sandbox, qa, staging and production tenants have the identical configuration items loaded.  Every record has a UID assigned when persisted. When not specified the system assigns one by default.  A default value looks like a 32 character string of random hexadecimal characters.

### Return type
[**SubmitAttributeOption200Response**](../models/submit-attribute-option200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | SubmitAttributeOption200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.attribute_options_api import AttributeOptionsApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.submit_attribute_option200_response import SubmitAttributeOption200Response
from sailpoint.nerm.models.submit_attribute_option_request import SubmitAttributeOptionRequest
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    submit_attribute_option_request = '''sailpoint.nerm.SubmitAttributeOptionRequest()''' # SubmitAttributeOptionRequest | 
    uid = 'middle_initial_attribute' # str | UID of the object to retrieve, update, or delete.  A UID or \"specified identifier\" is a string typically in \"snake_case\" format that provides a human-readable description of the record.  They are commonly used to ensure sandbox, qa, staging and production tenants have the identical configuration items loaded.  Every record has a UID assigned when persisted. When not specified the system assigns one by default.  A default value looks like a 32 character string of random hexadecimal characters. (optional) # str | UID of the object to retrieve, update, or delete.  A UID or \"specified identifier\" is a string typically in \"snake_case\" format that provides a human-readable description of the record.  They are commonly used to ensure sandbox, qa, staging and production tenants have the identical configuration items loaded.  Every record has a UID assigned when persisted. When not specified the system assigns one by default.  A default value looks like a 32 character string of random hexadecimal characters. (optional)

    try:
        # Update option value
        new_submit_attribute_option_request = SubmitAttributeOptionRequest.from_json(submit_attribute_option_request)
        results = AttributeOptionsApi(api_client).patch_attribute_option_by_uid(submit_attribute_option_request=new_submit_attribute_option_request)
        # Below is a request that includes all optional parameters
        # results = AttributeOptionsApi(api_client).patch_attribute_option_by_uid(new_submit_attribute_option_request, uid)
        print("The response of AttributeOptionsApi->patch_attribute_option_by_uid:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling AttributeOptionsApi->patch_attribute_option_by_uid: %s\n" % e)
```



[[Back to top]](#) 

## patch-attribute-options
Update multiple option values
Update multiple option based attribute values

[API Spec](https://developer.sailpoint.com/docs/api//patch-attribute-options)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
 Body  | submit_attribute_options_request | [**SubmitAttributeOptionsRequest**](../models/submit-attribute-options-request) | True  | 

### Return type
[**SubmitAttributeOptions200Response**](../models/submit-attribute-options200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | SubmitAttributeOptions200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.attribute_options_api import AttributeOptionsApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.submit_attribute_options200_response import SubmitAttributeOptions200Response
from sailpoint.nerm.models.submit_attribute_options_request import SubmitAttributeOptionsRequest
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    submit_attribute_options_request = '''sailpoint.nerm.SubmitAttributeOptionsRequest()''' # SubmitAttributeOptionsRequest | 

    try:
        # Update multiple option values
        new_submit_attribute_options_request = SubmitAttributeOptionsRequest.from_json(submit_attribute_options_request)
        results = AttributeOptionsApi(api_client).patch_attribute_options(submit_attribute_options_request=new_submit_attribute_options_request)
        # Below is a request that includes all optional parameters
        # results = AttributeOptionsApi(api_client).patch_attribute_options(new_submit_attribute_options_request)
        print("The response of AttributeOptionsApi->patch_attribute_options:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling AttributeOptionsApi->patch_attribute_options: %s\n" % e)
```



[[Back to top]](#) 

## submit-attribute-option
Add value to option
Adds a value to an option based attribute

[API Spec](https://developer.sailpoint.com/docs/api//submit-attribute-option)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
 Body  | submit_attribute_option_request | [**SubmitAttributeOptionRequest**](../models/submit-attribute-option-request) | True  | 

### Return type
[**SubmitAttributeOption200Response**](../models/submit-attribute-option200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | SubmitAttributeOption200Response |  -  |
405 | Invalid input |  |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.attribute_options_api import AttributeOptionsApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.submit_attribute_option200_response import SubmitAttributeOption200Response
from sailpoint.nerm.models.submit_attribute_option_request import SubmitAttributeOptionRequest
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    submit_attribute_option_request = '''sailpoint.nerm.SubmitAttributeOptionRequest()''' # SubmitAttributeOptionRequest | 

    try:
        # Add value to option
        new_submit_attribute_option_request = SubmitAttributeOptionRequest.from_json(submit_attribute_option_request)
        results = AttributeOptionsApi(api_client).submit_attribute_option(submit_attribute_option_request=new_submit_attribute_option_request)
        # Below is a request that includes all optional parameters
        # results = AttributeOptionsApi(api_client).submit_attribute_option(new_submit_attribute_option_request)
        print("The response of AttributeOptionsApi->submit_attribute_option:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling AttributeOptionsApi->submit_attribute_option: %s\n" % e)
```



[[Back to top]](#) 

## submit-attribute-options
Create multiple option values
Create multiple new option based attribute values

[API Spec](https://developer.sailpoint.com/docs/api//submit-attribute-options)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
 Body  | submit_attribute_options_request | [**SubmitAttributeOptionsRequest**](../models/submit-attribute-options-request) | True  | 

### Return type
[**SubmitAttributeOptions200Response**](../models/submit-attribute-options200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | SubmitAttributeOptions200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.attribute_options_api import AttributeOptionsApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.submit_attribute_options200_response import SubmitAttributeOptions200Response
from sailpoint.nerm.models.submit_attribute_options_request import SubmitAttributeOptionsRequest
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    submit_attribute_options_request = '''sailpoint.nerm.SubmitAttributeOptionsRequest()''' # SubmitAttributeOptionsRequest | 

    try:
        # Create multiple option values
        new_submit_attribute_options_request = SubmitAttributeOptionsRequest.from_json(submit_attribute_options_request)
        results = AttributeOptionsApi(api_client).submit_attribute_options(submit_attribute_options_request=new_submit_attribute_options_request)
        # Below is a request that includes all optional parameters
        # results = AttributeOptionsApi(api_client).submit_attribute_options(new_submit_attribute_options_request)
        print("The response of AttributeOptionsApi->submit_attribute_options:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling AttributeOptionsApi->submit_attribute_options: %s\n" % e)
```



[[Back to top]](#) 



