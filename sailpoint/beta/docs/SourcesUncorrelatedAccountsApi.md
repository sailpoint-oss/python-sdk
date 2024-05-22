# sailpoint.beta.SourcesUncorrelatedAccountsApi

All URIs are relative to *https://sailpoint.api.identitynow.com/beta*

Method | HTTP request | Description
------------- | ------------- | -------------
[**import_uncorrelated_accounts**](SourcesUncorrelatedAccountsApi.md#import_uncorrelated_accounts) | **POST** /sources/{id}/load-uncorrelated-accounts | Process Uncorrelated Accounts


# **import_uncorrelated_accounts**
> LoadUncorrelatedAccountsTask import_uncorrelated_accounts(id, file=file)

Process Uncorrelated Accounts

File is required for upload. You will also need to set the Content-Type header to `multipart/form-data`

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.beta
from sailpoint.beta.models.load_uncorrelated_accounts_task import LoadUncorrelatedAccountsTask
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
    api_instance = sailpoint.beta.SourcesUncorrelatedAccountsApi(api_client)
    id = '75dbec1ebe154d5785da27b95e1dd5d7' # str | Source Id
    file = None # bytearray |  (optional)

    try:
        # Process Uncorrelated Accounts
        api_response = api_instance.import_uncorrelated_accounts(id, file=file)
        print("The response of SourcesUncorrelatedAccountsApi->import_uncorrelated_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesUncorrelatedAccountsApi->import_uncorrelated_accounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Source Id | 
 **file** | **bytearray**|  | [optional] 

### Return type

[**LoadUncorrelatedAccountsTask**](LoadUncorrelatedAccountsTask.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Uncorrelated Accounts Task |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

