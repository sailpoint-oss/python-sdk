# v3.PasswordDictionaryApi

All URIs are relative to *https://sailpoint.api.identitynow.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_password_dictionary**](PasswordDictionaryApi.md#get_password_dictionary) | **GET** /password-dictionary | Get Password Dictionary
[**update_password_dictionary**](PasswordDictionaryApi.md#update_password_dictionary) | **PUT** /password-dictionary | Update Password Dictionary


# **get_password_dictionary**
> str get_password_dictionary()

Get Password Dictionary

This gets password dictionary for the organization. A token with ORG_ADMIN authority is required to call this API.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import v3
from v3.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = v3.Configuration(
    host = "https://sailpoint.api.identitynow.com/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with v3.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = v3.PasswordDictionaryApi(api_client)

    try:
        # Get Password Dictionary
        api_response = api_instance.get_password_dictionary()
        print("The response of PasswordDictionaryApi->get_password_dictionary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PasswordDictionaryApi->get_password_dictionary: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  The password dictionary file can contain lines that are: 1. comment lines - the first character is &#39;#&#39;, can be 128 Unicode codepoints in length, and are ignored during processing 2. empty lines 3. locale line - the first line that starts with \&quot;locale&#x3D;\&quot; is considered to be locale line, the rest are treated as normal content lines 4. line containing the password dictionary word - it must start with non-whitespace character and only non-whitespace characters are allowed;         maximum length of the line is 128 Unicode codepoints   Password dictionary file may not contain more than 2,500 lines (not counting whitespace lines, comment lines and locale line).  Password dict file must contain UTF-8 characters only.  # Sample password text file  &#x60;&#x60;&#x60;  # Password dictionary small test file  locale&#x3D;en_US  # Password dictionary prohibited words  qwerty abcd aaaaa password qazxsws  &#x60;&#x60;&#x60; |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_password_dictionary**
> update_password_dictionary(file=file)

Update Password Dictionary

This updates password dictionary for the organization. A token with ORG_ADMIN authority is required to call this API.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import v3
from v3.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = v3.Configuration(
    host = "https://sailpoint.api.identitynow.com/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with v3.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = v3.PasswordDictionaryApi(api_client)
    file = None # bytearray |  (optional)

    try:
        # Update Password Dictionary
        api_instance.update_password_dictionary(file=file)
    except Exception as e:
        print("Exception when calling PasswordDictionaryApi->update_password_dictionary: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **bytearray**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated. |  -  |
**201** | Created. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

