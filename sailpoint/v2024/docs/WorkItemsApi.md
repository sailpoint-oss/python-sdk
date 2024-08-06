# sailpoint.v2024.WorkItemsApi

All URIs are relative to *https://sailpoint.api.identitynow.com/v2024*

Method | HTTP request | Description
------------- | ------------- | -------------
[**approve_approval_item**](WorkItemsApi.md#approve_approval_item) | **POST** /work-items/{id}/approve/{approvalItemId} | Approve an Approval Item
[**approve_approval_items_in_bulk**](WorkItemsApi.md#approve_approval_items_in_bulk) | **POST** /work-items/bulk-approve/{id} | Bulk approve Approval Items
[**complete_work_item**](WorkItemsApi.md#complete_work_item) | **POST** /work-items/{id} | Complete a Work Item
[**get_completed_work_items**](WorkItemsApi.md#get_completed_work_items) | **GET** /work-items/completed | Completed Work Items
[**get_count_completed_work_items**](WorkItemsApi.md#get_count_completed_work_items) | **GET** /work-items/completed/count | Count Completed Work Items
[**get_count_work_items**](WorkItemsApi.md#get_count_work_items) | **GET** /work-items/count | Count Work Items
[**get_work_item**](WorkItemsApi.md#get_work_item) | **GET** /work-items/{id} | Get a Work Item
[**get_work_items_summary**](WorkItemsApi.md#get_work_items_summary) | **GET** /work-items/summary | Work Items Summary
[**list_work_items**](WorkItemsApi.md#list_work_items) | **GET** /work-items | List Work Items
[**reject_approval_item**](WorkItemsApi.md#reject_approval_item) | **POST** /work-items/{id}/reject/{approvalItemId} | Reject an Approval Item
[**reject_approval_items_in_bulk**](WorkItemsApi.md#reject_approval_items_in_bulk) | **POST** /work-items/bulk-reject/{id} | Bulk reject Approval Items
[**send_work_item_forward**](WorkItemsApi.md#send_work_item_forward) | **POST** /work-items/{id}/forward | Forward a Work Item
[**submit_account_selection**](WorkItemsApi.md#submit_account_selection) | **POST** /work-items/{id}/submit-account-selection | Submit Account Selections


# **approve_approval_item**
> WorkItems approve_approval_item(id, approval_item_id)

Approve an Approval Item

This API approves an Approval Item. Either an admin, or the owning/current user must make this request.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.v2024
from sailpoint.v2024.models.work_items import WorkItems
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
    api_instance = sailpoint.v2024.WorkItemsApi(api_client)
    id = 'ef38f94347e94562b5bb8424a56397d8' # str | The ID of the work item
    approval_item_id = '1211bcaa32112bcef6122adb21cef1ac' # str | The ID of the approval item.

    try:
        # Approve an Approval Item
        api_response = api_instance.approve_approval_item(id, approval_item_id)
        print("The response of WorkItemsApi->approve_approval_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkItemsApi->approve_approval_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the work item | 
 **approval_item_id** | **str**| The ID of the approval item. | 

### Return type

[**WorkItems**](WorkItems.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A work items details object. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **approve_approval_items_in_bulk**
> WorkItems approve_approval_items_in_bulk(id)

Bulk approve Approval Items

This API bulk approves Approval Items. Either an admin, or the owning/current user must make this request.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.v2024
from sailpoint.v2024.models.work_items import WorkItems
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
    api_instance = sailpoint.v2024.WorkItemsApi(api_client)
    id = 'ef38f94347e94562b5bb8424a56397d8' # str | The ID of the work item

    try:
        # Bulk approve Approval Items
        api_response = api_instance.approve_approval_items_in_bulk(id)
        print("The response of WorkItemsApi->approve_approval_items_in_bulk:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkItemsApi->approve_approval_items_in_bulk: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the work item | 

### Return type

[**WorkItems**](WorkItems.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A work items details object. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **complete_work_item**
> WorkItems complete_work_item(id)

Complete a Work Item

This API completes a work item. Either an admin, or the owning/current user must make this request.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.v2024
from sailpoint.v2024.models.work_items import WorkItems
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
    api_instance = sailpoint.v2024.WorkItemsApi(api_client)
    id = 'ef38f94347e94562b5bb8424a56397d8' # str | The ID of the work item

    try:
        # Complete a Work Item
        api_response = api_instance.complete_work_item(id)
        print("The response of WorkItemsApi->complete_work_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkItemsApi->complete_work_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the work item | 

### Return type

[**WorkItems**](WorkItems.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A WorkItems object |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_completed_work_items**
> List[WorkItems] get_completed_work_items(owner_id=owner_id, limit=limit, offset=offset, count=count)

Completed Work Items

This gets a collection of completed work items belonging to either the specified user(admin required), or the current user.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.v2024
from sailpoint.v2024.models.work_items import WorkItems
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
    api_instance = sailpoint.v2024.WorkItemsApi(api_client)
    owner_id = '1211bcaa32112bcef6122adb21cef1ac' # str | The id of the owner of the work item list being requested.  Either an admin, or the owning/current user must make this request. (optional)
    limit = 250 # int | Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 250)
    offset = 0 # int | Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 0)
    count = False # bool | If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count=true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to False)

    try:
        # Completed Work Items
        api_response = api_instance.get_completed_work_items(owner_id=owner_id, limit=limit, offset=offset, count=count)
        print("The response of WorkItemsApi->get_completed_work_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkItemsApi->get_completed_work_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_id** | **str**| The id of the owner of the work item list being requested.  Either an admin, or the owning/current user must make this request. | [optional] 
 **limit** | **int**| Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to 250]
 **offset** | **int**| Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to 0]
 **count** | **bool**| If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count&#x3D;true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to False]

### Return type

[**List[WorkItems]**](WorkItems.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of completed work items. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_count_completed_work_items**
> WorkItemsCount get_count_completed_work_items(owner_id=owner_id)

Count Completed Work Items

This gets a count of completed work items belonging to either the specified user(admin required), or the current user.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.v2024
from sailpoint.v2024.models.work_items_count import WorkItemsCount
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
    api_instance = sailpoint.v2024.WorkItemsApi(api_client)
    owner_id = '1211bcaa32112bcef6122adb21cef1ac' # str | ID of the work item owner. (optional)

    try:
        # Count Completed Work Items
        api_response = api_instance.get_count_completed_work_items(owner_id=owner_id)
        print("The response of WorkItemsApi->get_count_completed_work_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkItemsApi->get_count_completed_work_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_id** | **str**| ID of the work item owner. | [optional] 

### Return type

[**WorkItemsCount**](WorkItemsCount.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of work items |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_count_work_items**
> WorkItemsCount get_count_work_items(owner_id=owner_id)

Count Work Items

This gets a count of work items belonging to either the specified user(admin required), or the current user.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.v2024
from sailpoint.v2024.models.work_items_count import WorkItemsCount
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
    api_instance = sailpoint.v2024.WorkItemsApi(api_client)
    owner_id = 'ef38f94347e94562b5bb8424a56397d8' # str | ID of the work item owner. (optional)

    try:
        # Count Work Items
        api_response = api_instance.get_count_work_items(owner_id=owner_id)
        print("The response of WorkItemsApi->get_count_work_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkItemsApi->get_count_work_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_id** | **str**| ID of the work item owner. | [optional] 

### Return type

[**WorkItemsCount**](WorkItemsCount.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of work items |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_work_item**
> WorkItems get_work_item(id)

Get a Work Item

This gets the details of a Work Item belonging to either the specified user(admin required), or the current user.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.v2024
from sailpoint.v2024.models.work_items import WorkItems
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
    api_instance = sailpoint.v2024.WorkItemsApi(api_client)
    id = '2c9180835d191a86015d28455b4a2329' # str | ID of the work item.

    try:
        # Get a Work Item
        api_response = api_instance.get_work_item(id)
        print("The response of WorkItemsApi->get_work_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkItemsApi->get_work_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the work item. | 

### Return type

[**WorkItems**](WorkItems.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The work item with the given ID. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_work_items_summary**
> WorkItemsSummary get_work_items_summary(owner_id=owner_id)

Work Items Summary

This gets a summary of work items belonging to either the specified user(admin required), or the current user.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.v2024
from sailpoint.v2024.models.work_items_summary import WorkItemsSummary
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
    api_instance = sailpoint.v2024.WorkItemsApi(api_client)
    owner_id = '1211bcaa32112bcef6122adb21cef1ac' # str | ID of the work item owner. (optional)

    try:
        # Work Items Summary
        api_response = api_instance.get_work_items_summary(owner_id=owner_id)
        print("The response of WorkItemsApi->get_work_items_summary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkItemsApi->get_work_items_summary: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_id** | **str**| ID of the work item owner. | [optional] 

### Return type

[**WorkItemsSummary**](WorkItemsSummary.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of work items |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_work_items**
> List[WorkItems] list_work_items(limit=limit, offset=offset, count=count, owner_id=owner_id)

List Work Items

This gets a collection of work items belonging to either the specified user(admin required), or the current user.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.v2024
from sailpoint.v2024.models.work_items import WorkItems
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
    api_instance = sailpoint.v2024.WorkItemsApi(api_client)
    limit = 250 # int | Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 250)
    offset = 0 # int | Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 0)
    count = False # bool | If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count=true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to False)
    owner_id = '1211bcaa32112bcef6122adb21cef1ac' # str | ID of the work item owner. (optional)

    try:
        # List Work Items
        api_response = api_instance.list_work_items(limit=limit, offset=offset, count=count, owner_id=owner_id)
        print("The response of WorkItemsApi->list_work_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkItemsApi->list_work_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to 250]
 **offset** | **int**| Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to 0]
 **count** | **bool**| If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count&#x3D;true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to False]
 **owner_id** | **str**| ID of the work item owner. | [optional] 

### Return type

[**List[WorkItems]**](WorkItems.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of work items |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reject_approval_item**
> WorkItems reject_approval_item(id, approval_item_id)

Reject an Approval Item

This API rejects an Approval Item. Either an admin, or the owning/current user must make this request.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.v2024
from sailpoint.v2024.models.work_items import WorkItems
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
    api_instance = sailpoint.v2024.WorkItemsApi(api_client)
    id = 'ef38f94347e94562b5bb8424a56397d8' # str | The ID of the work item
    approval_item_id = '1211bcaa32112bcef6122adb21cef1ac' # str | The ID of the approval item.

    try:
        # Reject an Approval Item
        api_response = api_instance.reject_approval_item(id, approval_item_id)
        print("The response of WorkItemsApi->reject_approval_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkItemsApi->reject_approval_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the work item | 
 **approval_item_id** | **str**| The ID of the approval item. | 

### Return type

[**WorkItems**](WorkItems.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A work items details object. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reject_approval_items_in_bulk**
> WorkItems reject_approval_items_in_bulk(id)

Bulk reject Approval Items

This API bulk rejects Approval Items. Either an admin, or the owning/current user must make this request.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.v2024
from sailpoint.v2024.models.work_items import WorkItems
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
    api_instance = sailpoint.v2024.WorkItemsApi(api_client)
    id = 'ef38f94347e94562b5bb8424a56397d8' # str | The ID of the work item

    try:
        # Bulk reject Approval Items
        api_response = api_instance.reject_approval_items_in_bulk(id)
        print("The response of WorkItemsApi->reject_approval_items_in_bulk:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkItemsApi->reject_approval_items_in_bulk: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the work item | 

### Return type

[**WorkItems**](WorkItems.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A work items details object. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_work_item_forward**
> send_work_item_forward(id, work_item_forward)

Forward a Work Item

This API forwards a work item to a new owner. Either an admin, or the owning/current user must make this request. Accessible to work-item Owner, ORG_ADMIN, REPORT_ADMIN, ROLE_ADMIN, ROLE_SUBADMIN, SOURCE_ADMIN, SOURCE_SUBADMIN.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.v2024
from sailpoint.v2024.models.work_item_forward import WorkItemForward
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
    api_instance = sailpoint.v2024.WorkItemsApi(api_client)
    id = 'ef38f94347e94562b5bb8424a56397d8' # str | The ID of the work item
    work_item_forward = sailpoint.v2024.WorkItemForward() # WorkItemForward | 

    try:
        # Forward a Work Item
        api_instance.send_work_item_forward(id, work_item_forward)
    except Exception as e:
        print("Exception when calling WorkItemsApi->send_work_item_forward: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the work item | 
 **work_item_forward** | [**WorkItemForward**](WorkItemForward.md)|  | 

### Return type

void (empty response body)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success, but no data is returned. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_account_selection**
> WorkItems submit_account_selection(id, request_body)

Submit Account Selections

This API submits account selections. Either an admin, or the owning/current user must make this request.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.v2024
from sailpoint.v2024.models.work_items import WorkItems
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
    api_instance = sailpoint.v2024.WorkItemsApi(api_client)
    id = 'ef38f94347e94562b5bb8424a56397d8' # str | The ID of the work item
    request_body = {fieldName=fieldValue} # Dict[str, object] | Account Selection Data map, keyed on fieldName

    try:
        # Submit Account Selections
        api_response = api_instance.submit_account_selection(id, request_body)
        print("The response of WorkItemsApi->submit_account_selection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkItemsApi->submit_account_selection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the work item | 
 **request_body** | [**Dict[str, object]**](object.md)| Account Selection Data map, keyed on fieldName | 

### Return type

[**WorkItems**](WorkItems.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A work items details object. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

