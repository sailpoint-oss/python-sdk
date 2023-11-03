# cc.ApplicationsApi

All URIs are relative to *https://sailpoint.api.identitynow.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_application**](ApplicationsApi.md#create_application) | **POST** /cc/api/app/create | Create Application
[**delete_application**](ApplicationsApi.md#delete_application) | **POST** /cc/api/app/delete/{id} | Delete Application
[**get_application**](ApplicationsApi.md#get_application) | **GET** /cc/api/app/get/{id} | Get Single Application
[**get_application_access_profiles**](ApplicationsApi.md#get_application_access_profiles) | **GET** /cc/api/app/getAccessProfiles/{id} | Get Access Profiles for Application
[**list_applications**](ApplicationsApi.md#list_applications) | **GET** /cc/api/app/list | List Applications
[**update_application**](ApplicationsApi.md#update_application) | **POST** /cc/api/app/update/{id} | Update Application


# **create_application**
> Dict[str, object] create_application(create_application_request=create_application_request)

Create Application

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import cc
from cc.models.create_application_request import CreateApplicationRequest
from cc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com
# See configuration.py for a list of all supported configuration parameters.
configuration = cc.Configuration(
    host = "https://sailpoint.api.identitynow.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cc.ApplicationsApi(api_client)
    create_application_request = cc.CreateApplicationRequest() # CreateApplicationRequest |  (optional)

    try:
        # Create Application
        api_response = api_instance.create_application(create_application_request=create_application_request)
        print("The response of ApplicationsApi->create_application:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationsApi->create_application: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_application_request** | [**CreateApplicationRequest**](CreateApplicationRequest.md)|  | [optional] 

### Return type

**Dict[str, object]**

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

# **delete_application**
> delete_application(id)

Delete Application

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import cc
from cc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com
# See configuration.py for a list of all supported configuration parameters.
configuration = cc.Configuration(
    host = "https://sailpoint.api.identitynow.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cc.ApplicationsApi(api_client)
    id = '12345' # str | 

    try:
        # Delete Application
        api_instance.delete_application(id)
    except Exception as e:
        print("Exception when calling ApplicationsApi->delete_application: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

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
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_application**
> GetApplication200Response get_application(id)

Get Single Application

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import cc
from cc.models.get_application200_response import GetApplication200Response
from cc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com
# See configuration.py for a list of all supported configuration parameters.
configuration = cc.Configuration(
    host = "https://sailpoint.api.identitynow.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cc.ApplicationsApi(api_client)
    id = '12345' # str | 

    try:
        # Get Single Application
        api_response = api_instance.get_application(id)
        print("The response of ApplicationsApi->get_application:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationsApi->get_application: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**GetApplication200Response**](GetApplication200Response.md)

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

# **get_application_access_profiles**
> Dict[str, object] get_application_access_profiles(id)

Get Access Profiles for Application

### Example

```python
import time
import os
import cc
from cc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com
# See configuration.py for a list of all supported configuration parameters.
configuration = cc.Configuration(
    host = "https://sailpoint.api.identitynow.com"
)


# Enter a context with an instance of the API client
with cc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cc.ApplicationsApi(api_client)
    id = '12345' # str | 

    try:
        # Get Access Profiles for Application
        api_response = api_instance.get_application_access_profiles(id)
        print("The response of ApplicationsApi->get_application_access_profiles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationsApi->get_application_access_profiles: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

**Dict[str, object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_applications**
> List[ListApplications200ResponseInner] list_applications()

List Applications

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import cc
from cc.models.list_applications200_response_inner import ListApplications200ResponseInner
from cc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com
# See configuration.py for a list of all supported configuration parameters.
configuration = cc.Configuration(
    host = "https://sailpoint.api.identitynow.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cc.ApplicationsApi(api_client)

    try:
        # List Applications
        api_response = api_instance.list_applications()
        print("The response of ApplicationsApi->list_applications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationsApi->list_applications: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**List[ListApplications200ResponseInner]**](ListApplications200ResponseInner.md)

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

# **update_application**
> Dict[str, object] update_application(id, request_body=request_body)

Update Application

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import cc
from cc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com
# See configuration.py for a list of all supported configuration parameters.
configuration = cc.Configuration(
    host = "https://sailpoint.api.identitynow.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cc.ApplicationsApi(api_client)
    id = '12345' # str | 
    request_body = None # Dict[str, object] |  (optional)

    try:
        # Update Application
        api_response = api_instance.update_application(id, request_body=request_body)
        print("The response of ApplicationsApi->update_application:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationsApi->update_application: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **request_body** | [**Dict[str, object]**](object.md)|  | [optional] 

### Return type

**Dict[str, object]**

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

