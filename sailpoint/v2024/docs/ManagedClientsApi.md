# sailpoint.v2024.ManagedClientsApi

All URIs are relative to *https://sailpoint.api.identitynow.com/v2024*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_managed_client**](ManagedClientsApi.md#create_managed_client) | **POST** /managed-clients | Create a new Managed Client
[**delete_managed_client**](ManagedClientsApi.md#delete_managed_client) | **DELETE** /managed-clients/{id} | Delete a Managed Client
[**get_managed_client**](ManagedClientsApi.md#get_managed_client) | **GET** /managed-clients/{id} | Get a Managed Client
[**get_managed_client_status**](ManagedClientsApi.md#get_managed_client_status) | **GET** /managed-clients/{id}/status | Get Managed Client Status.
[**get_managed_clients**](ManagedClientsApi.md#get_managed_clients) | **GET** /managed-clients | Get Managed Clients
[**update_managed_client**](ManagedClientsApi.md#update_managed_client) | **PATCH** /managed-clients/{id} | Update a Managed Client


# **create_managed_client**
> ManagedClient create_managed_client(managed_client_request)

Create a new Managed Client

Create a new Managed Client. The API returns a result that includes the Managed Client ID.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.v2024
from sailpoint.v2024.models.managed_client import ManagedClient
from sailpoint.v2024.models.managed_client_request import ManagedClientRequest
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
    api_instance = sailpoint.v2024.ManagedClientsApi(api_client)
    managed_client_request = sailpoint.v2024.ManagedClientRequest() # ManagedClientRequest | 

    try:
        # Create a new Managed Client
        api_response = api_instance.create_managed_client(managed_client_request)
        print("The response of ManagedClientsApi->create_managed_client:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagedClientsApi->create_managed_client: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **managed_client_request** | [**ManagedClientRequest**](ManagedClientRequest.md)|  | 

### Return type

[**ManagedClient**](ManagedClient.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The created ManagedClient |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_managed_client**
> delete_managed_client(id)

Delete a Managed Client

Delete an existing Managed Client.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.v2024
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
    api_instance = sailpoint.v2024.ManagedClientsApi(api_client)
    id = '4440278c-0ce2-41ee-a0a9-f5cfd5e8d3b7' # str | Managed Client ID.

    try:
        # Delete a Managed Client
        api_instance.delete_managed_client(id)
    except Exception as e:
        print("Exception when calling ManagedClientsApi->delete_managed_client: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Managed Client ID. | 

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
**204** | No content - indicates the request was successful but there is no content to be returned in the response. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_managed_client**
> ManagedClient get_managed_client(id)

Get a Managed Client

Get a Managed Client.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.v2024
from sailpoint.v2024.models.managed_client import ManagedClient
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
    api_instance = sailpoint.v2024.ManagedClientsApi(api_client)
    id = '4440278c-0ce2-41ee-a0a9-f5cfd5e8d3b7' # str | Managed Client ID.

    try:
        # Get a Managed Client
        api_response = api_instance.get_managed_client(id)
        print("The response of ManagedClientsApi->get_managed_client:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagedClientsApi->get_managed_client: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Managed Client ID. | 

### Return type

[**ManagedClient**](ManagedClient.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Responds with a Managed Client |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_managed_client_status**
> ManagedClientStatus get_managed_client_status(id, type)

Get Managed Client Status.

Retrieve the Status of a Managed Client by ID.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.v2024
from sailpoint.v2024.models.managed_client_status import ManagedClientStatus
from sailpoint.v2024.models.managed_client_type import ManagedClientType
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
    api_instance = sailpoint.v2024.ManagedClientsApi(api_client)
    id = 'aClientId' # str | ID of the Managed Client to get Status of
    type = sailpoint.v2024.ManagedClientType() # ManagedClientType | Type of the Managed Client to get Status of

    try:
        # Get Managed Client Status.
        api_response = api_instance.get_managed_client_status(id, type)
        print("The response of ManagedClientsApi->get_managed_client_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagedClientsApi->get_managed_client_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the Managed Client to get Status of | 
 **type** | [**ManagedClientType**](.md)| Type of the Managed Client to get Status of | 

### Return type

[**ManagedClientStatus**](ManagedClientStatus.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Responds with the Status of the Managed Client with the given ID and Type. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_managed_clients**
> List[ManagedClient] get_managed_clients(offset=offset, limit=limit, count=count, filters=filters)

Get Managed Clients

Get a list of Managed Clients.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.v2024
from sailpoint.v2024.models.managed_client import ManagedClient
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
    api_instance = sailpoint.v2024.ManagedClientsApi(api_client)
    offset = 0 # int | Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 0)
    limit = 250 # int | Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 250)
    count = False # bool | If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count=true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to False)
    filters = 'name eq \"client name\"' # str | Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **id**: *eq*  **name**: *eq*  **clientId**: *eq*  **clusterId**: *eq* (optional)

    try:
        # Get Managed Clients
        api_response = api_instance.get_managed_clients(offset=offset, limit=limit, count=count, filters=filters)
        print("The response of ManagedClientsApi->get_managed_clients:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagedClientsApi->get_managed_clients: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to 0]
 **limit** | **int**| Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to 250]
 **count** | **bool**| If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count&#x3D;true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to False]
 **filters** | **str**| Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **id**: *eq*  **name**: *eq*  **clientId**: *eq*  **clusterId**: *eq* | [optional] 

### Return type

[**List[ManagedClient]**](ManagedClient.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Responds with a list of ManagedClient based on the query params provided |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_managed_client**
> ManagedClient update_managed_client(id, json_patch_operation)

Update a Managed Client

Update an existing Managed Client.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.v2024
from sailpoint.v2024.models.json_patch_operation import JsonPatchOperation
from sailpoint.v2024.models.managed_client import ManagedClient
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
    api_instance = sailpoint.v2024.ManagedClientsApi(api_client)
    id = '4440278c-0ce2-41ee-a0a9-f5cfd5e8d3b7' # str | Managed Client ID.
    json_patch_operation = [sailpoint.v2024.JsonPatchOperation()] # List[JsonPatchOperation] | The JSONPatch payload used to update the object.

    try:
        # Update a Managed Client
        api_response = api_instance.update_managed_client(id, json_patch_operation)
        print("The response of ManagedClientsApi->update_managed_client:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagedClientsApi->update_managed_client: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Managed Client ID. | 
 **json_patch_operation** | [**List[JsonPatchOperation]**](JsonPatchOperation.md)| The JSONPatch payload used to update the object. | 

### Return type

[**ManagedClient**](ManagedClient.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated Managed Client |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

