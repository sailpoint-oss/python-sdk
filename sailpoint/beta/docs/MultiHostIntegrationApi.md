# sailpoint.beta.MultiHostIntegrationApi

All URIs are relative to *https://sailpoint.api.identitynow.com/beta*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_multi_host_integration**](MultiHostIntegrationApi.md#create_multi_host_integration) | **POST** /multihosts | Create Multi-Host Integration
[**create_sources_within_multi_host**](MultiHostIntegrationApi.md#create_sources_within_multi_host) | **POST** /multihosts/{id} | Create Sources Within Multi-Host Integration
[**delete_multi_host**](MultiHostIntegrationApi.md#delete_multi_host) | **DELETE** /multihosts/{id} | Delete Multi-Host Integration
[**get_acct_aggregation_groups**](MultiHostIntegrationApi.md#get_acct_aggregation_groups) | **GET** /multihosts/{multihostId}/acctAggregationGroups | Get Account Aggregation Groups Within Multi-Host Integration ID
[**get_entitlement_aggregation_groups**](MultiHostIntegrationApi.md#get_entitlement_aggregation_groups) | **GET** /multihosts/{multiHostId}/entitlementAggregationGroups | Get Entitlement Aggregation Groups Within Multi-Host Integration ID
[**get_multi_host_integrations**](MultiHostIntegrationApi.md#get_multi_host_integrations) | **GET** /multihosts/{id} | Get Multi-Host Integration By ID
[**get_multi_host_integrations_list**](MultiHostIntegrationApi.md#get_multi_host_integrations_list) | **GET** /multihosts | List All Existing Multi-Host Integrations
[**get_multi_host_source_creation_errors**](MultiHostIntegrationApi.md#get_multi_host_source_creation_errors) | **GET** /multihosts/{multiHostId}/sources/errors | List Multi-Host Source Creation Errors
[**get_multihost_integration_types**](MultiHostIntegrationApi.md#get_multihost_integration_types) | **GET** /multihosts/types | List Multi-Host Integration Types
[**get_sources_within_multi_host**](MultiHostIntegrationApi.md#get_sources_within_multi_host) | **GET** /multihosts/{id}/sources | List Sources Within Multi-Host Integration
[**test_connection_multi_host_sources**](MultiHostIntegrationApi.md#test_connection_multi_host_sources) | **POST** /multihosts/{multihost_id}/sources/testConnection | Test Configuration For Multi-Host Integration
[**test_source_connection_multihost**](MultiHostIntegrationApi.md#test_source_connection_multihost) | **GET** /multihosts/{multihost_id}/sources/{sourceId}/testConnection | Test Configuration For Multi-Host Integration&#39;s Single Source
[**update_multi_host_sources**](MultiHostIntegrationApi.md#update_multi_host_sources) | **PATCH** /multihosts/{id} | Update Multi-Host Integration


# **create_multi_host_integration**
> MultiHostIntegrations create_multi_host_integration(multi_host_integrations_create)

Create Multi-Host Integration

This API is used to create Multi-Host Integration. Multi-host Integration holds similar types of sources.  A token with Org Admin or Multi-Host Admin authority is required to access this endpoint.

### Example

* OAuth Authentication (userAuth):
* OAuth Authentication (userAuth):

```python
import sailpoint.beta
from sailpoint.beta.models.multi_host_integrations import MultiHostIntegrations
from sailpoint.beta.models.multi_host_integrations_create import MultiHostIntegrationsCreate
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
    api_instance = sailpoint.beta.MultiHostIntegrationApi(api_client)
    multi_host_integrations_create = sailpoint.beta.MultiHostIntegrationsCreate() # MultiHostIntegrationsCreate | The specifics of the Multi-Host Integration to create

    try:
        # Create Multi-Host Integration
        api_response = api_instance.create_multi_host_integration(multi_host_integrations_create)
        print("The response of MultiHostIntegrationApi->create_multi_host_integration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MultiHostIntegrationApi->create_multi_host_integration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **multi_host_integrations_create** | [**MultiHostIntegrationsCreate**](MultiHostIntegrationsCreate.md)| The specifics of the Multi-Host Integration to create | 

### Return type

[**MultiHostIntegrations**](MultiHostIntegrations.md)

### Authorization

[userAuth](../README.md#userAuth), [userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | OK. Returned if the request was successfully accepted into the system. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_sources_within_multi_host**
> create_sources_within_multi_host(id, multi_host_integrations_create_sources)

Create Sources Within Multi-Host Integration

This API is used to create sources within Multi-Host Integration. Multi-Host Integration holds similar types of sources.  A token with Org Admin or Multi-Host Admin authority is required to access this endpoint.

### Example

* OAuth Authentication (userAuth):
* OAuth Authentication (userAuth):

```python
import sailpoint.beta
from sailpoint.beta.models.multi_host_integrations_create_sources import MultiHostIntegrationsCreateSources
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
    api_instance = sailpoint.beta.MultiHostIntegrationApi(api_client)
    id = '2c91808568c529c60168cca6f90c1326' # str | ID of the Multi-Host Integration.
    multi_host_integrations_create_sources = [sailpoint.beta.MultiHostIntegrationsCreateSources()] # List[MultiHostIntegrationsCreateSources] | The specifics of the sources to create within Multi-Host Integration.

    try:
        # Create Sources Within Multi-Host Integration
        api_instance.create_sources_within_multi_host(id, multi_host_integrations_create_sources)
    except Exception as e:
        print("Exception when calling MultiHostIntegrationApi->create_sources_within_multi_host: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the Multi-Host Integration. | 
 **multi_host_integrations_create_sources** | [**List[MultiHostIntegrationsCreateSources]**](MultiHostIntegrationsCreateSources.md)| The specifics of the sources to create within Multi-Host Integration. | 

### Return type

void (empty response body)

### Authorization

[userAuth](../README.md#userAuth), [userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK. Returned if the request was successfully accepted into the system. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_multi_host**
> delete_multi_host(id)

Delete Multi-Host Integration

Delete an existing Multi-Host Integration by ID.    A token with Org Admin or Multi Host Admin authority is required to access this endpoint.

### Example

* OAuth Authentication (userAuth):
* OAuth Authentication (userAuth):

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
    api_instance = sailpoint.beta.MultiHostIntegrationApi(api_client)
    id = '2c91808568c529c60168cca6f90c1326' # str | ID of Multi-Host Integration to delete.

    try:
        # Delete Multi-Host Integration
        api_instance.delete_multi_host(id)
    except Exception as e:
        print("Exception when calling MultiHostIntegrationApi->delete_multi_host: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of Multi-Host Integration to delete. | 

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
**200** | OK. Returned if the request was successfully accepted into the system. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_acct_aggregation_groups**
> MultiHostIntegrationsAggScheduleUpdate get_acct_aggregation_groups(multi_host_id)

Get Account Aggregation Groups Within Multi-Host Integration ID

This API will return array of account aggregation groups within provided Multi-Host Integration ID.  A token with Org Admin or Multi-Host Admin authority is required to access this endpoint.

### Example

* OAuth Authentication (userAuth):
* OAuth Authentication (userAuth):

```python
import sailpoint.beta
from sailpoint.beta.models.multi_host_integrations_agg_schedule_update import MultiHostIntegrationsAggScheduleUpdate
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
    api_instance = sailpoint.beta.MultiHostIntegrationApi(api_client)
    multi_host_id = 'aMultiHostId' # str | ID of the Multi-Host Integration to update

    try:
        # Get Account Aggregation Groups Within Multi-Host Integration ID
        api_response = api_instance.get_acct_aggregation_groups(multi_host_id)
        print("The response of MultiHostIntegrationApi->get_acct_aggregation_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MultiHostIntegrationApi->get_acct_aggregation_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **multi_host_id** | **str**| ID of the Multi-Host Integration to update | 

### Return type

[**MultiHostIntegrationsAggScheduleUpdate**](MultiHostIntegrationsAggScheduleUpdate.md)

### Authorization

[userAuth](../README.md#userAuth), [userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK. Returned if the request was successfully accepted into the system. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_entitlement_aggregation_groups**
> MultiHostIntegrationsAggScheduleUpdate get_entitlement_aggregation_groups(multi_host_id)

Get Entitlement Aggregation Groups Within Multi-Host Integration ID

This API will return array of aggregation groups within provided Multi-Host Integration ID.    A token with Org Admin or Multi-Host Admin authority is required to access this endpoint.

### Example

* OAuth Authentication (userAuth):
* OAuth Authentication (userAuth):

```python
import sailpoint.beta
from sailpoint.beta.models.multi_host_integrations_agg_schedule_update import MultiHostIntegrationsAggScheduleUpdate
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
    api_instance = sailpoint.beta.MultiHostIntegrationApi(api_client)
    multi_host_id = 'aMultiHostId' # str | ID of the Multi-Host Integration to update

    try:
        # Get Entitlement Aggregation Groups Within Multi-Host Integration ID
        api_response = api_instance.get_entitlement_aggregation_groups(multi_host_id)
        print("The response of MultiHostIntegrationApi->get_entitlement_aggregation_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MultiHostIntegrationApi->get_entitlement_aggregation_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **multi_host_id** | **str**| ID of the Multi-Host Integration to update | 

### Return type

[**MultiHostIntegrationsAggScheduleUpdate**](MultiHostIntegrationsAggScheduleUpdate.md)

### Authorization

[userAuth](../README.md#userAuth), [userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK. Returned if the request was successfully accepted into the system. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_multi_host_integrations**
> MultiHostIntegrations get_multi_host_integrations(id)

Get Multi-Host Integration By ID

Get an existing Multi-Host Integration.   A token with Org Admin or Multi-Host Integration Admin authority is required to access this endpoint.

### Example

* OAuth Authentication (userAuth):
* OAuth Authentication (userAuth):

```python
import sailpoint.beta
from sailpoint.beta.models.multi_host_integrations import MultiHostIntegrations
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
    api_instance = sailpoint.beta.MultiHostIntegrationApi(api_client)
    id = '2c91808568c529c60168cca6f90c1326' # str | ID of the Multi-Host Integration.

    try:
        # Get Multi-Host Integration By ID
        api_response = api_instance.get_multi_host_integrations(id)
        print("The response of MultiHostIntegrationApi->get_multi_host_integrations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MultiHostIntegrationApi->get_multi_host_integrations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the Multi-Host Integration. | 

### Return type

[**MultiHostIntegrations**](MultiHostIntegrations.md)

### Authorization

[userAuth](../README.md#userAuth), [userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK. Returned if the request was successfully accepted into the system. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_multi_host_integrations_list**
> List[MultiHostIntegrations] get_multi_host_integrations_list(offset=offset, limit=limit, sorters=sorters, filters=filters, count=count, for_subadmin=for_subadmin)

List All Existing Multi-Host Integrations

Get a list of Multi-Host Integrations.    A token with Org Admin or Multi-Host Admin authority is required to access this endpoint.

### Example

* OAuth Authentication (userAuth):
* OAuth Authentication (userAuth):

```python
import sailpoint.beta
from sailpoint.beta.models.multi_host_integrations import MultiHostIntegrations
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
    api_instance = sailpoint.beta.MultiHostIntegrationApi(api_client)
    offset = 0 # int | Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 0)
    limit = 250 # int | Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 250)
    sorters = 'name' # str | Sort results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#sorting-results)  Sorting is supported for the following fields: **name** (optional)
    filters = 'id eq 2c91808b6ef1d43e016efba0ce470904' # str | Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **type**: *in*  **forSubAdminId**: *in* (optional)
    count = False # bool | If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count=true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to False)
    for_subadmin = '5168015d32f890ca15812c9180835d2e' # str | If provided, filters the returned list according to what is visible to the indicated ROLE_SUBADMIN Identity or SOURCE_SUBADMIN identity.  The value of the parameter is either an Identity ID, or the special value **me**, which is shorthand for the calling Identity's ID.  A 400 Bad Request error is returned if the **for-subadmin** parameter is specified for an Identity that is not a subadmin. (optional)

    try:
        # List All Existing Multi-Host Integrations
        api_response = api_instance.get_multi_host_integrations_list(offset=offset, limit=limit, sorters=sorters, filters=filters, count=count, for_subadmin=for_subadmin)
        print("The response of MultiHostIntegrationApi->get_multi_host_integrations_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MultiHostIntegrationApi->get_multi_host_integrations_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to 0]
 **limit** | **int**| Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to 250]
 **sorters** | **str**| Sort results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#sorting-results)  Sorting is supported for the following fields: **name** | [optional] 
 **filters** | **str**| Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **type**: *in*  **forSubAdminId**: *in* | [optional] 
 **count** | **bool**| If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count&#x3D;true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to False]
 **for_subadmin** | **str**| If provided, filters the returned list according to what is visible to the indicated ROLE_SUBADMIN Identity or SOURCE_SUBADMIN identity.  The value of the parameter is either an Identity ID, or the special value **me**, which is shorthand for the calling Identity&#39;s ID.  A 400 Bad Request error is returned if the **for-subadmin** parameter is specified for an Identity that is not a subadmin. | [optional] 

### Return type

[**List[MultiHostIntegrations]**](MultiHostIntegrations.md)

### Authorization

[userAuth](../README.md#userAuth), [userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK. Returned if the request was successfully accepted into the system. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_multi_host_source_creation_errors**
> List[SourceCreationErrors] get_multi_host_source_creation_errors(multi_host_id)

List Multi-Host Source Creation Errors

Get a list of sources creation errors within Multi-Host Integration ID.    A token with Org Admin or Multi-Host Admin authority is required to access this endpoint.

### Example

* OAuth Authentication (userAuth):
* OAuth Authentication (userAuth):

```python
import sailpoint.beta
from sailpoint.beta.models.source_creation_errors import SourceCreationErrors
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
    api_instance = sailpoint.beta.MultiHostIntegrationApi(api_client)
    multi_host_id = '004091cb79b04636b88662afa50a4440' # str | ID of the Multi-Host Integration

    try:
        # List Multi-Host Source Creation Errors
        api_response = api_instance.get_multi_host_source_creation_errors(multi_host_id)
        print("The response of MultiHostIntegrationApi->get_multi_host_source_creation_errors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MultiHostIntegrationApi->get_multi_host_source_creation_errors: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **multi_host_id** | **str**| ID of the Multi-Host Integration | 

### Return type

[**List[SourceCreationErrors]**](SourceCreationErrors.md)

### Authorization

[userAuth](../README.md#userAuth), [userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK. Returned if the request was successfully accepted into the system. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_multihost_integration_types**
> List[MultiHostIntegrationTemplateType] get_multihost_integration_types()

List Multi-Host Integration Types

This API endpoint returns the current list of supported Multi-Host Integration types.    A token with Org Admin or Multi-Host Admin authority is required to access this endpoint.

### Example

* OAuth Authentication (userAuth):
* OAuth Authentication (userAuth):

```python
import sailpoint.beta
from sailpoint.beta.models.multi_host_integration_template_type import MultiHostIntegrationTemplateType
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
    api_instance = sailpoint.beta.MultiHostIntegrationApi(api_client)

    try:
        # List Multi-Host Integration Types
        api_response = api_instance.get_multihost_integration_types()
        print("The response of MultiHostIntegrationApi->get_multihost_integration_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MultiHostIntegrationApi->get_multihost_integration_types: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[MultiHostIntegrationTemplateType]**](MultiHostIntegrationTemplateType.md)

### Authorization

[userAuth](../README.md#userAuth), [userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK. Returned if the request was successfully accepted into the system. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sources_within_multi_host**
> List[MultiHostSources] get_sources_within_multi_host(offset=offset, limit=limit, sorters=sorters, filters=filters, count=count)

List Sources Within Multi-Host Integration

Get a list of sources within Multi-Host Integration ID.    A token with Org Admin or Multi-Host Admin authority is required to access this endpoint.

### Example

* OAuth Authentication (userAuth):
* OAuth Authentication (userAuth):

```python
import sailpoint.beta
from sailpoint.beta.models.multi_host_sources import MultiHostSources
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
    api_instance = sailpoint.beta.MultiHostIntegrationApi(api_client)
    offset = 0 # int | Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 0)
    limit = 250 # int | Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 250)
    sorters = 'name' # str | Sort results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#sorting-results)  Sorting is supported for the following fields: **name** (optional)
    filters = 'id eq 2c91808b6ef1d43e016efba0ce470904' # str | Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **id**: *in* (optional)
    count = False # bool | If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count=true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to False)

    try:
        # List Sources Within Multi-Host Integration
        api_response = api_instance.get_sources_within_multi_host(offset=offset, limit=limit, sorters=sorters, filters=filters, count=count)
        print("The response of MultiHostIntegrationApi->get_sources_within_multi_host:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MultiHostIntegrationApi->get_sources_within_multi_host: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to 0]
 **limit** | **int**| Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to 250]
 **sorters** | **str**| Sort results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#sorting-results)  Sorting is supported for the following fields: **name** | [optional] 
 **filters** | **str**| Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **id**: *in* | [optional] 
 **count** | **bool**| If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count&#x3D;true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to False]

### Return type

[**List[MultiHostSources]**](MultiHostSources.md)

### Authorization

[userAuth](../README.md#userAuth), [userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK. Returned if the request was successfully accepted into the system. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_connection_multi_host_sources**
> test_connection_multi_host_sources(multihost_id)

Test Configuration For Multi-Host Integration

This endpoint performs a more detailed validation of the Multi-Host Integration's configuration.  A token with Org Admin or Multi-Host Admin authority is required to access this endpoint.

### Example

* OAuth Authentication (userAuth):
* OAuth Authentication (userAuth):

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
    api_instance = sailpoint.beta.MultiHostIntegrationApi(api_client)
    multihost_id = '2c91808568c529c60168cca6f90c1324' # str | ID of the Multi-Host Integration

    try:
        # Test Configuration For Multi-Host Integration
        api_instance.test_connection_multi_host_sources(multihost_id)
    except Exception as e:
        print("Exception when calling MultiHostIntegrationApi->test_connection_multi_host_sources: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **multihost_id** | **str**| ID of the Multi-Host Integration | 

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
**200** | OK. Returned if the request was successfully accepted into the system. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_source_connection_multihost**
> TestSourceConnectionMultihost200Response test_source_connection_multihost(multihost_id, source_id)

Test Configuration For Multi-Host Integration's Single Source

This endpoint performs a more detailed validation of the source's configuration.    A token with Org Admin or Multi-Host Admin authority is required to access this endpoint.

### Example

* OAuth Authentication (userAuth):
* OAuth Authentication (userAuth):

```python
import sailpoint.beta
from sailpoint.beta.models.test_source_connection_multihost200_response import TestSourceConnectionMultihost200Response
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
    api_instance = sailpoint.beta.MultiHostIntegrationApi(api_client)
    multihost_id = '2c91808568c529c60168cca6f90c1326' # str | ID of the Multi-Host Integration
    source_id = '2c91808568c529f60168cca6f90c1324' # str | ID of the source within the Multi-Host Integration

    try:
        # Test Configuration For Multi-Host Integration's Single Source
        api_response = api_instance.test_source_connection_multihost(multihost_id, source_id)
        print("The response of MultiHostIntegrationApi->test_source_connection_multihost:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MultiHostIntegrationApi->test_source_connection_multihost: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **multihost_id** | **str**| ID of the Multi-Host Integration | 
 **source_id** | **str**| ID of the source within the Multi-Host Integration | 

### Return type

[**TestSourceConnectionMultihost200Response**](TestSourceConnectionMultihost200Response.md)

### Authorization

[userAuth](../README.md#userAuth), [userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK. Returned if the request was successfully accepted into the system. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_multi_host_sources**
> update_multi_host_sources(multihost_id, update_multi_host_sources_request_inner)

Update Multi-Host Integration

Update existing sources within Multi-Host Integration.  A token with Org Admin or Multi-Host Admin authority is required to access this endpoint.

### Example

* OAuth Authentication (userAuth):
* OAuth Authentication (userAuth):

```python
import sailpoint.beta
from sailpoint.beta.models.update_multi_host_sources_request_inner import UpdateMultiHostSourcesRequestInner
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
    api_instance = sailpoint.beta.MultiHostIntegrationApi(api_client)
    multihost_id = 'anId' # str | ID of the Multi-Host Integration to update.
    update_multi_host_sources_request_inner = [{op=add, path=/description, value=MDK Multi-Host Integration 222 description}] # List[UpdateMultiHostSourcesRequestInner] | This endpoint allows you to update a Multi-Host Integration. 

    try:
        # Update Multi-Host Integration
        api_instance.update_multi_host_sources(multihost_id, update_multi_host_sources_request_inner)
    except Exception as e:
        print("Exception when calling MultiHostIntegrationApi->update_multi_host_sources: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **multihost_id** | **str**| ID of the Multi-Host Integration to update. | 
 **update_multi_host_sources_request_inner** | [**List[UpdateMultiHostSourcesRequestInner]**](UpdateMultiHostSourcesRequestInner.md)| This endpoint allows you to update a Multi-Host Integration.  | 

### Return type

void (empty response body)

### Authorization

[userAuth](../README.md#userAuth), [userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK. Returned if the request was successfully accepted into the system. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

