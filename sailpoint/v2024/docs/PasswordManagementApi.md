# sailpoint.v2024.PasswordManagementApi

All URIs are relative to *https://sailpoint.api.identitynow.com/v2024*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_digit_token**](PasswordManagementApi.md#create_digit_token) | **POST** /generate-password-reset-token/digit | Generate a digit token
[**get_password_change_status**](PasswordManagementApi.md#get_password_change_status) | **GET** /password-change-status/{id} | Get Password Change Request Status
[**query_password_info**](PasswordManagementApi.md#query_password_info) | **POST** /query-password-info | Query Password Info
[**set_password**](PasswordManagementApi.md#set_password) | **POST** /set-password | Set Identity&#39;s Password


# **create_digit_token**
> PasswordDigitToken create_digit_token(x_sail_point_experimental, password_digit_token_reset)

Generate a digit token

This API is used to generate a digit token for password management. Requires authorization scope of \"idn:password-digit-token:create\".

### Example

* OAuth Authentication (userAuth):
* OAuth Authentication (userAuth):

```python
import sailpoint.v2024
from sailpoint.v2024.models.password_digit_token import PasswordDigitToken
from sailpoint.v2024.models.password_digit_token_reset import PasswordDigitTokenReset
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
    api_instance = sailpoint.v2024.PasswordManagementApi(api_client)
    x_sail_point_experimental = 'true' # str | Use this header to enable this experimental API. (default to 'true')
    password_digit_token_reset = {userId=Abby.Smith, length=8, durationMinutes=5} # PasswordDigitTokenReset | 

    try:
        # Generate a digit token
        api_response = api_instance.create_digit_token(x_sail_point_experimental, password_digit_token_reset)
        print("The response of PasswordManagementApi->create_digit_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PasswordManagementApi->create_digit_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_sail_point_experimental** | **str**| Use this header to enable this experimental API. | [default to &#39;true&#39;]
 **password_digit_token_reset** | [**PasswordDigitTokenReset**](PasswordDigitTokenReset.md)|  | 

### Return type

[**PasswordDigitToken**](PasswordDigitToken.md)

### Authorization

[userAuth](../README.md#userAuth), [userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The digit token for password management. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_password_change_status**
> PasswordStatus get_password_change_status(id)

Get Password Change Request Status

This API returns the status of a password change request.

### Example

* OAuth Authentication (userAuth):
* OAuth Authentication (userAuth):
* OAuth Authentication (applicationAuth):

```python
import sailpoint.v2024
from sailpoint.v2024.models.password_status import PasswordStatus
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.v2024.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.v2024.PasswordManagementApi(api_client)
    id = '089899f13a8f4da7824996191587bab9' # str | Password change request ID

    try:
        # Get Password Change Request Status
        api_response = api_instance.get_password_change_status(id)
        print("The response of PasswordManagementApi->get_password_change_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PasswordManagementApi->get_password_change_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Password change request ID | 

### Return type

[**PasswordStatus**](PasswordStatus.md)

### Authorization

[userAuth](../README.md#userAuth), [userAuth](../README.md#userAuth), [applicationAuth](../README.md#applicationAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Status of the password change request |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_password_info**
> PasswordInfo query_password_info(password_info_query_dto)

Query Password Info

This API is used to query password related information.  

### Example

* OAuth Authentication (applicationAuth):

```python
import sailpoint.v2024
from sailpoint.v2024.models.password_info import PasswordInfo
from sailpoint.v2024.models.password_info_query_dto import PasswordInfoQueryDTO
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

# Enter a context with an instance of the API client
with sailpoint.v2024.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.v2024.PasswordManagementApi(api_client)
    password_info_query_dto = sailpoint.v2024.PasswordInfoQueryDTO() # PasswordInfoQueryDTO | 

    try:
        # Query Password Info
        api_response = api_instance.query_password_info(password_info_query_dto)
        print("The response of PasswordManagementApi->query_password_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PasswordManagementApi->query_password_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **password_info_query_dto** | [**PasswordInfoQueryDTO**](PasswordInfoQueryDTO.md)|  | 

### Return type

[**PasswordInfo**](PasswordInfo.md)

### Authorization

[applicationAuth](../README.md#applicationAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Reference to the password info. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_password**
> PasswordChangeResponse set_password(password_change_request)

Set Identity's Password

This API is used to set a password for an identity.   An identity can change their own password (as well as any of their accounts' passwords) if they use a token generated by their ISC user, such as a [personal access token](https://developer.sailpoint.com/idn/api/authentication#personal-access-tokens) or [\"authorization_code\" derived OAuth token](https://developer.sailpoint.com/idn/api/authentication#authorization-code-grant-flow).  >**Note: If you want to set an identity's source account password, you must enable `PASSWORD` as one of the source's features. You can use the [PATCH Source endpoint](https://developer.sailpoint.com/docs/api/v3/update-source) to add the `PASSWORD` feature.**  To generate the encryptedPassword (RSA encrypted using publicKey) for the request body, run the following command:  ```bash echo -n \"myPassword\" | openssl pkeyutl -encrypt -inkey public_key.pem -pubin | base64 ```  In this example, myPassword is the plain text password being set and encrypted, and public_key.pem is the path to the public key file. You can retrieve the required publicKey, along with other information like identityId, sourceId, publicKeyId, accounts, and policies, using the Query Password Info endpoint.  To successfully run this command, you must have OpenSSL installed on your machine. If OpenSSL is unavailable, consider using the Virtual Appliance (VA), which has OpenSSL pre-installed and configured.  If you are using a Windows machine, refer to this [guide](https://tecadmin.net/install-openssl-on-windows/) for instructions on installing OpenSSL.  You can then use [Get Password Change Request Status](https://developer.sailpoint.com/idn/api/v3/get-password-change-status) to check the password change request status. To do so, you must provide the `requestId` from your earlier request to set the password.  

### Example

* OAuth Authentication (applicationAuth):

```python
import sailpoint.v2024
from sailpoint.v2024.models.password_change_request import PasswordChangeRequest
from sailpoint.v2024.models.password_change_response import PasswordChangeResponse
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

# Enter a context with an instance of the API client
with sailpoint.v2024.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.v2024.PasswordManagementApi(api_client)
    password_change_request = sailpoint.v2024.PasswordChangeRequest() # PasswordChangeRequest | 

    try:
        # Set Identity's Password
        api_response = api_instance.set_password(password_change_request)
        print("The response of PasswordManagementApi->set_password:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PasswordManagementApi->set_password: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **password_change_request** | [**PasswordChangeRequest**](PasswordChangeRequest.md)|  | 

### Return type

[**PasswordChangeResponse**](PasswordChangeResponse.md)

### Authorization

[applicationAuth](../README.md#applicationAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Reference to the password change. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

