# beta.MFAConfigurationApi

All URIs are relative to *https://sailpoint.api.identitynow.com/beta*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_mfa_config**](MFAConfigurationApi.md#get_mfa_config) | **GET** /mfa/{method}/config | Configuration of a MFA method
[**set_mfa_config**](MFAConfigurationApi.md#set_mfa_config) | **PUT** /mfa/{method}/config | Set MFA method configuration
[**test_mfa_config**](MFAConfigurationApi.md#test_mfa_config) | **GET** /mfa/{method}/test | MFA method&#39;s test configuration


# **get_mfa_config**
> MfaConfig get_mfa_config(method)

Configuration of a MFA method

This API returns the configuration of a given MFA method. A token with ORG_ADMIN authority is required to call this API.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import beta
from beta.models.mfa_config import MfaConfig
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
    api_instance = beta.MFAConfigurationApi(api_client)
    method = 'okta-verify' # str | The name of the MFA method. The currently supported method name is okta-verify.

    try:
        # Configuration of a MFA method
        api_response = api_instance.get_mfa_config(method)
        print("The response of MFAConfigurationApi->get_mfa_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MFAConfigurationApi->get_mfa_config: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **method** | **str**| The name of the MFA method. The currently supported method name is okta-verify. | 

### Return type

[**MfaConfig**](MfaConfig.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | MFA configuration of a given method. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_mfa_config**
> MfaConfig set_mfa_config(method, mfa_config)

Set MFA method configuration

This API sets the configuration of a given MFA method. A token with ORG_ADMIN authority is required to call this API.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import beta
from beta.models.mfa_config import MfaConfig
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
    api_instance = beta.MFAConfigurationApi(api_client)
    method = 'okta-verify' # str | The name of the MFA method. The currently supported method name is okta-verify.
    mfa_config = {enabled=true, host=www.example.com, accessKey=dk778Y3QlA5UqocYpdU3rEkzrK2D497y, identityAttribute=email} # MfaConfig | 

    try:
        # Set MFA method configuration
        api_response = api_instance.set_mfa_config(method, mfa_config)
        print("The response of MFAConfigurationApi->set_mfa_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MFAConfigurationApi->set_mfa_config: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **method** | **str**| The name of the MFA method. The currently supported method name is okta-verify. | 
 **mfa_config** | [**MfaConfig**](MfaConfig.md)|  | 

### Return type

[**MfaConfig**](MfaConfig.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | MFA configuration of a given method. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_mfa_config**
> MfaConfigTestResponse test_mfa_config(method)

MFA method's test configuration

This API validates that the configuration is valid and will properly authenticate with the MFA provider identified by the method path parameter. A token with ORG_ADMIN authority is required to call this API.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import beta
from beta.models.mfa_config_test_response import MfaConfigTestResponse
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
    api_instance = beta.MFAConfigurationApi(api_client)
    method = 'okta-verify' # str | The name of the MFA method. The currently supported method name is okta-verify.

    try:
        # MFA method's test configuration
        api_response = api_instance.test_mfa_config(method)
        print("The response of MFAConfigurationApi->test_mfa_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MFAConfigurationApi->test_mfa_config: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **method** | **str**| The name of the MFA method. The currently supported method name is okta-verify. | 

### Return type

[**MfaConfigTestResponse**](MfaConfigTestResponse.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The result of configuration test for the MFA provider. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

