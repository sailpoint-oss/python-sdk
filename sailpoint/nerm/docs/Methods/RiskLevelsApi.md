---
id: risk-levels
title: Risk_levels
pagination_label: risk_levels
sidebar_label: risk_levels
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'risk_levels', 'risk_levels'] 
slug: /tools/sdk/python//methods/risk-levels
tags: ['SDK', 'Software Development Kit', 'risk_levels', 'risk_levels']
---

# sailpoint.nerm.RiskLevelsApi
   
All URIs are relative to *https://acmeco.nonemployee.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get-risk-level**](#get-risk-level) | **GET** `/risk_levels/{id}` | Find risk level data
[**get-risk-levels**](#get-risk-levels) | **GET** `/risk_levels` | Get risk level data


## get-risk-level
Find risk level data
Find risk level data by id

[API Spec](https://developer.sailpoint.com/docs/api//get-risk-level)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | id | **str** | True  | ID of the object to retrieve, update, or delete

### Return type
[**GetRiskLevel200Response**](../models/get-risk-level200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | GetRiskLevel200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.risk_levels_api import RiskLevelsApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.get_risk_level200_response import GetRiskLevel200Response
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    id = '1246d8b3-ac29-4015-8154-dea4434a73fa' # str | ID of the object to retrieve, update, or delete # str | ID of the object to retrieve, update, or delete

    try:
        # Find risk level data
        
        results = RiskLevelsApi(api_client).get_risk_level(id=id)
        # Below is a request that includes all optional parameters
        # results = RiskLevelsApi(api_client).get_risk_level(id)
        print("The response of RiskLevelsApi->get_risk_level:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling RiskLevelsApi->get_risk_level: %s\n" % e)
```



[[Back to top]](#) 

## get-risk-levels
Get risk level data
This endpoint can retrieve risk level data in bulk from Lifecycle

[API Spec](https://developer.sailpoint.com/docs/api//get-risk-levels)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
  Query | limit | **int** |   (optional) | The maximum number of items to return.
  Query | offset | **int** |   (optional) | The number of items to skip before starting to collect the result set.
  Query | order | **str** |   (optional) | The field to order results by.
  Query | label | **str** |   (optional) | The attribute label to filter by
  Query | metadata | **bool** |   (optional) (default to False) | Returns batching metadata in the response. This includes `total` as the total quantity, `next` as the path of the following query url, `limit` and `after_id` (if requested) with the next following id (null if it is the last \"page\").

### Return type
[**GetRiskLevels200Response**](../models/get-risk-levels200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | GetRiskLevels200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.risk_levels_api import RiskLevelsApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.get_risk_levels200_response import GetRiskLevels200Response
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    limit = 5 # int | The maximum number of items to return. (optional) # int | The maximum number of items to return. (optional)
    offset = 5 # int | The number of items to skip before starting to collect the result set. (optional) # int | The number of items to skip before starting to collect the result set. (optional)
    order = 'created_at' # str | The field to order results by. (optional) # str | The field to order results by. (optional)
    label = 'birthday' # str | The attribute label to filter by (optional) # str | The attribute label to filter by (optional)
    metadata = False # bool | Returns batching metadata in the response. This includes `total` as the total quantity, `next` as the path of the following query url, `limit` and `after_id` (if requested) with the next following id (null if it is the last \"page\"). (optional) (default to False) # bool | Returns batching metadata in the response. This includes `total` as the total quantity, `next` as the path of the following query url, `limit` and `after_id` (if requested) with the next following id (null if it is the last \"page\"). (optional) (default to False)

    try:
        # Get risk level data
        
        results = RiskLevelsApi(api_client).get_risk_levels()
        # Below is a request that includes all optional parameters
        # results = RiskLevelsApi(api_client).get_risk_levels(limit, offset, order, label, metadata)
        print("The response of RiskLevelsApi->get_risk_levels:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling RiskLevelsApi->get_risk_levels: %s\n" % e)
```



[[Back to top]](#) 



