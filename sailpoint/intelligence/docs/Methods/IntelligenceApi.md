---
id: intelligence
title: Intelligence
pagination_label: Intelligence
sidebar_label: Intelligence
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Intelligence', 'Intelligence'] 
slug: /tools/sdk/python/intelligence/methods/intelligence
tags: ['SDK', 'Software Development Kit', 'Intelligence', 'Intelligence']
---

# sailpoint.intelligence.IntelligenceApi
  Read-only HTTP API that returns the Intelligence (identity context)
for SecOps enrichment use cases (SIEM/SOAR connectors, MCP, browser
extension). Backed by Atlas internal-REST calls to MICE, Shelby List Accounts,
SDS Search, IDA-outliers, and identity-history.
 
All URIs are relative to *https://sailpoint.api.identitynow.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get-identity-intelligence-v1**](#get-identity-intelligence-v1) | **GET** `/intelligence/v1/identities` | Get identity by filter
[**get-intel-identity-access-item-history-v1**](#get-intel-identity-access-item-history-v1) | **GET** `/intelligence/v1/identities/{id}/access-history/access-items` | List identity access item history
[**get-intel-identity-accounts-v1**](#get-intel-identity-accounts-v1) | **GET** `/intelligence/v1/identities/{id}/accounts` | List identity accounts
[**get-intel-identity-certification-history-v1**](#get-intel-identity-certification-history-v1) | **GET** `/intelligence/v1/identities/{id}/access-history/certifications` | List identity certification history
[**get-intel-identity-rare-access-v1**](#get-intel-identity-rare-access-v1) | **GET** `/intelligence/v1/identities/{id}/outliers/rare-access` | List identity rare access


## get-identity-intelligence-v1
Get identity by filter
Requires tenant license idn:response-and-remediation.

Resolves exactly one identity by SCIM-style filters expression and returns the Intelligence envelope.
Supported queryable fields are id and email only.
The response embeds the first page of accounts, rare access, access-history access items, and
access-history certifications. Paged slices include a next link only when more results exist.
The privilegedAccess slice contains the full result and is not paged.
The outliers slice is omitted when the tenant lacks the IDA-outliers license.


[API Spec](https://developer.sailpoint.com/docs/api/get-identity-intelligence-v-1)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
  Query | filters | **str** | True  | Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **id**: *eq*  **email**: *eq*

### Return type
[**IntelIdentityAggregate**](../models/intel-identity-aggregate)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Exactly one identity matched. | IntelIdentityAggregate |  -  |
400 | Client Error - Returned if the request body is invalid. | ErrorResponseDto |  -  |
401 | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. | GetIdentityIntelligenceV1401Response |  -  |
403 | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. | ErrorResponseDto |  -  |
404 | Not Found - returned if the request URL refers to a resource or object that does not exist | ErrorResponseDto |  -  |
409 | Multiple identities matched the filter. | ErrorResponseDto |  -  |
429 | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. | GetIdentityIntelligenceV1429Response |  -  |
500 | Internal Server Error - Returned if there is an unexpected error. | ErrorResponseDto |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.intelligence.api.intelligence_api import IntelligenceApi
from sailpoint.intelligence.api_client import ApiClient
from sailpoint.intelligence.models.intel_identity_aggregate import IntelIdentityAggregate
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    filters = 'id eq \"ef38f94347e94562b5bb8424a56397d8\"' # str | Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **id**: *eq*  **email**: *eq* # str | Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **id**: *eq*  **email**: *eq*

    try:
        # Get identity by filter
        
        results = IntelligenceApi(api_client).get_identity_intelligence_v1(filters=filters)
        # Below is a request that includes all optional parameters
        # results = IntelligenceApi(api_client).get_identity_intelligence_v1(filters)
        print("The response of IntelligenceApi->get_identity_intelligence_v1:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling IntelligenceApi->get_identity_intelligence_v1: %s\n" % e)
```



[[Back to top]](#) 

## get-intel-identity-access-item-history-v1
List identity access item history
Continuation endpoint for the parent response's `accessHistory.accessItems.next` link.
Returns one page of access-item history events for the supplied limit and offset values.
Unsupported event types and per-record decode failures are dropped server-side.
Requires tenant license idn:response-and-remediation.


[API Spec](https://developer.sailpoint.com/docs/api/get-intel-identity-access-item-history-v-1)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | id | **str** | True  | Non-empty identity id path segment for Intelligence sub-resources.
  Query | limit | **int** |   (optional) (default to 250) | Page size. Defaults to 250; values above 250 are rejected with 400.
  Query | offset | **int** |   (optional) (default to 0) | Zero-based page offset. Defaults to 0.

### Return type
[**List[IntelAccessItemHistoryEvent]**](../models/intel-access-item-history-event)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | One page of access-item history events. | List[IntelAccessItemHistoryEvent] |  -  |
400 | Invalid path or query parameters. | ErrorResponseDto |  -  |
401 | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. | GetIdentityIntelligenceV1401Response |  -  |
403 | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. | ErrorResponseDto |  -  |
429 | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. | GetIdentityIntelligenceV1429Response |  -  |
500 | Internal or upstream server failure. | ErrorResponseDto |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.intelligence.api.intelligence_api import IntelligenceApi
from sailpoint.intelligence.api_client import ApiClient
from sailpoint.intelligence.models.intel_access_item_history_event import IntelAccessItemHistoryEvent
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    id = 'ef38f94347e94562b5bb8424a56397d8' # str | Non-empty identity id path segment for Intelligence sub-resources. # str | Non-empty identity id path segment for Intelligence sub-resources.
    limit = 250 # int | Page size. Defaults to 250; values above 250 are rejected with 400. (optional) (default to 250) # int | Page size. Defaults to 250; values above 250 are rejected with 400. (optional) (default to 250)
    offset = 0 # int | Zero-based page offset. Defaults to 0. (optional) (default to 0) # int | Zero-based page offset. Defaults to 0. (optional) (default to 0)

    try:
        # List identity access item history
        
        results = IntelligenceApi(api_client).get_intel_identity_access_item_history_v1(id=id)
        # Below is a request that includes all optional parameters
        # results = IntelligenceApi(api_client).get_intel_identity_access_item_history_v1(id, limit, offset)
        print("The response of IntelligenceApi->get_intel_identity_access_item_history_v1:\n")
        for item in results:
            print(item.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling IntelligenceApi->get_intel_identity_access_item_history_v1: %s\n" % e)
```



[[Back to top]](#) 

## get-intel-identity-accounts-v1
List identity accounts
Continuation endpoint for the parent response's `accounts.next` link.
Returns one page of account rows for the supplied limit and offset values.
Requires tenant license idn:response-and-remediation.


[API Spec](https://developer.sailpoint.com/docs/api/get-intel-identity-accounts-v-1)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | id | **str** | True  | Non-empty identity id path segment for Intelligence sub-resources.
  Query | limit | **int** |   (optional) (default to 250) | Page size. Defaults to 250; values above 250 are rejected with 400.
  Query | offset | **int** |   (optional) (default to 0) | Zero-based page offset. Defaults to 0.

### Return type
[**List[IntelAccessAccountWire]**](../models/intel-access-account-wire)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | One page of accounts. | List[IntelAccessAccountWire] |  -  |
400 | Invalid path or query parameters. | ErrorResponseDto |  -  |
401 | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. | GetIdentityIntelligenceV1401Response |  -  |
403 | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. | ErrorResponseDto |  -  |
429 | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. | GetIdentityIntelligenceV1429Response |  -  |
500 | Internal or upstream server failure. | ErrorResponseDto |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.intelligence.api.intelligence_api import IntelligenceApi
from sailpoint.intelligence.api_client import ApiClient
from sailpoint.intelligence.models.intel_access_account_wire import IntelAccessAccountWire
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    id = 'ef38f94347e94562b5bb8424a56397d8' # str | Non-empty identity id path segment for Intelligence sub-resources. # str | Non-empty identity id path segment for Intelligence sub-resources.
    limit = 250 # int | Page size. Defaults to 250; values above 250 are rejected with 400. (optional) (default to 250) # int | Page size. Defaults to 250; values above 250 are rejected with 400. (optional) (default to 250)
    offset = 0 # int | Zero-based page offset. Defaults to 0. (optional) (default to 0) # int | Zero-based page offset. Defaults to 0. (optional) (default to 0)

    try:
        # List identity accounts
        
        results = IntelligenceApi(api_client).get_intel_identity_accounts_v1(id=id)
        # Below is a request that includes all optional parameters
        # results = IntelligenceApi(api_client).get_intel_identity_accounts_v1(id, limit, offset)
        print("The response of IntelligenceApi->get_intel_identity_accounts_v1:\n")
        for item in results:
            print(item.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling IntelligenceApi->get_intel_identity_accounts_v1: %s\n" % e)
```



[[Back to top]](#) 

## get-intel-identity-certification-history-v1
List identity certification history
Continuation endpoint for the parent response's `accessHistory.certifications.next` link.
Returns one page of certification history events for the supplied limit and offset values.
Per-record decode failures are dropped server-side.
Requires tenant license idn:response-and-remediation.


[API Spec](https://developer.sailpoint.com/docs/api/get-intel-identity-certification-history-v-1)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | id | **str** | True  | Non-empty identity id path segment for Intelligence sub-resources.
  Query | limit | **int** |   (optional) (default to 250) | Page size. Defaults to 250; values above 250 are rejected with 400.
  Query | offset | **int** |   (optional) (default to 0) | Zero-based page offset. Defaults to 0.

### Return type
[**List[IntelCertificationHistoryEvent]**](../models/intel-certification-history-event)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | One page of certification history events. | List[IntelCertificationHistoryEvent] |  -  |
400 | Invalid path or query parameters. | ErrorResponseDto |  -  |
401 | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. | GetIdentityIntelligenceV1401Response |  -  |
403 | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. | ErrorResponseDto |  -  |
429 | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. | GetIdentityIntelligenceV1429Response |  -  |
500 | Internal or upstream server failure. | ErrorResponseDto |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.intelligence.api.intelligence_api import IntelligenceApi
from sailpoint.intelligence.api_client import ApiClient
from sailpoint.intelligence.models.intel_certification_history_event import IntelCertificationHistoryEvent
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    id = 'ef38f94347e94562b5bb8424a56397d8' # str | Non-empty identity id path segment for Intelligence sub-resources. # str | Non-empty identity id path segment for Intelligence sub-resources.
    limit = 250 # int | Page size. Defaults to 250; values above 250 are rejected with 400. (optional) (default to 250) # int | Page size. Defaults to 250; values above 250 are rejected with 400. (optional) (default to 250)
    offset = 0 # int | Zero-based page offset. Defaults to 0. (optional) (default to 0) # int | Zero-based page offset. Defaults to 0. (optional) (default to 0)

    try:
        # List identity certification history
        
        results = IntelligenceApi(api_client).get_intel_identity_certification_history_v1(id=id)
        # Below is a request that includes all optional parameters
        # results = IntelligenceApi(api_client).get_intel_identity_certification_history_v1(id, limit, offset)
        print("The response of IntelligenceApi->get_intel_identity_certification_history_v1:\n")
        for item in results:
            print(item.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling IntelligenceApi->get_intel_identity_certification_history_v1: %s\n" % e)
```



[[Back to top]](#) 

## get-intel-identity-rare-access-v1
List identity rare access
Continuation endpoint for the parent response's `outliers.rareAccess.next` link.
Resolves the identity's first outlier, then returns one page of rare access
items for the supplied limit and offset values. An identity with no outlier
returns an empty array. Requires tenant license idn:response-and-remediation
and the IDA-outliers license.


[API Spec](https://developer.sailpoint.com/docs/api/get-intel-identity-rare-access-v-1)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | id | **str** | True  | Non-empty identity id path segment for Intelligence sub-resources.
  Query | limit | **int** |   (optional) (default to 250) | Page size. Defaults to 250; values above 250 are rejected with 400.
  Query | offset | **int** |   (optional) (default to 0) | Zero-based page offset. Defaults to 0.

### Return type
[**List[IntelOutlierAccessItem]**](../models/intel-outlier-access-item)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | One page of rare access items. | List[IntelOutlierAccessItem] |  -  |
400 | Invalid path or query parameters. | ErrorResponseDto |  -  |
401 | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. | GetIdentityIntelligenceV1401Response |  -  |
403 | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. | ErrorResponseDto |  -  |
429 | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. | GetIdentityIntelligenceV1429Response |  -  |
500 | Internal or upstream server failure. | ErrorResponseDto |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.intelligence.api.intelligence_api import IntelligenceApi
from sailpoint.intelligence.api_client import ApiClient
from sailpoint.intelligence.models.intel_outlier_access_item import IntelOutlierAccessItem
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    id = 'ef38f94347e94562b5bb8424a56397d8' # str | Non-empty identity id path segment for Intelligence sub-resources. # str | Non-empty identity id path segment for Intelligence sub-resources.
    limit = 250 # int | Page size. Defaults to 250; values above 250 are rejected with 400. (optional) (default to 250) # int | Page size. Defaults to 250; values above 250 are rejected with 400. (optional) (default to 250)
    offset = 0 # int | Zero-based page offset. Defaults to 0. (optional) (default to 0) # int | Zero-based page offset. Defaults to 0. (optional) (default to 0)

    try:
        # List identity rare access
        
        results = IntelligenceApi(api_client).get_intel_identity_rare_access_v1(id=id)
        # Below is a request that includes all optional parameters
        # results = IntelligenceApi(api_client).get_intel_identity_rare_access_v1(id, limit, offset)
        print("The response of IntelligenceApi->get_intel_identity_rare_access_v1:\n")
        for item in results:
            print(item.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling IntelligenceApi->get_intel_identity_rare_access_v1: %s\n" % e)
```



[[Back to top]](#) 



