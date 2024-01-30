# sailpoint.v3.PasswordConfigurationApi

All URIs are relative to *https://sailpoint.api.identitynow.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_password_org_config**](PasswordConfigurationApi.md#create_password_org_config) | **POST** /password-org-config | Create Password Org Config
[**get_password_org_config**](PasswordConfigurationApi.md#get_password_org_config) | **GET** /password-org-config | Get Password Org Config
[**put_password_org_config**](PasswordConfigurationApi.md#put_password_org_config) | **PUT** /password-org-config | Update Password Org Config


# **create_password_org_config**
> PasswordOrgConfig create_password_org_config(password_org_config)

Create Password Org Config

This API creates the password org config. Unspecified fields will use default value. To be able to use the custom password instructions, you must set the `customInstructionsEnabled` field to \"true\". Requires ORG_ADMIN, API role or authorization scope of 'idn:password-org-config:write'

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.v3
from sailpoint.v3.models.password_org_config import PasswordOrgConfig
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
    api_instance = sailpoint.v3.PasswordConfigurationApi(api_client)
    password_org_config = {customInstructionsEnabled=true, digitTokenEnabled=true, digitTokenDurationMinutes=12, digitTokenLength=9} # PasswordOrgConfig | 

    try:
        # Create Password Org Config
        api_response = api_instance.create_password_org_config(password_org_config)
        print("The response of PasswordConfigurationApi->create_password_org_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PasswordConfigurationApi->create_password_org_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **password_org_config** | [**PasswordOrgConfig**](PasswordOrgConfig.md)|  | 

### Return type

[**PasswordOrgConfig**](PasswordOrgConfig.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Reference to the password org config. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_password_org_config**
> PasswordOrgConfig get_password_org_config()

Get Password Org Config

This API returns the password org config . Requires ORG_ADMIN, API role or authorization scope of 'idn:password-org-config:read'

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.v3
from sailpoint.v3.models.password_org_config import PasswordOrgConfig
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
    api_instance = sailpoint.v3.PasswordConfigurationApi(api_client)

    try:
        # Get Password Org Config
        api_response = api_instance.get_password_org_config()
        print("The response of PasswordConfigurationApi->get_password_org_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PasswordConfigurationApi->get_password_org_config: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**PasswordOrgConfig**](PasswordOrgConfig.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Reference to the password org config. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_password_org_config**
> PasswordOrgConfig put_password_org_config(password_org_config)

Update Password Org Config

This API updates the password org config for specified fields. Other fields will keep original value. You must set the `customInstructionsEnabled` field to \"true\" to be able to use custom password instructions.  Requires ORG_ADMIN, API role or authorization scope of 'idn:password-org-config:write'

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.v3
from sailpoint.v3.models.password_org_config import PasswordOrgConfig
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
    api_instance = sailpoint.v3.PasswordConfigurationApi(api_client)
    password_org_config = {digitTokenEnabled=true, digitTokenDurationMinutes=12} # PasswordOrgConfig | 

    try:
        # Update Password Org Config
        api_response = api_instance.put_password_org_config(password_org_config)
        print("The response of PasswordConfigurationApi->put_password_org_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PasswordConfigurationApi->put_password_org_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **password_org_config** | [**PasswordOrgConfig**](PasswordOrgConfig.md)|  | 

### Return type

[**PasswordOrgConfig**](PasswordOrgConfig.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Reference to the password org config. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

