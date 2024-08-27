# sailpoint.beta.WorkReassignmentApi

All URIs are relative to *https://sailpoint.api.identitynow.com/beta*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_reassignment_configuration**](WorkReassignmentApi.md#create_reassignment_configuration) | **POST** /reassignment-configurations | Create a Reassignment Configuration
[**delete_reassignment_configuration**](WorkReassignmentApi.md#delete_reassignment_configuration) | **DELETE** /reassignment-configurations/{identityId} | Delete Reassignment Configuration
[**get_evaluate_reassignment_configuration**](WorkReassignmentApi.md#get_evaluate_reassignment_configuration) | **GET** /reassignment-configurations/{identityId}/evaluate/{configType} | Evaluate Reassignment Configuration
[**get_reassignment_config_types**](WorkReassignmentApi.md#get_reassignment_config_types) | **GET** /reassignment-configurations/types | List Reassignment Config Types
[**get_reassignment_configuration**](WorkReassignmentApi.md#get_reassignment_configuration) | **GET** /reassignment-configurations/{identityId} | Get Reassignment Configuration
[**get_tenant_config_configuration**](WorkReassignmentApi.md#get_tenant_config_configuration) | **GET** /reassignment-configurations/tenant-config | Get Tenant-wide Reassignment Configuration settings
[**list_reassignment_configurations**](WorkReassignmentApi.md#list_reassignment_configurations) | **GET** /reassignment-configurations | List Reassignment Configurations
[**put_reassignment_config**](WorkReassignmentApi.md#put_reassignment_config) | **PUT** /reassignment-configurations/{identityId} | Update Reassignment Configuration
[**put_tenant_configuration**](WorkReassignmentApi.md#put_tenant_configuration) | **PUT** /reassignment-configurations/tenant-config | Update Tenant-wide Reassignment Configuration settings


# **create_reassignment_configuration**
> ConfigurationItemResponse create_reassignment_configuration(configuration_item_request)

Create a Reassignment Configuration

Creates a new Reassignment Configuration for the specified identity.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import sailpoint.beta
from sailpoint.beta.models.configuration_item_request import ConfigurationItemRequest
from sailpoint.beta.models.configuration_item_response import ConfigurationItemResponse
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
    api_instance = sailpoint.beta.WorkReassignmentApi(api_client)
    configuration_item_request = sailpoint.beta.ConfigurationItemRequest() # ConfigurationItemRequest | 

    try:
        # Create a Reassignment Configuration
        api_response = api_instance.create_reassignment_configuration(configuration_item_request)
        print("The response of WorkReassignmentApi->create_reassignment_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkReassignmentApi->create_reassignment_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **configuration_item_request** | [**ConfigurationItemRequest**](ConfigurationItemRequest.md)|  | 

### Return type

[**ConfigurationItemResponse**](ConfigurationItemResponse.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The newly created Reassignment Configuration object |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_reassignment_configuration**
> delete_reassignment_configuration(identity_id)

Delete Reassignment Configuration

Deletes all Reassignment Configuration for the specified identity

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
    api_instance = sailpoint.beta.WorkReassignmentApi(api_client)
    identity_id = '2c91808781a71ddb0181b9090b5c504e' # str | unique identity id

    try:
        # Delete Reassignment Configuration
        api_instance.delete_reassignment_configuration(identity_id)
    except Exception as e:
        print("Exception when calling WorkReassignmentApi->delete_reassignment_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identity_id** | **str**| unique identity id | 

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
**204** | Reassignment Configuration deleted |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_evaluate_reassignment_configuration**
> List[EvaluateResponse] get_evaluate_reassignment_configuration(identity_id, config_type, exclusion_filters=exclusion_filters)

Evaluate Reassignment Configuration

Evaluates the Reassignment Configuration for an `Identity` to determine if work items for the specified type should be reassigned. If a valid Reassignment Configuration is found for the identity & work type, then a lookup is initiated which recursively fetches the Reassignment Configuration for the next `TargetIdentity` until no more results are found or a max depth of 5. That lookup trail is provided in the response and the final reassigned identity in the lookup list is returned as the `reassignToId` property. If no Reassignment Configuration is found for the specified identity & config type then the requested Identity ID will be used as the `reassignToId` value and the lookupTrail node will be empty.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import sailpoint.beta
from sailpoint.beta.models.config_type_enum import ConfigTypeEnum
from sailpoint.beta.models.evaluate_response import EvaluateResponse
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
    api_instance = sailpoint.beta.WorkReassignmentApi(api_client)
    identity_id = '2c91808781a71ddb0181b9090b5c504e' # str | unique identity id
    config_type = sailpoint.beta.ConfigTypeEnum() # ConfigTypeEnum | Reassignment work type
    exclusion_filters = ['SELF_REVIEW_DELEGATION'] # List[str] | Exclusion filters that disable parts of the reassignment evaluation. Possible values are listed below: - `SELF_REVIEW_DELEGATION`: This will exclude delegations of self-review reassignments (optional)

    try:
        # Evaluate Reassignment Configuration
        api_response = api_instance.get_evaluate_reassignment_configuration(identity_id, config_type, exclusion_filters=exclusion_filters)
        print("The response of WorkReassignmentApi->get_evaluate_reassignment_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkReassignmentApi->get_evaluate_reassignment_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identity_id** | **str**| unique identity id | 
 **config_type** | [**ConfigTypeEnum**](.md)| Reassignment work type | 
 **exclusion_filters** | [**List[str]**](str.md)| Exclusion filters that disable parts of the reassignment evaluation. Possible values are listed below: - &#x60;SELF_REVIEW_DELEGATION&#x60;: This will exclude delegations of self-review reassignments | [optional] 

### Return type

[**List[EvaluateResponse]**](EvaluateResponse.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Evaluated Reassignment Configuration |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reassignment_config_types**
> List[ConfigType] get_reassignment_config_types()

List Reassignment Config Types

Gets a collection of types which are available in the Reassignment Configuration UI.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import sailpoint.beta
from sailpoint.beta.models.config_type import ConfigType
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
    api_instance = sailpoint.beta.WorkReassignmentApi(api_client)

    try:
        # List Reassignment Config Types
        api_response = api_instance.get_reassignment_config_types()
        print("The response of WorkReassignmentApi->get_reassignment_config_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkReassignmentApi->get_reassignment_config_types: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[ConfigType]**](ConfigType.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of Reassignment Configuration Types |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reassignment_configuration**
> ConfigurationResponse get_reassignment_configuration(identity_id)

Get Reassignment Configuration

Gets the Reassignment Configuration for an identity.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import sailpoint.beta
from sailpoint.beta.models.configuration_response import ConfigurationResponse
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
    api_instance = sailpoint.beta.WorkReassignmentApi(api_client)
    identity_id = '2c91808781a71ddb0181b9090b5c504f' # str | unique identity id

    try:
        # Get Reassignment Configuration
        api_response = api_instance.get_reassignment_configuration(identity_id)
        print("The response of WorkReassignmentApi->get_reassignment_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkReassignmentApi->get_reassignment_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identity_id** | **str**| unique identity id | 

### Return type

[**ConfigurationResponse**](ConfigurationResponse.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Reassignment Configuration for an identity |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tenant_config_configuration**
> TenantConfigurationResponse get_tenant_config_configuration()

Get Tenant-wide Reassignment Configuration settings

Gets the global Reassignment Configuration settings for the requestor's tenant.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import sailpoint.beta
from sailpoint.beta.models.tenant_configuration_response import TenantConfigurationResponse
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
    api_instance = sailpoint.beta.WorkReassignmentApi(api_client)

    try:
        # Get Tenant-wide Reassignment Configuration settings
        api_response = api_instance.get_tenant_config_configuration()
        print("The response of WorkReassignmentApi->get_tenant_config_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkReassignmentApi->get_tenant_config_configuration: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**TenantConfigurationResponse**](TenantConfigurationResponse.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Tenant-wide Reassignment Configuration settings |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_reassignment_configurations**
> List[ConfigurationResponse] list_reassignment_configurations()

List Reassignment Configurations

Gets all Reassignment configuration for the current org.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import sailpoint.beta
from sailpoint.beta.models.configuration_response import ConfigurationResponse
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
    api_instance = sailpoint.beta.WorkReassignmentApi(api_client)

    try:
        # List Reassignment Configurations
        api_response = api_instance.list_reassignment_configurations()
        print("The response of WorkReassignmentApi->list_reassignment_configurations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkReassignmentApi->list_reassignment_configurations: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[ConfigurationResponse]**](ConfigurationResponse.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of Reassignment Configurations for an org |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_reassignment_config**
> ConfigurationItemResponse put_reassignment_config(identity_id, configuration_item_request)

Update Reassignment Configuration

Replaces existing Reassignment configuration for an identity with the newly provided configuration.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import sailpoint.beta
from sailpoint.beta.models.configuration_item_request import ConfigurationItemRequest
from sailpoint.beta.models.configuration_item_response import ConfigurationItemResponse
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
    api_instance = sailpoint.beta.WorkReassignmentApi(api_client)
    identity_id = '2c91808781a71ddb0181b9090b5c504e' # str | unique identity id
    configuration_item_request = sailpoint.beta.ConfigurationItemRequest() # ConfigurationItemRequest | 

    try:
        # Update Reassignment Configuration
        api_response = api_instance.put_reassignment_config(identity_id, configuration_item_request)
        print("The response of WorkReassignmentApi->put_reassignment_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkReassignmentApi->put_reassignment_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identity_id** | **str**| unique identity id | 
 **configuration_item_request** | [**ConfigurationItemRequest**](ConfigurationItemRequest.md)|  | 

### Return type

[**ConfigurationItemResponse**](ConfigurationItemResponse.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Reassignment Configuration updated |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_tenant_configuration**
> TenantConfigurationResponse put_tenant_configuration(tenant_configuration_request)

Update Tenant-wide Reassignment Configuration settings

Replaces existing Tenant-wide Reassignment Configuration settings with the newly provided settings.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import sailpoint.beta
from sailpoint.beta.models.tenant_configuration_request import TenantConfigurationRequest
from sailpoint.beta.models.tenant_configuration_response import TenantConfigurationResponse
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
    api_instance = sailpoint.beta.WorkReassignmentApi(api_client)
    tenant_configuration_request = sailpoint.beta.TenantConfigurationRequest() # TenantConfigurationRequest | 

    try:
        # Update Tenant-wide Reassignment Configuration settings
        api_response = api_instance.put_tenant_configuration(tenant_configuration_request)
        print("The response of WorkReassignmentApi->put_tenant_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkReassignmentApi->put_tenant_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_configuration_request** | [**TenantConfigurationRequest**](TenantConfigurationRequest.md)|  | 

### Return type

[**TenantConfigurationResponse**](TenantConfigurationResponse.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Tenant-wide Reassignment Configuration settings |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

