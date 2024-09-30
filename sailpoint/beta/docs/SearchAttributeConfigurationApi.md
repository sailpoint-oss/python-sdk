# sailpoint.beta.SearchAttributeConfigurationApi

All URIs are relative to *https://sailpoint.api.identitynow.com/beta*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_search_attribute_config**](SearchAttributeConfigurationApi.md#create_search_attribute_config) | **POST** /accounts/search-attribute-config | Create Extended Search Attributes
[**delete_search_attribute_config**](SearchAttributeConfigurationApi.md#delete_search_attribute_config) | **DELETE** /accounts/search-attribute-config/{name} | Delete Extended Search Attribute
[**get_search_attribute_config**](SearchAttributeConfigurationApi.md#get_search_attribute_config) | **GET** /accounts/search-attribute-config | List Extended Search Attributes
[**get_single_search_attribute_config**](SearchAttributeConfigurationApi.md#get_single_search_attribute_config) | **GET** /accounts/search-attribute-config/{name} | Get Extended Search Attribute
[**patch_search_attribute_config**](SearchAttributeConfigurationApi.md#patch_search_attribute_config) | **PATCH** /accounts/search-attribute-config/{name} | Update Extended Search Attribute


# **create_search_attribute_config**
> object create_search_attribute_config(search_attribute_config)

Create Extended Search Attributes

Create and configure extended search attributes. This API accepts an attribute name, an attribute display name and a list of name/value pair associates of application IDs to attribute names. It will then validate the inputs and configure/create and attribute promotion configuration in the Link ObjectConfig. A token with ORG_ADMIN authority is required to call this API.

### Example

* OAuth Authentication (userAuth):
* OAuth Authentication (userAuth):

```python
import sailpoint.beta
from sailpoint.beta.models.search_attribute_config import SearchAttributeConfig
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
    api_instance = sailpoint.beta.SearchAttributeConfigurationApi(api_client)
    search_attribute_config = {name=newMailAttribute, displayName=New Mail Attribute, applicationAttributes={2c9180866166b5b0016167c32ef31a66=mail, 2c9180866166b5b0016167c32ef31a67=mail}} # SearchAttributeConfig | 

    try:
        # Create Extended Search Attributes
        api_response = api_instance.create_search_attribute_config(search_attribute_config)
        print("The response of SearchAttributeConfigurationApi->create_search_attribute_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchAttributeConfigurationApi->create_search_attribute_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_attribute_config** | [**SearchAttributeConfig**](SearchAttributeConfig.md)|  | 

### Return type

**object**

### Authorization

[userAuth](../README.md#userAuth), [userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted - Returned if the request was successfully accepted into the system. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_search_attribute_config**
> delete_search_attribute_config(name)

Delete Extended Search Attribute

Delete an extended attribute configuration by name.

### Example

* OAuth Authentication (userAuth):
* OAuth Authentication (userAuth):

```python
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
    api_instance = sailpoint.beta.SearchAttributeConfigurationApi(api_client)
    name = 'newMailAttribute' # str | Name of the extended search attribute configuration to delete.

    try:
        # Delete Extended Search Attribute
        api_instance.delete_search_attribute_config(name)
    except Exception as e:
        print("Exception when calling SearchAttributeConfigurationApi->delete_search_attribute_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the extended search attribute configuration to delete. | 

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
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_search_attribute_config**
> List[SearchAttributeConfig] get_search_attribute_config()

List Extended Search Attributes

Get a list of attribute/application associates currently configured in Identity Security Cloud (ISC). A token with ORG_ADMIN authority is required to call this API.

### Example

* OAuth Authentication (userAuth):
* OAuth Authentication (userAuth):

```python
import sailpoint.beta
from sailpoint.beta.models.search_attribute_config import SearchAttributeConfig
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
    api_instance = sailpoint.beta.SearchAttributeConfigurationApi(api_client)

    try:
        # List Extended Search Attributes
        api_response = api_instance.get_search_attribute_config()
        print("The response of SearchAttributeConfigurationApi->get_search_attribute_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchAttributeConfigurationApi->get_search_attribute_config: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[SearchAttributeConfig]**](SearchAttributeConfig.md)

### Authorization

[userAuth](../README.md#userAuth), [userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of attribute configurations in ISC. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_single_search_attribute_config**
> List[SearchAttributeConfig] get_single_search_attribute_config(name)

Get Extended Search Attribute

Get an extended attribute configuration by name.

### Example

* OAuth Authentication (userAuth):
* OAuth Authentication (userAuth):

```python
import sailpoint.beta
from sailpoint.beta.models.search_attribute_config import SearchAttributeConfig
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
    api_instance = sailpoint.beta.SearchAttributeConfigurationApi(api_client)
    name = 'newMailAttribute' # str | Name of the extended search attribute configuration to get.

    try:
        # Get Extended Search Attribute
        api_response = api_instance.get_single_search_attribute_config(name)
        print("The response of SearchAttributeConfigurationApi->get_single_search_attribute_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchAttributeConfigurationApi->get_single_search_attribute_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the extended search attribute configuration to get. | 

### Return type

[**List[SearchAttributeConfig]**](SearchAttributeConfig.md)

### Authorization

[userAuth](../README.md#userAuth), [userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Specific attribute configuration in IdentityNow. |  -  |
**204** | No content - indicates the request was successful but there is no content to be returned in the response. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_search_attribute_config**
> SearchAttributeConfig patch_search_attribute_config(name, json_patch_operation)

Update Extended Search Attribute

Update an existing search attribute configuration.  You can patch these fields: * name  * displayName * applicationAttributes

### Example

* OAuth Authentication (userAuth):
* OAuth Authentication (userAuth):

```python
import sailpoint.beta
from sailpoint.beta.models.json_patch_operation import JsonPatchOperation
from sailpoint.beta.models.search_attribute_config import SearchAttributeConfig
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
    api_instance = sailpoint.beta.SearchAttributeConfigurationApi(api_client)
    name = 'promotedMailAttribute' # str | Name of the extended search attribute configuration to patch.
    json_patch_operation = [{op=replace, path=/name, value=newAttributeName}, {op=replace, path=/displayName, value=new attribute display name}, {op=add, path=/applicationAttributes, value={2c91808b79fd2422017a0b35d30f3968=employeeNumber}}] # List[JsonPatchOperation] | 

    try:
        # Update Extended Search Attribute
        api_response = api_instance.patch_search_attribute_config(name, json_patch_operation)
        print("The response of SearchAttributeConfigurationApi->patch_search_attribute_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchAttributeConfigurationApi->patch_search_attribute_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the extended search attribute configuration to patch. | 
 **json_patch_operation** | [**List[JsonPatchOperation]**](JsonPatchOperation.md)|  | 

### Return type

[**SearchAttributeConfig**](SearchAttributeConfig.md)

### Authorization

[userAuth](../README.md#userAuth), [userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Responds with the search attribute configuration as updated. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

