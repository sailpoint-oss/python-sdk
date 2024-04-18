# sailpoint.beta.SourcesAggregationApi

All URIs are relative to *https://sailpoint.api.identitynow.com/beta*

Method | HTTP request | Description
------------- | ------------- | -------------
[**import_accounts**](SourcesAggregationApi.md#import_accounts) | **POST** /sources/{id}/load-accounts | Account Aggregation


# **import_accounts**
> LoadAccountsTask import_accounts(id, file=file, disable_optimization=disable_optimization)

Account Aggregation

Starts an account aggregation on the specified source.  If the target source is a direct connection, then the request body must be empty. If the target source is a delimited file source, then the CSV file needs to be included in the request body. You will also need to set the Content-Type header to `multipart/form-data`.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.beta
from sailpoint.beta.models.load_accounts_task import LoadAccountsTask
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
    api_instance = sailpoint.beta.SourcesAggregationApi(api_client)
    id = 'ef38f94347e94562b5bb8424a56397d8' # str | Source Id
    file = None # bytearray |  (optional)
    disable_optimization = True # bool |  (optional)

    try:
        # Account Aggregation
        api_response = api_instance.import_accounts(id, file=file, disable_optimization=disable_optimization)
        print("The response of SourcesAggregationApi->import_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesAggregationApi->import_accounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Source Id | 
 **file** | **bytearray**|  | [optional] 
 **disable_optimization** | **bool**|  | [optional] 

### Return type

[**LoadAccountsTask**](LoadAccountsTask.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Aggregate Accounts Task |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

