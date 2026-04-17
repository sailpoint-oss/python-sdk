---
id: attributes
title: Attributes
pagination_label: attributes
sidebar_label: attributes
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'attributes', 'attributes'] 
slug: /tools/sdk/python//methods/attributes
tags: ['SDK', 'Software Development Kit', 'attributes', 'attributes']
---

# sailpoint.nerm.AttributesApi
   
All URIs are relative to *https://acmeco.nonemployee.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create-attribute**](#create-attribute) | **POST** `/ne_attributes` | Create an attribute
[**delete-attribute-by-id**](#delete-attribute-by-id) | **DELETE** `/ne_attributes/{id}` | Delete attribute by id
[**delete-attribute-by-uid**](#delete-attribute-by-uid) | **DELETE** `/ne_attributes/{uid}` | Delete attribute
[**get-attribute-by-id**](#get-attribute-by-id) | **GET** `/ne_attributes/{id}` | Find attribute data by id
[**get-attribute-by-uid**](#get-attribute-by-uid) | **GET** `/ne_attributes/{uid}` | Find attribute data
[**get-attributes**](#get-attributes) | **GET** `/ne_attributes` | Get attribute data in bulk
[**update-attribute-by-id**](#update-attribute-by-id) | **PATCH** `/ne_attributes/{id}` | Update attribute data by id
[**update-attribute-by-uid**](#update-attribute-by-uid) | **PATCH** `/ne_attributes/{uid}` | Update attribute data


## create-attribute
Create an attribute
This endpoint can create an attribute

[API Spec](https://developer.sailpoint.com/docs/api//create-attribute)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
 Body  | create_attribute_request | [**CreateAttributeRequest**](../models/create-attribute-request) | True  | 

### Return type
[**CreateAttribute201Response**](../models/create-attribute201-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
201 | Expected response to a valid request | CreateAttribute201Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.attributes_api import AttributesApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.create_attribute201_response import CreateAttribute201Response
from sailpoint.nerm.models.create_attribute_request import CreateAttributeRequest
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    create_attribute_request = '''sailpoint.nerm.CreateAttributeRequest()''' # CreateAttributeRequest | 

    try:
        # Create an attribute
        new_create_attribute_request = CreateAttributeRequest.from_json(create_attribute_request)
        results = AttributesApi(api_client).create_attribute(create_attribute_request=new_create_attribute_request)
        # Below is a request that includes all optional parameters
        # results = AttributesApi(api_client).create_attribute(new_create_attribute_request)
        print("The response of AttributesApi->create_attribute:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling AttributesApi->create_attribute: %s\n" % e)
```



[[Back to top]](#) 

## delete-attribute-by-id
Delete attribute by id
Delete attribute by id

[API Spec](https://developer.sailpoint.com/docs/api//delete-attribute-by-id)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | id | **str** | True  | ID of the object to retrieve, update, or delete

### Return type
[**CreateAttribute201Response**](../models/create-attribute201-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | CreateAttribute201Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.attributes_api import AttributesApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.create_attribute201_response import CreateAttribute201Response
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    id = '1246d8b3-ac29-4015-8154-dea4434a73fa' # str | ID of the object to retrieve, update, or delete # str | ID of the object to retrieve, update, or delete

    try:
        # Delete attribute by id
        
        results = AttributesApi(api_client).delete_attribute_by_id(id=id)
        # Below is a request that includes all optional parameters
        # results = AttributesApi(api_client).delete_attribute_by_id(id)
        print("The response of AttributesApi->delete_attribute_by_id:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling AttributesApi->delete_attribute_by_id: %s\n" % e)
```



[[Back to top]](#) 

## delete-attribute-by-uid
Delete attribute
Delete attribute by UID (user-specified identifier)

[API Spec](https://developer.sailpoint.com/docs/api//delete-attribute-by-uid)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | uid | **str** |   (optional) | UID of the object to retrieve, update, or delete.  A UID or \"specified identifier\" is a string typically in \"snake_case\" format that provides a human-readable description of the record.  They are commonly used to ensure sandbox, qa, staging and production tenants have the identical configuration items loaded.  Every record has a UID assigned when persisted. When not specified the system assigns one by default.  A default value looks like a 32 character string of random hexadecimal characters.

### Return type
[**CreateAttribute201Response**](../models/create-attribute201-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | CreateAttribute201Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.attributes_api import AttributesApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.create_attribute201_response import CreateAttribute201Response
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    uid = 'middle_initial_attribute' # str | UID of the object to retrieve, update, or delete.  A UID or \"specified identifier\" is a string typically in \"snake_case\" format that provides a human-readable description of the record.  They are commonly used to ensure sandbox, qa, staging and production tenants have the identical configuration items loaded.  Every record has a UID assigned when persisted. When not specified the system assigns one by default.  A default value looks like a 32 character string of random hexadecimal characters. (optional) # str | UID of the object to retrieve, update, or delete.  A UID or \"specified identifier\" is a string typically in \"snake_case\" format that provides a human-readable description of the record.  They are commonly used to ensure sandbox, qa, staging and production tenants have the identical configuration items loaded.  Every record has a UID assigned when persisted. When not specified the system assigns one by default.  A default value looks like a 32 character string of random hexadecimal characters. (optional)

    try:
        # Delete attribute
        
        results = AttributesApi(api_client).delete_attribute_by_uid()
        # Below is a request that includes all optional parameters
        # results = AttributesApi(api_client).delete_attribute_by_uid(uid)
        print("The response of AttributesApi->delete_attribute_by_uid:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling AttributesApi->delete_attribute_by_uid: %s\n" % e)
```



[[Back to top]](#) 

## get-attribute-by-id
Find attribute data by id
Info for a specific attribute

[API Spec](https://developer.sailpoint.com/docs/api//get-attribute-by-id)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | id | **str** | True  | ID of the object to retrieve, update, or delete

### Return type
[**CreateAttribute201Response**](../models/create-attribute201-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | CreateAttribute201Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.attributes_api import AttributesApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.create_attribute201_response import CreateAttribute201Response
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    id = '1246d8b3-ac29-4015-8154-dea4434a73fa' # str | ID of the object to retrieve, update, or delete # str | ID of the object to retrieve, update, or delete

    try:
        # Find attribute data by id
        
        results = AttributesApi(api_client).get_attribute_by_id(id=id)
        # Below is a request that includes all optional parameters
        # results = AttributesApi(api_client).get_attribute_by_id(id)
        print("The response of AttributesApi->get_attribute_by_id:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling AttributesApi->get_attribute_by_id: %s\n" % e)
```



[[Back to top]](#) 

## get-attribute-by-uid
Find attribute data
Info for a specific attribute by UID (user-specified identifier)

[API Spec](https://developer.sailpoint.com/docs/api//get-attribute-by-uid)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | uid | **str** |   (optional) | UID of the object to retrieve, update, or delete.  A UID or \"specified identifier\" is a string typically in \"snake_case\" format that provides a human-readable description of the record.  They are commonly used to ensure sandbox, qa, staging and production tenants have the identical configuration items loaded.  Every record has a UID assigned when persisted. When not specified the system assigns one by default.  A default value looks like a 32 character string of random hexadecimal characters.

### Return type
[**CreateAttribute201Response**](../models/create-attribute201-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | CreateAttribute201Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.attributes_api import AttributesApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.create_attribute201_response import CreateAttribute201Response
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    uid = 'middle_initial_attribute' # str | UID of the object to retrieve, update, or delete.  A UID or \"specified identifier\" is a string typically in \"snake_case\" format that provides a human-readable description of the record.  They are commonly used to ensure sandbox, qa, staging and production tenants have the identical configuration items loaded.  Every record has a UID assigned when persisted. When not specified the system assigns one by default.  A default value looks like a 32 character string of random hexadecimal characters. (optional) # str | UID of the object to retrieve, update, or delete.  A UID or \"specified identifier\" is a string typically in \"snake_case\" format that provides a human-readable description of the record.  They are commonly used to ensure sandbox, qa, staging and production tenants have the identical configuration items loaded.  Every record has a UID assigned when persisted. When not specified the system assigns one by default.  A default value looks like a 32 character string of random hexadecimal characters. (optional)

    try:
        # Find attribute data
        
        results = AttributesApi(api_client).get_attribute_by_uid()
        # Below is a request that includes all optional parameters
        # results = AttributesApi(api_client).get_attribute_by_uid(uid)
        print("The response of AttributesApi->get_attribute_by_uid:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling AttributesApi->get_attribute_by_uid: %s\n" % e)
```



[[Back to top]](#) 

## get-attributes
Get attribute data in bulk
This endpoint can retrieve attribute data in bulk from Lifecycle or you can search for attributes using parameters

[API Spec](https://developer.sailpoint.com/docs/api//get-attributes)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
  Query | limit | **int** |   (optional) | The maximum number of items to return.
  Query | offset | **int** |   (optional) | The number of items to skip before starting to collect the result set.
  Query | order | **str** |   (optional) | The field to order results by.
  Query | label | **str** |   (optional) | The attribute label to filter by
  Query | data_type | **str** |   (optional) | The attribute data type to filter by
  Query | metadata | **bool** |   (optional) (default to False) | Returns batching metadata in the response. This includes `total` as the total quantity, `next` as the path of the following query url, `limit` and `after_id` (if requested) with the next following id (null if it is the last \"page\").

### Return type
[**GetAttributes200Response**](../models/get-attributes200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | GetAttributes200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.attributes_api import AttributesApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.get_attributes200_response import GetAttributes200Response
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    limit = 5 # int | The maximum number of items to return. (optional) # int | The maximum number of items to return. (optional)
    offset = 5 # int | The number of items to skip before starting to collect the result set. (optional) # int | The number of items to skip before starting to collect the result set. (optional)
    order = 'created_at' # str | The field to order results by. (optional) # str | The field to order results by. (optional)
    label = 'birthday' # str | The attribute label to filter by (optional) # str | The attribute label to filter by (optional)
    data_type = 'text field' # str | The attribute data type to filter by (optional) # str | The attribute data type to filter by (optional)
    metadata = False # bool | Returns batching metadata in the response. This includes `total` as the total quantity, `next` as the path of the following query url, `limit` and `after_id` (if requested) with the next following id (null if it is the last \"page\"). (optional) (default to False) # bool | Returns batching metadata in the response. This includes `total` as the total quantity, `next` as the path of the following query url, `limit` and `after_id` (if requested) with the next following id (null if it is the last \"page\"). (optional) (default to False)

    try:
        # Get attribute data in bulk
        
        results = AttributesApi(api_client).get_attributes()
        # Below is a request that includes all optional parameters
        # results = AttributesApi(api_client).get_attributes(limit, offset, order, label, data_type, metadata)
        print("The response of AttributesApi->get_attributes:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling AttributesApi->get_attributes: %s\n" % e)
```



[[Back to top]](#) 

## update-attribute-by-id
Update attribute data by id
Update info for a specific attribute

[API Spec](https://developer.sailpoint.com/docs/api//update-attribute-by-id)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | id | **str** | True  | ID of the object to retrieve, update, or delete
 Body  | create_attribute_request | [**CreateAttributeRequest**](../models/create-attribute-request) | True  | 

### Return type
[**CreateAttribute201Response**](../models/create-attribute201-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | CreateAttribute201Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.attributes_api import AttributesApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.create_attribute201_response import CreateAttribute201Response
from sailpoint.nerm.models.create_attribute_request import CreateAttributeRequest
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    id = '1246d8b3-ac29-4015-8154-dea4434a73fa' # str | ID of the object to retrieve, update, or delete # str | ID of the object to retrieve, update, or delete
    create_attribute_request = '''sailpoint.nerm.CreateAttributeRequest()''' # CreateAttributeRequest | 

    try:
        # Update attribute data by id
        new_create_attribute_request = CreateAttributeRequest.from_json(create_attribute_request)
        results = AttributesApi(api_client).update_attribute_by_id(id=id, create_attribute_request=new_create_attribute_request)
        # Below is a request that includes all optional parameters
        # results = AttributesApi(api_client).update_attribute_by_id(id, new_create_attribute_request)
        print("The response of AttributesApi->update_attribute_by_id:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling AttributesApi->update_attribute_by_id: %s\n" % e)
```



[[Back to top]](#) 

## update-attribute-by-uid
Update attribute data
Update info for a specific attribute by UID (user-specified identifier)

[API Spec](https://developer.sailpoint.com/docs/api//update-attribute-by-uid)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
 Body  | create_attribute_request | [**CreateAttributeRequest**](../models/create-attribute-request) | True  | 
Path   | uid | **str** |   (optional) | UID of the object to retrieve, update, or delete.  A UID or \"specified identifier\" is a string typically in \"snake_case\" format that provides a human-readable description of the record.  They are commonly used to ensure sandbox, qa, staging and production tenants have the identical configuration items loaded.  Every record has a UID assigned when persisted. When not specified the system assigns one by default.  A default value looks like a 32 character string of random hexadecimal characters.

### Return type
[**CreateAttribute201Response**](../models/create-attribute201-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | CreateAttribute201Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.attributes_api import AttributesApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.create_attribute201_response import CreateAttribute201Response
from sailpoint.nerm.models.create_attribute_request import CreateAttributeRequest
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    create_attribute_request = '''sailpoint.nerm.CreateAttributeRequest()''' # CreateAttributeRequest | 
    uid = 'middle_initial_attribute' # str | UID of the object to retrieve, update, or delete.  A UID or \"specified identifier\" is a string typically in \"snake_case\" format that provides a human-readable description of the record.  They are commonly used to ensure sandbox, qa, staging and production tenants have the identical configuration items loaded.  Every record has a UID assigned when persisted. When not specified the system assigns one by default.  A default value looks like a 32 character string of random hexadecimal characters. (optional) # str | UID of the object to retrieve, update, or delete.  A UID or \"specified identifier\" is a string typically in \"snake_case\" format that provides a human-readable description of the record.  They are commonly used to ensure sandbox, qa, staging and production tenants have the identical configuration items loaded.  Every record has a UID assigned when persisted. When not specified the system assigns one by default.  A default value looks like a 32 character string of random hexadecimal characters. (optional)

    try:
        # Update attribute data
        new_create_attribute_request = CreateAttributeRequest.from_json(create_attribute_request)
        results = AttributesApi(api_client).update_attribute_by_uid(create_attribute_request=new_create_attribute_request)
        # Below is a request that includes all optional parameters
        # results = AttributesApi(api_client).update_attribute_by_uid(new_create_attribute_request, uid)
        print("The response of AttributesApi->update_attribute_by_uid:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling AttributesApi->update_attribute_by_uid: %s\n" % e)
```



[[Back to top]](#) 



