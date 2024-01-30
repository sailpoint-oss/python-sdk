# sailpoint.v3.PersonalAccessTokensApi

All URIs are relative to *https://sailpoint.api.identitynow.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_personal_access_token**](PersonalAccessTokensApi.md#create_personal_access_token) | **POST** /personal-access-tokens | Create Personal Access Token
[**delete_personal_access_token**](PersonalAccessTokensApi.md#delete_personal_access_token) | **DELETE** /personal-access-tokens/{id} | Delete Personal Access Token
[**list_personal_access_tokens**](PersonalAccessTokensApi.md#list_personal_access_tokens) | **GET** /personal-access-tokens | List Personal Access Tokens
[**patch_personal_access_token**](PersonalAccessTokensApi.md#patch_personal_access_token) | **PATCH** /personal-access-tokens/{id} | Patch Personal Access Token


# **create_personal_access_token**
> CreatePersonalAccessTokenResponse create_personal_access_token(create_personal_access_token_request)

Create Personal Access Token

This creates a personal access token.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.v3
from sailpoint.v3.models.create_personal_access_token_request import CreatePersonalAccessTokenRequest
from sailpoint.v3.models.create_personal_access_token_response import CreatePersonalAccessTokenResponse
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
    api_instance = sailpoint.v3.PersonalAccessTokensApi(api_client)
    create_personal_access_token_request = sailpoint.v3.CreatePersonalAccessTokenRequest() # CreatePersonalAccessTokenRequest | Name and scope of personal access token.

    try:
        # Create Personal Access Token
        api_response = api_instance.create_personal_access_token(create_personal_access_token_request)
        print("The response of PersonalAccessTokensApi->create_personal_access_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PersonalAccessTokensApi->create_personal_access_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_personal_access_token_request** | [**CreatePersonalAccessTokenRequest**](CreatePersonalAccessTokenRequest.md)| Name and scope of personal access token. | 

### Return type

[**CreatePersonalAccessTokenResponse**](CreatePersonalAccessTokenResponse.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Created. Note - this is the only time Personal Access Tokens&#39; secret attribute will be displayed. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_personal_access_token**
> delete_personal_access_token(id)

Delete Personal Access Token

This deletes a personal access token.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.v3
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
    api_instance = sailpoint.v3.PersonalAccessTokensApi(api_client)
    id = 'ef38f94347e94562b5bb8424a56397d8' # str | The personal access token id

    try:
        # Delete Personal Access Token
        api_instance.delete_personal_access_token(id)
    except Exception as e:
        print("Exception when calling PersonalAccessTokensApi->delete_personal_access_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The personal access token id | 

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
**204** | No content. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_personal_access_tokens**
> List[GetPersonalAccessTokenResponse] list_personal_access_tokens(owner_id=owner_id, filters=filters)

List Personal Access Tokens

This gets a collection of personal access tokens associated with the optional `owner-id`.  query parameter. If the `owner-id` query parameter is omitted, all personal access tokens  for a tenant will be retrieved, but the caller must have the 'idn:all-personal-access-tokens:read' right.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.v3
from sailpoint.v3.models.get_personal_access_token_response import GetPersonalAccessTokenResponse
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
    api_instance = sailpoint.v3.PersonalAccessTokensApi(api_client)
    owner_id = '2c9180867b50d088017b554662fb281e' # str | The identity ID of the owner whose personal access tokens should be listed.  If \"me\", the caller should have the following right: 'idn:my-personal-access-tokens:read' If an actual owner ID or if the `owner-id` parameter is omitted in the request,  the caller should have the following right: 'idn:all-personal-access-tokens:read'.  If the caller has the following right, then managed personal access tokens associated with `owner-id`  will be retrieved: 'idn:managed-personal-access-tokens:read' (optional)
    filters = 'lastUsed le 2023-02-05T10:59:27.214Z' # str | Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **lastUsed**: *le, isnull* (optional)

    try:
        # List Personal Access Tokens
        api_response = api_instance.list_personal_access_tokens(owner_id=owner_id, filters=filters)
        print("The response of PersonalAccessTokensApi->list_personal_access_tokens:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PersonalAccessTokensApi->list_personal_access_tokens: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_id** | **str**| The identity ID of the owner whose personal access tokens should be listed.  If \&quot;me\&quot;, the caller should have the following right: &#39;idn:my-personal-access-tokens:read&#39; If an actual owner ID or if the &#x60;owner-id&#x60; parameter is omitted in the request,  the caller should have the following right: &#39;idn:all-personal-access-tokens:read&#39;.  If the caller has the following right, then managed personal access tokens associated with &#x60;owner-id&#x60;  will be retrieved: &#39;idn:managed-personal-access-tokens:read&#39; | [optional] 
 **filters** | **str**| Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **lastUsed**: *le, isnull* | [optional] 

### Return type

[**List[GetPersonalAccessTokenResponse]**](GetPersonalAccessTokenResponse.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of personal access tokens. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_personal_access_token**
> GetPersonalAccessTokenResponse patch_personal_access_token(id, json_patch_operation)

Patch Personal Access Token

This performs a targeted update to the field(s) of a Personal Access Token.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.v3
from sailpoint.v3.models.get_personal_access_token_response import GetPersonalAccessTokenResponse
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
    api_instance = sailpoint.v3.PersonalAccessTokensApi(api_client)
    id = 'ef38f94347e94562b5bb8424a56397d8' # str | The Personal Access Token id
    json_patch_operation = [{op=replace, path=/name, value=New name}, {op=replace, path=/scope, value=[sp:scopes:all]}] # List[JsonPatchOperation] | A list of OAuth client update operations according to the [JSON Patch](https://tools.ietf.org/html/rfc6902) standard.  The following fields are patchable: * name * scope 

    try:
        # Patch Personal Access Token
        api_response = api_instance.patch_personal_access_token(id, json_patch_operation)
        print("The response of PersonalAccessTokensApi->patch_personal_access_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PersonalAccessTokensApi->patch_personal_access_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Personal Access Token id | 
 **json_patch_operation** | [**List[JsonPatchOperation]**](JsonPatchOperation.md)| A list of OAuth client update operations according to the [JSON Patch](https://tools.ietf.org/html/rfc6902) standard.  The following fields are patchable: * name * scope  | 

### Return type

[**GetPersonalAccessTokenResponse**](GetPersonalAccessTokenResponse.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Indicates the PATCH operation succeeded, and returns the PAT&#39;s new representation. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

