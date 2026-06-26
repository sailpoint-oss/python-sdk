---
id: intelligence-package
title: Intelligence_Package
pagination_label: Intelligence_Package
sidebar_label: Intelligence_Package
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Intelligence_Package', 'Intelligence_Package'] 
slug: /tools/sdk/python/intelligence-package/methods/intelligence-package
tags: ['SDK', 'Software Development Kit', 'Intelligence_Package', 'Intelligence_Package']
---

# sailpoint.intelligence_package.IntelligencePackageApi
  Read-only HTTP API that returns the Intelligence Package (identity context)
for SecOps enrichment use cases (SIEM/SOAR connectors, MCP, browser
extension). Backed by Atlas internal-REST calls to MICE, Shelby List Accounts,
SDS Search, IDA-outliers, and identity-history.
 
All URIs are relative to *https://sailpoint.api.identitynow.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get-intel-identity-access-history-v1**](#get-intel-identity-access-history-v1) | **GET** `/intelligence/v1/identities/{identityID}/access-history` | Return identity access-history events
[**get-intel-identity-access-v1**](#get-intel-identity-access-v1) | **GET** `/intelligence/v1/identities/{identityID}/access` | Accounts merged with privileged data
[**get-intel-identity-risk-outliers-v1**](#get-intel-identity-risk-outliers-v1) | **GET** `/intelligence/v1/identities/{identityID}/risk/outliers` | Risk outliers continuation paging
[**get-intel-identity-risk-v1**](#get-intel-identity-risk-v1) | **GET** `/intelligence/v1/identities/{identityID}/risk` | Identity risk snapshot
[**search-intel-identities-v1**](#search-intel-identities-v1) | **GET** `/intelligence/v1/identities` | Resolve one identity by filter


## get-intel-identity-access-history-v1
Return identity access-history events
Requires tenant license idn:response-and-remediation.

Events are relayed from identity-history; optional limit, offset, and count
are forwarded to the upstream when supplied.


[API Spec](https://developer.sailpoint.com/docs/api/v1/get-intel-identity-access-history-v1)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | identity_id | **str** | True  | Non-empty identity id path segment for Intelligence Package sub-resources.
  Query | limit | **int** |   (optional) | Maximum number of historical events to return in this page of results.
  Query | offset | **int** |   (optional) | Zero-based index of the first event row to return for pagination.
  Query | count | **bool** |   (optional) (default to False) | When true, the service may include total count metadata alongside the result list.

### Return type
[**Intelidentityaccesshistorybody**](../models/intelidentityaccesshistorybody)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Events relayed from identity-history. | Intelidentityaccesshistorybody |  -  |
400 | Invalid path or query parameters. | Errorbody |  -  |
401 | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. | SearchIntelIdentitiesV1401Response |  -  |
403 | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. | Errorresponsedto |  -  |
429 | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. | SearchIntelIdentitiesV1429Response |  -  |
500 | Internal or upstream server failure. | Errorbody |  -  |
4XX | Upstream non-success passed through as-is. |  |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.intelligence_package.api.intelligence_package_api import IntelligencePackageApi
from sailpoint.intelligence_package.api_client import ApiClient
from sailpoint.intelligence_package.models.intelidentityaccesshistorybody import Intelidentityaccesshistorybody
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    identity_id = 'ef38f94347e94562b5bb8424a56397d8' # str | Non-empty identity id path segment for Intelligence Package sub-resources. # str | Non-empty identity id path segment for Intelligence Package sub-resources.
    limit = 100 # int | Maximum number of historical events to return in this page of results. (optional) # int | Maximum number of historical events to return in this page of results. (optional)
    offset = 0 # int | Zero-based index of the first event row to return for pagination. (optional) # int | Zero-based index of the first event row to return for pagination. (optional)
    count = False # bool | When true, the service may include total count metadata alongside the result list. (optional) (default to False) # bool | When true, the service may include total count metadata alongside the result list. (optional) (default to False)

    try:
        # Return identity access-history events
        
        results = IntelligencePackageApi(api_client).get_intel_identity_access_history_v1(identity_id=identity_id)
        # Below is a request that includes all optional parameters
        # results = IntelligencePackageApi(api_client).get_intel_identity_access_history_v1(identity_id, limit, offset, count)
        print("The response of IntelligencePackageApi->get_intel_identity_access_history_v1:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling IntelligencePackageApi->get_intel_identity_access_history_v1: %s\n" % e)
```



[[Back to top]](#) 

## get-intel-identity-access-v1
Accounts merged with privileged data
Requires tenant license idn:response-and-remediation.

Client-facing pagination (limit, offset, count) is not supported on this route.
The service issues one Shelby List Accounts request at the upstream maximum page size
and one SDS Search request per identity.


[API Spec](https://developer.sailpoint.com/docs/api/v1/get-intel-identity-access-v1)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | identity_id | **str** | True  | Non-empty identity id path segment for Intelligence Package sub-resources.

### Return type
[**Intelidentityaccessbody**](../models/intelidentityaccessbody)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Accounts response. | Intelidentityaccessbody |  -  |
400 | Invalid path parameter. | Errorbody |  -  |
401 | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. | SearchIntelIdentitiesV1401Response |  -  |
403 | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. | Errorresponsedto |  -  |
429 | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. | SearchIntelIdentitiesV1429Response |  -  |
500 | Internal or upstream server failure. | Errorbody |  -  |
4XX | Upstream non-success passed through as-is. |  |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.intelligence_package.api.intelligence_package_api import IntelligencePackageApi
from sailpoint.intelligence_package.api_client import ApiClient
from sailpoint.intelligence_package.models.intelidentityaccessbody import Intelidentityaccessbody
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    identity_id = 'ef38f94347e94562b5bb8424a56397d8' # str | Non-empty identity id path segment for Intelligence Package sub-resources. # str | Non-empty identity id path segment for Intelligence Package sub-resources.

    try:
        # Accounts merged with privileged data
        
        results = IntelligencePackageApi(api_client).get_intel_identity_access_v1(identity_id=identity_id)
        # Below is a request that includes all optional parameters
        # results = IntelligencePackageApi(api_client).get_intel_identity_access_v1(identity_id)
        print("The response of IntelligencePackageApi->get_intel_identity_access_v1:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling IntelligencePackageApi->get_intel_identity_access_v1: %s\n" % e)
```



[[Back to top]](#) 

## get-intel-identity-risk-outliers-v1
Risk outliers continuation paging
Continuation endpoint for risk outlier access-items. Returns one page based on
the supplied limit and offset values and includes an optional continuation link
when more rows remain. Requires tenant license idn:response-and-remediation.


[API Spec](https://developer.sailpoint.com/docs/api/v1/get-intel-identity-risk-outliers-v1)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | identity_id | **str** | True  | Non-empty identity id path segment for Intelligence Package sub-resources.
  Query | limit | **int** |   (optional) (default to 250) | Maximum number of outlier rows to return for this page.
  Query | offset | **int** |   (optional) (default to 0) | Zero-based row index for the first returned outlier item.

### Return type
[**Intelidentityriskbody**](../models/intelidentityriskbody)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | One page of outlier items plus optional continuation link. | Intelidentityriskbody |  -  |
400 | Invalid path or query parameters. | Errorbody |  -  |
401 | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. | SearchIntelIdentitiesV1401Response |  -  |
403 | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. | Errorresponsedto |  -  |
429 | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. | SearchIntelIdentitiesV1429Response |  -  |
500 | Internal or upstream server failure. | Errorbody |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.intelligence_package.api.intelligence_package_api import IntelligencePackageApi
from sailpoint.intelligence_package.api_client import ApiClient
from sailpoint.intelligence_package.models.intelidentityriskbody import Intelidentityriskbody
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    identity_id = 'ef38f94347e94562b5bb8424a56397d8' # str | Non-empty identity id path segment for Intelligence Package sub-resources. # str | Non-empty identity id path segment for Intelligence Package sub-resources.
    limit = 250 # int | Maximum number of outlier rows to return for this page. (optional) (default to 250) # int | Maximum number of outlier rows to return for this page. (optional) (default to 250)
    offset = 0 # int | Zero-based row index for the first returned outlier item. (optional) (default to 0) # int | Zero-based row index for the first returned outlier item. (optional) (default to 0)

    try:
        # Risk outliers continuation paging
        
        results = IntelligencePackageApi(api_client).get_intel_identity_risk_outliers_v1(identity_id=identity_id)
        # Below is a request that includes all optional parameters
        # results = IntelligencePackageApi(api_client).get_intel_identity_risk_outliers_v1(identity_id, limit, offset)
        print("The response of IntelligencePackageApi->get_intel_identity_risk_outliers_v1:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling IntelligencePackageApi->get_intel_identity_risk_outliers_v1: %s\n" % e)
```



[[Back to top]](#) 

## get-intel-identity-risk-v1
Identity risk snapshot
Risk snapshot envelope for the identity. The service resolves the first matching
outlier for identityID and returns one page of access-items plus an optional
continuation link for additional pages.

Clients should continue paging using _links.outliers.href when provided.
Requires tenant license idn:response-and-remediation.


[API Spec](https://developer.sailpoint.com/docs/api/v1/get-intel-identity-risk-v1)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | identity_id | **str** | True  | Non-empty identity id path segment for Intelligence Package sub-resources.

### Return type
[**Intelidentityriskbody**](../models/intelidentityriskbody)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Risk envelope with first page and optional continuation link. | Intelidentityriskbody |  -  |
400 | Invalid path parameter. | Errorbody |  -  |
401 | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. | SearchIntelIdentitiesV1401Response |  -  |
403 | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. | Errorresponsedto |  -  |
429 | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. | SearchIntelIdentitiesV1429Response |  -  |
500 | Internal or upstream server failure. | Errorbody |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.intelligence_package.api.intelligence_package_api import IntelligencePackageApi
from sailpoint.intelligence_package.api_client import ApiClient
from sailpoint.intelligence_package.models.intelidentityriskbody import Intelidentityriskbody
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    identity_id = 'ef38f94347e94562b5bb8424a56397d8' # str | Non-empty identity id path segment for Intelligence Package sub-resources. # str | Non-empty identity id path segment for Intelligence Package sub-resources.

    try:
        # Identity risk snapshot
        
        results = IntelligencePackageApi(api_client).get_intel_identity_risk_v1(identity_id=identity_id)
        # Below is a request that includes all optional parameters
        # results = IntelligencePackageApi(api_client).get_intel_identity_risk_v1(identity_id)
        print("The response of IntelligencePackageApi->get_intel_identity_risk_v1:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling IntelligencePackageApi->get_intel_identity_risk_v1: %s\n" % e)
```



[[Back to top]](#) 

## search-intel-identities-v1
Resolve one identity by filter
Requires tenant license idn:response-and-remediation.

Returns the Intelligence Package envelope for the identity that matches the SCIM-style filters expression.
Supported queryable fields are id and email only.

A single match returns HTTP 200 with IntelIdentityResponse.

Zero matches returns HTTP 404 with detailCode IDC_IDENTITY_NOT_FOUND. 

Multiple matches returns HTTP 409 with detailCode IDC_IDENTITY_AMBIGUOUS and candidates listing each match.


[API Spec](https://developer.sailpoint.com/docs/api/v1/search-intel-identities-v1)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
  Query | filters | **str** | True  | Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **id**: *eq*  **email**: *eq*

### Return type
[**Intelidentityresponse**](../models/intelidentityresponse)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | One identity matched. | Intelidentityresponse |  -  |
400 | Missing or invalid filters. | Errorbody |  -  |
401 | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. | SearchIntelIdentitiesV1401Response |  -  |
403 | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. | Errorresponsedto |  -  |
404 | No identity matched the filter. | Intelidentitynotfoundbody |  -  |
409 | Multiple identities matched the filter. | Intelidentityambiguousbody |  -  |
429 | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. | SearchIntelIdentitiesV1429Response |  -  |
500 | Upstream or internal failure. | Errorbody |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.intelligence_package.api.intelligence_package_api import IntelligencePackageApi
from sailpoint.intelligence_package.api_client import ApiClient
from sailpoint.intelligence_package.models.intelidentityresponse import Intelidentityresponse
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    filters = 'id eq \"00000000-0000-0000-0000-000000000000\"' # str | Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **id**: *eq*  **email**: *eq* # str | Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **id**: *eq*  **email**: *eq*

    try:
        # Resolve one identity by filter
        
        results = IntelligencePackageApi(api_client).search_intel_identities_v1(filters=filters)
        # Below is a request that includes all optional parameters
        # results = IntelligencePackageApi(api_client).search_intel_identities_v1(filters)
        print("The response of IntelligencePackageApi->search_intel_identities_v1:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling IntelligencePackageApi->search_intel_identities_v1: %s\n" % e)
```



[[Back to top]](#) 



