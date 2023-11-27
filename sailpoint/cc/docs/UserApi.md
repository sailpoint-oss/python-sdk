# sailpoint.cc.UserApi

All URIs are relative to *https://sailpoint.api.identitynow.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_identity**](UserApi.md#get_identity) | **GET** /cc/api/user/get/{id} | Get Single Identity
[**update_user_permissions**](UserApi.md#update_user_permissions) | **POST** /cc/api/user/updatePermissions | Update User Permissions


# **get_identity**
> GetIdentity200Response get_identity(id)

Get Single Identity

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import sailpoint.cc
from sailpoint.cc.models.get_identity200_response import GetIdentity200Response
from sailpoint.cc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.cc.Configuration(
    host = "https://sailpoint.api.identitynow.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.cc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.cc.UserApi(api_client)
    id = '5433236' # str | 

    try:
        # Get Single Identity
        api_response = api_instance.get_identity(id)
        print("The response of UserApi->get_identity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->get_identity: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**GetIdentity200Response**](GetIdentity200Response.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_permissions**
> update_user_permissions(update_user_permissions_request=update_user_permissions_request)

Update User Permissions

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import sailpoint.cc
from sailpoint.cc.models.update_user_permissions_request import UpdateUserPermissionsRequest
from sailpoint.cc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.cc.Configuration(
    host = "https://sailpoint.api.identitynow.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.cc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.cc.UserApi(api_client)
    update_user_permissions_request = sailpoint.cc.UpdateUserPermissionsRequest() # UpdateUserPermissionsRequest |  (optional)

    try:
        # Update User Permissions
        api_instance.update_user_permissions(update_user_permissions_request=update_user_permissions_request)
    except Exception as e:
        print("Exception when calling UserApi->update_user_permissions: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_user_permissions_request** | [**UpdateUserPermissionsRequest**](UpdateUserPermissionsRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

