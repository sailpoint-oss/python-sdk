# sailpoint.v3.AuthUsersApi

All URIs are relative to *https://sailpoint.api.identitynow.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_auth_user**](AuthUsersApi.md#get_auth_user) | **GET** /auth-users/{id} | Auth User Details
[**patch_auth_user**](AuthUsersApi.md#patch_auth_user) | **PATCH** /auth-users/{id} | Auth User Update


# **get_auth_user**
> AuthUser get_auth_user(id)

Auth User Details

Return the specified user's authentication system details.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.v3
from sailpoint.v3.models.auth_user import AuthUser
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
    api_instance = sailpoint.v3.AuthUsersApi(api_client)
    id = 'ef38f94347e94562b5bb8424a56397d8' # str | Identity ID

    try:
        # Auth User Details
        api_response = api_instance.get_auth_user(id)
        print("The response of AuthUsersApi->get_auth_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthUsersApi->get_auth_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identity ID | 

### Return type

[**AuthUser**](AuthUser.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The specified user&#39;s authentication system details. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_auth_user**
> AuthUser patch_auth_user(id, json_patch_operation)

Auth User Update

Use a PATCH request to update an existing user in the authentication system. Use this endpoint to modify these fields:    * `capabilities`  A '400.1.1 Illegal update attempt' detail code indicates that you attempted to PATCH a field that is not allowed.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.v3
from sailpoint.v3.models.auth_user import AuthUser
from sailpoint.v3.models.json_patch_operation import JsonPatchOperation
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
    api_instance = sailpoint.v3.AuthUsersApi(api_client)
    id = 'ef38f94347e94562b5bb8424a56397d8' # str | Identity ID
    json_patch_operation = [{op=replace, path=/capabilities, value=[ORG_ADMIN]}] # List[JsonPatchOperation] | A list of auth user update operations according to the [JSON Patch](https://tools.ietf.org/html/rfc6902) standard.

    try:
        # Auth User Update
        api_response = api_instance.patch_auth_user(id, json_patch_operation)
        print("The response of AuthUsersApi->patch_auth_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthUsersApi->patch_auth_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identity ID | 
 **json_patch_operation** | [**List[JsonPatchOperation]**](JsonPatchOperation.md)| A list of auth user update operations according to the [JSON Patch](https://tools.ietf.org/html/rfc6902) standard. | 

### Return type

[**AuthUser**](AuthUser.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Auth user updated. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

