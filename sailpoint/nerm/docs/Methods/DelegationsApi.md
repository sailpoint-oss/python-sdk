---
id: delegations
title: Delegations
pagination_label: delegations
sidebar_label: delegations
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'delegations', 'delegations'] 
slug: /tools/sdk/python//methods/delegations
tags: ['SDK', 'Software Development Kit', 'delegations', 'delegations']
---

# sailpoint.nerm.DelegationsApi
   
All URIs are relative to *https://acmeco.nonemployee.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delegations-get**](#delegations-get) | **GET** `/delegations` | List delegations
[**delegations-id-delete**](#delegations-id-delete) | **DELETE** `/delegations/{id}` | Delete a delegation
[**delegations-id-get**](#delegations-id-get) | **GET** `/delegations/{id}` | Get a single delegation
[**delegations-id-patch**](#delegations-id-patch) | **PATCH** `/delegations/{id}` | Update a delegation
[**delegations-post**](#delegations-post) | **POST** `/delegations` | Create a delegation


## delegations-get
List delegations
Returns a list of delegation records, optionally filtered by delegate, delegator, or expiration status.

[API Spec](https://developer.sailpoint.com/docs/api//delegations-get)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
  Query | delegate_id | **str** |   (optional) (default to 'false') | Filter by delegate ID
  Query | delegator_id | **str** |   (optional) (default to 'false') | Filter by delegator ID
  Query | expired | **bool** |   (optional) (default to False) | Filter by expiration status (true for expired, false for not expired)
  Query | metadata | **bool** |   (optional) (default to False) | Returns batching metadata in the response. This includes `total` as the total quantity, `next` as the path of the following query url, `limit` and `after_id` (if requested) with the next following id (null if it is the last \"page\").
  Query | limit | **int** |   (optional) | The maximum number of items to return.
  Query | offset | **int** |   (optional) | The number of items to skip before starting to collect the result set.

### Return type
[**DelegationsGet200Response**](../models/delegations-get200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | DelegationsGet200Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.delegations_api import DelegationsApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.delegations_get200_response import DelegationsGet200Response
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    delegate_id = 'false' # str | Filter by delegate ID (optional) (default to 'false') # str | Filter by delegate ID (optional) (default to 'false')
    delegator_id = 'false' # str | Filter by delegator ID (optional) (default to 'false') # str | Filter by delegator ID (optional) (default to 'false')
    expired = False # bool | Filter by expiration status (true for expired, false for not expired) (optional) (default to False) # bool | Filter by expiration status (true for expired, false for not expired) (optional) (default to False)
    metadata = False # bool | Returns batching metadata in the response. This includes `total` as the total quantity, `next` as the path of the following query url, `limit` and `after_id` (if requested) with the next following id (null if it is the last \"page\"). (optional) (default to False) # bool | Returns batching metadata in the response. This includes `total` as the total quantity, `next` as the path of the following query url, `limit` and `after_id` (if requested) with the next following id (null if it is the last \"page\"). (optional) (default to False)
    limit = 5 # int | The maximum number of items to return. (optional) # int | The maximum number of items to return. (optional)
    offset = 5 # int | The number of items to skip before starting to collect the result set. (optional) # int | The number of items to skip before starting to collect the result set. (optional)

    try:
        # List delegations
        
        results = DelegationsApi(api_client).delegations_get()
        # Below is a request that includes all optional parameters
        # results = DelegationsApi(api_client).delegations_get(delegate_id, delegator_id, expired, metadata, limit, offset)
        print("The response of DelegationsApi->delegations_get:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling DelegationsApi->delegations_get: %s\n" % e)
```



[[Back to top]](#) 

## delegations-id-delete
Delete a delegation
Delete an existing delegation record.

[API Spec](https://developer.sailpoint.com/docs/api//delegations-id-delete)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | id | **str** | True  | ID of the object to retrieve, update, or delete

### Return type
 (empty response body)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | The delegation record &#39;&lt;delegation_id&gt;&#39; has been destroyed. |  |  -  |
404 | Record Not Found | DelegationsPost404Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.delegations_api import DelegationsApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    id = '1246d8b3-ac29-4015-8154-dea4434a73fa' # str | ID of the object to retrieve, update, or delete # str | ID of the object to retrieve, update, or delete

    try:
        # Delete a delegation
        
        DelegationsApi(api_client).delegations_id_delete(id=id)
        # Below is a request that includes all optional parameters
        # DelegationsApi(api_client).delegations_id_delete(id)
    except Exception as e:
        print("Exception when calling DelegationsApi->delegations_id_delete: %s\n" % e)
```



[[Back to top]](#) 

## delegations-id-get
Get a single delegation
Returns a single delegation record by its ID.

[API Spec](https://developer.sailpoint.com/docs/api//delegations-id-get)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | id | **str** | True  | ID of the object to retrieve, update, or delete

### Return type
[**DelegationsPost201Response**](../models/delegations-post201-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | DelegationsPost201Response |  -  |
404 | Record Not Found | DelegationsPost404Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.delegations_api import DelegationsApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.delegations_post201_response import DelegationsPost201Response
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    id = '1246d8b3-ac29-4015-8154-dea4434a73fa' # str | ID of the object to retrieve, update, or delete # str | ID of the object to retrieve, update, or delete

    try:
        # Get a single delegation
        
        results = DelegationsApi(api_client).delegations_id_get(id=id)
        # Below is a request that includes all optional parameters
        # results = DelegationsApi(api_client).delegations_id_get(id)
        print("The response of DelegationsApi->delegations_id_get:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling DelegationsApi->delegations_id_get: %s\n" % e)
```



[[Back to top]](#) 

## delegations-id-patch
Update a delegation
Update an existing delegation record.

[API Spec](https://developer.sailpoint.com/docs/api//delegations-id-patch)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | id | **str** | True  | ID of the object to retrieve, update, or delete
 Body  | delegations_post_request | [**DelegationsPostRequest**](../models/delegations-post-request) | True  | 

### Return type
[**DelegationsPost201Response**](../models/delegations-post201-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | DelegationsPost201Response |  -  |
404 | Record Not Found | DelegationsPost404Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.delegations_api import DelegationsApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.delegations_post201_response import DelegationsPost201Response
from sailpoint.nerm.models.delegations_post_request import DelegationsPostRequest
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    id = '1246d8b3-ac29-4015-8154-dea4434a73fa' # str | ID of the object to retrieve, update, or delete # str | ID of the object to retrieve, update, or delete
    delegations_post_request = '''sailpoint.nerm.DelegationsPostRequest()''' # DelegationsPostRequest | 

    try:
        # Update a delegation
        new_delegations_post_request = DelegationsPostRequest.from_json(delegations_post_request)
        results = DelegationsApi(api_client).delegations_id_patch(id=id, delegations_post_request=new_delegations_post_request)
        # Below is a request that includes all optional parameters
        # results = DelegationsApi(api_client).delegations_id_patch(id, new_delegations_post_request)
        print("The response of DelegationsApi->delegations_id_patch:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling DelegationsApi->delegations_id_patch: %s\n" % e)
```



[[Back to top]](#) 

## delegations-post
Create a delegation
Create a new delegation record.

[API Spec](https://developer.sailpoint.com/docs/api//delegations-post)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
 Body  | delegations_post_request | [**DelegationsPostRequest**](../models/delegations-post-request) | True  | 

### Return type
[**DelegationsPost201Response**](../models/delegations-post201-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
201 | Expected response to a valid request | DelegationsPost201Response |  -  |
404 | Record Not Found | DelegationsPost404Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.delegations_api import DelegationsApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.delegations_post201_response import DelegationsPost201Response
from sailpoint.nerm.models.delegations_post_request import DelegationsPostRequest
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    delegations_post_request = '''sailpoint.nerm.DelegationsPostRequest()''' # DelegationsPostRequest | 

    try:
        # Create a delegation
        new_delegations_post_request = DelegationsPostRequest.from_json(delegations_post_request)
        results = DelegationsApi(api_client).delegations_post(delegations_post_request=new_delegations_post_request)
        # Below is a request that includes all optional parameters
        # results = DelegationsApi(api_client).delegations_post(new_delegations_post_request)
        print("The response of DelegationsApi->delegations_post:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling DelegationsApi->delegations_post: %s\n" % e)
```



[[Back to top]](#) 



