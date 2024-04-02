# sailpoint.beta.ManualDiscoverApplicationsTemplateApi

All URIs are relative to *https://sailpoint.api.identitynow.com/beta*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_manual_discover_applications_csv_template**](ManualDiscoverApplicationsTemplateApi.md#get_manual_discover_applications_csv_template) | **GET** /manual-discover-applications-template | CSV template download for discovery


# **get_manual_discover_applications_csv_template**
> ManualDiscoverApplicationsTemplate get_manual_discover_applications_csv_template()

CSV template download for discovery

Allows the user to download an example CSV file with two columns `application_name` and `domain`. The CSV file contains a single row with the values 'Example Application' and 'Example Description'. 

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.beta
from sailpoint.beta.models.manual_discover_applications_template import ManualDiscoverApplicationsTemplate
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
    api_instance = sailpoint.beta.ManualDiscoverApplicationsTemplateApi(api_client)

    try:
        # CSV template download for discovery
        api_response = api_instance.get_manual_discover_applications_csv_template()
        print("The response of ManualDiscoverApplicationsTemplateApi->get_manual_discover_applications_csv_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManualDiscoverApplicationsTemplateApi->get_manual_discover_applications_csv_template: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ManualDiscoverApplicationsTemplate**](ManualDiscoverApplicationsTemplate.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/csv, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A CSV file download was successful. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

