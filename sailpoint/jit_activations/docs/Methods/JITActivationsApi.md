---
id: jit-activations
title: JIT_Activations
pagination_label: JIT_Activations
sidebar_label: JIT_Activations
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'JIT_Activations', 'JIT_Activations'] 
slug: /tools/sdk/python/jit-activations/methods/jit-activations
tags: ['SDK', 'Software Development Kit', 'JIT_Activations', 'JIT_Activations']
---

# sailpoint.jit_activations.JITActivationsApi
  Use this API to start and manage Just-In-Time (JIT) Privileged activation workflows for entitlement connections,
and to search activation history.

OAuth scopes: **idn:jit-activation-workflow:*** (activate, extend, deactivate, manage) for workflow APIs.
**idn:jit-activation-history:read** (admin history view) and **idn:jit-activation-history-self:read** (self history view).
 
All URIs are relative to *https://sailpoint.api.identitynow.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list-jit-activation-history-for-current-identity-v1**](#list-jit-activation-history-for-current-identity-v1) | **GET** `/jit-activation-history/v1/current-identity` | List JIT activation history (self)
[**list-jit-activation-history-v1**](#list-jit-activation-history-v1) | **GET** `/jit-activation-history/v1` | List JIT activation history (admin)
[**start-activate-workflow-v1**](#start-activate-workflow-v1) | **POST** `/jit-activations/v1/activate` | Start JIT activation workflow
[**start-deactivate-workflow-v1**](#start-deactivate-workflow-v1) | **POST** `/jit-activations/v1/deactivate` | Deactivate JIT activation workflow
[**start-extend-workflow-v1**](#start-extend-workflow-v1) | **POST** `/jit-activations/v1/extend` | Extend JIT activation workflow


## list-jit-activation-history-for-current-identity-v1
List JIT activation history (self)
Returns JIT activation history records for the authenticated identity only.

This is the self-service view - results are automatically scoped to the calling identity.
Requires `idn:jit-activation-history-self:read`.

Returns HTTP 403 when the `PSPM_858_JIT_ACCESS_ACTIVATION_HISTORY_SEARCH` feature flag is disabled.


[API Spec](https://developer.sailpoint.com/docs/api/list-jit-activation-history-for-current-identity-v-1)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
  Query | limit | **int** |   (optional) (default to 250) | Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information.
  Query | offset | **int** |   (optional) (default to 0) | Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information.
  Query | count | **bool** |   (optional) (default to False) | If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count=true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information.
  Query | sorters | **str** |   (optional) | Sort results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#sorting-results)  Sorting is supported for the following fields: **activationInitiated, provisionCompleted, status**  Default sort is **-activationInitiated** (newest first).
  Query | search_after | **str** |   (optional) | Used to begin the search window at the values specified. This parameter consists of the last values of the sorted fields in the current record set.  searchAfter length must match the number of sorters. Used to paginate beyond the offset limit of 10,000.  It is recommended to always include the ID of the object in addition to any other sort fields to ensure no duplicate results while paging.  For example, if sorting by activationInitiated you will also want to include ID: searchAfter=2026-07-08T14:33:52.029Z,367fb802-1026-1835-a619-11a56e4c5be3&sorters=activationInitiated,id
  Query | filters | **str** |   (optional) | Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **entitlementId**: *eq, in*  **sourceId**: *eq*  **connectionId**: *eq*  **status**: *eq, in*  **activationInitiated**: *gt, lt, ge, le*  **policyFrictionOutcome**: *eq, in*

### Return type
[**List[Jitactivationhistorydocument]**](../models/jitactivationhistorydocument)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | List of JIT activation history records for the authenticated identity. | List[Jitactivationhistorydocument] |  * X-Total-Count - The total result count (returned when count=true is passed).  |
400 | Client Error - Returned if the request body is invalid. | ErrorResponseDto |  -  |
401 | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. | StartActivateWorkflowV1401Response |  -  |
403 | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. | ErrorResponseDto |  -  |
429 | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. | StartActivateWorkflowV1429Response |  -  |
500 | Internal Server Error - Returned if there is an unexpected error. | ErrorResponseDto |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.jit_activations.api.jit_activations_api import JITActivationsApi
from sailpoint.jit_activations.api_client import ApiClient
from sailpoint.jit_activations.models.jitactivationhistorydocument import Jitactivationhistorydocument
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    limit = 250 # int | Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 250) # int | Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 250)
    offset = 0 # int | Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 0) # int | Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 0)
    count = False # bool | If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count=true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to False) # bool | If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count=true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to False)
    sorters = '-activationInitiated' # str | Sort results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#sorting-results)  Sorting is supported for the following fields: **activationInitiated, provisionCompleted, status**  Default sort is **-activationInitiated** (newest first). (optional) # str | Sort results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#sorting-results)  Sorting is supported for the following fields: **activationInitiated, provisionCompleted, status**  Default sort is **-activationInitiated** (newest first). (optional)
    search_after = '2026-07-08T14:33:52.029Z,367fb802-1026-1835-a619-11a56e4c5be3' # str | Used to begin the search window at the values specified. This parameter consists of the last values of the sorted fields in the current record set.  searchAfter length must match the number of sorters. Used to paginate beyond the offset limit of 10,000.  It is recommended to always include the ID of the object in addition to any other sort fields to ensure no duplicate results while paging.  For example, if sorting by activationInitiated you will also want to include ID: searchAfter=2026-07-08T14:33:52.029Z,367fb802-1026-1835-a619-11a56e4c5be3&sorters=activationInitiated,id (optional) # str | Used to begin the search window at the values specified. This parameter consists of the last values of the sorted fields in the current record set.  searchAfter length must match the number of sorters. Used to paginate beyond the offset limit of 10,000.  It is recommended to always include the ID of the object in addition to any other sort fields to ensure no duplicate results while paging.  For example, if sorting by activationInitiated you will also want to include ID: searchAfter=2026-07-08T14:33:52.029Z,367fb802-1026-1835-a619-11a56e4c5be3&sorters=activationInitiated,id (optional)
    filters = 'status eq \"PROVISIONED\"' # str | Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **entitlementId**: *eq, in*  **sourceId**: *eq*  **connectionId**: *eq*  **status**: *eq, in*  **activationInitiated**: *gt, lt, ge, le*  **policyFrictionOutcome**: *eq, in* (optional) # str | Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **entitlementId**: *eq, in*  **sourceId**: *eq*  **connectionId**: *eq*  **status**: *eq, in*  **activationInitiated**: *gt, lt, ge, le*  **policyFrictionOutcome**: *eq, in* (optional)

    try:
        # List JIT activation history (self)
        
        results = JITActivationsApi(api_client).list_jit_activation_history_for_current_identity_v1()
        # Below is a request that includes all optional parameters
        # results = JITActivationsApi(api_client).list_jit_activation_history_for_current_identity_v1(limit, offset, count, sorters, search_after, filters)
        print("The response of JITActivationsApi->list_jit_activation_history_for_current_identity_v1:\n")
        for item in results:
            print(item.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling JITActivationsApi->list_jit_activation_history_for_current_identity_v1: %s\n" % e)
```



[[Back to top]](#) 

## list-jit-activation-history-v1
List JIT activation history (admin)
Returns JIT activation history records for the tenant.

This is the admin/operator view - it returns activations across all identities in the tenant.
Requires `idn:jit-activation-history:read`.

Returns HTTP 403 when the `PSPM_858_JIT_ACCESS_ACTIVATION_HISTORY_SEARCH` feature flag is disabled.


[API Spec](https://developer.sailpoint.com/docs/api/list-jit-activation-history-v-1)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
  Query | limit | **int** |   (optional) (default to 250) | Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information.
  Query | offset | **int** |   (optional) (default to 0) | Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information.
  Query | count | **bool** |   (optional) (default to False) | If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count=true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information.
  Query | sorters | **str** |   (optional) | Sort results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#sorting-results)  Sorting is supported for the following fields: **activationInitiated, provisionCompleted, status**  Default sort is **-activationInitiated** (newest first).
  Query | search_after | **str** |   (optional) | Used to begin the search window at the values specified. This parameter consists of the last values of the sorted fields in the current record set.  searchAfter length must match the number of sorters. Used to paginate beyond the offset limit of 10,000.  It is recommended to always include the ID of the object in addition to any other sort fields to ensure no duplicate results while paging.  For example, if sorting by activationInitiated you will also want to include ID: searchAfter=2026-07-08T14:33:52.029Z,367fb802-1026-1835-a619-11a56e4c5be3&sorters=activationInitiated,id
  Query | filters | **str** |   (optional) | Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **identityId**: *eq, in*  **entitlementId**: *eq, in*  **sourceId**: *eq*  **connectionId**: *eq*  **status**: *eq, in*  **activationInitiated**: *gt, lt, ge, le*  **policyFrictionOutcome**: *eq, in*

### Return type
[**List[Jitactivationhistorydocument]**](../models/jitactivationhistorydocument)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | List of JIT activation history records matching the request. | List[Jitactivationhistorydocument] |  * X-Total-Count - The total result count (returned when count=true is passed).  |
400 | Client Error - Returned if the request body is invalid. | ErrorResponseDto |  -  |
401 | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. | StartActivateWorkflowV1401Response |  -  |
403 | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. | ErrorResponseDto |  -  |
429 | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. | StartActivateWorkflowV1429Response |  -  |
500 | Internal Server Error - Returned if there is an unexpected error. | ErrorResponseDto |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.jit_activations.api.jit_activations_api import JITActivationsApi
from sailpoint.jit_activations.api_client import ApiClient
from sailpoint.jit_activations.models.jitactivationhistorydocument import Jitactivationhistorydocument
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    limit = 250 # int | Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 250) # int | Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 250)
    offset = 0 # int | Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 0) # int | Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 0)
    count = False # bool | If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count=true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to False) # bool | If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count=true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to False)
    sorters = '-activationInitiated' # str | Sort results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#sorting-results)  Sorting is supported for the following fields: **activationInitiated, provisionCompleted, status**  Default sort is **-activationInitiated** (newest first). (optional) # str | Sort results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#sorting-results)  Sorting is supported for the following fields: **activationInitiated, provisionCompleted, status**  Default sort is **-activationInitiated** (newest first). (optional)
    search_after = '2026-07-08T14:33:52.029Z,367fb802-1026-1835-a619-11a56e4c5be3' # str | Used to begin the search window at the values specified. This parameter consists of the last values of the sorted fields in the current record set.  searchAfter length must match the number of sorters. Used to paginate beyond the offset limit of 10,000.  It is recommended to always include the ID of the object in addition to any other sort fields to ensure no duplicate results while paging.  For example, if sorting by activationInitiated you will also want to include ID: searchAfter=2026-07-08T14:33:52.029Z,367fb802-1026-1835-a619-11a56e4c5be3&sorters=activationInitiated,id (optional) # str | Used to begin the search window at the values specified. This parameter consists of the last values of the sorted fields in the current record set.  searchAfter length must match the number of sorters. Used to paginate beyond the offset limit of 10,000.  It is recommended to always include the ID of the object in addition to any other sort fields to ensure no duplicate results while paging.  For example, if sorting by activationInitiated you will also want to include ID: searchAfter=2026-07-08T14:33:52.029Z,367fb802-1026-1835-a619-11a56e4c5be3&sorters=activationInitiated,id (optional)
    filters = 'status eq \"PROVISIONED\"' # str | Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **identityId**: *eq, in*  **entitlementId**: *eq, in*  **sourceId**: *eq*  **connectionId**: *eq*  **status**: *eq, in*  **activationInitiated**: *gt, lt, ge, le*  **policyFrictionOutcome**: *eq, in* (optional) # str | Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **identityId**: *eq, in*  **entitlementId**: *eq, in*  **sourceId**: *eq*  **connectionId**: *eq*  **status**: *eq, in*  **activationInitiated**: *gt, lt, ge, le*  **policyFrictionOutcome**: *eq, in* (optional)

    try:
        # List JIT activation history (admin)
        
        results = JITActivationsApi(api_client).list_jit_activation_history_v1()
        # Below is a request that includes all optional parameters
        # results = JITActivationsApi(api_client).list_jit_activation_history_v1(limit, offset, count, sorters, search_after, filters)
        print("The response of JITActivationsApi->list_jit_activation_history_v1:\n")
        for item in results:
            print(item.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling JITActivationsApi->list_jit_activation_history_v1: %s\n" % e)
```



[[Back to top]](#) 

## start-activate-workflow-v1
Start JIT activation workflow
Starts a JIT Privileged (JIT P) activation workflow for the given entitlement connection and duration.
The service performs quick validation; the workflow performs additional validation.

The response is returned with HTTP 202 Accepted while the workflow initializes.


[API Spec](https://developer.sailpoint.com/docs/api/start-activate-workflow-v-1)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
 Body  | jit_activation_activate_request | [**JitActivationActivateRequest**](../models/jit-activation-activate-request) | True  | 

### Return type
[**JitActivationActivateResponse**](../models/jit-activation-activate-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
202 | Accepted. The activation workflow was accepted and is running.  | JitActivationActivateResponse |  -  |
400 | Client Error - Returned if the request body is invalid. | ErrorResponseDto |  -  |
401 | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. | StartActivateWorkflowV1401Response |  -  |
403 | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. | ErrorResponseDto |  -  |
429 | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. | StartActivateWorkflowV1429Response |  -  |
500 | Internal Server Error - Returned if there is an unexpected error. | ErrorResponseDto |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.jit_activations.api.jit_activations_api import JITActivationsApi
from sailpoint.jit_activations.api_client import ApiClient
from sailpoint.jit_activations.models.jit_activation_activate_request import JitActivationActivateRequest
from sailpoint.jit_activations.models.jit_activation_activate_response import JitActivationActivateResponse
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    jit_activation_activate_request = '''{
          "activationPeriodMins" : 120,
          "connectionId" : "757fb803-9024-5861-e510-83a56e4c5bd3"
        }''' # JitActivationActivateRequest | 

    try:
        # Start JIT activation workflow
        new_jit_activation_activate_request = JitActivationActivateRequest.from_json(jit_activation_activate_request)
        results = JITActivationsApi(api_client).start_activate_workflow_v1(jit_activation_activate_request=new_jit_activation_activate_request)
        # Below is a request that includes all optional parameters
        # results = JITActivationsApi(api_client).start_activate_workflow_v1(new_jit_activation_activate_request)
        print("The response of JITActivationsApi->start_activate_workflow_v1:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling JITActivationsApi->start_activate_workflow_v1: %s\n" % e)
```



[[Back to top]](#) 

## start-deactivate-workflow-v1
Deactivate JIT activation workflow
Sends a signal to a running JIT Privileged (JIT P) activation workflow to deactivate.

This request cannot be applied to a workflow that does not exist or whose execution has already completed.
The client receives an error response in those cases.

The response is returned with HTTP 202 Accepted after the signal is sent.


[API Spec](https://developer.sailpoint.com/docs/api/start-deactivate-workflow-v-1)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
 Body  | jit_activation_deactivate_request | [**JitActivationDeactivateRequest**](../models/jit-activation-deactivate-request) | True  | 

### Return type
[**JitActivationDeactivateResponse**](../models/jit-activation-deactivate-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
202 | Accepted. The deactivation signal was sent to the workflow.  | JitActivationDeactivateResponse |  -  |
400 | Client Error - Returned if the request body is invalid. | ErrorResponseDto |  -  |
401 | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. | StartActivateWorkflowV1401Response |  -  |
403 | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. | ErrorResponseDto |  -  |
404 | Not Found - returned if the request URL refers to a resource or object that does not exist | ErrorResponseDto |  -  |
429 | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. | StartActivateWorkflowV1429Response |  -  |
500 | Internal Server Error - Returned if there is an unexpected error. | ErrorResponseDto |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.jit_activations.api.jit_activations_api import JITActivationsApi
from sailpoint.jit_activations.api_client import ApiClient
from sailpoint.jit_activations.models.jit_activation_deactivate_request import JitActivationDeactivateRequest
from sailpoint.jit_activations.models.jit_activation_deactivate_response import JitActivationDeactivateResponse
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    jit_activation_deactivate_request = '''{
          "connectionId" : "757fb803-9024-5861-e510-83a56e4c5bd3"
        }''' # JitActivationDeactivateRequest | 

    try:
        # Deactivate JIT activation workflow
        new_jit_activation_deactivate_request = JitActivationDeactivateRequest.from_json(jit_activation_deactivate_request)
        results = JITActivationsApi(api_client).start_deactivate_workflow_v1(jit_activation_deactivate_request=new_jit_activation_deactivate_request)
        # Below is a request that includes all optional parameters
        # results = JITActivationsApi(api_client).start_deactivate_workflow_v1(new_jit_activation_deactivate_request)
        print("The response of JITActivationsApi->start_deactivate_workflow_v1:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling JITActivationsApi->start_deactivate_workflow_v1: %s\n" % e)
```



[[Back to top]](#) 

## start-extend-workflow-v1
Extend JIT activation workflow
Sends a signal to a running JIT Privileged (JIT P) activation workflow to extend the activation period
by the requested number of minutes.

This request cannot be applied to a workflow that does not exist or whose execution has already completed.
The client receives an error response in those cases.

The response is returned with HTTP 202 Accepted after the signal is sent.


[API Spec](https://developer.sailpoint.com/docs/api/start-extend-workflow-v-1)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
 Body  | jit_activation_extend_request | [**JitActivationExtendRequest**](../models/jit-activation-extend-request) | True  | 

### Return type
[**JitActivationExtendResponse**](../models/jit-activation-extend-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
202 | Accepted. The extend signal was sent to the workflow.  | JitActivationExtendResponse |  -  |
400 | Client Error - Returned if the request body is invalid. | ErrorResponseDto |  -  |
401 | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. | StartActivateWorkflowV1401Response |  -  |
403 | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. | ErrorResponseDto |  -  |
404 | Not Found - returned if the request URL refers to a resource or object that does not exist | ErrorResponseDto |  -  |
429 | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. | StartActivateWorkflowV1429Response |  -  |
500 | Internal Server Error - Returned if there is an unexpected error. | ErrorResponseDto |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.jit_activations.api.jit_activations_api import JITActivationsApi
from sailpoint.jit_activations.api_client import ApiClient
from sailpoint.jit_activations.models.jit_activation_extend_request import JitActivationExtendRequest
from sailpoint.jit_activations.models.jit_activation_extend_response import JitActivationExtendResponse
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    jit_activation_extend_request = '''{
          "activationPeriodExtensionMins" : 120,
          "connectionId" : "757fb803-9024-5861-e510-83a56e4c5bd3"
        }''' # JitActivationExtendRequest | 

    try:
        # Extend JIT activation workflow
        new_jit_activation_extend_request = JitActivationExtendRequest.from_json(jit_activation_extend_request)
        results = JITActivationsApi(api_client).start_extend_workflow_v1(jit_activation_extend_request=new_jit_activation_extend_request)
        # Below is a request that includes all optional parameters
        # results = JITActivationsApi(api_client).start_extend_workflow_v1(new_jit_activation_extend_request)
        print("The response of JITActivationsApi->start_extend_workflow_v1:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling JITActivationsApi->start_extend_workflow_v1: %s\n" % e)
```



[[Back to top]](#) 



