# sailpoint.v3.VendorConnectorMappingsApi

All URIs are relative to *https://sailpoint.api.identitynow.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_vendor_connector_mapping**](VendorConnectorMappingsApi.md#create_vendor_connector_mapping) | **POST** /vendor-connector-mappings | Create Vendor Connector Mapping
[**delete_vendor_connector_mapping**](VendorConnectorMappingsApi.md#delete_vendor_connector_mapping) | **DELETE** /vendor-connector-mappings | Delete Vendor Connector Mapping


# **create_vendor_connector_mapping**
> VendorConnectorMapping create_vendor_connector_mapping(vendor_connector_mapping)

Create Vendor Connector Mapping

Create a new mapping between a SaaS vendor and an ISC connector to establish correlation paths. 

### Example

* OAuth Authentication (userAuth):
* OAuth Authentication (userAuth):

```python
import sailpoint.v3
from sailpoint.v3.models.vendor_connector_mapping import VendorConnectorMapping
from sailpoint.v3.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.v3.Configuration(
    host = "https://sailpoint.api.identitynow.com/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.v3.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.v3.VendorConnectorMappingsApi(api_client)
    vendor_connector_mapping = sailpoint.v3.VendorConnectorMapping() # VendorConnectorMapping | 

    try:
        # Create Vendor Connector Mapping
        api_response = api_instance.create_vendor_connector_mapping(vendor_connector_mapping)
        print("The response of VendorConnectorMappingsApi->create_vendor_connector_mapping:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VendorConnectorMappingsApi->create_vendor_connector_mapping: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vendor_connector_mapping** | [**VendorConnectorMapping**](VendorConnectorMapping.md)|  | 

### Return type

[**VendorConnectorMapping**](VendorConnectorMapping.md)

### Authorization

[userAuth](../README.md#userAuth), [userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully created a new vendor connector mapping. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**405** | Method Not Allowed - indicates that the server knows the request method, but the target resource doesn&#39;t support this method. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_vendor_connector_mapping**
> DeleteVendorConnectorMapping200Response delete_vendor_connector_mapping(vendor_connector_mapping)

Delete Vendor Connector Mapping

Soft delete a mapping between a SaaS vendor and an ISC connector, removing the established correlation. 

### Example

* OAuth Authentication (userAuth):
* OAuth Authentication (userAuth):

```python
import sailpoint.v3
from sailpoint.v3.models.delete_vendor_connector_mapping200_response import DeleteVendorConnectorMapping200Response
from sailpoint.v3.models.vendor_connector_mapping import VendorConnectorMapping
from sailpoint.v3.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.v3.Configuration(
    host = "https://sailpoint.api.identitynow.com/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.v3.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.v3.VendorConnectorMappingsApi(api_client)
    vendor_connector_mapping = sailpoint.v3.VendorConnectorMapping() # VendorConnectorMapping | 

    try:
        # Delete Vendor Connector Mapping
        api_response = api_instance.delete_vendor_connector_mapping(vendor_connector_mapping)
        print("The response of VendorConnectorMappingsApi->delete_vendor_connector_mapping:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VendorConnectorMappingsApi->delete_vendor_connector_mapping: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vendor_connector_mapping** | [**VendorConnectorMapping**](VendorConnectorMapping.md)|  | 

### Return type

[**DeleteVendorConnectorMapping200Response**](DeleteVendorConnectorMapping200Response.md)

### Authorization

[userAuth](../README.md#userAuth), [userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully deleted the specified vendor connector mapping. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

