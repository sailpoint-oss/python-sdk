---
id: profile-types
title: Profile_types
pagination_label: profile_types
sidebar_label: profile_types
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'profile_types', 'profile_types'] 
slug: /tools/sdk/python//methods/profile-types
tags: ['SDK', 'Software Development Kit', 'profile_types', 'profile_types']
---

# sailpoint.nerm.ProfileTypesApi
   
All URIs are relative to *https://acmeco.nonemployee.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete-profile-type-by-id**](#delete-profile-type-by-id) | **DELETE** `/profile_types/{id}` | Delete profile type
[**delete-profile-type-by-uid**](#delete-profile-type-by-uid) | **DELETE** `/profile_types/{uid}` | Delete profile type
[**get-profile-type-by-id**](#get-profile-type-by-id) | **GET** `/profile_types/{id}` | Find profile type
[**get-profile-type-by-uid**](#get-profile-type-by-uid) | **GET** `/profile_types/{uid}` | Find profile type
[**get-profile-types**](#get-profile-types) | **GET** `/profile_types` | Get profile types
[**patch-profile-type-by-id**](#patch-profile-type-by-id) | **PATCH** `/profile_types/{id}` | Update a profile type
[**patch-profile-type-by-uid**](#patch-profile-type-by-uid) | **PATCH** `/profile_types/{uid}` | Update a profile type
[**submit-profile-type**](#submit-profile-type) | **POST** `/profile_type` | Create a profile type


## delete-profile-type-by-id
Delete profile type
Delete a profile type. All profiles of that type must first be destroyed before the profile type can be destroyed.

[API Spec](https://developer.sailpoint.com/docs/api//delete-profile-type-by-id)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | id | **str** | True  | ID of the object to retrieve, update, or delete

### Return type
[**DeleteProfileTypeById200Response**](../models/delete-profile-type-by-id200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Info about the operation | DeleteProfileTypeById200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.profile_types_api import ProfileTypesApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.delete_profile_type_by_id200_response import DeleteProfileTypeById200Response
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    id = '1246d8b3-ac29-4015-8154-dea4434a73fa' # str | ID of the object to retrieve, update, or delete # str | ID of the object to retrieve, update, or delete

    try:
        # Delete profile type
        
        results = ProfileTypesApi(api_client).delete_profile_type_by_id(id=id)
        # Below is a request that includes all optional parameters
        # results = ProfileTypesApi(api_client).delete_profile_type_by_id(id)
        print("The response of ProfileTypesApi->delete_profile_type_by_id:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling ProfileTypesApi->delete_profile_type_by_id: %s\n" % e)
```



[[Back to top]](#) 

## delete-profile-type-by-uid
Delete profile type
Delete a profile type by UID (user-specified identifier). All profiles of that type must first be destroyed before the profile type can be destroyed.

[API Spec](https://developer.sailpoint.com/docs/api//delete-profile-type-by-uid)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | uid | **str** |   (optional) | UID of the object to retrieve, update, or delete.  A UID or \"specified identifier\" is a string typically in \"snake_case\" format that provides a human-readable description of the record.  They are commonly used to ensure sandbox, qa, staging and production tenants have the identical configuration items loaded.  Every record has a UID assigned when persisted. When not specified the system assigns one by default.  A default value looks like a 32 character string of random hexadecimal characters.

### Return type
[**DeleteProfileTypeById200Response**](../models/delete-profile-type-by-id200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Info about the operation | DeleteProfileTypeById200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.profile_types_api import ProfileTypesApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.delete_profile_type_by_id200_response import DeleteProfileTypeById200Response
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    uid = 'middle_initial_attribute' # str | UID of the object to retrieve, update, or delete.  A UID or \"specified identifier\" is a string typically in \"snake_case\" format that provides a human-readable description of the record.  They are commonly used to ensure sandbox, qa, staging and production tenants have the identical configuration items loaded.  Every record has a UID assigned when persisted. When not specified the system assigns one by default.  A default value looks like a 32 character string of random hexadecimal characters. (optional) # str | UID of the object to retrieve, update, or delete.  A UID or \"specified identifier\" is a string typically in \"snake_case\" format that provides a human-readable description of the record.  They are commonly used to ensure sandbox, qa, staging and production tenants have the identical configuration items loaded.  Every record has a UID assigned when persisted. When not specified the system assigns one by default.  A default value looks like a 32 character string of random hexadecimal characters. (optional)

    try:
        # Delete profile type
        
        results = ProfileTypesApi(api_client).delete_profile_type_by_uid()
        # Below is a request that includes all optional parameters
        # results = ProfileTypesApi(api_client).delete_profile_type_by_uid(uid)
        print("The response of ProfileTypesApi->delete_profile_type_by_uid:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling ProfileTypesApi->delete_profile_type_by_uid: %s\n" % e)
```



[[Back to top]](#) 

## get-profile-type-by-id
Find profile type
Find profile type by id

[API Spec](https://developer.sailpoint.com/docs/api//get-profile-type-by-id)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | id | **str** | True  | ID of the object to retrieve, update, or delete

### Return type
[**SubmitProfileType200Response**](../models/submit-profile-type200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | SubmitProfileType200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.profile_types_api import ProfileTypesApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.submit_profile_type200_response import SubmitProfileType200Response
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    id = '1246d8b3-ac29-4015-8154-dea4434a73fa' # str | ID of the object to retrieve, update, or delete # str | ID of the object to retrieve, update, or delete

    try:
        # Find profile type
        
        results = ProfileTypesApi(api_client).get_profile_type_by_id(id=id)
        # Below is a request that includes all optional parameters
        # results = ProfileTypesApi(api_client).get_profile_type_by_id(id)
        print("The response of ProfileTypesApi->get_profile_type_by_id:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling ProfileTypesApi->get_profile_type_by_id: %s\n" % e)
```



[[Back to top]](#) 

## get-profile-type-by-uid
Find profile type
Find profile type by UID (user-specified identifier)

[API Spec](https://developer.sailpoint.com/docs/api//get-profile-type-by-uid)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | uid | **str** |   (optional) | UID of the object to retrieve, update, or delete.  A UID or \"specified identifier\" is a string typically in \"snake_case\" format that provides a human-readable description of the record.  They are commonly used to ensure sandbox, qa, staging and production tenants have the identical configuration items loaded.  Every record has a UID assigned when persisted. When not specified the system assigns one by default.  A default value looks like a 32 character string of random hexadecimal characters.

### Return type
[**SubmitProfileType200Response**](../models/submit-profile-type200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | SubmitProfileType200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.profile_types_api import ProfileTypesApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.submit_profile_type200_response import SubmitProfileType200Response
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    uid = 'middle_initial_attribute' # str | UID of the object to retrieve, update, or delete.  A UID or \"specified identifier\" is a string typically in \"snake_case\" format that provides a human-readable description of the record.  They are commonly used to ensure sandbox, qa, staging and production tenants have the identical configuration items loaded.  Every record has a UID assigned when persisted. When not specified the system assigns one by default.  A default value looks like a 32 character string of random hexadecimal characters. (optional) # str | UID of the object to retrieve, update, or delete.  A UID or \"specified identifier\" is a string typically in \"snake_case\" format that provides a human-readable description of the record.  They are commonly used to ensure sandbox, qa, staging and production tenants have the identical configuration items loaded.  Every record has a UID assigned when persisted. When not specified the system assigns one by default.  A default value looks like a 32 character string of random hexadecimal characters. (optional)

    try:
        # Find profile type
        
        results = ProfileTypesApi(api_client).get_profile_type_by_uid()
        # Below is a request that includes all optional parameters
        # results = ProfileTypesApi(api_client).get_profile_type_by_uid(uid)
        print("The response of ProfileTypesApi->get_profile_type_by_uid:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling ProfileTypesApi->get_profile_type_by_uid: %s\n" % e)
```



[[Back to top]](#) 

## get-profile-types
Get profile types
Get option based attribute values

[API Spec](https://developer.sailpoint.com/docs/api//get-profile-types)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
  Query | limit | **int** |   (optional) | The maximum number of items to return.
  Query | offset | **int** |   (optional) | The number of items to skip before starting to collect the result set.
  Query | order | **str** |   (optional) | The field to order results by.
  Query | name | **str** |   (optional) | object name for filtering
  Query | archived | **bool** |   (optional) (default to False) | Filter by archive status
  Query | metadata | **bool** |   (optional) (default to False) | Returns batching metadata in the response. This includes `total` as the total quantity, `next` as the path of the following query url, `limit` and `after_id` (if requested) with the next following id (null if it is the last \"page\").

### Return type
[**GetProfileTypes200Response**](../models/get-profile-types200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | GetProfileTypes200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.profile_types_api import ProfileTypesApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.get_profile_types200_response import GetProfileTypes200Response
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    limit = 5 # int | The maximum number of items to return. (optional) # int | The maximum number of items to return. (optional)
    offset = 5 # int | The number of items to skip before starting to collect the result set. (optional) # int | The number of items to skip before starting to collect the result set. (optional)
    order = 'created_at' # str | The field to order results by. (optional) # str | The field to order results by. (optional)
    name = 'name' # str | object name for filtering (optional) # str | object name for filtering (optional)
    archived = False # bool | Filter by archive status (optional) (default to False) # bool | Filter by archive status (optional) (default to False)
    metadata = False # bool | Returns batching metadata in the response. This includes `total` as the total quantity, `next` as the path of the following query url, `limit` and `after_id` (if requested) with the next following id (null if it is the last \"page\"). (optional) (default to False) # bool | Returns batching metadata in the response. This includes `total` as the total quantity, `next` as the path of the following query url, `limit` and `after_id` (if requested) with the next following id (null if it is the last \"page\"). (optional) (default to False)

    try:
        # Get profile types
        
        results = ProfileTypesApi(api_client).get_profile_types()
        # Below is a request that includes all optional parameters
        # results = ProfileTypesApi(api_client).get_profile_types(limit, offset, order, name, archived, metadata)
        print("The response of ProfileTypesApi->get_profile_types:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling ProfileTypesApi->get_profile_types: %s\n" % e)
```



[[Back to top]](#) 

## patch-profile-type-by-id
Update a profile type
Update a profile type by id

[API Spec](https://developer.sailpoint.com/docs/api//patch-profile-type-by-id)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | id | **str** | True  | ID of the object to retrieve, update, or delete
 Body  | submit_profile_type_request | [**SubmitProfileTypeRequest**](../models/submit-profile-type-request) | True  | 

### Return type
[**SubmitProfileType200Response**](../models/submit-profile-type200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | SubmitProfileType200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.profile_types_api import ProfileTypesApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.submit_profile_type200_response import SubmitProfileType200Response
from sailpoint.nerm.models.submit_profile_type_request import SubmitProfileTypeRequest
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    id = '1246d8b3-ac29-4015-8154-dea4434a73fa' # str | ID of the object to retrieve, update, or delete # str | ID of the object to retrieve, update, or delete
    submit_profile_type_request = '''sailpoint.nerm.SubmitProfileTypeRequest()''' # SubmitProfileTypeRequest | 

    try:
        # Update a profile type
        new_submit_profile_type_request = SubmitProfileTypeRequest.from_json(submit_profile_type_request)
        results = ProfileTypesApi(api_client).patch_profile_type_by_id(id=id, submit_profile_type_request=new_submit_profile_type_request)
        # Below is a request that includes all optional parameters
        # results = ProfileTypesApi(api_client).patch_profile_type_by_id(id, new_submit_profile_type_request)
        print("The response of ProfileTypesApi->patch_profile_type_by_id:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling ProfileTypesApi->patch_profile_type_by_id: %s\n" % e)
```



[[Back to top]](#) 

## patch-profile-type-by-uid
Update a profile type
Update a profile type by UID (user-specified identifier)

[API Spec](https://developer.sailpoint.com/docs/api//patch-profile-type-by-uid)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
 Body  | submit_profile_type_request | [**SubmitProfileTypeRequest**](../models/submit-profile-type-request) | True  | 
Path   | uid | **str** |   (optional) | UID of the object to retrieve, update, or delete.  A UID or \"specified identifier\" is a string typically in \"snake_case\" format that provides a human-readable description of the record.  They are commonly used to ensure sandbox, qa, staging and production tenants have the identical configuration items loaded.  Every record has a UID assigned when persisted. When not specified the system assigns one by default.  A default value looks like a 32 character string of random hexadecimal characters.

### Return type
[**SubmitProfileType200Response**](../models/submit-profile-type200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | SubmitProfileType200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.profile_types_api import ProfileTypesApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.submit_profile_type200_response import SubmitProfileType200Response
from sailpoint.nerm.models.submit_profile_type_request import SubmitProfileTypeRequest
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    submit_profile_type_request = '''sailpoint.nerm.SubmitProfileTypeRequest()''' # SubmitProfileTypeRequest | 
    uid = 'middle_initial_attribute' # str | UID of the object to retrieve, update, or delete.  A UID or \"specified identifier\" is a string typically in \"snake_case\" format that provides a human-readable description of the record.  They are commonly used to ensure sandbox, qa, staging and production tenants have the identical configuration items loaded.  Every record has a UID assigned when persisted. When not specified the system assigns one by default.  A default value looks like a 32 character string of random hexadecimal characters. (optional) # str | UID of the object to retrieve, update, or delete.  A UID or \"specified identifier\" is a string typically in \"snake_case\" format that provides a human-readable description of the record.  They are commonly used to ensure sandbox, qa, staging and production tenants have the identical configuration items loaded.  Every record has a UID assigned when persisted. When not specified the system assigns one by default.  A default value looks like a 32 character string of random hexadecimal characters. (optional)

    try:
        # Update a profile type
        new_submit_profile_type_request = SubmitProfileTypeRequest.from_json(submit_profile_type_request)
        results = ProfileTypesApi(api_client).patch_profile_type_by_uid(submit_profile_type_request=new_submit_profile_type_request)
        # Below is a request that includes all optional parameters
        # results = ProfileTypesApi(api_client).patch_profile_type_by_uid(new_submit_profile_type_request, uid)
        print("The response of ProfileTypesApi->patch_profile_type_by_uid:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling ProfileTypesApi->patch_profile_type_by_uid: %s\n" % e)
```



[[Back to top]](#) 

## submit-profile-type
Create a profile type
Create a profile type

[API Spec](https://developer.sailpoint.com/docs/api//submit-profile-type)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
 Body  | submit_profile_type_request | [**SubmitProfileTypeRequest**](../models/submit-profile-type-request) | True  | 

### Return type
[**SubmitProfileType200Response**](../models/submit-profile-type200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | SubmitProfileType200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.profile_types_api import ProfileTypesApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.submit_profile_type200_response import SubmitProfileType200Response
from sailpoint.nerm.models.submit_profile_type_request import SubmitProfileTypeRequest
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    submit_profile_type_request = '''sailpoint.nerm.SubmitProfileTypeRequest()''' # SubmitProfileTypeRequest | 

    try:
        # Create a profile type
        new_submit_profile_type_request = SubmitProfileTypeRequest.from_json(submit_profile_type_request)
        results = ProfileTypesApi(api_client).submit_profile_type(submit_profile_type_request=new_submit_profile_type_request)
        # Below is a request that includes all optional parameters
        # results = ProfileTypesApi(api_client).submit_profile_type(new_submit_profile_type_request)
        print("The response of ProfileTypesApi->submit_profile_type:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling ProfileTypesApi->submit_profile_type: %s\n" % e)
```



[[Back to top]](#) 



