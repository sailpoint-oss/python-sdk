# sailpoint.beta.PasswordPoliciesApi

All URIs are relative to *https://sailpoint.api.identitynow.com/beta*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_password_policy**](PasswordPoliciesApi.md#create_password_policy) | **POST** /password-policies | Create Password Policy
[**delete_password_policy**](PasswordPoliciesApi.md#delete_password_policy) | **DELETE** /password-policies/{id} | Delete Password Policy by ID
[**get_password_policy_by_id**](PasswordPoliciesApi.md#get_password_policy_by_id) | **GET** /password-policies/{id} | Get Password Policy by ID
[**list_password_policies**](PasswordPoliciesApi.md#list_password_policies) | **GET** /password-policies | List Password Policies
[**set_password_policy**](PasswordPoliciesApi.md#set_password_policy) | **PUT** /password-policies/{id} | Update Password Policy by ID


# **create_password_policy**
> PasswordPolicyV3Dto create_password_policy(password_policy_v3_dto)

Create Password Policy

This API creates the specified password policy. A token with ORG_ADMIN authority is required to call this API.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.beta
from sailpoint.beta.models.password_policy_v3_dto import PasswordPolicyV3Dto
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
    api_instance = sailpoint.beta.PasswordPoliciesApi(api_client)
    password_policy_v3_dto = {description=New Password Policy with high requirements to password complexity., id=null, name=High security Password Policy, dateCreated=1639056206564, lastUpdated=1662385430753, firstExpirationReminder=90, accountIdMinWordLength=3, accountNameMinWordLength=3, maxLength=0, maxRepeatedChars=4, minAlpha=1, minCharacterTypes=-1, minLength=8, minLower=0, minNumeric=1, minSpecial=0, minUpper=0, passwordExpiration=90, defaultPolicy=false, enablePasswdExpiration=false, requireStrongAuthn=false, requireStrongAuthOffNetwork=false, requireStrongAuthUntrustedGeographies=false, useAccountAttributes=false, useDictionary=false, useIdentityAttributes=false, validateAgainstAccountId=true, validateAgainstAccountName=true, sourceIds=[2c91808382ffee0b01830de154f14034, 2c91808582ffee0c01830de36511405f]} # PasswordPolicyV3Dto | 

    try:
        # Create Password Policy
        api_response = api_instance.create_password_policy(password_policy_v3_dto)
        print("The response of PasswordPoliciesApi->create_password_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PasswordPoliciesApi->create_password_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **password_policy_v3_dto** | [**PasswordPolicyV3Dto**](PasswordPolicyV3Dto.md)|  | 

### Return type

[**PasswordPolicyV3Dto**](PasswordPolicyV3Dto.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Reference to the password policy. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_password_policy**
> delete_password_policy(id)

Delete Password Policy by ID

This API deletes the specified password policy. A token with ORG_ADMIN authority is required to call this API.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.beta
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
    api_instance = sailpoint.beta.PasswordPoliciesApi(api_client)
    id = 'ff808081838d9e9d01838da6a03e0002' # str | The ID of password policy to delete.

    try:
        # Delete Password Policy by ID
        api_instance.delete_password_policy(id)
    except Exception as e:
        print("Exception when calling PasswordPoliciesApi->delete_password_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of password policy to delete. | 

### Return type

void (empty response body)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No content - indicates the request was successful but there is no content to be returned in the response. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_password_policy_by_id**
> PasswordPolicyV3Dto get_password_policy_by_id(id)

Get Password Policy by ID

This API returns the password policy for the specified ID. A token with ORG_ADMIN authority is required to call this API.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.beta
from sailpoint.beta.models.password_policy_v3_dto import PasswordPolicyV3Dto
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
    api_instance = sailpoint.beta.PasswordPoliciesApi(api_client)
    id = 'ff808081838d9e9d01838da6a03e0005' # str | The ID of password policy to retrieve.

    try:
        # Get Password Policy by ID
        api_response = api_instance.get_password_policy_by_id(id)
        print("The response of PasswordPoliciesApi->get_password_policy_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PasswordPoliciesApi->get_password_policy_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of password policy to retrieve. | 

### Return type

[**PasswordPolicyV3Dto**](PasswordPolicyV3Dto.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Reference to the password policy. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_password_policies**
> List[PasswordPolicyV3Dto] list_password_policies(limit=limit, offset=offset, count=count)

List Password Policies

This gets list of all Password Policies. Requires role of ORG_ADMIN

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.beta
from sailpoint.beta.models.password_policy_v3_dto import PasswordPolicyV3Dto
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
    api_instance = sailpoint.beta.PasswordPoliciesApi(api_client)
    limit = 250 # int | Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 250)
    offset = 0 # int | Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 0)
    count = False # bool | If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count=true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to False)

    try:
        # List Password Policies
        api_response = api_instance.list_password_policies(limit=limit, offset=offset, count=count)
        print("The response of PasswordPoliciesApi->list_password_policies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PasswordPoliciesApi->list_password_policies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to 250]
 **offset** | **int**| Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to 0]
 **count** | **bool**| If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count&#x3D;true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to False]

### Return type

[**List[PasswordPolicyV3Dto]**](PasswordPolicyV3Dto.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of all Password Policies. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_password_policy**
> PasswordPolicyV3Dto set_password_policy(id, password_policy_v3_dto)

Update Password Policy by ID

This API updates the specified password policy. A token with ORG_ADMIN authority is required to call this API.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.beta
from sailpoint.beta.models.password_policy_v3_dto import PasswordPolicyV3Dto
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
    api_instance = sailpoint.beta.PasswordPoliciesApi(api_client)
    id = 'ff808081838d9e9d01838da6a03e0007' # str | The ID of password policy to update.
    password_policy_v3_dto = {description=Password Policy after update., id=2c91808e7d976f3b017d9f5ceae440c8, name=Improved Password Policy, dateCreated=1639056206564, lastUpdated=1662385430753, firstExpirationReminder=90, accountIdMinWordLength=3, accountNameMinWordLength=3, maxLength=0, maxRepeatedChars=4, minAlpha=1, minCharacterTypes=-1, minLength=8, minLower=0, minNumeric=1, minSpecial=0, minUpper=0, passwordExpiration=90, defaultPolicy=false, enablePasswdExpiration=false, requireStrongAuthn=false, requireStrongAuthOffNetwork=false, requireStrongAuthUntrustedGeographies=false, useAccountAttributes=false, useDictionary=false, useIdentityAttributes=false, validateAgainstAccountId=true, validateAgainstAccountName=true, sourceIds=[2c91808382ffee0b01830de154f14034, 2c91808582ffee0c01830de36511405f]} # PasswordPolicyV3Dto | 

    try:
        # Update Password Policy by ID
        api_response = api_instance.set_password_policy(id, password_policy_v3_dto)
        print("The response of PasswordPoliciesApi->set_password_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PasswordPoliciesApi->set_password_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of password policy to update. | 
 **password_policy_v3_dto** | [**PasswordPolicyV3Dto**](PasswordPolicyV3Dto.md)|  | 

### Return type

[**PasswordPolicyV3Dto**](PasswordPolicyV3Dto.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Reference to the password policy. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

