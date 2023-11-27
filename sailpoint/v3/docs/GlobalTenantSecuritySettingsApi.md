# sailpoint.v3.GlobalTenantSecuritySettingsApi

All URIs are relative to *https://sailpoint.api.identitynow.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_auth_org_network_config**](GlobalTenantSecuritySettingsApi.md#create_auth_org_network_config) | **POST** /auth-org/network-config | Create security network configuration.
[**get_auth_org_network_config**](GlobalTenantSecuritySettingsApi.md#get_auth_org_network_config) | **GET** /auth-org/network-config | Get security network configuration.
[**patch_auth_org_network_config**](GlobalTenantSecuritySettingsApi.md#patch_auth_org_network_config) | **PATCH** /auth-org/network-config | Update security network configuration.


# **create_auth_org_network_config**
> NetworkConfiguration create_auth_org_network_config(network_configuration)

Create security network configuration.

This API returns the details of an org's network auth configuration. Requires security scope of: 'sp:auth-org:create'

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import sailpoint.v3
from sailpoint.v3.models.network_configuration import NetworkConfiguration
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
    api_instance = sailpoint.v3.GlobalTenantSecuritySettingsApi(api_client)
    network_configuration = sailpoint.v3.NetworkConfiguration() # NetworkConfiguration | Network configuration creation request body.   The following constraints ensure the request body conforms to certain logical guidelines, which are:   1. Each string element in the range array must be a valid ip address or ip subnet mask.   2. Each string element in the geolocation array must be 2 characters, and they can only be uppercase letters.

    try:
        # Create security network configuration.
        api_response = api_instance.create_auth_org_network_config(network_configuration)
        print("The response of GlobalTenantSecuritySettingsApi->create_auth_org_network_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GlobalTenantSecuritySettingsApi->create_auth_org_network_config: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_configuration** | [**NetworkConfiguration**](NetworkConfiguration.md)| Network configuration creation request body.   The following constraints ensure the request body conforms to certain logical guidelines, which are:   1. Each string element in the range array must be a valid ip address or ip subnet mask.   2. Each string element in the geolocation array must be 2 characters, and they can only be uppercase letters. | 

### Return type

[**NetworkConfiguration**](NetworkConfiguration.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Network configuration for the tenant. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_auth_org_network_config**
> NetworkConfiguration get_auth_org_network_config()

Get security network configuration.

This API returns the details of an org's network auth configuration. Requires security scope of: 'sp:auth-org:read'

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import sailpoint.v3
from sailpoint.v3.models.network_configuration import NetworkConfiguration
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
    api_instance = sailpoint.v3.GlobalTenantSecuritySettingsApi(api_client)

    try:
        # Get security network configuration.
        api_response = api_instance.get_auth_org_network_config()
        print("The response of GlobalTenantSecuritySettingsApi->get_auth_org_network_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GlobalTenantSecuritySettingsApi->get_auth_org_network_config: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**NetworkConfiguration**](NetworkConfiguration.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Network configuration for the tenant&#39;s auth org. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_auth_org_network_config**
> NetworkConfiguration patch_auth_org_network_config(json_patch_operation)

Update security network configuration.

This API updates an existing network configuration for an org using PATCH  Requires security scope of:  'sp:auth-org:update'

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import sailpoint.v3
from sailpoint.v3.models.json_patch_operation import JsonPatchOperation
from sailpoint.v3.models.network_configuration import NetworkConfiguration
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
    api_instance = sailpoint.v3.GlobalTenantSecuritySettingsApi(api_client)
    json_patch_operation = [{op=replace, path=/whitelisted, value=false,}, {op=add, path=/geolocation, value=[AF, HN, ES]}] # List[JsonPatchOperation] | A list of auth org network configuration update operations according to the [JSON Patch](https://tools.ietf.org/html/rfc6902) standard. Ensures that the patched Network Config conforms to certain logical guidelines, which are:   1. Each string element in the range array must be a valid ip address or ip subnet mask.   2. Each string element in the geolocation array must be 2 characters, and they can only be uppercase letters.

    try:
        # Update security network configuration.
        api_response = api_instance.patch_auth_org_network_config(json_patch_operation)
        print("The response of GlobalTenantSecuritySettingsApi->patch_auth_org_network_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GlobalTenantSecuritySettingsApi->patch_auth_org_network_config: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **json_patch_operation** | [**List[JsonPatchOperation]**](JsonPatchOperation.md)| A list of auth org network configuration update operations according to the [JSON Patch](https://tools.ietf.org/html/rfc6902) standard. Ensures that the patched Network Config conforms to certain logical guidelines, which are:   1. Each string element in the range array must be a valid ip address or ip subnet mask.   2. Each string element in the geolocation array must be 2 characters, and they can only be uppercase letters. | 

### Return type

[**NetworkConfiguration**](NetworkConfiguration.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated Auth Org network configuration. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

