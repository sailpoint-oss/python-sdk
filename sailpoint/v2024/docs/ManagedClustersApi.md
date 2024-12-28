# sailpoint.v2024.ManagedClustersApi

All URIs are relative to *https://sailpoint.api.identitynow.com/v2024*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_managed_cluster**](ManagedClustersApi.md#create_managed_cluster) | **POST** /managed-clusters | Create Create Managed Cluster
[**delete_managed_cluster**](ManagedClustersApi.md#delete_managed_cluster) | **DELETE** /managed-clusters/{id} | Delete Managed Cluster
[**get_client_log_configuration**](ManagedClustersApi.md#get_client_log_configuration) | **GET** /managed-clusters/{id}/log-config | Get Managed Cluster Log Configuration
[**get_managed_cluster**](ManagedClustersApi.md#get_managed_cluster) | **GET** /managed-clusters/{id} | Get Managed Cluster
[**get_managed_clusters**](ManagedClustersApi.md#get_managed_clusters) | **GET** /managed-clusters | Get Managed Clusters
[**put_client_log_configuration**](ManagedClustersApi.md#put_client_log_configuration) | **PUT** /managed-clusters/{id}/log-config | Update Managed Cluster Log Configuration
[**update_managed_cluster**](ManagedClustersApi.md#update_managed_cluster) | **PATCH** /managed-clusters/{id} | Update Managed Cluster


# **create_managed_cluster**
> ManagedCluster create_managed_cluster(managed_cluster_request)

Create Create Managed Cluster

Create a new Managed Cluster. The API returns a result that includes the managed cluster ID.

### Example

* OAuth Authentication (userAuth):
* OAuth Authentication (userAuth):

```python
import sailpoint.v2024
from sailpoint.v2024.models.managed_cluster import ManagedCluster
from sailpoint.v2024.models.managed_cluster_request import ManagedClusterRequest
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
    api_instance = sailpoint.v2024.ManagedClustersApi(api_client)
    managed_cluster_request = sailpoint.v2024.ManagedClusterRequest() # ManagedClusterRequest | 

    try:
        # Create Create Managed Cluster
        api_response = api_instance.create_managed_cluster(managed_cluster_request)
        print("The response of ManagedClustersApi->create_managed_cluster:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagedClustersApi->create_managed_cluster: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **managed_cluster_request** | [**ManagedClusterRequest**](ManagedClusterRequest.md)|  | 

### Return type

[**ManagedCluster**](ManagedCluster.md)

### Authorization

[userAuth](../README.md#userAuth), [userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Created managed cluster. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_managed_cluster**
> delete_managed_cluster(id, remove_clients=remove_clients)

Delete Managed Cluster

Delete an existing managed cluster.

### Example

* OAuth Authentication (userAuth):
* OAuth Authentication (userAuth):

```python
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
    api_instance = sailpoint.v2024.ManagedClustersApi(api_client)
    id = '2c9180897de347a2017de8859e8c5039' # str | Managed cluster ID.
    remove_clients = False # bool | Flag to determine the need to delete a cluster with clients. (optional) (default to False)

    try:
        # Delete Managed Cluster
        api_instance.delete_managed_cluster(id, remove_clients=remove_clients)
    except Exception as e:
        print("Exception when calling ManagedClustersApi->delete_managed_cluster: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Managed cluster ID. | 
 **remove_clients** | **bool**| Flag to determine the need to delete a cluster with clients. | [optional] [default to False]

### Return type

void (empty response body)

### Authorization

[userAuth](../README.md#userAuth), [userAuth](../README.md#userAuth)

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

# **get_client_log_configuration**
> ClientLogConfiguration get_client_log_configuration(id)

Get Managed Cluster Log Configuration

Get a managed cluster's log configuration.

### Example

* OAuth Authentication (userAuth):
* OAuth Authentication (userAuth):

```python
import sailpoint.v2024
from sailpoint.v2024.models.client_log_configuration import ClientLogConfiguration
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
    api_instance = sailpoint.v2024.ManagedClustersApi(api_client)
    id = '2b838de9-db9b-abcf-e646-d4f274ad4238' # str | ID of managed cluster to get log configuration for.

    try:
        # Get Managed Cluster Log Configuration
        api_response = api_instance.get_client_log_configuration(id)
        print("The response of ManagedClustersApi->get_client_log_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagedClustersApi->get_client_log_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of managed cluster to get log configuration for. | 

### Return type

[**ClientLogConfiguration**](ClientLogConfiguration.md)

### Authorization

[userAuth](../README.md#userAuth), [userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Log configuration of managed cluster for given cluster ID. |  -  |
**204** | No content - indicates the request was successful but there is no content to be returned in the response. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_managed_cluster**
> ManagedCluster get_managed_cluster(id)

Get Managed Cluster

Get a managed cluster by ID.

### Example

* OAuth Authentication (userAuth):
* OAuth Authentication (userAuth):

```python
import sailpoint.v2024
from sailpoint.v2024.models.managed_cluster import ManagedCluster
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
    api_instance = sailpoint.v2024.ManagedClustersApi(api_client)
    id = '2c9180897de347a2017de8859e8c5039' # str | Managed cluster ID.

    try:
        # Get Managed Cluster
        api_response = api_instance.get_managed_cluster(id)
        print("The response of ManagedClustersApi->get_managed_cluster:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagedClustersApi->get_managed_cluster: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Managed cluster ID. | 

### Return type

[**ManagedCluster**](ManagedCluster.md)

### Authorization

[userAuth](../README.md#userAuth), [userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response with managed cluster for the given ID. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_managed_clusters**
> List[ManagedCluster] get_managed_clusters(offset=offset, limit=limit, count=count, filters=filters)

Get Managed Clusters

List current organization's managed clusters, based on request context.

### Example

* OAuth Authentication (userAuth):
* OAuth Authentication (userAuth):

```python
import sailpoint.v2024
from sailpoint.v2024.models.managed_cluster import ManagedCluster
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
    api_instance = sailpoint.v2024.ManagedClustersApi(api_client)
    offset = 0 # int | Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 0)
    limit = 250 # int | Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 250)
    count = False # bool | If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count=true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to False)
    filters = 'operational eq \"operation\"' # str | Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **operational**: *eq* (optional)

    try:
        # Get Managed Clusters
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
 **filters** | **str**| Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **operational**: *eq* | [optional] 

### Return type

[**List[ManagedCluster]**](ManagedCluster.md)

### Authorization

[userAuth](../README.md#userAuth), [userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response with a list of managed clusters. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_client_log_configuration**
> ClientLogConfiguration put_client_log_configuration(id, put_client_log_configuration_request)

Update Managed Cluster Log Configuration

Update a managed cluster's log configuration. You may only specify one of `durationMinutes` or `expiration`, up to 1440 minutes (24 hours) in the future. If neither is specified, the default value for `durationMinutes` is 240.

### Example

* OAuth Authentication (userAuth):
* OAuth Authentication (userAuth):

```python
import sailpoint.v2024
from sailpoint.v2024.models.client_log_configuration import ClientLogConfiguration
from sailpoint.v2024.models.put_client_log_configuration_request import PutClientLogConfigurationRequest
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
    api_instance = sailpoint.v2024.ManagedClustersApi(api_client)
    id = '2b838de9-db9b-abcf-e646-d4f274ad4238' # str | ID of the managed cluster to update the log configuration for.
    put_client_log_configuration_request = sailpoint.v2024.PutClientLogConfigurationRequest() # PutClientLogConfigurationRequest | Client log configuration for the given managed cluster.

    try:
        # Update Managed Cluster Log Configuration
        api_response = api_instance.put_client_log_configuration(id, put_client_log_configuration_request)
        print("The response of ManagedClustersApi->put_client_log_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagedClustersApi->put_client_log_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the managed cluster to update the log configuration for. | 
 **put_client_log_configuration_request** | [**PutClientLogConfigurationRequest**](PutClientLogConfigurationRequest.md)| Client log configuration for the given managed cluster. | 

### Return type

[**ClientLogConfiguration**](ClientLogConfiguration.md)

### Authorization

[userAuth](../README.md#userAuth), [userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response with updated client log configuration for the given managed cluster. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_managed_cluster**
> ManagedCluster update_managed_cluster(id, json_patch_operation)

Update Managed Cluster

Update an existing managed cluster.

### Example

* OAuth Authentication (userAuth):
* OAuth Authentication (userAuth):

```python
import sailpoint.v2024
from sailpoint.v2024.models.json_patch_operation import JsonPatchOperation
from sailpoint.v2024.models.managed_cluster import ManagedCluster
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
    api_instance = sailpoint.v2024.ManagedClustersApi(api_client)
    id = '2c9180897de347a2017de8859e8c5039' # str | Managed cluster ID.
    json_patch_operation = [sailpoint.v2024.JsonPatchOperation()] # List[JsonPatchOperation] | JSONPatch payload used to update the object.

    try:
        # Update Managed Cluster
        api_response = api_instance.update_managed_cluster(id, json_patch_operation)
        print("The response of ManagedClustersApi->update_managed_cluster:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagedClustersApi->update_managed_cluster: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Managed cluster ID. | 
 **json_patch_operation** | [**List[JsonPatchOperation]**](JsonPatchOperation.md)| JSONPatch payload used to update the object. | 

### Return type

[**ManagedCluster**](ManagedCluster.md)

### Authorization

[userAuth](../README.md#userAuth), [userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated managed cluster. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

