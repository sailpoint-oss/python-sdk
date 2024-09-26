# sailpoint.v2024.BrandingApi

All URIs are relative to *https://sailpoint.api.identitynow.com/v2024*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_branding_item**](BrandingApi.md#create_branding_item) | **POST** /brandings | Create a branding item
[**delete_branding**](BrandingApi.md#delete_branding) | **DELETE** /brandings/{name} | Delete a branding item
[**get_branding**](BrandingApi.md#get_branding) | **GET** /brandings/{name} | Get a branding item
[**get_branding_list**](BrandingApi.md#get_branding_list) | **GET** /brandings | List of branding items
[**set_branding_item**](BrandingApi.md#set_branding_item) | **PUT** /brandings/{name} | Update a branding item


# **create_branding_item**
> BrandingItem create_branding_item(name, product_name, action_button_color=action_button_color, active_link_color=active_link_color, navigation_color=navigation_color, email_from_address=email_from_address, login_informational_message=login_informational_message, file_standard=file_standard)

Create a branding item

This API endpoint creates a branding item. A token with API, ORG_ADMIN authority is required to call this API.

### Example

* OAuth Authentication (userAuth):
* OAuth Authentication (userAuth):

```python
import sailpoint.v2024
from sailpoint.v2024.models.branding_item import BrandingItem
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
    api_instance = sailpoint.v2024.BrandingApi(api_client)
    name = 'name_example' # str | name of branding item
    product_name = 'product_name_example' # str | product name
    action_button_color = 'action_button_color_example' # str | hex value of color for action button (optional)
    active_link_color = 'active_link_color_example' # str | hex value of color for link (optional)
    navigation_color = 'navigation_color_example' # str | hex value of color for navigation bar (optional)
    email_from_address = 'email_from_address_example' # str | email from address (optional)
    login_informational_message = 'login_informational_message_example' # str | login information message (optional)
    file_standard = None # bytearray | png file with logo (optional)

    try:
        # Create a branding item
        api_response = api_instance.create_branding_item(name, product_name, action_button_color=action_button_color, active_link_color=active_link_color, navigation_color=navigation_color, email_from_address=email_from_address, login_informational_message=login_informational_message, file_standard=file_standard)
        print("The response of BrandingApi->create_branding_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BrandingApi->create_branding_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of branding item | 
 **product_name** | **str**| product name | 
 **action_button_color** | **str**| hex value of color for action button | [optional] 
 **active_link_color** | **str**| hex value of color for link | [optional] 
 **navigation_color** | **str**| hex value of color for navigation bar | [optional] 
 **email_from_address** | **str**| email from address | [optional] 
 **login_informational_message** | **str**| login information message | [optional] 
 **file_standard** | **bytearray**| png file with logo | [optional] 

### Return type

[**BrandingItem**](BrandingItem.md)

### Authorization

[userAuth](../README.md#userAuth), [userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Branding item created |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_branding**
> delete_branding(name)

Delete a branding item

This API endpoint delete information for an existing branding item by name. A token with API, ORG_ADMIN authority is required to call this API.

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
    api_instance = sailpoint.v2024.BrandingApi(api_client)
    name = 'default' # str | The name of the branding item to be deleted

    try:
        # Delete a branding item
        api_instance.delete_branding(name)
    except Exception as e:
        print("Exception when calling BrandingApi->delete_branding: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the branding item to be deleted | 

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
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_branding**
> BrandingItem get_branding(name)

Get a branding item

This API endpoint retrieves information for an existing branding item by name. A token with API, ORG_ADMIN authority is required to call this API.

### Example

* OAuth Authentication (userAuth):
* OAuth Authentication (userAuth):

```python
import sailpoint.v2024
from sailpoint.v2024.models.branding_item import BrandingItem
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
    api_instance = sailpoint.v2024.BrandingApi(api_client)
    name = 'default' # str | The name of the branding item to be retrieved

    try:
        # Get a branding item
        api_response = api_instance.get_branding(name)
        print("The response of BrandingApi->get_branding:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BrandingApi->get_branding: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the branding item to be retrieved | 

### Return type

[**BrandingItem**](BrandingItem.md)

### Authorization

[userAuth](../README.md#userAuth), [userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A branding item object |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_branding_list**
> List[BrandingItem] get_branding_list()

List of branding items

This API endpoint returns a list of branding items.  A token with API, ORG_ADMIN authority is required to call this API.

### Example

* OAuth Authentication (userAuth):
* OAuth Authentication (userAuth):

```python
import sailpoint.v2024
from sailpoint.v2024.models.branding_item import BrandingItem
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
    api_instance = sailpoint.v2024.BrandingApi(api_client)

    try:
        # List of branding items
        api_response = api_instance.get_branding_list()
        print("The response of BrandingApi->get_branding_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BrandingApi->get_branding_list: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[BrandingItem]**](BrandingItem.md)

### Authorization

[userAuth](../README.md#userAuth), [userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of branding items. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_branding_item**
> BrandingItem set_branding_item(name, name2, product_name, action_button_color=action_button_color, active_link_color=active_link_color, navigation_color=navigation_color, email_from_address=email_from_address, login_informational_message=login_informational_message, file_standard=file_standard)

Update a branding item

This API endpoint updates information for an existing branding item. A token with API, ORG_ADMIN authority is required to call this API.

### Example

* OAuth Authentication (userAuth):
* OAuth Authentication (userAuth):

```python
import sailpoint.v2024
from sailpoint.v2024.models.branding_item import BrandingItem
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
    api_instance = sailpoint.v2024.BrandingApi(api_client)
    name = 'default' # str | The name of the branding item to be retrieved
    name2 = 'name_example' # str | name of branding item
    product_name = 'product_name_example' # str | product name
    action_button_color = 'action_button_color_example' # str | hex value of color for action button (optional)
    active_link_color = 'active_link_color_example' # str | hex value of color for link (optional)
    navigation_color = 'navigation_color_example' # str | hex value of color for navigation bar (optional)
    email_from_address = 'email_from_address_example' # str | email from address (optional)
    login_informational_message = 'login_informational_message_example' # str | login information message (optional)
    file_standard = None # bytearray | png file with logo (optional)

    try:
        # Update a branding item
        api_response = api_instance.set_branding_item(name, name2, product_name, action_button_color=action_button_color, active_link_color=active_link_color, navigation_color=navigation_color, email_from_address=email_from_address, login_informational_message=login_informational_message, file_standard=file_standard)
        print("The response of BrandingApi->set_branding_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BrandingApi->set_branding_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the branding item to be retrieved | 
 **name2** | **str**| name of branding item | 
 **product_name** | **str**| product name | 
 **action_button_color** | **str**| hex value of color for action button | [optional] 
 **active_link_color** | **str**| hex value of color for link | [optional] 
 **navigation_color** | **str**| hex value of color for navigation bar | [optional] 
 **email_from_address** | **str**| email from address | [optional] 
 **login_informational_message** | **str**| login information message | [optional] 
 **file_standard** | **bytearray**| png file with logo | [optional] 

### Return type

[**BrandingItem**](BrandingItem.md)

### Authorization

[userAuth](../README.md#userAuth), [userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Branding item updated |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

