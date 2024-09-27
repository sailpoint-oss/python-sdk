# sailpoint.v2024.UIMetadataApi

All URIs are relative to *https://sailpoint.api.identitynow.com/v2024*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_tenant_ui_metadata**](UIMetadataApi.md#get_tenant_ui_metadata) | **GET** /ui-metadata/tenant | Get a tenant UI metadata
[**set_tenant_ui_metadata**](UIMetadataApi.md#set_tenant_ui_metadata) | **PUT** /ui-metadata/tenant | Update tenant UI metadata


# **get_tenant_ui_metadata**
> TenantUiMetadataItemResponse get_tenant_ui_metadata(x_sail_point_experimental)

Get a tenant UI metadata

This API endpoint retrieves UI metadata configured for your tenant.

### Example

* OAuth Authentication (userAuth):
* OAuth Authentication (userAuth):

```python
import sailpoint.v2024
from sailpoint.v2024.models.tenant_ui_metadata_item_response import TenantUiMetadataItemResponse
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
    api_instance = sailpoint.v2024.UIMetadataApi(api_client)
    x_sail_point_experimental = 'true' # str | Use this header to enable this experimental API. (default to 'true')

    try:
        # Get a tenant UI metadata
        api_response = api_instance.get_tenant_ui_metadata(x_sail_point_experimental)
        print("The response of UIMetadataApi->get_tenant_ui_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UIMetadataApi->get_tenant_ui_metadata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_sail_point_experimental** | **str**| Use this header to enable this experimental API. | [default to &#39;true&#39;]

### Return type

[**TenantUiMetadataItemResponse**](TenantUiMetadataItemResponse.md)

### Authorization

[userAuth](../README.md#userAuth), [userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A tenant UI metadata object |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_tenant_ui_metadata**
> TenantUiMetadataItemResponse set_tenant_ui_metadata(x_sail_point_experimental, tenant_ui_metadata_item_update_request)

Update tenant UI metadata

This API endpoint updates UI metadata for your tenant. These changes may require up to 5 minutes to take effect on the UI.

### Example

* OAuth Authentication (userAuth):
* OAuth Authentication (userAuth):

```python
import sailpoint.v2024
from sailpoint.v2024.models.tenant_ui_metadata_item_response import TenantUiMetadataItemResponse
from sailpoint.v2024.models.tenant_ui_metadata_item_update_request import TenantUiMetadataItemUpdateRequest
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
    api_instance = sailpoint.v2024.UIMetadataApi(api_client)
    x_sail_point_experimental = 'true' # str | Use this header to enable this experimental API. (default to 'true')
    tenant_ui_metadata_item_update_request = sailpoint.v2024.TenantUiMetadataItemUpdateRequest() # TenantUiMetadataItemUpdateRequest | 

    try:
        # Update tenant UI metadata
        api_response = api_instance.set_tenant_ui_metadata(x_sail_point_experimental, tenant_ui_metadata_item_update_request)
        print("The response of UIMetadataApi->set_tenant_ui_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UIMetadataApi->set_tenant_ui_metadata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_sail_point_experimental** | **str**| Use this header to enable this experimental API. | [default to &#39;true&#39;]
 **tenant_ui_metadata_item_update_request** | [**TenantUiMetadataItemUpdateRequest**](TenantUiMetadataItemUpdateRequest.md)|  | 

### Return type

[**TenantUiMetadataItemResponse**](TenantUiMetadataItemResponse.md)

### Authorization

[userAuth](../README.md#userAuth), [userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A tenant UI metadata object |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

