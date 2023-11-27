# sailpoint.cc.SourcesAggregationApi

All URIs are relative to *https://sailpoint.api.identitynow.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**load_accounts**](SourcesAggregationApi.md#load_accounts) | **POST** /cc/api/source/loadAccounts/{id} | Account Aggregation (File)
[**load_entitlements**](SourcesAggregationApi.md#load_entitlements) | **POST** /cc/api/source/loadEntitlements/{id} | Account Aggregation (File)


# **load_accounts**
> Dict[str, object] load_accounts(id, content_type=content_type, disable_optimization=disable_optimization, file=file)

Account Aggregation (File)

Aggregates a delimited file for the given source.  This only works for file-based sources.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import sailpoint.cc
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
    api_instance = sailpoint.cc.SourcesAggregationApi(api_client)
    id = 'id_example' # str | 
    content_type = 'application/x-www-form-urlencoded' # str |  (optional)
    disable_optimization = True # bool |  (optional)
    file = None # bytearray |  (optional)

    try:
        # Account Aggregation (File)
        api_response = api_instance.load_accounts(id, content_type=content_type, disable_optimization=disable_optimization, file=file)
        print("The response of SourcesAggregationApi->load_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesAggregationApi->load_accounts: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **content_type** | **str**|  | [optional] 
 **disable_optimization** | **bool**|  | [optional] 
 **file** | **bytearray**|  | [optional] 

### Return type

**Dict[str, object]**

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **load_entitlements**
> Dict[str, object] load_entitlements(id, content_type=content_type, file=file)

Account Aggregation (File)

Aggregates a delimited file for the given source.  This only works for file-based sources.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import sailpoint.cc
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
    api_instance = sailpoint.cc.SourcesAggregationApi(api_client)
    id = 'id_example' # str | 
    content_type = 'application/x-www-form-urlencoded' # str |  (optional)
    file = None # bytearray |  (optional)

    try:
        # Account Aggregation (File)
        api_response = api_instance.load_entitlements(id, content_type=content_type, file=file)
        print("The response of SourcesAggregationApi->load_entitlements:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesAggregationApi->load_entitlements: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **content_type** | **str**|  | [optional] 
 **file** | **bytearray**|  | [optional] 

### Return type

**Dict[str, object]**

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

