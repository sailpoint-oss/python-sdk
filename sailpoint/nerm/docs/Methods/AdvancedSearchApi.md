---
id: advanced-search
title: Advanced_search
pagination_label: advanced_search
sidebar_label: advanced_search
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'advanced_search', 'advanced_search'] 
slug: /tools/sdk/python//methods/advanced-search
tags: ['SDK', 'Software Development Kit', 'advanced_search', 'advanced_search']
---

# sailpoint.nerm.AdvancedSearchApi
   
All URIs are relative to *https://acmeco.nonemployee.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get-advanced-search**](#get-advanced-search) | **GET** `/advanced_search` | Get saved advanced search queries
[**patch-advanced-search**](#patch-advanced-search) | **PATCH** `/advanced_search/{id}` | Update a saved advanced search
[**search-advanced-search**](#search-advanced-search) | **POST** `/advanced_search/run` | Run profiles advanced search
[**search-advanced-searchby-id**](#search-advanced-searchby-id) | **GET** `/advanced_search/{id}/run` | Run a saved advanced search
[**submit-advanced-search**](#submit-advanced-search) | **POST** `/advanced_search` | Save an advanced search query


## get-advanced-search
Get saved advanced search queries
Get saved advanced search queries

[API Spec](https://developer.sailpoint.com/docs/api//get-advanced-search)

### Parameters 
This endpoint does not need any parameter. 

### Return type
[**GetAdvancedSearch200Response**](../models/get-advanced-search200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | GetAdvancedSearch200Response |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.advanced_search_api import AdvancedSearchApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.get_advanced_search200_response import GetAdvancedSearch200Response
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:

    try:
        # Get saved advanced search queries
        
        results = AdvancedSearchApi(api_client).get_advanced_search()
        # Below is a request that includes all optional parameters
        # results = AdvancedSearchApi(api_client).get_advanced_search()
        print("The response of AdvancedSearchApi->get_advanced_search:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling AdvancedSearchApi->get_advanced_search: %s\n" % e)
```



[[Back to top]](#) 

## patch-advanced-search
Update a saved advanced search
Update a saved advanced search query

[API Spec](https://developer.sailpoint.com/docs/api//patch-advanced-search)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | id | **str** | True  | ID of the object to retrieve, update, or delete
 Body  | submit_advanced_search_request | [**SubmitAdvancedSearchRequest**](../models/submit-advanced-search-request) | True  | 

### Return type
[**SubmitAdvancedSearch200Response**](../models/submit-advanced-search200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | SubmitAdvancedSearch200Response |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.advanced_search_api import AdvancedSearchApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.submit_advanced_search200_response import SubmitAdvancedSearch200Response
from sailpoint.nerm.models.submit_advanced_search_request import SubmitAdvancedSearchRequest
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    id = '1246d8b3-ac29-4015-8154-dea4434a73fa' # str | ID of the object to retrieve, update, or delete # str | ID of the object to retrieve, update, or delete
    submit_advanced_search_request = '''sailpoint.nerm.SubmitAdvancedSearchRequest()''' # SubmitAdvancedSearchRequest | 

    try:
        # Update a saved advanced search
        new_submit_advanced_search_request = SubmitAdvancedSearchRequest.from_json(submit_advanced_search_request)
        results = AdvancedSearchApi(api_client).patch_advanced_search(id=id, submit_advanced_search_request=new_submit_advanced_search_request)
        # Below is a request that includes all optional parameters
        # results = AdvancedSearchApi(api_client).patch_advanced_search(id, new_submit_advanced_search_request)
        print("The response of AdvancedSearchApi->patch_advanced_search:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling AdvancedSearchApi->patch_advanced_search: %s\n" % e)
```



[[Back to top]](#) 

## search-advanced-search
Run profiles advanced search
Run an advanced search for profiles, without saving the query

[API Spec](https://developer.sailpoint.com/docs/api//search-advanced-search)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
 Body  | submit_advanced_search_request | [**SubmitAdvancedSearchRequest**](../models/submit-advanced-search-request) | True  | 
  Query | limit | **int** |   (optional) | The maximum number of items to return.
  Query | offset | **int** |   (optional) | The number of items to skip before starting to collect the result set.
  Query | order | **str** |   (optional) | The field to order results by.

### Return type
[**SearchAdvancedSearch200Response**](../models/search-advanced-search200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | SearchAdvancedSearch200Response |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.advanced_search_api import AdvancedSearchApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.search_advanced_search200_response import SearchAdvancedSearch200Response
from sailpoint.nerm.models.submit_advanced_search_request import SubmitAdvancedSearchRequest
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    submit_advanced_search_request = '''sailpoint.nerm.SubmitAdvancedSearchRequest()''' # SubmitAdvancedSearchRequest | 
    limit = 5 # int | The maximum number of items to return. (optional) # int | The maximum number of items to return. (optional)
    offset = 5 # int | The number of items to skip before starting to collect the result set. (optional) # int | The number of items to skip before starting to collect the result set. (optional)
    order = 'created_at' # str | The field to order results by. (optional) # str | The field to order results by. (optional)

    try:
        # Run profiles advanced search
        new_submit_advanced_search_request = SubmitAdvancedSearchRequest.from_json(submit_advanced_search_request)
        results = AdvancedSearchApi(api_client).search_advanced_search(submit_advanced_search_request=new_submit_advanced_search_request)
        # Below is a request that includes all optional parameters
        # results = AdvancedSearchApi(api_client).search_advanced_search(new_submit_advanced_search_request, limit, offset, order)
        print("The response of AdvancedSearchApi->search_advanced_search:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling AdvancedSearchApi->search_advanced_search: %s\n" % e)
```



[[Back to top]](#) 

## search-advanced-searchby-id
Run a saved advanced search
Run a saved advanced search query

[API Spec](https://developer.sailpoint.com/docs/api//search-advanced-searchby-id)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | id | **str** | True  | ID of the object to retrieve, update, or delete
  Query | limit | **int** |   (optional) | The maximum number of items to return.
  Query | offset | **int** |   (optional) | The number of items to skip before starting to collect the result set.
  Query | order | **str** |   (optional) | The field to order results by.

### Return type
[**SearchAdvancedSearch200Response**](../models/search-advanced-search200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | SearchAdvancedSearch200Response |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.advanced_search_api import AdvancedSearchApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.search_advanced_search200_response import SearchAdvancedSearch200Response
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    id = '1246d8b3-ac29-4015-8154-dea4434a73fa' # str | ID of the object to retrieve, update, or delete # str | ID of the object to retrieve, update, or delete
    limit = 5 # int | The maximum number of items to return. (optional) # int | The maximum number of items to return. (optional)
    offset = 5 # int | The number of items to skip before starting to collect the result set. (optional) # int | The number of items to skip before starting to collect the result set. (optional)
    order = 'created_at' # str | The field to order results by. (optional) # str | The field to order results by. (optional)

    try:
        # Run a saved advanced search
        
        results = AdvancedSearchApi(api_client).search_advanced_searchby_id(id=id)
        # Below is a request that includes all optional parameters
        # results = AdvancedSearchApi(api_client).search_advanced_searchby_id(id, limit, offset, order)
        print("The response of AdvancedSearchApi->search_advanced_searchby_id:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling AdvancedSearchApi->search_advanced_searchby_id: %s\n" % e)
```



[[Back to top]](#) 

## submit-advanced-search
Save an advanced search query
Save an advanced search query for later use

[API Spec](https://developer.sailpoint.com/docs/api//submit-advanced-search)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
 Body  | submit_advanced_search_request | [**SubmitAdvancedSearchRequest**](../models/submit-advanced-search-request) | True  | 

### Return type
[**SubmitAdvancedSearch200Response**](../models/submit-advanced-search200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | SubmitAdvancedSearch200Response |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.advanced_search_api import AdvancedSearchApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.submit_advanced_search200_response import SubmitAdvancedSearch200Response
from sailpoint.nerm.models.submit_advanced_search_request import SubmitAdvancedSearchRequest
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    submit_advanced_search_request = '''sailpoint.nerm.SubmitAdvancedSearchRequest()''' # SubmitAdvancedSearchRequest | 

    try:
        # Save an advanced search query
        new_submit_advanced_search_request = SubmitAdvancedSearchRequest.from_json(submit_advanced_search_request)
        results = AdvancedSearchApi(api_client).submit_advanced_search(submit_advanced_search_request=new_submit_advanced_search_request)
        # Below is a request that includes all optional parameters
        # results = AdvancedSearchApi(api_client).submit_advanced_search(new_submit_advanced_search_request)
        print("The response of AdvancedSearchApi->submit_advanced_search:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling AdvancedSearchApi->submit_advanced_search: %s\n" % e)
```



[[Back to top]](#) 



