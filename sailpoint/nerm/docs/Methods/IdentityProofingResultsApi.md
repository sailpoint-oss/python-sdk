---
id: identity-proofing-results
title: Identity_proofing_results
pagination_label: identity_proofing_results
sidebar_label: identity_proofing_results
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'identity_proofing_results', 'identity_proofing_results'] 
slug: /tools/sdk/python//methods/identity-proofing-results
tags: ['SDK', 'Software Development Kit', 'identity_proofing_results', 'identity_proofing_results']
---

# sailpoint.nerm.IdentityProofingResultsApi
   
All URIs are relative to *https://acmeco.nonemployee.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get-identity-proofing-results**](#get-identity-proofing-results) | **GET** `/identity_proofing_results` | Get identity proofing result data


## get-identity-proofing-results
Get identity proofing result data
Retrieves identity proofing result data in bulk from Lifecycle

[API Spec](https://developer.sailpoint.com/docs/api//get-identity-proofing-results)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
  Query | limit | **int** |   (optional) | The maximum number of items to return.
  Query | offset | **int** |   (optional) | The number of items to skip before starting to collect the result set.
  Query | order | **str** |   (optional) | The field to order results by.
  Query | profile_id | **str** |   (optional) | Profile ID to filter by
  Query | workflow_session_id | **str** |   (optional) | Workflow Session ID to filter by
  Query | result | **str** |   (optional) | ID Proofing Result to filter by
  Query | metadata | **bool** |   (optional) (default to False) | Returns batching metadata in the response. This includes `total` as the total quantity, `next` as the path of the following query url, `limit` and `after_id` (if requested) with the next following id (null if it is the last \"page\").

### Return type
[**GetIdentityProofingResults200Response**](../models/get-identity-proofing-results200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | GetIdentityProofingResults200Response |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.identity_proofing_results_api import IdentityProofingResultsApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.get_identity_proofing_results200_response import GetIdentityProofingResults200Response
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    limit = 5 # int | The maximum number of items to return. (optional) # int | The maximum number of items to return. (optional)
    offset = 5 # int | The number of items to skip before starting to collect the result set. (optional) # int | The number of items to skip before starting to collect the result set. (optional)
    order = 'created_at' # str | The field to order results by. (optional) # str | The field to order results by. (optional)
    profile_id = '4e480441-451d-47d9-87c2-9a0f0fe135eb' # str | Profile ID to filter by (optional) # str | Profile ID to filter by (optional)
    workflow_session_id = 'c5e1dd38-7e29-464f-a0da-0c0d886d022a' # str | Workflow Session ID to filter by (optional) # str | Workflow Session ID to filter by (optional)
    result = 'pass' # str | ID Proofing Result to filter by (optional) # str | ID Proofing Result to filter by (optional)
    metadata = False # bool | Returns batching metadata in the response. This includes `total` as the total quantity, `next` as the path of the following query url, `limit` and `after_id` (if requested) with the next following id (null if it is the last \"page\"). (optional) (default to False) # bool | Returns batching metadata in the response. This includes `total` as the total quantity, `next` as the path of the following query url, `limit` and `after_id` (if requested) with the next following id (null if it is the last \"page\"). (optional) (default to False)

    try:
        # Get identity proofing result data
        
        results = IdentityProofingResultsApi(api_client).get_identity_proofing_results()
        # Below is a request that includes all optional parameters
        # results = IdentityProofingResultsApi(api_client).get_identity_proofing_results(limit, offset, order, profile_id, workflow_session_id, result, metadata)
        print("The response of IdentityProofingResultsApi->get_identity_proofing_results:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling IdentityProofingResultsApi->get_identity_proofing_results: %s\n" % e)
```



[[Back to top]](#) 



