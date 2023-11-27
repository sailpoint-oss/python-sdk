# sailpoint.beta.AccountAggregationsApi

All URIs are relative to *https://sailpoint.api.identitynow.com/beta*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_account_aggregation_status**](AccountAggregationsApi.md#get_account_aggregation_status) | **GET** /account-aggregations/{id}/status | In-progress Account Aggregation status


# **get_account_aggregation_status**
> AccountAggregationStatus get_account_aggregation_status(id)

In-progress Account Aggregation status

This API returns the status of an *in-progress* account aggregation, along with the total number of **NEW**, **CHANGED** and **DELETED** accounts found since the previous aggregation, and the number of those accounts that have been processed so far.  Accounts that have not changed since the previous aggregation are not included in **totalAccounts** and **processedAccounts** counts returned by this API. This is distinct from **Accounts Scanned** shown in the Aggregation UI, which indicates total accounts scanned regardless of whether they changed or not.  Since this endpoint reports on the status of an *in-progress* account aggregation, totalAccounts and processedAccounts may change between calls to this endpoint.  *Only available up to an hour after the aggregation completes. May respond with *404 Not Found* after that.*  A token with ORG_ADMIN, SOURCE_ADMIN, SOURCE_SUBADMIN or DASHBOARD authority is required to call this API.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import sailpoint.beta
from sailpoint.beta.models.account_aggregation_status import AccountAggregationStatus
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
    api_instance = sailpoint.beta.AccountAggregationsApi(api_client)
    id = '2c91808477a6b0c60177a81146b8110b' # str | The account aggregation id

    try:
        # In-progress Account Aggregation status
        api_response = api_instance.get_account_aggregation_status(id)
        print("The response of AccountAggregationsApi->get_account_aggregation_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountAggregationsApi->get_account_aggregation_status: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The account aggregation id | 

### Return type

[**AccountAggregationStatus**](AccountAggregationStatus.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An account aggregation status object |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

