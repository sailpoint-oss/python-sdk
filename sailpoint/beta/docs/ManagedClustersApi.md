# beta.ManagedClustersApi

All URIs are relative to *https://sailpoint.api.identitynow.com/beta*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_client_log_configuration**](ManagedClustersApi.md#get_client_log_configuration) | **GET** /managed-clusters/{id}/log-config | Get managed cluster&#39;s log configuration
[**get_managed_cluster**](ManagedClustersApi.md#get_managed_cluster) | **GET** /managed-clusters/{id} | Get a specified ManagedCluster.
[**get_managed_clusters**](ManagedClustersApi.md#get_managed_clusters) | **GET** /managed-clusters | Retrieve all Managed Clusters.
[**put_client_log_configuration**](ManagedClustersApi.md#put_client_log_configuration) | **PUT** /managed-clusters/{id}/log-config | Update managed cluster&#39;s log configuration


# **get_client_log_configuration**
> ClientLogConfiguration get_client_log_configuration(id)

Get managed cluster's log configuration

Get managed cluster's log configuration.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import beta
from beta.models.client_log_configuration import ClientLogConfiguration
from beta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/beta
# See configuration.py for a list of all supported configuration parameters.
configuration = beta.Configuration(
    host = "https://sailpoint.api.identitynow.com/beta"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with beta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = beta.ManagedClustersApi(api_client)
    id = 'aClusterId' # str | ID of ManagedCluster to get log configuration for

    try:
        # Get managed cluster's log configuration
        api_response = api_instance.get_client_log_configuration(id)
        print("The response of ManagedClustersApi->get_client_log_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagedClustersApi->get_client_log_configuration: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of ManagedCluster to get log configuration for | 

### Return type

[**ClientLogConfiguration**](ClientLogConfiguration.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Log configuration of ManagedCluster matching given cluster ID |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_managed_cluster**
> ManagedCluster get_managed_cluster(id)

Get a specified ManagedCluster.

Retrieve a ManagedCluster by ID.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import beta
from beta.models.managed_cluster import ManagedCluster
from beta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/beta
# See configuration.py for a list of all supported configuration parameters.
configuration = beta.Configuration(
    host = "https://sailpoint.api.identitynow.com/beta"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with beta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = beta.ManagedClustersApi(api_client)
    id = 'aClusterId' # str | ID of the ManagedCluster to get

    try:
        # Get a specified ManagedCluster.
        api_response = api_instance.get_managed_cluster(id)
        print("The response of ManagedClustersApi->get_managed_cluster:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagedClustersApi->get_managed_cluster: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the ManagedCluster to get | 

### Return type

[**ManagedCluster**](ManagedCluster.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Responds with ManagedCluster having the given ID. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_managed_clusters**
> List[ManagedCluster] get_managed_clusters(offset=offset, limit=limit, count=count, filters=filters)

Retrieve all Managed Clusters.

Retrieve all Managed Clusters for the current Org, based on request context.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import beta
from beta.models.managed_cluster import ManagedCluster
from beta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/beta
# See configuration.py for a list of all supported configuration parameters.
configuration = beta.Configuration(
    host = "https://sailpoint.api.identitynow.com/beta"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with beta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = beta.ManagedClustersApi(api_client)
    offset = 0 # int | Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 0)
    limit = 250 # int | Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 250)
    count = False # bool | If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count=true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to False)
    filters = 'operational eq operation' # str | Filtering is supported for the following fields and operators:  **operational**: *eq* (optional)

    try:
        # Retrieve all Managed Clusters.
        api_response = api_instance.get_managed_clusters(offset=offset, limit=limit, count=count, filters=filters)
        print("The response of ManagedClustersApi->get_managed_clusters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagedClustersApi->get_managed_clusters: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to 0]
 **limit** | **int**| Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to 250]
 **count** | **bool**| If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count&#x3D;true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to False]
 **filters** | **str**| Filtering is supported for the following fields and operators:  **operational**: *eq* | [optional] 

### Return type

[**List[ManagedCluster]**](ManagedCluster.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Responds with a list of ManagedCluster. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_client_log_configuration**
> ClientLogConfiguration put_client_log_configuration(id, client_log_configuration)

Update managed cluster's log configuration

Update managed cluster's log configuration

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import beta
from beta.models.client_log_configuration import ClientLogConfiguration
from beta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/beta
# See configuration.py for a list of all supported configuration parameters.
configuration = beta.Configuration(
    host = "https://sailpoint.api.identitynow.com/beta"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with beta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = beta.ManagedClustersApi(api_client)
    id = 'aClusterId' # str | ID of ManagedCluster to update log configuration for
    client_log_configuration = beta.ClientLogConfiguration() # ClientLogConfiguration | ClientLogConfiguration for given ManagedCluster

    try:
        # Update managed cluster's log configuration
        api_response = api_instance.put_client_log_configuration(id, client_log_configuration)
        print("The response of ManagedClustersApi->put_client_log_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagedClustersApi->put_client_log_configuration: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of ManagedCluster to update log configuration for | 
 **client_log_configuration** | [**ClientLogConfiguration**](ClientLogConfiguration.md)| ClientLogConfiguration for given ManagedCluster | 

### Return type

[**ClientLogConfiguration**](ClientLogConfiguration.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Responds with updated ClientLogConfiguration for given ManagedCluster |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

