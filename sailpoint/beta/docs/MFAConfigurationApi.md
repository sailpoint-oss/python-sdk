# sailpoint.beta.MFAConfigurationApi

All URIs are relative to *https://sailpoint.api.identitynow.com/beta*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_mfa_config**](MFAConfigurationApi.md#delete_mfa_config) | **DELETE** /mfa/{method}/delete | Delete MFA method configuration
[**get_mfa_duo_config**](MFAConfigurationApi.md#get_mfa_duo_config) | **GET** /mfa/duo-web/config | Configuration of Duo MFA method
[**get_mfa_okta_config**](MFAConfigurationApi.md#get_mfa_okta_config) | **GET** /mfa/okta-verify/config | Configuration of Okta MFA method
[**set_mfa_duo_config**](MFAConfigurationApi.md#set_mfa_duo_config) | **PUT** /mfa/duo-web/config | Set Duo MFA configuration
[**set_mfa_okta_config**](MFAConfigurationApi.md#set_mfa_okta_config) | **PUT** /mfa/okta-verify/config | Set Okta MFA configuration
[**test_mfa_config**](MFAConfigurationApi.md#test_mfa_config) | **GET** /mfa/{method}/test | MFA method&#39;s test configuration


# **delete_mfa_config**
> MfaOktaConfig delete_mfa_config(method)

Delete MFA method configuration

This API removes the configuration for the specified MFA method. A token with ORG_ADMIN authority is required to call this API.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.beta
from sailpoint.beta.models.mfa_okta_config import MfaOktaConfig
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
    api_instance = sailpoint.beta.MFAConfigurationApi(api_client)
    method = 'okta-verify' # str | The name of the MFA method. The currently supported method names are 'okta-verify' and 'duo-web'.

    try:
        # Delete MFA method configuration
        api_response = api_instance.delete_mfa_config(method)
        print("The response of MFAConfigurationApi->delete_mfa_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MFAConfigurationApi->delete_mfa_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **method** | **str**| The name of the MFA method. The currently supported method names are &#39;okta-verify&#39; and &#39;duo-web&#39;. | 

### Return type

[**MfaOktaConfig**](MfaOktaConfig.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | MFA configuration of an MFA method. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mfa_duo_config**
> MfaDuoConfig get_mfa_duo_config()

Configuration of Duo MFA method

This API returns the configuration of an Duo MFA method. A token with ORG_ADMIN authority is required to call this API.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.beta
from sailpoint.beta.models.mfa_duo_config import MfaDuoConfig
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
    api_instance = sailpoint.beta.MFAConfigurationApi(api_client)

    try:
        # Configuration of Duo MFA method
        api_response = api_instance.get_mfa_duo_config()
        print("The response of MFAConfigurationApi->get_mfa_duo_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MFAConfigurationApi->get_mfa_duo_config: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**MfaDuoConfig**](MfaDuoConfig.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The configuration of an Duo MFA method. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mfa_okta_config**
> MfaOktaConfig get_mfa_okta_config()

Configuration of Okta MFA method

This API returns the configuration of an Okta MFA method. A token with ORG_ADMIN authority is required to call this API.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.beta
from sailpoint.beta.models.mfa_okta_config import MfaOktaConfig
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
    api_instance = sailpoint.beta.MFAConfigurationApi(api_client)

    try:
        # Configuration of Okta MFA method
        api_response = api_instance.get_mfa_okta_config()
        print("The response of MFAConfigurationApi->get_mfa_okta_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MFAConfigurationApi->get_mfa_okta_config: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**MfaOktaConfig**](MfaOktaConfig.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The configuration of an Okta MFA method. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_mfa_duo_config**
> MfaDuoConfig set_mfa_duo_config(mfa_duo_config)

Set Duo MFA configuration

This API sets the configuration of an Duo MFA method. A token with ORG_ADMIN authority is required to call this API.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.beta
from sailpoint.beta.models.mfa_duo_config import MfaDuoConfig
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
    api_instance = sailpoint.beta.MFAConfigurationApi(api_client)
    mfa_duo_config = {mfaMethod=duo-web, enabled=true, host=www.example.com, accessKey=qw123Y3QlA5UqocYpdU3rEkzrK2D497y, identityAttribute=email, configProperties={skey=12q3WERlcUHWJmiMqyCXI3uOF7EaDJTbdeOp6E2B, ikey=Q123WE45R6TY7890ZXCV}} # MfaDuoConfig | 

    try:
        # Set Duo MFA configuration
        api_response = api_instance.set_mfa_duo_config(mfa_duo_config)
        print("The response of MFAConfigurationApi->set_mfa_duo_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MFAConfigurationApi->set_mfa_duo_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mfa_duo_config** | [**MfaDuoConfig**](MfaDuoConfig.md)|  | 

### Return type

[**MfaDuoConfig**](MfaDuoConfig.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | MFA configuration of an Duo MFA method. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_mfa_okta_config**
> MfaOktaConfig set_mfa_okta_config(mfa_okta_config)

Set Okta MFA configuration

This API sets the configuration of an Okta MFA method. A token with ORG_ADMIN authority is required to call this API.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.beta
from sailpoint.beta.models.mfa_okta_config import MfaOktaConfig
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
    api_instance = sailpoint.beta.MFAConfigurationApi(api_client)
    mfa_okta_config = {mfaMethod=okta-verify, enabled=true, host=www.example.com, accessKey=dk778Y3QlA5UqocYpdU3rEkzrK2D497y, identityAttribute=email} # MfaOktaConfig | 

    try:
        # Set Okta MFA configuration
        api_response = api_instance.set_mfa_okta_config(mfa_okta_config)
        print("The response of MFAConfigurationApi->set_mfa_okta_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MFAConfigurationApi->set_mfa_okta_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mfa_okta_config** | [**MfaOktaConfig**](MfaOktaConfig.md)|  | 

### Return type

[**MfaOktaConfig**](MfaOktaConfig.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | MFA configuration of an Okta MFA method. |  -  |
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
import sailpoint.beta
from sailpoint.beta.models.mfa_config_test_response import MfaConfigTestResponse
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
    api_instance = sailpoint.beta.MFAConfigurationApi(api_client)
    method = 'okta-verify' # str | The name of the MFA method. The currently supported method names are 'okta-verify' and 'duo-web'.

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
 **method** | **str**| The name of the MFA method. The currently supported method names are &#39;okta-verify&#39; and &#39;duo-web&#39;. | 

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

