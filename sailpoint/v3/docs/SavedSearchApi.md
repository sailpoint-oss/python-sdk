# sailpoint.v3.SavedSearchApi

All URIs are relative to *https://sailpoint.api.identitynow.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_saved_search**](SavedSearchApi.md#create_saved_search) | **POST** /saved-searches | Create a saved search
[**delete_saved_search**](SavedSearchApi.md#delete_saved_search) | **DELETE** /saved-searches/{id} | Delete document by ID
[**execute_saved_search**](SavedSearchApi.md#execute_saved_search) | **POST** /saved-searches/{id}/execute | Execute a saved search by ID
[**get_saved_search**](SavedSearchApi.md#get_saved_search) | **GET** /saved-searches/{id} | Return saved search by ID
[**list_saved_searches**](SavedSearchApi.md#list_saved_searches) | **GET** /saved-searches | A list of Saved Searches
[**put_saved_search**](SavedSearchApi.md#put_saved_search) | **PUT** /saved-searches/{id} | Updates an existing saved search 


# **create_saved_search**
> SavedSearch create_saved_search(create_saved_search_request)

Create a saved search

Creates a new saved search. 

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.v3
from sailpoint.v3.models.create_saved_search_request import CreateSavedSearchRequest
from sailpoint.v3.models.saved_search import SavedSearch
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
    api_instance = sailpoint.v3.SavedSearchApi(api_client)
    create_saved_search_request = sailpoint.v3.CreateSavedSearchRequest() # CreateSavedSearchRequest | The saved search to persist.

    try:
        # Create a saved search
        api_response = api_instance.create_saved_search(create_saved_search_request)
        print("The response of SavedSearchApi->create_saved_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SavedSearchApi->create_saved_search: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_saved_search_request** | [**CreateSavedSearchRequest**](CreateSavedSearchRequest.md)| The saved search to persist. | 

### Return type

[**SavedSearch**](SavedSearch.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The persisted saved search. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_saved_search**
> delete_saved_search(id)

Delete document by ID

Deletes the specified saved search. 

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
    api_instance = sailpoint.v3.SavedSearchApi(api_client)
    id = '2c91808568c529c60168cca6f90c1313' # str | ID of the requested document.

    try:
        # Delete document by ID
        api_instance.delete_saved_search(id)
    except Exception as e:
        print("Exception when calling SavedSearchApi->delete_saved_search: %s\n" % e)
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

# **execute_saved_search**
> execute_saved_search(id, search_arguments)

Execute a saved search by ID

Executes the specified saved search. 

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.v3
from sailpoint.v3.models.search_arguments import SearchArguments
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
    api_instance = sailpoint.v3.SavedSearchApi(api_client)
    id = '2c91808568c529c60168cca6f90c1313' # str | ID of the requested document.
    search_arguments = sailpoint.v3.SearchArguments() # SearchArguments | When saved search execution is triggered by a scheduled search, *scheduleId* will specify the ID of the triggering scheduled search.  If *scheduleId* is not specified (when execution is triggered by a UI test), the *owner* and *recipients* arguments must be provided. 

    try:
        # Execute a saved search by ID
        api_instance.execute_saved_search(id, search_arguments)
    except Exception as e:
        print("Exception when calling SavedSearchApi->execute_saved_search: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the requested document. | 
 **search_arguments** | [**SearchArguments**](SearchArguments.md)| When saved search execution is triggered by a scheduled search, *scheduleId* will specify the ID of the triggering scheduled search.  If *scheduleId* is not specified (when execution is triggered by a UI test), the *owner* and *recipients* arguments must be provided.  | 

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
**202** | Accepted - Returned if the request was successfully accepted into the system. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_saved_search**
> SavedSearch get_saved_search(id)

Return saved search by ID

Returns the specified saved search. 

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.v3
from sailpoint.v3.models.saved_search import SavedSearch
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
    api_instance = sailpoint.v3.SavedSearchApi(api_client)
    id = '2c91808568c529c60168cca6f90c1313' # str | ID of the requested document.

    try:
        # Return saved search by ID
        api_response = api_instance.get_saved_search(id)
        print("The response of SavedSearchApi->get_saved_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SavedSearchApi->get_saved_search: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the requested document. | 

### Return type

[**SavedSearch**](SavedSearch.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested saved search. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_saved_searches**
> List[SavedSearch] list_saved_searches(offset=offset, limit=limit, count=count, filters=filters)

A list of Saved Searches

Returns a list of saved searches. 

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.v3
from sailpoint.v3.models.saved_search import SavedSearch
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
    api_instance = sailpoint.v3.SavedSearchApi(api_client)
    offset = 0 # int | Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 0)
    limit = 250 # int | Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 250)
    count = False # bool | If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count=true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to False)
    filters = 'owner.id eq \"7a724640-0c17-4ce9-a8c3-4a89738459c8\"' # str | Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **owner.id**: *eq* (optional)

    try:
        # A list of Saved Searches
        api_response = api_instance.list_saved_searches(offset=offset, limit=limit, count=count, filters=filters)
        print("The response of SavedSearchApi->list_saved_searches:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SavedSearchApi->list_saved_searches: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to 0]
 **limit** | **int**| Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to 250]
 **count** | **bool**| If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count&#x3D;true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to False]
 **filters** | **str**| Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **owner.id**: *eq* | [optional] 

### Return type

[**List[SavedSearch]**](SavedSearch.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of requested saved searches. |  * X-Total-Count - The total result count (returned only if the *count* parameter is specified as *true*). <br>  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_saved_search**
> SavedSearch put_saved_search(id, saved_search)

Updates an existing saved search 

Updates an existing saved search.   >**NOTE: You cannot update the `owner` of the saved search.** 

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.v3
from sailpoint.v3.models.saved_search import SavedSearch
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
    api_instance = sailpoint.v3.SavedSearchApi(api_client)
    id = '2c91808568c529c60168cca6f90c1313' # str | ID of the requested document.
    saved_search = sailpoint.v3.SavedSearch() # SavedSearch | The saved search to persist.

    try:
        # Updates an existing saved search 
        api_response = api_instance.put_saved_search(id, saved_search)
        print("The response of SavedSearchApi->put_saved_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SavedSearchApi->put_saved_search: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the requested document. | 
 **saved_search** | [**SavedSearch**](SavedSearch.md)| The saved search to persist. | 

### Return type

[**SavedSearch**](SavedSearch.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The persisted saved search. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

