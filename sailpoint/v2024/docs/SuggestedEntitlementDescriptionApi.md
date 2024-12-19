# sailpoint.v2024.SuggestedEntitlementDescriptionApi

All URIs are relative to *https://sailpoint.api.identitynow.com/v2024*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_sed_batch_stats**](SuggestedEntitlementDescriptionApi.md#get_sed_batch_stats) | **GET** /suggested-entitlement-description-batches/{batchId}/stats | Submit Sed Batch Stats Request
[**get_sed_batches**](SuggestedEntitlementDescriptionApi.md#get_sed_batches) | **GET** /suggested-entitlement-description-batches | List Sed Batch Request
[**list_seds**](SuggestedEntitlementDescriptionApi.md#list_seds) | **GET** /suggested-entitlement-descriptions | List Suggested Entitlement Descriptions
[**patch_sed**](SuggestedEntitlementDescriptionApi.md#patch_sed) | **PATCH** /suggested-entitlement-descriptions | Patch Suggested Entitlement Description
[**submit_sed_approval**](SuggestedEntitlementDescriptionApi.md#submit_sed_approval) | **POST** /suggested-entitlement-description-approvals | Submit Bulk Approval Request
[**submit_sed_assignment**](SuggestedEntitlementDescriptionApi.md#submit_sed_assignment) | **POST** /suggested-entitlement-description-assignments | Submit Sed Assignment Request
[**submit_sed_batch_request**](SuggestedEntitlementDescriptionApi.md#submit_sed_batch_request) | **POST** /suggested-entitlement-description-batches | Submit Sed Batch Request


# **get_sed_batch_stats**
> SedBatchStats get_sed_batch_stats(batch_id, x_sail_point_experimental)

Submit Sed Batch Stats Request

'Submit Sed Batch Stats Request.   Submits batchId in the path param `(e.g. {batchId}/stats)`. API responses with stats  of the batchId.' 

### Example

* OAuth Authentication (userAuth):
* OAuth Authentication (userAuth):

```python
import sailpoint.v2024
from sailpoint.v2024.models.sed_batch_stats import SedBatchStats
from sailpoint.v2024.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/v2024
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.v2024.Configuration(
    host = "https://sailpoint.api.identitynow.com/v2024"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.v2024.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.v2024.SuggestedEntitlementDescriptionApi(api_client)
    batch_id = '8c190e67-87aa-4ed9-a90b-d9d5344523fb' # str | Batch Id
    x_sail_point_experimental = 'true' # str | Use this header to enable this experimental API. (default to 'true')

    try:
        # Submit Sed Batch Stats Request
        api_response = api_instance.get_sed_batch_stats(batch_id, x_sail_point_experimental)
        print("The response of SuggestedEntitlementDescriptionApi->get_sed_batch_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SuggestedEntitlementDescriptionApi->get_sed_batch_stats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_id** | **str**| Batch Id | 
 **x_sail_point_experimental** | **str**| Use this header to enable this experimental API. | [default to &#39;true&#39;]

### Return type

[**SedBatchStats**](SedBatchStats.md)

### Authorization

[userAuth](../README.md#userAuth), [userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Stats of Sed batch. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sed_batches**
> SedBatchStatus get_sed_batches(x_sail_point_experimental)

List Sed Batch Request

List Sed Batches. API responses with Sed Batch Status

### Example

* OAuth Authentication (userAuth):
* OAuth Authentication (userAuth):

```python
import sailpoint.v2024
from sailpoint.v2024.models.sed_batch_status import SedBatchStatus
from sailpoint.v2024.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/v2024
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.v2024.Configuration(
    host = "https://sailpoint.api.identitynow.com/v2024"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.v2024.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.v2024.SuggestedEntitlementDescriptionApi(api_client)
    x_sail_point_experimental = 'true' # str | Use this header to enable this experimental API. (default to 'true')

    try:
        # List Sed Batch Request
        api_response = api_instance.get_sed_batches(x_sail_point_experimental)
        print("The response of SuggestedEntitlementDescriptionApi->get_sed_batches:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SuggestedEntitlementDescriptionApi->get_sed_batches: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_sail_point_experimental** | **str**| Use this header to enable this experimental API. | [default to &#39;true&#39;]

### Return type

[**SedBatchStatus**](SedBatchStatus.md)

### Authorization

[userAuth](../README.md#userAuth), [userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Status of batch |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_seds**
> List[Sed] list_seds(x_sail_point_experimental, limit=limit, filters=filters, sorters=sorters, count=count, count_only=count_only, requested_by_anyone=requested_by_anyone, show_pending_status_only=show_pending_status_only)

List Suggested Entitlement Descriptions

List of Suggested Entitlement Descriptions (SED)  SED field descriptions:  **batchId**: the ID of the batch of entitlements that are submitted for description generation  **displayName**: the display name of the entitlement that we are generating a description for  **sourceName**: the name of the source associated with the entitlement that we are generating the description for  **sourceId**: the ID of the source associated with the entitlement that we are generating the description for  **status**: the status of the suggested entitlement description, valid status options: \"requested\", \"suggested\", \"not_suggested\", \"failed\", \"assigned\", \"approved\", \"denied\"  **fullText**: will filter suggested entitlement description records by text found in any of the following fields: entitlement name, entitlement display name, suggested description, source name

### Example

* OAuth Authentication (userAuth):
* OAuth Authentication (userAuth):

```python
import sailpoint.v2024
from sailpoint.v2024.models.sed import Sed
from sailpoint.v2024.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/v2024
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.v2024.Configuration(
    host = "https://sailpoint.api.identitynow.com/v2024"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.v2024.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.v2024.SuggestedEntitlementDescriptionApi(api_client)
    x_sail_point_experimental = 'true' # str | Use this header to enable this experimental API. (default to 'true')
    limit = limit=25 # int | Integer specifying the maximum number of records to return in a single API call.  The standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#paginating-results). If it is not specified, a default limit is used. (optional)
    filters = 'displayName co \"Read and Write\"' # str | Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **batchId**: *eq, ne*  **displayName**: *eq, ne, co*  **sourceName**: *eq, ne, co*  **sourceId**: *eq, ne*  **status**: *eq, ne*  **fullText**: *co* (optional)
    sorters = 'sorters=displayName' # str | Sort results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#sorting-results)  Sorting is supported for the following fields: **displayName, sourceName, status** (optional)
    count = count=true # bool | If `true` it will populate the `X-Total-Count` response header with the number of results that would be returned if `limit` and `offset` were ignored.  The standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#paginating-results). Since requesting a total count can have a performance impact, it is recommended not to send `count=true` if that value will not be used. (optional)
    count_only = count-only=true # bool | If `true` it will populate the `X-Total-Count` response header with the number of results that would be returned if `limit` and `offset` were ignored. This parameter differs from the Coun parameter in that this one skip executing the actual query and always return an empty array. (optional)
    requested_by_anyone = requested-by-anyone=true # bool | By default, the ListSeds API will only return items that you have requested to be generated.   This option will allow you to see all items that have been requested (optional)
    show_pending_status_only = show-pending-status-only=true # bool | Will limit records to items that are in \"suggested\" or \"approved\" status (optional)

    try:
        # List Suggested Entitlement Descriptions
        api_response = api_instance.list_seds(x_sail_point_experimental, limit=limit, filters=filters, sorters=sorters, count=count, count_only=count_only, requested_by_anyone=requested_by_anyone, show_pending_status_only=show_pending_status_only)
        print("The response of SuggestedEntitlementDescriptionApi->list_seds:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SuggestedEntitlementDescriptionApi->list_seds: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_sail_point_experimental** | **str**| Use this header to enable this experimental API. | [default to &#39;true&#39;]
 **limit** | **int**| Integer specifying the maximum number of records to return in a single API call.  The standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#paginating-results). If it is not specified, a default limit is used. | [optional] 
 **filters** | **str**| Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **batchId**: *eq, ne*  **displayName**: *eq, ne, co*  **sourceName**: *eq, ne, co*  **sourceId**: *eq, ne*  **status**: *eq, ne*  **fullText**: *co* | [optional] 
 **sorters** | **str**| Sort results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#sorting-results)  Sorting is supported for the following fields: **displayName, sourceName, status** | [optional] 
 **count** | **bool**| If &#x60;true&#x60; it will populate the &#x60;X-Total-Count&#x60; response header with the number of results that would be returned if &#x60;limit&#x60; and &#x60;offset&#x60; were ignored.  The standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#paginating-results). Since requesting a total count can have a performance impact, it is recommended not to send &#x60;count&#x3D;true&#x60; if that value will not be used. | [optional] 
 **count_only** | **bool**| If &#x60;true&#x60; it will populate the &#x60;X-Total-Count&#x60; response header with the number of results that would be returned if &#x60;limit&#x60; and &#x60;offset&#x60; were ignored. This parameter differs from the Coun parameter in that this one skip executing the actual query and always return an empty array. | [optional] 
 **requested_by_anyone** | **bool**| By default, the ListSeds API will only return items that you have requested to be generated.   This option will allow you to see all items that have been requested | [optional] 
 **show_pending_status_only** | **bool**| Will limit records to items that are in \&quot;suggested\&quot; or \&quot;approved\&quot; status | [optional] 

### Return type

[**List[Sed]**](Sed.md)

### Authorization

[userAuth](../README.md#userAuth), [userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of Suggested Entitlement Details |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_sed**
> Sed patch_sed(id, x_sail_point_experimental, sed_patch)

Patch Suggested Entitlement Description

Patch Suggested Entitlement Description

### Example

* OAuth Authentication (userAuth):
* OAuth Authentication (userAuth):

```python
import sailpoint.v2024
from sailpoint.v2024.models.sed import Sed
from sailpoint.v2024.models.sed_patch import SedPatch
from sailpoint.v2024.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/v2024
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.v2024.Configuration(
    host = "https://sailpoint.api.identitynow.com/v2024"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.v2024.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.v2024.SuggestedEntitlementDescriptionApi(api_client)
    id = 'ebab396f-0af1-4050-89b7-dafc63ec70e7' # str | id is sed id
    x_sail_point_experimental = 'true' # str | Use this header to enable this experimental API. (default to 'true')
    sed_patch = [sailpoint.v2024.SedPatch()] # List[SedPatch] | Sed Patch Request

    try:
        # Patch Suggested Entitlement Description
        api_response = api_instance.patch_sed(id, x_sail_point_experimental, sed_patch)
        print("The response of SuggestedEntitlementDescriptionApi->patch_sed:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SuggestedEntitlementDescriptionApi->patch_sed: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id is sed id | 
 **x_sail_point_experimental** | **str**| Use this header to enable this experimental API. | [default to &#39;true&#39;]
 **sed_patch** | [**List[SedPatch]**](SedPatch.md)| Sed Patch Request | 

### Return type

[**Sed**](Sed.md)

### Authorization

[userAuth](../README.md#userAuth), [userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | detail of patched sed |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_sed_approval**
> List[SedApprovalStatus] submit_sed_approval(x_sail_point_experimental, sed_approval)

Submit Bulk Approval Request

Submit Bulk Approval Request for SED. Request body takes list of SED Ids. API responses with list of SED Approval Status

### Example

* OAuth Authentication (userAuth):
* OAuth Authentication (userAuth):

```python
import sailpoint.v2024
from sailpoint.v2024.models.sed_approval import SedApproval
from sailpoint.v2024.models.sed_approval_status import SedApprovalStatus
from sailpoint.v2024.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/v2024
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.v2024.Configuration(
    host = "https://sailpoint.api.identitynow.com/v2024"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.v2024.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.v2024.SuggestedEntitlementDescriptionApi(api_client)
    x_sail_point_experimental = 'true' # str | Use this header to enable this experimental API. (default to 'true')
    sed_approval = [sailpoint.v2024.SedApproval()] # List[SedApproval] | Sed Approval

    try:
        # Submit Bulk Approval Request
        api_response = api_instance.submit_sed_approval(x_sail_point_experimental, sed_approval)
        print("The response of SuggestedEntitlementDescriptionApi->submit_sed_approval:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SuggestedEntitlementDescriptionApi->submit_sed_approval: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_sail_point_experimental** | **str**| Use this header to enable this experimental API. | [default to &#39;true&#39;]
 **sed_approval** | [**List[SedApproval]**](SedApproval.md)| Sed Approval | 

### Return type

[**List[SedApprovalStatus]**](SedApprovalStatus.md)

### Authorization

[userAuth](../README.md#userAuth), [userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of SED Approval Status |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_sed_assignment**
> SedAssignmentResponse submit_sed_assignment(x_sail_point_experimental, sed_assignment)

Submit Sed Assignment Request

Submit Assignment Request. Request body has an assignee, and list of SED Ids that are assigned to that assignee API responses with batchId that groups all approval requests together

### Example

* OAuth Authentication (userAuth):
* OAuth Authentication (userAuth):

```python
import sailpoint.v2024
from sailpoint.v2024.models.sed_assignment import SedAssignment
from sailpoint.v2024.models.sed_assignment_response import SedAssignmentResponse
from sailpoint.v2024.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/v2024
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.v2024.Configuration(
    host = "https://sailpoint.api.identitynow.com/v2024"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.v2024.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.v2024.SuggestedEntitlementDescriptionApi(api_client)
    x_sail_point_experimental = 'true' # str | Use this header to enable this experimental API. (default to 'true')
    sed_assignment = sailpoint.v2024.SedAssignment() # SedAssignment | Sed Assignment Request

    try:
        # Submit Sed Assignment Request
        api_response = api_instance.submit_sed_assignment(x_sail_point_experimental, sed_assignment)
        print("The response of SuggestedEntitlementDescriptionApi->submit_sed_assignment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SuggestedEntitlementDescriptionApi->submit_sed_assignment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_sail_point_experimental** | **str**| Use this header to enable this experimental API. | [default to &#39;true&#39;]
 **sed_assignment** | [**SedAssignment**](SedAssignment.md)| Sed Assignment Request | 

### Return type

[**SedAssignmentResponse**](SedAssignmentResponse.md)

### Authorization

[userAuth](../README.md#userAuth), [userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Sed Assignment Response |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_sed_batch_request**
> SedBatchResponse submit_sed_batch_request(x_sail_point_experimental, sed_batch_request=sed_batch_request)

Submit Sed Batch Request

Submit Sed Batch Request. Request body has one of the following: - a list of entitlement Ids - a list of SED Ids that user wants to have description generated by LLM. API responses with batchId that groups Ids together

### Example

* OAuth Authentication (userAuth):
* OAuth Authentication (userAuth):

```python
import sailpoint.v2024
from sailpoint.v2024.models.sed_batch_request import SedBatchRequest
from sailpoint.v2024.models.sed_batch_response import SedBatchResponse
from sailpoint.v2024.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/v2024
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.v2024.Configuration(
    host = "https://sailpoint.api.identitynow.com/v2024"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.v2024.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.v2024.SuggestedEntitlementDescriptionApi(api_client)
    x_sail_point_experimental = 'true' # str | Use this header to enable this experimental API. (default to 'true')
    sed_batch_request = sailpoint.v2024.SedBatchRequest() # SedBatchRequest | Sed Batch Request (optional)

    try:
        # Submit Sed Batch Request
        api_response = api_instance.submit_sed_batch_request(x_sail_point_experimental, sed_batch_request=sed_batch_request)
        print("The response of SuggestedEntitlementDescriptionApi->submit_sed_batch_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SuggestedEntitlementDescriptionApi->submit_sed_batch_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_sail_point_experimental** | **str**| Use this header to enable this experimental API. | [default to &#39;true&#39;]
 **sed_batch_request** | [**SedBatchRequest**](SedBatchRequest.md)| Sed Batch Request | [optional] 

### Return type

[**SedBatchResponse**](SedBatchResponse.md)

### Authorization

[userAuth](../README.md#userAuth), [userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Sed Batch Response |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

