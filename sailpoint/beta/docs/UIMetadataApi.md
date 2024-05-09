# sailpoint.beta.UIMetadataApi

All URIs are relative to *https://sailpoint.api.identitynow.com/beta*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_tenant_ui_metadata**](UIMetadataApi.md#get_tenant_ui_metadata) | **GET** /ui-metadata/tenant | Get a tenant UI metadata
[**set_tenant_ui_metadata**](UIMetadataApi.md#set_tenant_ui_metadata) | **PUT** /ui-metadata/tenant | Update tenant UI metadata


# **get_tenant_ui_metadata**
> TenantUiMetadataItemResponse get_tenant_ui_metadata()

Get a tenant UI metadata

This API endpoint retrieves UI metadata configured for your tenant. A token with ORG_ADMIN authority is required to call this API.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.beta
from sailpoint.beta.models.tenant_ui_metadata_item_response import TenantUiMetadataItemResponse
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
    api_instance = sailpoint.beta.UIMetadataApi(api_client)

    try:
        # Get a tenant UI metadata
        api_response = api_instance.get_tenant_ui_metadata()
        print("The response of UIMetadataApi->get_tenant_ui_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UIMetadataApi->get_tenant_ui_metadata: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**TenantUiMetadataItemResponse**](TenantUiMetadataItemResponse.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

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
> TenantUiMetadataItemResponse set_tenant_ui_metadata(tenant_ui_metadata_item_update_request)

Update tenant UI metadata

This API endpoint updates UI metadata for your tenant. These changes may require up to 5 minutes to take effect on the UI. A token with ORG_ADMIN authority is required to call this API.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.beta
from sailpoint.beta.models.tenant_ui_metadata_item_response import TenantUiMetadataItemResponse
from sailpoint.beta.models.tenant_ui_metadata_item_update_request import TenantUiMetadataItemUpdateRequest
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
    api_instance = sailpoint.beta.UIMetadataApi(api_client)
    tenant_ui_metadata_item_update_request = sailpoint.beta.TenantUiMetadataItemUpdateRequest() # TenantUiMetadataItemUpdateRequest | 

    try:
        # Update tenant UI metadata
        api_response = api_instance.set_tenant_ui_metadata(tenant_ui_metadata_item_update_request)
        print("The response of UIMetadataApi->set_tenant_ui_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UIMetadataApi->set_tenant_ui_metadata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_ui_metadata_item_update_request** | [**TenantUiMetadataItemUpdateRequest**](TenantUiMetadataItemUpdateRequest.md)|  | 

### Return type

[**TenantUiMetadataItemResponse**](TenantUiMetadataItemResponse.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

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

