# sailpoint.beta.ManualDiscoverApplicationsApi

All URIs are relative to *https://sailpoint.api.identitynow.com/beta*

Method | HTTP request | Description
------------- | ------------- | -------------
[**send_manual_discover_applications_csv_template**](ManualDiscoverApplicationsApi.md#send_manual_discover_applications_csv_template) | **POST** /manual-discover-applications | CSV Upload to discover applications


# **send_manual_discover_applications_csv_template**
> ManualDiscoverApplications send_manual_discover_applications_csv_template(csv_file)

CSV Upload to discover applications

This API allows for the upload of a CSV file containing application data to be manually correlated to potential IDN connector(s).

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.beta
from sailpoint.beta.models.manual_discover_applications import ManualDiscoverApplications
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
    api_instance = sailpoint.beta.ManualDiscoverApplicationsApi(api_client)
    csv_file = None # bytearray | 

    try:
        # CSV Upload to discover applications
        api_response = api_instance.send_manual_discover_applications_csv_template(csv_file)
        print("The response of ManualDiscoverApplicationsApi->send_manual_discover_applications_csv_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManualDiscoverApplicationsApi->send_manual_discover_applications_csv_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **csv_file** | **bytearray**|  | 

### Return type

[**ManualDiscoverApplications**](ManualDiscoverApplications.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: multipart/form-data, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The CSV has been successfully processed. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

