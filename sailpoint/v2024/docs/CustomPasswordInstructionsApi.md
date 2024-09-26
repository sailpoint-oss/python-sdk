# sailpoint.v2024.CustomPasswordInstructionsApi

All URIs are relative to *https://sailpoint.api.identitynow.com/v2024*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_custom_password_instructions**](CustomPasswordInstructionsApi.md#create_custom_password_instructions) | **POST** /custom-password-instructions | Create Custom Password Instructions
[**delete_custom_password_instructions**](CustomPasswordInstructionsApi.md#delete_custom_password_instructions) | **DELETE** /custom-password-instructions/{pageId} | Delete Custom Password Instructions by page ID
[**get_custom_password_instructions**](CustomPasswordInstructionsApi.md#get_custom_password_instructions) | **GET** /custom-password-instructions/{pageId} | Get Custom Password Instructions by Page ID


# **create_custom_password_instructions**
> CustomPasswordInstruction create_custom_password_instructions(x_sail_point_experimental, custom_password_instruction)

Create Custom Password Instructions

This API creates the custom password instructions for the specified page ID. A token with ORG_ADMIN authority is required to call this API.

### Example

* OAuth Authentication (userAuth):
* OAuth Authentication (userAuth):

```python
import sailpoint.v2024
from sailpoint.v2024.models.custom_password_instruction import CustomPasswordInstruction
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
    api_instance = sailpoint.v2024.CustomPasswordInstructionsApi(api_client)
    x_sail_point_experimental = 'true' # str | Use this header to enable this experimental API. (default to 'true')
    custom_password_instruction = {pageId=reset-password:enter-password, pageContent=See company password policies for details by clicking <a href="url">here</a>} # CustomPasswordInstruction | 

    try:
        # Create Custom Password Instructions
        api_response = api_instance.create_custom_password_instructions(x_sail_point_experimental, custom_password_instruction)
        print("The response of CustomPasswordInstructionsApi->create_custom_password_instructions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomPasswordInstructionsApi->create_custom_password_instructions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_sail_point_experimental** | **str**| Use this header to enable this experimental API. | [default to &#39;true&#39;]
 **custom_password_instruction** | [**CustomPasswordInstruction**](CustomPasswordInstruction.md)|  | 

### Return type

[**CustomPasswordInstruction**](CustomPasswordInstruction.md)

### Authorization

[userAuth](../README.md#userAuth), [userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Reference to the custom password instructions. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_custom_password_instructions**
> delete_custom_password_instructions(page_id, x_sail_point_experimental, locale=locale)

Delete Custom Password Instructions by page ID

This API delete the custom password instructions for the specified page ID. A token with ORG_ADMIN authority is required to call this API.

### Example

* OAuth Authentication (userAuth):
* OAuth Authentication (userAuth):

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
    api_instance = sailpoint.v2024.CustomPasswordInstructionsApi(api_client)
    page_id = 'mfa:select' # str | The page ID of custom password instructions to delete.
    x_sail_point_experimental = 'true' # str | Use this header to enable this experimental API. (default to 'true')
    locale = 'locale_example' # str | The locale for the custom instructions, a BCP47 language tag. The default value is \\\"default\\\". (optional)

    try:
        # Delete Custom Password Instructions by page ID
        api_instance.delete_custom_password_instructions(page_id, x_sail_point_experimental, locale=locale)
    except Exception as e:
        print("Exception when calling CustomPasswordInstructionsApi->delete_custom_password_instructions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| The page ID of custom password instructions to delete. | 
 **x_sail_point_experimental** | **str**| Use this header to enable this experimental API. | [default to &#39;true&#39;]
 **locale** | **str**| The locale for the custom instructions, a BCP47 language tag. The default value is \\\&quot;default\\\&quot;. | [optional] 

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
**204** | No content - indicates the request was successful but there is no content to be returned in the response. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_custom_password_instructions**
> CustomPasswordInstruction get_custom_password_instructions(page_id, x_sail_point_experimental, locale=locale)

Get Custom Password Instructions by Page ID

This API returns the custom password instructions for the specified page ID. A token with ORG_ADMIN authority is required to call this API.

### Example

* OAuth Authentication (userAuth):
* OAuth Authentication (userAuth):

```python
import sailpoint.v2024
from sailpoint.v2024.models.custom_password_instruction import CustomPasswordInstruction
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
    api_instance = sailpoint.v2024.CustomPasswordInstructionsApi(api_client)
    page_id = 'mfa:select' # str | The page ID of custom password instructions to query.
    x_sail_point_experimental = 'true' # str | Use this header to enable this experimental API. (default to 'true')
    locale = 'locale_example' # str | The locale for the custom instructions, a BCP47 language tag. The default value is \\\"default\\\". (optional)

    try:
        # Get Custom Password Instructions by Page ID
        api_response = api_instance.get_custom_password_instructions(page_id, x_sail_point_experimental, locale=locale)
        print("The response of CustomPasswordInstructionsApi->get_custom_password_instructions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomPasswordInstructionsApi->get_custom_password_instructions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| The page ID of custom password instructions to query. | 
 **x_sail_point_experimental** | **str**| Use this header to enable this experimental API. | [default to &#39;true&#39;]
 **locale** | **str**| The locale for the custom instructions, a BCP47 language tag. The default value is \\\&quot;default\\\&quot;. | [optional] 

### Return type

[**CustomPasswordInstruction**](CustomPasswordInstruction.md)

### Authorization

[userAuth](../README.md#userAuth), [userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Reference to the custom password instructions. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

