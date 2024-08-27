# sailpoint.v3.GlobalTenantSecuritySettingsApi

All URIs are relative to *https://sailpoint.api.identitynow.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_auth_org_network_config**](GlobalTenantSecuritySettingsApi.md#create_auth_org_network_config) | **POST** /auth-org/network-config | Create security network configuration.
[**get_auth_org_lockout_config**](GlobalTenantSecuritySettingsApi.md#get_auth_org_lockout_config) | **GET** /auth-org/lockout-config | Get Auth Org Lockout Configuration.
[**get_auth_org_network_config**](GlobalTenantSecuritySettingsApi.md#get_auth_org_network_config) | **GET** /auth-org/network-config | Get security network configuration.
[**get_auth_org_service_provider_config**](GlobalTenantSecuritySettingsApi.md#get_auth_org_service_provider_config) | **GET** /auth-org/service-provider-config | Get Service Provider Configuration.
[**get_auth_org_session_config**](GlobalTenantSecuritySettingsApi.md#get_auth_org_session_config) | **GET** /auth-org/session-config | Get Auth Org Session Configuration.
[**patch_auth_org_lockout_config**](GlobalTenantSecuritySettingsApi.md#patch_auth_org_lockout_config) | **PATCH** /auth-org/lockout-config | Update Auth Org Lockout Configuration
[**patch_auth_org_network_config**](GlobalTenantSecuritySettingsApi.md#patch_auth_org_network_config) | **PATCH** /auth-org/network-config | Update security network configuration.
[**patch_auth_org_service_provider_config**](GlobalTenantSecuritySettingsApi.md#patch_auth_org_service_provider_config) | **PATCH** /auth-org/service-provider-config | Update Service Provider Configuration
[**patch_auth_org_session_config**](GlobalTenantSecuritySettingsApi.md#patch_auth_org_session_config) | **PATCH** /auth-org/session-config | Update Auth Org Session Configuration


# **create_auth_org_network_config**
> NetworkConfiguration create_auth_org_network_config(network_configuration)

Create security network configuration.

This API returns the details of an org's network auth configuration. Requires security scope of: 'sp:auth-org:manage'

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
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

# **get_auth_org_lockout_config**
> LockoutConfiguration get_auth_org_lockout_config()

Get Auth Org Lockout Configuration.

This API returns the details of an org's lockout auth configuration.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import sailpoint.v3
from sailpoint.v3.models.lockout_configuration import LockoutConfiguration
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
        # Get Auth Org Lockout Configuration.
        api_response = api_instance.get_auth_org_lockout_config()
        print("The response of GlobalTenantSecuritySettingsApi->get_auth_org_lockout_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GlobalTenantSecuritySettingsApi->get_auth_org_lockout_config: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**LockoutConfiguration**](LockoutConfiguration.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Lockout configuration for the tenant&#39;s auth org. |  -  |
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

# **get_auth_org_service_provider_config**
> ServiceProviderConfiguration get_auth_org_service_provider_config()

Get Service Provider Configuration.

This API returns the details of an org's service provider auth configuration.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import sailpoint.v3
from sailpoint.v3.models.service_provider_configuration import ServiceProviderConfiguration
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
        # Get Service Provider Configuration.
        api_response = api_instance.get_auth_org_service_provider_config()
        print("The response of GlobalTenantSecuritySettingsApi->get_auth_org_service_provider_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GlobalTenantSecuritySettingsApi->get_auth_org_service_provider_config: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ServiceProviderConfiguration**](ServiceProviderConfiguration.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Service provider configuration for the tenant. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_auth_org_session_config**
> SessionConfiguration get_auth_org_session_config()

Get Auth Org Session Configuration.

This API returns the details of an org's session auth configuration.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import sailpoint.v3
from sailpoint.v3.models.session_configuration import SessionConfiguration
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
        # Get Auth Org Session Configuration.
        api_response = api_instance.get_auth_org_session_config()
        print("The response of GlobalTenantSecuritySettingsApi->get_auth_org_session_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GlobalTenantSecuritySettingsApi->get_auth_org_session_config: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SessionConfiguration**](SessionConfiguration.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Session configuration for the tenant&#39;s auth org. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_auth_org_lockout_config**
> LockoutConfiguration patch_auth_org_lockout_config(json_patch_operation)

Update Auth Org Lockout Configuration

This API updates an existing lockout configuration for an org using PATCH  Requires security scope of:  'sp:auth-org:update'

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import sailpoint.v3
from sailpoint.v3.models.json_patch_operation import JsonPatchOperation
from sailpoint.v3.models.lockout_configuration import LockoutConfiguration
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
    json_patch_operation = [{op=replace, path=/maximumAttempts, value=7,}, {op=add, path=/lockoutDuration, value=35}] # List[JsonPatchOperation] | A list of auth org lockout configuration update operations according to the [JSON Patch](https://tools.ietf.org/html/rfc6902) standard. Ensures that the patched Lockout Config conforms to certain logical guidelines, which are:   1. maximumAttempts >= 1 && maximumAttempts <= 15   2. lockoutDuration >= 5 && lockoutDuration <= 60   3. lockoutWindow >= 5 && lockoutDuration <= 60

    try:
        # Update Auth Org Lockout Configuration
        api_response = api_instance.patch_auth_org_lockout_config(json_patch_operation)
        print("The response of GlobalTenantSecuritySettingsApi->patch_auth_org_lockout_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GlobalTenantSecuritySettingsApi->patch_auth_org_lockout_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **json_patch_operation** | [**List[JsonPatchOperation]**](JsonPatchOperation.md)| A list of auth org lockout configuration update operations according to the [JSON Patch](https://tools.ietf.org/html/rfc6902) standard. Ensures that the patched Lockout Config conforms to certain logical guidelines, which are:   1. maximumAttempts &gt;&#x3D; 1 &amp;&amp; maximumAttempts &lt;&#x3D; 15   2. lockoutDuration &gt;&#x3D; 5 &amp;&amp; lockoutDuration &lt;&#x3D; 60   3. lockoutWindow &gt;&#x3D; 5 &amp;&amp; lockoutDuration &lt;&#x3D; 60 | 

### Return type

[**LockoutConfiguration**](LockoutConfiguration.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated Auth Org lockout configuration. |  -  |
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

This API updates an existing network configuration for an org using PATCH  Requires security scope of:  'sp:auth-org:manage'

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
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

# **patch_auth_org_service_provider_config**
> ServiceProviderConfiguration patch_auth_org_service_provider_config(json_patch_operation)

Update Service Provider Configuration

This API updates an existing service provider configuration for an org using PATCH.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import sailpoint.v3
from sailpoint.v3.models.json_patch_operation import JsonPatchOperation
from sailpoint.v3.models.service_provider_configuration import ServiceProviderConfiguration
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
    json_patch_operation = [{op=replace, path=/enabled, value=true,}, {op=add, path=/federationProtocolDetails/0/jitConfiguration, value={enabled=true, sourceId=2c9180857377ed2901739c12a2da5ac8, sourceAttributeMappings={firstName=okta.firstName, lastName=okta.lastName, email=okta.email, employeeNumber=okta.employeeNumber}}}] # List[JsonPatchOperation] | A list of auth org service provider configuration update operations according to the [JSON Patch](https://tools.ietf.org/html/rfc6902) standard. Note: /federationProtocolDetails/0 is IdpDetails /federationProtocolDetails/1 is SpDetails Ensures that the patched ServiceProviderConfig conforms to certain logical guidelines, which are:   1. Do not add or remove any elements in the federation protocol details in the service provider configuration.   2. Do not modify, add, or delete the service provider details element in the federation protocol details.   3. If this is the first time the patched ServiceProviderConfig enables Remote IDP sign-in, it must also include IDPDetails.   4. If the patch enables Remote IDP sign in, the entityID in the IDPDetails cannot be null. IDPDetails must include an entityID.   5. Any JIT configuration update must be valid.  Just in time configuration update must be valid when enabled. This includes:   - A Source ID   - Source attribute mappings   - Source attribute maps have all the required key values (firstName, lastName, email)

    try:
        # Update Service Provider Configuration
        api_response = api_instance.patch_auth_org_service_provider_config(json_patch_operation)
        print("The response of GlobalTenantSecuritySettingsApi->patch_auth_org_service_provider_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GlobalTenantSecuritySettingsApi->patch_auth_org_service_provider_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **json_patch_operation** | [**List[JsonPatchOperation]**](JsonPatchOperation.md)| A list of auth org service provider configuration update operations according to the [JSON Patch](https://tools.ietf.org/html/rfc6902) standard. Note: /federationProtocolDetails/0 is IdpDetails /federationProtocolDetails/1 is SpDetails Ensures that the patched ServiceProviderConfig conforms to certain logical guidelines, which are:   1. Do not add or remove any elements in the federation protocol details in the service provider configuration.   2. Do not modify, add, or delete the service provider details element in the federation protocol details.   3. If this is the first time the patched ServiceProviderConfig enables Remote IDP sign-in, it must also include IDPDetails.   4. If the patch enables Remote IDP sign in, the entityID in the IDPDetails cannot be null. IDPDetails must include an entityID.   5. Any JIT configuration update must be valid.  Just in time configuration update must be valid when enabled. This includes:   - A Source ID   - Source attribute mappings   - Source attribute maps have all the required key values (firstName, lastName, email) | 

### Return type

[**ServiceProviderConfiguration**](ServiceProviderConfiguration.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Auth Org Service Provider configuration updated. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_auth_org_session_config**
> SessionConfiguration patch_auth_org_session_config(json_patch_operation)

Update Auth Org Session Configuration

This API updates an existing session configuration for an org using PATCH.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import sailpoint.v3
from sailpoint.v3.models.json_patch_operation import JsonPatchOperation
from sailpoint.v3.models.session_configuration import SessionConfiguration
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
    json_patch_operation = [{op=replace, path=/rememberMe, value=true,}, {op=add, path=/maxSessionTime, value=480}] # List[JsonPatchOperation] | A list of auth org session configuration update operations according to the [JSON Patch](https://tools.ietf.org/html/rfc6902) standard. Ensures that the patched Session Config conforms to certain logical guidelines, which are:   1. maxSessionTime >= 1 && maxSessionTime <= 10080 (1 week)   2. maxIdleTime >= 1 && maxIdleTime <= 1440 (1 day)   3. maxSessionTime must have a greater duration than maxIdleTime.

    try:
        # Update Auth Org Session Configuration
        api_response = api_instance.patch_auth_org_session_config(json_patch_operation)
        print("The response of GlobalTenantSecuritySettingsApi->patch_auth_org_session_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GlobalTenantSecuritySettingsApi->patch_auth_org_session_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **json_patch_operation** | [**List[JsonPatchOperation]**](JsonPatchOperation.md)| A list of auth org session configuration update operations according to the [JSON Patch](https://tools.ietf.org/html/rfc6902) standard. Ensures that the patched Session Config conforms to certain logical guidelines, which are:   1. maxSessionTime &gt;&#x3D; 1 &amp;&amp; maxSessionTime &lt;&#x3D; 10080 (1 week)   2. maxIdleTime &gt;&#x3D; 1 &amp;&amp; maxIdleTime &lt;&#x3D; 1440 (1 day)   3. maxSessionTime must have a greater duration than maxIdleTime. | 

### Return type

[**SessionConfiguration**](SessionConfiguration.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated Auth Org session configuration. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

