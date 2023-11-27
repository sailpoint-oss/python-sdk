# sailpoint.cc.SourcesAccountsApi

All URIs are relative to *https://sailpoint.api.identitynow.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**export_account_feed**](SourcesAccountsApi.md#export_account_feed) | **GET** /cc/api/source/exportAccountFeed/{id} | Export Account Feed


# **export_account_feed**
> export_account_feed(id)

Export Account Feed

Exports a CSV of the accounts for a particular source.

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
    api_instance = sailpoint.cc.SourcesAccountsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Export Account Feed
        api_instance.export_account_feed(id)
    except Exception as e:
        print("Exception when calling SourcesAccountsApi->export_account_feed: %s\n" % e)
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

