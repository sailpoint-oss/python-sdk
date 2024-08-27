# sailpoint.v2024.SIMIntegrationsApi

All URIs are relative to *https://sailpoint.api.identitynow.com/v2024*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_sim_integration**](SIMIntegrationsApi.md#create_sim_integration) | **POST** /sim-integrations | Create new SIM integration
[**delete_sim_integration**](SIMIntegrationsApi.md#delete_sim_integration) | **DELETE** /sim-integrations/{id} | Delete a SIM integration
[**get_sim_integration**](SIMIntegrationsApi.md#get_sim_integration) | **GET** /sim-integrations/{id} | Get a SIM integration details.
[**get_sim_integrations**](SIMIntegrationsApi.md#get_sim_integrations) | **GET** /sim-integrations | List the existing SIM integrations.
[**patch_before_provisioning_rule**](SIMIntegrationsApi.md#patch_before_provisioning_rule) | **PATCH** /sim-integrations/{id}/beforeProvisioningRule | Patch a SIM beforeProvisioningRule attribute.
[**patch_sim_attributes**](SIMIntegrationsApi.md#patch_sim_attributes) | **PATCH** /sim-integrations/{id} | Patch a SIM attribute.
[**put_sim_integration**](SIMIntegrationsApi.md#put_sim_integration) | **PUT** /sim-integrations/{id} | Update an existing SIM integration


# **create_sim_integration**
> ServiceDeskIntegrationDto1 create_sim_integration(x_sail_point_experimental, sim_integration_details)

Create new SIM integration

Create a new SIM Integrations.  A token with Org Admin or Service Desk Admin authority is required to access this endpoint.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import sailpoint.v2024
from sailpoint.v2024.models.service_desk_integration_dto1 import ServiceDeskIntegrationDto1
from sailpoint.v2024.models.sim_integration_details import SimIntegrationDetails
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
    api_instance = sailpoint.v2024.SIMIntegrationsApi(api_client)
    x_sail_point_experimental = 'true' # str | Use this header to enable this experimental API. (default to 'true')
    sim_integration_details = sailpoint.v2024.SimIntegrationDetails() # SimIntegrationDetails | DTO containing the details of the SIM integration

    try:
        # Create new SIM integration
        api_response = api_instance.create_sim_integration(x_sail_point_experimental, sim_integration_details)
        print("The response of SIMIntegrationsApi->create_sim_integration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SIMIntegrationsApi->create_sim_integration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_sail_point_experimental** | **str**| Use this header to enable this experimental API. | [default to &#39;true&#39;]
 **sim_integration_details** | [**SimIntegrationDetails**](SimIntegrationDetails.md)| DTO containing the details of the SIM integration | 

### Return type

[**ServiceDeskIntegrationDto1**](ServiceDeskIntegrationDto1.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | details of the created integration |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sim_integration**
> delete_sim_integration(id, x_sail_point_experimental)

Delete a SIM integration

Get the details of a SIM integration. A token with Org Admin or Service Desk Admin authority is required to access this endpoint.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

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
    api_instance = sailpoint.v2024.SIMIntegrationsApi(api_client)
    id = '12345' # str | The id of the integration to delete.
    x_sail_point_experimental = 'true' # str | Use this header to enable this experimental API. (default to 'true')

    try:
        # Delete a SIM integration
        api_instance.delete_sim_integration(id, x_sail_point_experimental)
    except Exception as e:
        print("Exception when calling SIMIntegrationsApi->delete_sim_integration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the integration to delete. | 
 **x_sail_point_experimental** | **str**| Use this header to enable this experimental API. | [default to &#39;true&#39;]

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
**200** | No content response |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sim_integration**
> ServiceDeskIntegrationDto1 get_sim_integration(id, x_sail_point_experimental)

Get a SIM integration details.

Get the details of a SIM integration. A token with Org Admin or Service Desk Admin authority is required to access this endpoint.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import sailpoint.v2024
from sailpoint.v2024.models.service_desk_integration_dto1 import ServiceDeskIntegrationDto1
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
    api_instance = sailpoint.v2024.SIMIntegrationsApi(api_client)
    id = '12345' # str | The id of the integration.
    x_sail_point_experimental = 'true' # str | Use this header to enable this experimental API. (default to 'true')

    try:
        # Get a SIM integration details.
        api_response = api_instance.get_sim_integration(id, x_sail_point_experimental)
        print("The response of SIMIntegrationsApi->get_sim_integration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SIMIntegrationsApi->get_sim_integration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the integration. | 
 **x_sail_point_experimental** | **str**| Use this header to enable this experimental API. | [default to &#39;true&#39;]

### Return type

[**ServiceDeskIntegrationDto1**](ServiceDeskIntegrationDto1.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The DTO containing the details of the SIM integration |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sim_integrations**
> ServiceDeskIntegrationDto1 get_sim_integrations(x_sail_point_experimental)

List the existing SIM integrations.

List the existing SIM integrations. A token with Org Admin or Service Desk Admin authority is required to access this endpoint.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import sailpoint.v2024
from sailpoint.v2024.models.service_desk_integration_dto1 import ServiceDeskIntegrationDto1
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
    api_instance = sailpoint.v2024.SIMIntegrationsApi(api_client)
    x_sail_point_experimental = 'true' # str | Use this header to enable this experimental API. (default to 'true')

    try:
        # List the existing SIM integrations.
        api_response = api_instance.get_sim_integrations(x_sail_point_experimental)
        print("The response of SIMIntegrationsApi->get_sim_integrations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SIMIntegrationsApi->get_sim_integrations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_sail_point_experimental** | **str**| Use this header to enable this experimental API. | [default to &#39;true&#39;]

### Return type

[**ServiceDeskIntegrationDto1**](ServiceDeskIntegrationDto1.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The DTO containing the details of the SIM integration |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_before_provisioning_rule**
> ServiceDeskIntegrationDto1 patch_before_provisioning_rule(id, x_sail_point_experimental, json_patch)

Patch a SIM beforeProvisioningRule attribute.

Patch a SIM beforeProvisioningRule attribute given a JsonPatch object. A token with Org Admin or Service Desk Admin authority is required to access this endpoint.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import sailpoint.v2024
from sailpoint.v2024.models.json_patch import JsonPatch
from sailpoint.v2024.models.service_desk_integration_dto1 import ServiceDeskIntegrationDto1
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
    api_instance = sailpoint.v2024.SIMIntegrationsApi(api_client)
    id = '12345' # str | SIM integration id
    x_sail_point_experimental = 'true' # str | Use this header to enable this experimental API. (default to 'true')
    json_patch = sailpoint.v2024.JsonPatch() # JsonPatch | The JsonPatch object that describes the changes of SIM beforeProvisioningRule.

    try:
        # Patch a SIM beforeProvisioningRule attribute.
        api_response = api_instance.patch_before_provisioning_rule(id, x_sail_point_experimental, json_patch)
        print("The response of SIMIntegrationsApi->patch_before_provisioning_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SIMIntegrationsApi->patch_before_provisioning_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| SIM integration id | 
 **x_sail_point_experimental** | **str**| Use this header to enable this experimental API. | [default to &#39;true&#39;]
 **json_patch** | [**JsonPatch**](JsonPatch.md)| The JsonPatch object that describes the changes of SIM beforeProvisioningRule. | 

### Return type

[**ServiceDeskIntegrationDto1**](ServiceDeskIntegrationDto1.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated DTO containing the details of the SIM integration. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_sim_attributes**
> ServiceDeskIntegrationDto1 patch_sim_attributes(id, x_sail_point_experimental, json_patch)

Patch a SIM attribute.

Patch a SIM attribute given a JsonPatch object. A token with Org Admin or Service Desk Admin authority is required to access this endpoint.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import sailpoint.v2024
from sailpoint.v2024.models.json_patch import JsonPatch
from sailpoint.v2024.models.service_desk_integration_dto1 import ServiceDeskIntegrationDto1
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
    api_instance = sailpoint.v2024.SIMIntegrationsApi(api_client)
    id = '12345' # str | SIM integration id
    x_sail_point_experimental = 'true' # str | Use this header to enable this experimental API. (default to 'true')
    json_patch = sailpoint.v2024.JsonPatch() # JsonPatch | The JsonPatch object that describes the changes of SIM

    try:
        # Patch a SIM attribute.
        api_response = api_instance.patch_sim_attributes(id, x_sail_point_experimental, json_patch)
        print("The response of SIMIntegrationsApi->patch_sim_attributes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SIMIntegrationsApi->patch_sim_attributes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| SIM integration id | 
 **x_sail_point_experimental** | **str**| Use this header to enable this experimental API. | [default to &#39;true&#39;]
 **json_patch** | [**JsonPatch**](JsonPatch.md)| The JsonPatch object that describes the changes of SIM | 

### Return type

[**ServiceDeskIntegrationDto1**](ServiceDeskIntegrationDto1.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated DTO containing the details of the SIM integration. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_sim_integration**
> ServiceDeskIntegrationDto1 put_sim_integration(id, x_sail_point_experimental, sim_integration_details)

Update an existing SIM integration

Update an existing SIM integration.  A token with Org Admin or Service Desk Admin authority is required to access this endpoint.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import sailpoint.v2024
from sailpoint.v2024.models.service_desk_integration_dto1 import ServiceDeskIntegrationDto1
from sailpoint.v2024.models.sim_integration_details import SimIntegrationDetails
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
    api_instance = sailpoint.v2024.SIMIntegrationsApi(api_client)
    id = '12345' # str | The id of the integration.
    x_sail_point_experimental = 'true' # str | Use this header to enable this experimental API. (default to 'true')
    sim_integration_details = sailpoint.v2024.SimIntegrationDetails() # SimIntegrationDetails | The full DTO of the integration containing the updated model

    try:
        # Update an existing SIM integration
        api_response = api_instance.put_sim_integration(id, x_sail_point_experimental, sim_integration_details)
        print("The response of SIMIntegrationsApi->put_sim_integration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SIMIntegrationsApi->put_sim_integration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the integration. | 
 **x_sail_point_experimental** | **str**| Use this header to enable this experimental API. | [default to &#39;true&#39;]
 **sim_integration_details** | [**SimIntegrationDetails**](SimIntegrationDetails.md)| The full DTO of the integration containing the updated model | 

### Return type

[**ServiceDeskIntegrationDto1**](ServiceDeskIntegrationDto1.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | details of the updated integration |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

