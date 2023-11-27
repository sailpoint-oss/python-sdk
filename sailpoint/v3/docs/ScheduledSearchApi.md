# sailpoint.v3.ScheduledSearchApi

All URIs are relative to *https://sailpoint.api.identitynow.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_scheduled_search**](ScheduledSearchApi.md#create_scheduled_search) | **POST** /scheduled-searches | Create a new scheduled search
[**delete_scheduled_search**](ScheduledSearchApi.md#delete_scheduled_search) | **DELETE** /scheduled-searches/{id} | Delete a Scheduled Search
[**get_scheduled_search**](ScheduledSearchApi.md#get_scheduled_search) | **GET** /scheduled-searches/{id} | Get a Scheduled Search
[**list_scheduled_search**](ScheduledSearchApi.md#list_scheduled_search) | **GET** /scheduled-searches | List scheduled searches
[**unsubscribe_scheduled_search**](ScheduledSearchApi.md#unsubscribe_scheduled_search) | **POST** /scheduled-searches/{id}/unsubscribe | Unsubscribe a recipient from Scheduled Search
[**update_scheduled_search**](ScheduledSearchApi.md#update_scheduled_search) | **PUT** /scheduled-searches/{id} | Update an existing Scheduled Search


# **create_scheduled_search**
> ScheduledSearch create_scheduled_search(create_scheduled_search_request)

Create a new scheduled search

Creates a new scheduled search. 

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import sailpoint.v3
from sailpoint.v3.models.create_scheduled_search_request import CreateScheduledSearchRequest
from sailpoint.v3.models.scheduled_search import ScheduledSearch
from sailpoint.v3.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.v3.Configuration(
    host = "https://sailpoint.api.identitynow.com/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.v3.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.v3.ScheduledSearchApi(api_client)
    create_scheduled_search_request = {savedSearchId=9c620e13-cd33-4804-a13d-403bd7bcdbad, schedule={type=DAILY, hours={type=LIST, values=[9]}}, recipients=[{type=IDENTITY, id=2c9180867624cbd7017642d8c8c81f67}]} # CreateScheduledSearchRequest | The scheduled search to persist.

    try:
        # Create a new scheduled search
        api_response = api_instance.create_scheduled_search(create_scheduled_search_request)
        print("The response of ScheduledSearchApi->create_scheduled_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScheduledSearchApi->create_scheduled_search: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_scheduled_search_request** | [**CreateScheduledSearchRequest**](CreateScheduledSearchRequest.md)| The scheduled search to persist. | 

### Return type

[**ScheduledSearch**](ScheduledSearch.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The persisted scheduled search. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_scheduled_search**
> delete_scheduled_search(id)

Delete a Scheduled Search

Deletes the specified scheduled search. 

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import sailpoint.v3
from sailpoint.v3.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.v3.Configuration(
    host = "https://sailpoint.api.identitynow.com/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.v3.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.v3.ScheduledSearchApi(api_client)
    id = '2c91808568c529c60168cca6f90c1313' # str | ID of the requested document.

    try:
        # Delete a Scheduled Search
        api_instance.delete_scheduled_search(id)
    except Exception as e:
        print("Exception when calling ScheduledSearchApi->delete_scheduled_search: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the requested document. | 

### Return type

void (empty response body)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content - Indicates the request was successful but there is no content to be returned in the response. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_scheduled_search**
> ScheduledSearch get_scheduled_search(id)

Get a Scheduled Search

Returns the specified scheduled search.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import sailpoint.v3
from sailpoint.v3.models.scheduled_search import ScheduledSearch
from sailpoint.v3.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.v3.Configuration(
    host = "https://sailpoint.api.identitynow.com/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.v3.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.v3.ScheduledSearchApi(api_client)
    id = '2c91808568c529c60168cca6f90c1313' # str | ID of the requested document.

    try:
        # Get a Scheduled Search
        api_response = api_instance.get_scheduled_search(id)
        print("The response of ScheduledSearchApi->get_scheduled_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScheduledSearchApi->get_scheduled_search: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the requested document. | 

### Return type

[**ScheduledSearch**](ScheduledSearch.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested scheduled search. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_scheduled_search**
> List[ScheduledSearch] list_scheduled_search(offset=offset, limit=limit, count=count, filters=filters)

List scheduled searches

Returns a list of scheduled searches. 

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import sailpoint.v3
from sailpoint.v3.models.scheduled_search import ScheduledSearch
from sailpoint.v3.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.v3.Configuration(
    host = "https://sailpoint.api.identitynow.com/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.v3.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.v3.ScheduledSearchApi(api_client)
    offset = 0 # int | Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 0)
    limit = 250 # int | Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 250)
    count = False # bool | If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count=true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to False)
    filters = 'savedSearchId eq \"6cc0945d-9eeb-4948-9033-72d066e1153e\"' # str | Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **owner.id**: *eq*  **savedSearchId**: *eq* (optional)

    try:
        # List scheduled searches
        api_response = api_instance.list_scheduled_search(offset=offset, limit=limit, count=count, filters=filters)
        print("The response of ScheduledSearchApi->list_scheduled_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScheduledSearchApi->list_scheduled_search: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to 0]
 **limit** | **int**| Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to 250]
 **count** | **bool**| If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count&#x3D;true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to False]
 **filters** | **str**| Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **owner.id**: *eq*  **savedSearchId**: *eq* | [optional] 

### Return type

[**List[ScheduledSearch]**](ScheduledSearch.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of requested scheduled searches. |  * X-Total-Count - The total result count (returned only if the *count* parameter is specified as *true*). <br>  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unsubscribe_scheduled_search**
> unsubscribe_scheduled_search(id, typed_reference)

Unsubscribe a recipient from Scheduled Search

Unsubscribes a recipient from the specified scheduled search. 

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import sailpoint.v3
from sailpoint.v3.models.typed_reference import TypedReference
from sailpoint.v3.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.v3.Configuration(
    host = "https://sailpoint.api.identitynow.com/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.v3.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.v3.ScheduledSearchApi(api_client)
    id = '2c91808568c529c60168cca6f90c1313' # str | ID of the requested document.
    typed_reference = sailpoint.v3.TypedReference() # TypedReference | The recipient to be removed from the scheduled search. 

    try:
        # Unsubscribe a recipient from Scheduled Search
        api_instance.unsubscribe_scheduled_search(id, typed_reference)
    except Exception as e:
        print("Exception when calling ScheduledSearchApi->unsubscribe_scheduled_search: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the requested document. | 
 **typed_reference** | [**TypedReference**](TypedReference.md)| The recipient to be removed from the scheduled search.  | 

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
**204** | No Content - Indicates the request was successful but there is no content to be returned in the response. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_scheduled_search**
> ScheduledSearch update_scheduled_search(id, scheduled_search)

Update an existing Scheduled Search

Updates an existing scheduled search. 

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import sailpoint.v3
from sailpoint.v3.models.scheduled_search import ScheduledSearch
from sailpoint.v3.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.v3.Configuration(
    host = "https://sailpoint.api.identitynow.com/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.v3.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.v3.ScheduledSearchApi(api_client)
    id = '2c91808568c529c60168cca6f90c1313' # str | ID of the requested document.
    scheduled_search = sailpoint.v3.ScheduledSearch() # ScheduledSearch | The scheduled search to persist.

    try:
        # Update an existing Scheduled Search
        api_response = api_instance.update_scheduled_search(id, scheduled_search)
        print("The response of ScheduledSearchApi->update_scheduled_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScheduledSearchApi->update_scheduled_search: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the requested document. | 
 **scheduled_search** | [**ScheduledSearch**](ScheduledSearch.md)| The scheduled search to persist. | 

### Return type

[**ScheduledSearch**](ScheduledSearch.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The persisted scheduled search. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

