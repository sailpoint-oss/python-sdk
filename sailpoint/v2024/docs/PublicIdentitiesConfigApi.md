# sailpoint.v2024.PublicIdentitiesConfigApi

All URIs are relative to *https://sailpoint.api.identitynow.com/v2024*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_public_identity_config**](PublicIdentitiesConfigApi.md#get_public_identity_config) | **GET** /public-identities-config | Get the Public Identities Configuration
[**update_public_identity_config**](PublicIdentitiesConfigApi.md#update_public_identity_config) | **PUT** /public-identities-config | Update the Public Identities Configuration


# **get_public_identity_config**
> PublicIdentityConfig get_public_identity_config()

Get the Public Identities Configuration

Returns the publicly visible attributes of an identity available to request approvers for Access Requests and Certification Campaigns. A token with ORG ADMIN authority is required to call this API.

### Example

* OAuth Authentication (userAuth):
* OAuth Authentication (userAuth):

```python
import sailpoint.v2024
from sailpoint.v2024.models.public_identity_config import PublicIdentityConfig
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
    api_instance = sailpoint.v2024.PublicIdentitiesConfigApi(api_client)

    try:
        # Get the Public Identities Configuration
        api_response = api_instance.get_public_identity_config()
        print("The response of PublicIdentitiesConfigApi->get_public_identity_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicIdentitiesConfigApi->get_public_identity_config: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**PublicIdentityConfig**](PublicIdentityConfig.md)

### Authorization

[userAuth](../README.md#userAuth), [userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request succeeded. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_public_identity_config**
> PublicIdentityConfig update_public_identity_config(public_identity_config)

Update the Public Identities Configuration

Updates the publicly visible attributes of an identity available to request approvers for Access Requests and Certification Campaigns. A token with ORG ADMIN authority is required to call this API.

### Example

* OAuth Authentication (userAuth):
* OAuth Authentication (userAuth):

```python
import sailpoint.v2024
from sailpoint.v2024.models.public_identity_config import PublicIdentityConfig
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
    api_instance = sailpoint.v2024.PublicIdentitiesConfigApi(api_client)
    public_identity_config = sailpoint.v2024.PublicIdentityConfig() # PublicIdentityConfig | 

    try:
        # Update the Public Identities Configuration
        api_response = api_instance.update_public_identity_config(public_identity_config)
        print("The response of PublicIdentitiesConfigApi->update_public_identity_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicIdentitiesConfigApi->update_public_identity_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **public_identity_config** | [**PublicIdentityConfig**](PublicIdentityConfig.md)|  | 

### Return type

[**PublicIdentityConfig**](PublicIdentityConfig.md)

### Authorization

[userAuth](../README.md#userAuth), [userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request succeeded. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

