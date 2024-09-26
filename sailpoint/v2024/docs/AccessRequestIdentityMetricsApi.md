# sailpoint.v2024.AccessRequestIdentityMetricsApi

All URIs are relative to *https://sailpoint.api.identitynow.com/v2024*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_access_request_identity_metrics**](AccessRequestIdentityMetricsApi.md#get_access_request_identity_metrics) | **GET** /access-request-identity-metrics/{identityId}/requested-objects/{requestedObjectId}/type/{type} | Return access request identity metrics


# **get_access_request_identity_metrics**
> object get_access_request_identity_metrics(identity_id, requested_object_id, type, x_sail_point_experimental)

Return access request identity metrics

Use this API to return information access metrics.

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
    api_instance = sailpoint.v2024.AccessRequestIdentityMetricsApi(api_client)
    identity_id = '7025c863-c270-4ba6-beea-edf3cb091573' # str | Manager's identity ID.
    requested_object_id = '2db501be-f0fb-4cc5-a695-334133c52891' # str | Requested access item's ID.
    type = 'ENTITLEMENT' # str | Requested access item's type.
    x_sail_point_experimental = 'true' # str | Use this header to enable this experimental API. (default to 'true')

    try:
        # Return access request identity metrics
        api_response = api_instance.get_access_request_identity_metrics(identity_id, requested_object_id, type, x_sail_point_experimental)
        print("The response of AccessRequestIdentityMetricsApi->get_access_request_identity_metrics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccessRequestIdentityMetricsApi->get_access_request_identity_metrics: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identity_id** | **str**| Manager&#39;s identity ID. | 
 **requested_object_id** | **str**| Requested access item&#39;s ID. | 
 **type** | **str**| Requested access item&#39;s type. | 
 **x_sail_point_experimental** | **str**| Use this header to enable this experimental API. | [default to &#39;true&#39;]

### Return type

**object**

### Authorization

[userAuth](../README.md#userAuth), [userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Summary of the resource access and source activity for the direct reports of the provided manager. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

