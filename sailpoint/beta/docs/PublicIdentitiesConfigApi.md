# sailpoint.beta.PublicIdentitiesConfigApi

All URIs are relative to *https://sailpoint.api.identitynow.com/beta*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_public_identity_config**](PublicIdentitiesConfigApi.md#get_public_identity_config) | **GET** /public-identities-config | Get Public Identity Config
[**update_public_identity_config**](PublicIdentitiesConfigApi.md#update_public_identity_config) | **PUT** /public-identities-config | Update Public Identity Config


# **get_public_identity_config**
> PublicIdentityConfig get_public_identity_config()

Get Public Identity Config

This gets details of public identity config.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import sailpoint.beta
from sailpoint.beta.models.public_identity_config import PublicIdentityConfig
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
    api_instance = sailpoint.beta.PublicIdentitiesConfigApi(api_client)

    try:
        # Get Public Identity Config
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

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

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

Update Public Identity Config

This updates the details of public identity config.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import sailpoint.beta
from sailpoint.beta.models.public_identity_config import PublicIdentityConfig
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
    api_instance = sailpoint.beta.PublicIdentitiesConfigApi(api_client)
    public_identity_config = sailpoint.beta.PublicIdentityConfig() # PublicIdentityConfig | 

    try:
        # Update Public Identity Config
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

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

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

