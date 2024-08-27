# sailpoint.beta.IdentityHistoryApi

All URIs are relative to *https://sailpoint.api.identitynow.com/beta*

Method | HTTP request | Description
------------- | ------------- | -------------
[**compare_identity_snapshots**](IdentityHistoryApi.md#compare_identity_snapshots) | **GET** /historical-identities/{id}/compare | Gets a difference of count for each access item types for the given identity between 2 snapshots
[**compare_identity_snapshots_access_type**](IdentityHistoryApi.md#compare_identity_snapshots_access_type) | **GET** /historical-identities/{id}/compare/{access-type} | Gets a list of differences of specific accessType for the given identity between 2 snapshots
[**get_historical_identity**](IdentityHistoryApi.md#get_historical_identity) | **GET** /historical-identities/{id} | Get latest snapshot of identity
[**get_historical_identity_events**](IdentityHistoryApi.md#get_historical_identity_events) | **GET** /historical-identities/{id}/events | Lists all events for the given identity
[**get_identity_snapshot**](IdentityHistoryApi.md#get_identity_snapshot) | **GET** /historical-identities/{id}/snapshots/{date} | Gets an identity snapshot at a given date
[**get_identity_snapshot_summary**](IdentityHistoryApi.md#get_identity_snapshot_summary) | **GET** /historical-identities/{id}/snapshot-summary | Gets the summary for the event count for a specific identity
[**get_identity_start_date**](IdentityHistoryApi.md#get_identity_start_date) | **GET** /historical-identities/{id}/start-date | Gets the start date of the identity
[**list_historical_identities**](IdentityHistoryApi.md#list_historical_identities) | **GET** /historical-identities | Lists all the identities
[**list_identity_access_items**](IdentityHistoryApi.md#list_identity_access_items) | **GET** /historical-identities/{id}/access-items | Gets a list of access items for the identity filtered by item type
[**list_identity_snapshot_access_items**](IdentityHistoryApi.md#list_identity_snapshot_access_items) | **GET** /historical-identities/{id}/snapshots/{date}/access-items | Get Identity Access Items Snapshot
[**list_identity_snapshots**](IdentityHistoryApi.md#list_identity_snapshots) | **GET** /historical-identities/{id}/snapshots | Lists all the snapshots for the identity


# **compare_identity_snapshots**
> List[IdentityCompareResponse] compare_identity_snapshots(id, snapshot1=snapshot1, snapshot2=snapshot2, access_item_types=access_item_types, limit=limit, offset=offset, count=count)

Gets a difference of count for each access item types for the given identity between 2 snapshots

This method gets a difference of count for each access item types for the given identity between 2 snapshots Requires authorization scope of 'idn:identity-history:read' 

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import sailpoint.beta
from sailpoint.beta.models.identity_compare_response import IdentityCompareResponse
from sailpoint.beta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/beta
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.beta.Configuration(
    host = "https://sailpoint.api.identitynow.com/beta"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.beta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.beta.IdentityHistoryApi(api_client)
    id = '8c190e6787aa4ed9a90bd9d5344523fb' # str | The identity id
    snapshot1 = '2007-03-01T13:00:00Z' # str | The snapshot 1 of identity (optional)
    snapshot2 = '2008-03-01T13:00:00Z' # str | The snapshot 2 of identity (optional)
    access_item_types = ['access_item_types_example'] # List[str] | An optional list of access item types (app, account, entitlement, etc...) to return.   If null or empty, all access items types are returned  (optional)
    limit = 250 # int | Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 250)
    offset = 0 # int | Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 0)
    count = False # bool | If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count=true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to False)

    try:
        # Gets a difference of count for each access item types for the given identity between 2 snapshots
        api_response = api_instance.compare_identity_snapshots(id, snapshot1=snapshot1, snapshot2=snapshot2, access_item_types=access_item_types, limit=limit, offset=offset, count=count)
        print("The response of IdentityHistoryApi->compare_identity_snapshots:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityHistoryApi->compare_identity_snapshots: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The identity id | 
 **snapshot1** | **str**| The snapshot 1 of identity | [optional] 
 **snapshot2** | **str**| The snapshot 2 of identity | [optional] 
 **access_item_types** | [**List[str]**](str.md)| An optional list of access item types (app, account, entitlement, etc...) to return.   If null or empty, all access items types are returned  | [optional] 
 **limit** | **int**| Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to 250]
 **offset** | **int**| Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to 0]
 **count** | **bool**| If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count&#x3D;true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to False]

### Return type

[**List[IdentityCompareResponse]**](IdentityCompareResponse.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A IdentityCompare object with difference details for each access item type |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **compare_identity_snapshots_access_type**
> List[AccessItemDiff] compare_identity_snapshots_access_type(id, access_type, access_associated=access_associated, snapshot1=snapshot1, snapshot2=snapshot2, limit=limit, offset=offset, count=count)

Gets a list of differences of specific accessType for the given identity between 2 snapshots

This method gets a list of differences of specific accessType for the given identity between 2 snapshots Requires authorization scope of 'idn:identity-history:read' 

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import sailpoint.beta
from sailpoint.beta.models.access_item_diff import AccessItemDiff
from sailpoint.beta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/beta
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.beta.Configuration(
    host = "https://sailpoint.api.identitynow.com/beta"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.beta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.beta.IdentityHistoryApi(api_client)
    id = '8c190e6787aa4ed9a90bd9d5344523fb' # str | The identity id
    access_type = 'role' # str | The specific type which needs to be compared
    access_associated = 2007-03-01T13:00:00Z # bool | Indicates if added or removed access needs to be returned. true - added, false - removed, null - both added & removed (optional)
    snapshot1 = '2008-03-01T13:00:00Z' # str | The snapshot 1 of identity (optional)
    snapshot2 = '2009-03-01T13:00:00Z' # str | The snapshot 2 of identity (optional)
    limit = 250 # int | Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 250)
    offset = 0 # int | Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 0)
    count = False # bool | If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count=true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to False)

    try:
        # Gets a list of differences of specific accessType for the given identity between 2 snapshots
        api_response = api_instance.compare_identity_snapshots_access_type(id, access_type, access_associated=access_associated, snapshot1=snapshot1, snapshot2=snapshot2, limit=limit, offset=offset, count=count)
        print("The response of IdentityHistoryApi->compare_identity_snapshots_access_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityHistoryApi->compare_identity_snapshots_access_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The identity id | 
 **access_type** | **str**| The specific type which needs to be compared | 
 **access_associated** | **bool**| Indicates if added or removed access needs to be returned. true - added, false - removed, null - both added &amp; removed | [optional] 
 **snapshot1** | **str**| The snapshot 1 of identity | [optional] 
 **snapshot2** | **str**| The snapshot 2 of identity | [optional] 
 **limit** | **int**| Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to 250]
 **offset** | **int**| Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to 0]
 **count** | **bool**| If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count&#x3D;true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to False]

### Return type

[**List[AccessItemDiff]**](AccessItemDiff.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of events for the identity |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_historical_identity**
> IdentityHistoryResponse get_historical_identity(id)

Get latest snapshot of identity

This method retrieves a specified identity Requires authorization scope of 'idn:identity-history:read'

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import sailpoint.beta
from sailpoint.beta.models.identity_history_response import IdentityHistoryResponse
from sailpoint.beta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/beta
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.beta.Configuration(
    host = "https://sailpoint.api.identitynow.com/beta"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.beta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.beta.IdentityHistoryApi(api_client)
    id = '8c190e6787aa4ed9a90bd9d5344523fb' # str | The identity id

    try:
        # Get latest snapshot of identity
        api_response = api_instance.get_historical_identity(id)
        print("The response of IdentityHistoryApi->get_historical_identity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityHistoryApi->get_historical_identity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The identity id | 

### Return type

[**IdentityHistoryResponse**](IdentityHistoryResponse.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The identity object. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_historical_identity_events**
> List[GetHistoricalIdentityEvents200ResponseInner] get_historical_identity_events(id, var_from=var_from, event_types=event_types, access_item_types=access_item_types, limit=limit, offset=offset, count=count)

Lists all events for the given identity

This method retrieves all access events for the identity Requires authorization scope of 'idn:identity-history:read' 

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import sailpoint.beta
from sailpoint.beta.models.get_historical_identity_events200_response_inner import GetHistoricalIdentityEvents200ResponseInner
from sailpoint.beta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/beta
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.beta.Configuration(
    host = "https://sailpoint.api.identitynow.com/beta"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.beta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.beta.IdentityHistoryApi(api_client)
    id = '8c190e6787aa4ed9a90bd9d5344523fb' # str | The identity id
    var_from = '2024-03-01T13:00:00Z' # str | The optional instant until which access events are returned (optional)
    event_types = ['[AccessAddedEvent, AccessRemovedEvent]'] # List[str] | An optional list of event types to return.  If null or empty, all events are returned (optional)
    access_item_types = ['[entitlement, account]'] # List[str] | An optional list of access item types (app, account, entitlement, etc...) to return.   If null or empty, all access items types are returned (optional)
    limit = 250 # int | Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 250)
    offset = 0 # int | Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 0)
    count = False # bool | If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count=true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to False)

    try:
        # Lists all events for the given identity
        api_response = api_instance.get_historical_identity_events(id, var_from=var_from, event_types=event_types, access_item_types=access_item_types, limit=limit, offset=offset, count=count)
        print("The response of IdentityHistoryApi->get_historical_identity_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityHistoryApi->get_historical_identity_events: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The identity id | 
 **var_from** | **str**| The optional instant until which access events are returned | [optional] 
 **event_types** | [**List[str]**](str.md)| An optional list of event types to return.  If null or empty, all events are returned | [optional] 
 **access_item_types** | [**List[str]**](str.md)| An optional list of access item types (app, account, entitlement, etc...) to return.   If null or empty, all access items types are returned | [optional] 
 **limit** | **int**| Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to 250]
 **offset** | **int**| Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to 0]
 **count** | **bool**| If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count&#x3D;true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to False]

### Return type

[**List[GetHistoricalIdentityEvents200ResponseInner]**](GetHistoricalIdentityEvents200ResponseInner.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of events for the identity |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_identity_snapshot**
> IdentityHistoryResponse get_identity_snapshot(id, var_date)

Gets an identity snapshot at a given date

This method retrieves a specified identity snapshot at a given date Requires authorization scope of 'idn:identity-history:read' 

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import sailpoint.beta
from sailpoint.beta.models.identity_history_response import IdentityHistoryResponse
from sailpoint.beta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/beta
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.beta.Configuration(
    host = "https://sailpoint.api.identitynow.com/beta"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.beta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.beta.IdentityHistoryApi(api_client)
    id = '8c190e6787aa4ed9a90bd9d5344523fb' # str | The identity id
    var_date = '2007-03-01T13:00:00Z' # str | The specified date

    try:
        # Gets an identity snapshot at a given date
        api_response = api_instance.get_identity_snapshot(id, var_date)
        print("The response of IdentityHistoryApi->get_identity_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityHistoryApi->get_identity_snapshot: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The identity id | 
 **var_date** | **str**| The specified date | 

### Return type

[**IdentityHistoryResponse**](IdentityHistoryResponse.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The identity object. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_identity_snapshot_summary**
> List[MetricResponse] get_identity_snapshot_summary(id, before=before, interval=interval, time_zone=time_zone, limit=limit, offset=offset, count=count)

Gets the summary for the event count for a specific identity

This method gets the summary for the event count for a specific identity by month/day Requires authorization scope of 'idn:identity-history:read' 

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import sailpoint.beta
from sailpoint.beta.models.metric_response import MetricResponse
from sailpoint.beta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/beta
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.beta.Configuration(
    host = "https://sailpoint.api.identitynow.com/beta"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.beta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.beta.IdentityHistoryApi(api_client)
    id = '8c190e6787aa4ed9a90bd9d5344523fb' # str | The identity id
    before = '2007-03-01T13:00:00Z' # str | The date before which snapshot summary is required (optional)
    interval = 'interval_example' # str | The interval indicating day or month. Defaults to month if not specified (optional)
    time_zone = 'UTC' # str | The time zone. Defaults to UTC if not provided (optional)
    limit = 250 # int | Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 250)
    offset = 0 # int | Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 0)
    count = False # bool | If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count=true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to False)

    try:
        # Gets the summary for the event count for a specific identity
        api_response = api_instance.get_identity_snapshot_summary(id, before=before, interval=interval, time_zone=time_zone, limit=limit, offset=offset, count=count)
        print("The response of IdentityHistoryApi->get_identity_snapshot_summary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityHistoryApi->get_identity_snapshot_summary: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The identity id | 
 **before** | **str**| The date before which snapshot summary is required | [optional] 
 **interval** | **str**| The interval indicating day or month. Defaults to month if not specified | [optional] 
 **time_zone** | **str**| The time zone. Defaults to UTC if not provided | [optional] 
 **limit** | **int**| Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to 250]
 **offset** | **int**| Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to 0]
 **count** | **bool**| If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count&#x3D;true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to False]

### Return type

[**List[MetricResponse]**](MetricResponse.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A summary list of identity changes in date histogram format. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_identity_start_date**
> str get_identity_start_date(id)

Gets the start date of the identity

This method retrieves start date of the identity Requires authorization scope of 'idn:identity-history:read' 

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import sailpoint.beta
from sailpoint.beta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/beta
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.beta.Configuration(
    host = "https://sailpoint.api.identitynow.com/beta"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.beta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.beta.IdentityHistoryApi(api_client)
    id = '8c190e6787aa4ed9a90bd9d5344523fb' # str | The identity id

    try:
        # Gets the start date of the identity
        api_response = api_instance.get_identity_start_date(id)
        print("The response of IdentityHistoryApi->get_identity_start_date:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityHistoryApi->get_identity_start_date: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The identity id | 

### Return type

**str**

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The start date of the identity |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_historical_identities**
> List[IdentityListItem] list_historical_identities(starts_with_query=starts_with_query, is_deleted=is_deleted, is_active=is_active, limit=limit, offset=offset)

Lists all the identities

This gets the list of identities for the customer. This list end point does not support count=true request param. The total  count of identities would never be returned even if the count param is specified in the request Requires authorization scope of 'idn:identity-history:read'

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import sailpoint.beta
from sailpoint.beta.models.identity_list_item import IdentityListItem
from sailpoint.beta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/beta
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.beta.Configuration(
    host = "https://sailpoint.api.identitynow.com/beta"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.beta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.beta.IdentityHistoryApi(api_client)
    starts_with_query = 'Ada' # str | This param is used for starts-with search for first, last and display name of the identity (optional)
    is_deleted = true # bool | Indicates if we want to only list down deleted identities or not. (optional)
    is_active = true # bool | Indicates if we want to only list active or inactive identities. (optional)
    limit = 250 # int | Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 250)
    offset = 0 # int | Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 0)

    try:
        # Lists all the identities
        api_response = api_instance.list_historical_identities(starts_with_query=starts_with_query, is_deleted=is_deleted, is_active=is_active, limit=limit, offset=offset)
        print("The response of IdentityHistoryApi->list_historical_identities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityHistoryApi->list_historical_identities: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **starts_with_query** | **str**| This param is used for starts-with search for first, last and display name of the identity | [optional] 
 **is_deleted** | **bool**| Indicates if we want to only list down deleted identities or not. | [optional] 
 **is_active** | **bool**| Indicates if we want to only list active or inactive identities. | [optional] 
 **limit** | **int**| Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to 250]
 **offset** | **int**| Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to 0]

### Return type

[**List[IdentityListItem]**](IdentityListItem.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of identities for the customer. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_identity_access_items**
> List[ListIdentityAccessItems200ResponseInner] list_identity_access_items(id, type=type, filters=filters, sorters=sorters, query=query)

Gets a list of access items for the identity filtered by item type

This method retrieves a list of access item for the identity filtered by the access item type Requires authorization scope of 'idn:identity-history:read' 

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import sailpoint.beta
from sailpoint.beta.models.list_identity_access_items200_response_inner import ListIdentityAccessItems200ResponseInner
from sailpoint.beta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/beta
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.beta.Configuration(
    host = "https://sailpoint.api.identitynow.com/beta"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.beta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.beta.IdentityHistoryApi(api_client)
    id = '8c190e6787aa4ed9a90bd9d5344523fb' # str | The identity id
    type = 'account' # str | The type of access item for the identity. If not provided, it defaults to account.  Types of access items: **accessProfile, account, app, entitlement, role** (optional)
    filters = 'source eq \"DataScienceDataset\"' # str | Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **source**: *eq*  **standalone**: *eq*  **privileged**: *eq*  **attribute**: *eq*  **cloudGoverned**: *eq* (optional)
    sorters = 'name' # str | Sort results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#sorting-results)  Sorting is supported for the following fields: **name, value, standalone, privileged, attribute, source, cloudGoverned, removeDate, nativeIdentity, entitlementCount** (optional)
    query = 'Dr. Arden' # str | This param is used to search if certain fields of the access item contain the string provided.  Searching is supported for the following fields depending on the type:  Access Profiles: **name, description**  Accounts: **name, nativeIdentity**  Apps: **name**  Entitlements: **name, value, description**  Roles: **name, description** (optional)

    try:
        # Gets a list of access items for the identity filtered by item type
        api_response = api_instance.list_identity_access_items(id, type=type, filters=filters, sorters=sorters, query=query)
        print("The response of IdentityHistoryApi->list_identity_access_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityHistoryApi->list_identity_access_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The identity id | 
 **type** | **str**| The type of access item for the identity. If not provided, it defaults to account.  Types of access items: **accessProfile, account, app, entitlement, role** | [optional] 
 **filters** | **str**| Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **source**: *eq*  **standalone**: *eq*  **privileged**: *eq*  **attribute**: *eq*  **cloudGoverned**: *eq* | [optional] 
 **sorters** | **str**| Sort results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#sorting-results)  Sorting is supported for the following fields: **name, value, standalone, privileged, attribute, source, cloudGoverned, removeDate, nativeIdentity, entitlementCount** | [optional] 
 **query** | **str**| This param is used to search if certain fields of the access item contain the string provided.  Searching is supported for the following fields depending on the type:  Access Profiles: **name, description**  Accounts: **name, nativeIdentity**  Apps: **name**  Entitlements: **name, value, description**  Roles: **name, description** | [optional] 

### Return type

[**List[ListIdentityAccessItems200ResponseInner]**](ListIdentityAccessItems200ResponseInner.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of access items. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_identity_snapshot_access_items**
> List[ListIdentityAccessItems200ResponseInner] list_identity_snapshot_access_items(id, var_date, type=type)

Get Identity Access Items Snapshot

Use this API to get a list of identity access items at a specified date, filtered by item type.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import sailpoint.beta
from sailpoint.beta.models.list_identity_access_items200_response_inner import ListIdentityAccessItems200ResponseInner
from sailpoint.beta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/beta
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.beta.Configuration(
    host = "https://sailpoint.api.identitynow.com/beta"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.beta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.beta.IdentityHistoryApi(api_client)
    id = '8c190e6787aa4ed9a90bd9d5344523fb' # str | Identity ID.
    var_date = '2007-03-01T13:00:00Z' # str | Specified date.
    type = 'account' # str | Access item type. (optional)

    try:
        # Get Identity Access Items Snapshot
        api_response = api_instance.list_identity_snapshot_access_items(id, var_date, type=type)
        print("The response of IdentityHistoryApi->list_identity_snapshot_access_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityHistoryApi->list_identity_snapshot_access_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identity ID. | 
 **var_date** | **str**| Specified date. | 
 **type** | **str**| Access item type. | [optional] 

### Return type

[**List[ListIdentityAccessItems200ResponseInner]**](ListIdentityAccessItems200ResponseInner.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Identity object. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_identity_snapshots**
> List[IdentitySnapshotSummaryResponse] list_identity_snapshots(id, start=start, interval=interval, limit=limit, offset=offset, count=count)

Lists all the snapshots for the identity

This method retrieves all the snapshots for the identity Requires authorization scope of 'idn:identity-history:read' 

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import sailpoint.beta
from sailpoint.beta.models.identity_snapshot_summary_response import IdentitySnapshotSummaryResponse
from sailpoint.beta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/beta
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.beta.Configuration(
    host = "https://sailpoint.api.identitynow.com/beta"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.beta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.beta.IdentityHistoryApi(api_client)
    id = '8c190e6787aa4ed9a90bd9d5344523fb' # str | The identity id
    start = '2007-03-01T13:00:00Z' # str | The specified start date (optional)
    interval = 'interval_example' # str | The interval indicating the range in day or month for the specified interval-name (optional)
    limit = 250 # int | Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 250)
    offset = 0 # int | Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 0)
    count = False # bool | If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count=true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to False)

    try:
        # Lists all the snapshots for the identity
        api_response = api_instance.list_identity_snapshots(id, start=start, interval=interval, limit=limit, offset=offset, count=count)
        print("The response of IdentityHistoryApi->list_identity_snapshots:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityHistoryApi->list_identity_snapshots: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The identity id | 
 **start** | **str**| The specified start date | [optional] 
 **interval** | **str**| The interval indicating the range in day or month for the specified interval-name | [optional] 
 **limit** | **int**| Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to 250]
 **offset** | **int**| Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to 0]
 **count** | **bool**| If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count&#x3D;true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to False]

### Return type

[**List[IdentitySnapshotSummaryResponse]**](IdentitySnapshotSummaryResponse.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of identity summary for each snapshot. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

