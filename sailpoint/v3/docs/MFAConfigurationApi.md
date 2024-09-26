# sailpoint.v3.MFAConfigurationApi

All URIs are relative to *https://sailpoint.api.identitynow.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_mfa_config**](MFAConfigurationApi.md#delete_mfa_config) | **DELETE** /mfa/{method}/delete | Delete MFA method configuration
[**get_mfa_duo_config**](MFAConfigurationApi.md#get_mfa_duo_config) | **GET** /mfa/duo-web/config | Configuration of Duo MFA method
[**get_mfa_kba_config**](MFAConfigurationApi.md#get_mfa_kba_config) | **GET** /mfa/kba/config | Configuration of KBA MFA method
[**get_mfa_okta_config**](MFAConfigurationApi.md#get_mfa_okta_config) | **GET** /mfa/okta-verify/config | Configuration of Okta MFA method
[**set_mfa_duo_config**](MFAConfigurationApi.md#set_mfa_duo_config) | **PUT** /mfa/duo-web/config | Set Duo MFA configuration
[**set_mfa_okta_config**](MFAConfigurationApi.md#set_mfa_okta_config) | **PUT** /mfa/okta-verify/config | Set Okta MFA configuration
[**set_mfakba_config**](MFAConfigurationApi.md#set_mfakba_config) | **POST** /mfa/kba/config/answers | Set MFA KBA configuration
[**test_mfa_config**](MFAConfigurationApi.md#test_mfa_config) | **GET** /mfa/{method}/test | MFA method&#39;s test configuration


# **delete_mfa_config**
> MfaOktaConfig delete_mfa_config(method)

Delete MFA method configuration

This API removes the configuration for the specified MFA method. A token with ORG_ADMIN authority is required to call this API.

### Example

* OAuth Authentication (userAuth):
* OAuth Authentication (userAuth):

```python
import sailpoint.v3
from sailpoint.v3.models.mfa_okta_config import MfaOktaConfig
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
    api_instance = sailpoint.v3.MFAConfigurationApi(api_client)
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

[userAuth](../README.md#userAuth), [userAuth](../README.md#userAuth)

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

* OAuth Authentication (userAuth):
* OAuth Authentication (userAuth):

```python
import sailpoint.v3
from sailpoint.v3.models.mfa_duo_config import MfaDuoConfig
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
    api_instance = sailpoint.v3.MFAConfigurationApi(api_client)

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

[userAuth](../README.md#userAuth), [userAuth](../README.md#userAuth)

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

# **get_mfa_kba_config**
> List[KbaQuestion] get_mfa_kba_config(all_languages=all_languages)

Configuration of KBA MFA method

This API returns the KBA configuration for MFA. A token with USER or ORG_ADMIN authority is required to call this API.

### Example

* OAuth Authentication (userAuth):
* OAuth Authentication (userAuth):

```python
import sailpoint.v3
from sailpoint.v3.models.kba_question import KbaQuestion
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
    api_instance = sailpoint.v3.MFAConfigurationApi(api_client)
    all_languages = allLanguages=true # bool | Indicator whether the question text should be returned in all configured languages    * If true, the question text is returned in all languages that it is configured in.    * If false, the question text is returned in the user locale if available, else for the default locale.     * If not passed, it behaves the same way as passing this parameter as false (optional)

    try:
        # Configuration of KBA MFA method
        api_response = api_instance.get_mfa_kba_config(all_languages=all_languages)
        print("The response of MFAConfigurationApi->get_mfa_kba_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MFAConfigurationApi->get_mfa_kba_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **all_languages** | **bool**| Indicator whether the question text should be returned in all configured languages    * If true, the question text is returned in all languages that it is configured in.    * If false, the question text is returned in the user locale if available, else for the default locale.     * If not passed, it behaves the same way as passing this parameter as false | [optional] 

### Return type

[**List[KbaQuestion]**](KbaQuestion.md)

### Authorization

[userAuth](../README.md#userAuth), [userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The configuration for KBA MFA method. |  -  |
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

* OAuth Authentication (userAuth):
* OAuth Authentication (userAuth):

```python
import sailpoint.v3
from sailpoint.v3.models.mfa_okta_config import MfaOktaConfig
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
    api_instance = sailpoint.v3.MFAConfigurationApi(api_client)

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

[userAuth](../README.md#userAuth), [userAuth](../README.md#userAuth)

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

* OAuth Authentication (userAuth):
* OAuth Authentication (userAuth):

```python
import sailpoint.v3
from sailpoint.v3.models.mfa_duo_config import MfaDuoConfig
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
    api_instance = sailpoint.v3.MFAConfigurationApi(api_client)
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

[userAuth](../README.md#userAuth), [userAuth](../README.md#userAuth)

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

* OAuth Authentication (userAuth):
* OAuth Authentication (userAuth):

```python
import sailpoint.v3
from sailpoint.v3.models.mfa_okta_config import MfaOktaConfig
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
    api_instance = sailpoint.v3.MFAConfigurationApi(api_client)
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

[userAuth](../README.md#userAuth), [userAuth](../README.md#userAuth)

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

# **set_mfakba_config**
> List[KbaAnswerResponseItem] set_mfakba_config(kba_answer_request_item)

Set MFA KBA configuration

This API sets answers to challenge questions.  Any configured questions omitted from the request are removed from user KBA configuration. A token with USER authority is required to call this API.

### Example

* OAuth Authentication (userAuth):
* OAuth Authentication (userAuth):

```python
import sailpoint.v3
from sailpoint.v3.models.kba_answer_request_item import KbaAnswerRequestItem
from sailpoint.v3.models.kba_answer_response_item import KbaAnswerResponseItem
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
    api_instance = sailpoint.v3.MFAConfigurationApi(api_client)
    kba_answer_request_item = [{id=173423, answer=822cd15d6c15aa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a0859a2fea34}, {id=c54fee53-2d63-4fc5-9259-3e93b9994135, answer=9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08}] # List[KbaAnswerRequestItem] | 

    try:
        # Set MFA KBA configuration
        api_response = api_instance.set_mfakba_config(kba_answer_request_item)
        print("The response of MFAConfigurationApi->set_mfakba_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MFAConfigurationApi->set_mfakba_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kba_answer_request_item** | [**List[KbaAnswerRequestItem]**](KbaAnswerRequestItem.md)|  | 

### Return type

[**List[KbaAnswerResponseItem]**](KbaAnswerResponseItem.md)

### Authorization

[userAuth](../README.md#userAuth), [userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The new KBA configuration for the user. |  -  |
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

* OAuth Authentication (userAuth):
* OAuth Authentication (userAuth):

```python
import sailpoint.v3
from sailpoint.v3.models.mfa_config_test_response import MfaConfigTestResponse
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
    api_instance = sailpoint.v3.MFAConfigurationApi(api_client)
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

[userAuth](../README.md#userAuth), [userAuth](../README.md#userAuth)

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

