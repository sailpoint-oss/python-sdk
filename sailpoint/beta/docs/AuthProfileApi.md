# sailpoint.beta.AuthProfileApi

All URIs are relative to *https://sailpoint.api.identitynow.com/beta*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_profile_config**](AuthProfileApi.md#get_profile_config) | **GET** /auth-profiles/{id} | Get Auth Profile.
[**get_profile_config_list**](AuthProfileApi.md#get_profile_config_list) | **GET** /auth-profiles | Get list of Auth Profiles.
[**patch_profile_config**](AuthProfileApi.md#patch_profile_config) | **PATCH** /auth-profiles/{id} | Patch a specified Auth Profile


# **get_profile_config**
> AuthProfile get_profile_config()

Get Auth Profile.

This API returns auth profile information.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.beta
from sailpoint.beta.models.auth_profile import AuthProfile
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
    api_instance = sailpoint.beta.AuthProfileApi(api_client)

    try:
        # Get Auth Profile.
        api_response = api_instance.get_profile_config()
        print("The response of AuthProfileApi->get_profile_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthProfileApi->get_profile_config: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AuthProfile**](AuthProfile.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Auth Profile |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_profile_config_list**
> List[AuthProfileSummary] get_profile_config_list()

Get list of Auth Profiles.

This API returns a list of auth profiles.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.beta
from sailpoint.beta.models.auth_profile_summary import AuthProfileSummary
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
    api_instance = sailpoint.beta.AuthProfileApi(api_client)

    try:
        # Get list of Auth Profiles.
        api_response = api_instance.get_profile_config_list()
        print("The response of AuthProfileApi->get_profile_config_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthProfileApi->get_profile_config_list: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[AuthProfileSummary]**](AuthProfileSummary.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of Auth Profiles |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_profile_config**
> AuthProfile patch_profile_config(id, json_patch_operation)

Patch a specified Auth Profile

This API updates an existing Auth Profile. The following fields are patchable: **offNetwork**, **untrustedGeography**, **applicationId**, **applicationName**, **type**

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.beta
from sailpoint.beta.models.auth_profile import AuthProfile
from sailpoint.beta.models.json_patch_operation import JsonPatchOperation
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
    api_instance = sailpoint.beta.AuthProfileApi(api_client)
    id = '2c91808a7813090a017814121919ecca' # str | ID of the Auth Profile to patch.
    json_patch_operation = [sailpoint.beta.JsonPatchOperation()] # List[JsonPatchOperation] | 

    try:
        # Patch a specified Auth Profile
        api_response = api_instance.patch_profile_config(id, json_patch_operation)
        print("The response of AuthProfileApi->patch_profile_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthProfileApi->patch_profile_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the Auth Profile to patch. | 
 **json_patch_operation** | [**List[JsonPatchOperation]**](JsonPatchOperation.md)|  | 

### Return type

[**AuthProfile**](AuthProfile.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Responds with the Auth Profile as updated. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

