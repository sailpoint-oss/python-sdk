---
id: risk-scores
title: Risk_scores
pagination_label: risk_scores
sidebar_label: risk_scores
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'risk_scores', 'risk_scores'] 
slug: /tools/sdk/python//methods/risk-scores
tags: ['SDK', 'Software Development Kit', 'risk_scores', 'risk_scores']
---

# sailpoint.nerm.RiskScoresApi
   
All URIs are relative to *https://acmeco.nonemployee.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get-risk-score**](#get-risk-score) | **GET** `/risk_scores/{id}` | Find risk score data
[**get-risk-scores**](#get-risk-scores) | **GET** `/risk_scores` | Get risk score data


## get-risk-score
Find risk score data
Find risk score data by id

[API Spec](https://developer.sailpoint.com/docs/api//get-risk-score)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | id | **str** | True  | ID of the object to retrieve, update, or delete

### Return type
[**GetRiskScore200Response**](../models/get-risk-score200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | GetRiskScore200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.risk_scores_api import RiskScoresApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.get_risk_score200_response import GetRiskScore200Response
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    id = '1246d8b3-ac29-4015-8154-dea4434a73fa' # str | ID of the object to retrieve, update, or delete # str | ID of the object to retrieve, update, or delete

    try:
        # Find risk score data
        
        results = RiskScoresApi(api_client).get_risk_score(id=id)
        # Below is a request that includes all optional parameters
        # results = RiskScoresApi(api_client).get_risk_score(id)
        print("The response of RiskScoresApi->get_risk_score:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling RiskScoresApi->get_risk_score: %s\n" % e)
```



[[Back to top]](#) 

## get-risk-scores
Get risk score data
This endpoint can retrieve risk score data in bulk from Lifecycle

[API Spec](https://developer.sailpoint.com/docs/api//get-risk-scores)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
  Query | limit | **int** |   (optional) | The maximum number of items to return.
  Query | offset | **int** |   (optional) | The number of items to skip before starting to collect the result set.
  Query | order | **str** |   (optional) | The field to order results by.
  Query | object_id | **str** |   (optional) | ID of an object for filtering. Used along with object_type
  Query | object_type | **str** |   (optional) | Type of object that object_id represents
  Query | overall_risk_level_id | **str** |   (optional) | Overall risk level to filter by
  Query | impact_risk_level_id | **str** |   (optional) | Impact risk level to filter by
  Query | probability_risk_level_id | **str** |   (optional) | Probability risk level to filter by
  Query | metadata | **bool** |   (optional) (default to False) | Returns batching metadata in the response. This includes `total` as the total quantity, `next` as the path of the following query url, `limit` and `after_id` (if requested) with the next following id (null if it is the last \"page\").

### Return type
[**GetRiskScores200Response**](../models/get-risk-scores200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | GetRiskScores200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.risk_scores_api import RiskScoresApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.get_risk_scores200_response import GetRiskScores200Response
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    limit = 5 # int | The maximum number of items to return. (optional) # int | The maximum number of items to return. (optional)
    offset = 5 # int | The number of items to skip before starting to collect the result set. (optional) # int | The number of items to skip before starting to collect the result set. (optional)
    order = 'created_at' # str | The field to order results by. (optional) # str | The field to order results by. (optional)
    object_id = 'c5e1dd38-7e29-464f-a0da-0c0d886d022a' # str | ID of an object for filtering. Used along with object_type (optional) # str | ID of an object for filtering. Used along with object_type (optional)
    object_type = 'Profile' # str | Type of object that object_id represents (optional) # str | Type of object that object_id represents (optional)
    overall_risk_level_id = 'c5e1dd38-7e29-464f-a0da-0c0d886d022a' # str | Overall risk level to filter by (optional) # str | Overall risk level to filter by (optional)
    impact_risk_level_id = 'c5e1dd38-7e29-464f-a0da-0c0d886d022a' # str | Impact risk level to filter by (optional) # str | Impact risk level to filter by (optional)
    probability_risk_level_id = 'c5e1dd38-7e29-464f-a0da-0c0d886d022a' # str | Probability risk level to filter by (optional) # str | Probability risk level to filter by (optional)
    metadata = False # bool | Returns batching metadata in the response. This includes `total` as the total quantity, `next` as the path of the following query url, `limit` and `after_id` (if requested) with the next following id (null if it is the last \"page\"). (optional) (default to False) # bool | Returns batching metadata in the response. This includes `total` as the total quantity, `next` as the path of the following query url, `limit` and `after_id` (if requested) with the next following id (null if it is the last \"page\"). (optional) (default to False)

    try:
        # Get risk score data
        
        results = RiskScoresApi(api_client).get_risk_scores()
        # Below is a request that includes all optional parameters
        # results = RiskScoresApi(api_client).get_risk_scores(limit, offset, order, object_id, object_type, overall_risk_level_id, impact_risk_level_id, probability_risk_level_id, metadata)
        print("The response of RiskScoresApi->get_risk_scores:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling RiskScoresApi->get_risk_scores: %s\n" % e)
```



[[Back to top]](#) 



