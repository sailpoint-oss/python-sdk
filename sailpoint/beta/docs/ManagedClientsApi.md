# sailpoint.beta.ManagedClientsApi

All URIs are relative to *https://sailpoint.api.identitynow.com/beta*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_managed_client_status**](ManagedClientsApi.md#get_managed_client_status) | **GET** /managed-clients/{id}/status | Specified Managed Client Status.
[**update_managed_client_status**](ManagedClientsApi.md#update_managed_client_status) | **POST** /managed-clients/{id}/status | Handle status request from client


# **get_managed_client_status**
> ManagedClientStatus get_managed_client_status(id, type)

Specified Managed Client Status.

Retrieve Managed Client Status by ID.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import sailpoint.beta
from sailpoint.beta.models.managed_client_status import ManagedClientStatus
from sailpoint.beta.models.managed_client_type import ManagedClientType
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
    api_instance = sailpoint.beta.ManagedClientsApi(api_client)
    id = 'aClientId' # str | ID of the Managed Client Status to get
    type = sailpoint.beta.ManagedClientType() # ManagedClientType | Type of the Managed Client Status to get

    try:
        # Specified Managed Client Status.
        api_response = api_instance.get_managed_client_status(id, type)
        print("The response of ManagedClientsApi->get_managed_client_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagedClientsApi->get_managed_client_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the Managed Client Status to get | 
 **type** | [**ManagedClientType**](.md)| Type of the Managed Client Status to get | 

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
**200** | Responds with Managed Client Status having the given ID and Type. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_managed_client_status**
> ManagedClientStatusAggResponse update_managed_client_status(id, managed_client_status)

Handle status request from client

Update a status detail passed in from the client

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import sailpoint.beta
from sailpoint.beta.models.managed_client_status import ManagedClientStatus
from sailpoint.beta.models.managed_client_status_agg_response import ManagedClientStatusAggResponse
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
    api_instance = sailpoint.beta.ManagedClientsApi(api_client)
    id = 'aClientId' # str | ID of the Managed Client Status to update
    managed_client_status = sailpoint.beta.ManagedClientStatus() # ManagedClientStatus | 

    try:
        # Handle status request from client
        api_response = api_instance.update_managed_client_status(id, managed_client_status)
        print("The response of ManagedClientsApi->update_managed_client_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagedClientsApi->update_managed_client_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the Managed Client Status to update | 
 **managed_client_status** | [**ManagedClientStatus**](ManagedClientStatus.md)|  | 

### Return type

[**ManagedClientStatusAggResponse**](ManagedClientStatusAggResponse.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Responds with the updated Managed Client Status. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

