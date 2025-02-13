# sailpoint.beta.IAIMessageCatalogsApi

All URIs are relative to *https://sailpoint.api.identitynow.com/beta*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_message_catalogs**](IAIMessageCatalogsApi.md#get_message_catalogs) | **GET** /translation-catalogs/{catalog-id} | Get Message catalogs


# **get_message_catalogs**
> List[MessageCatalogDto] get_message_catalogs(catalog_id)

Get Message catalogs

The getMessageCatalogs API returns message catalog based on the language headers in the requested object.

### Example

* OAuth Authentication (userAuth):
* OAuth Authentication (userAuth):

```python
import sailpoint.beta
from sailpoint.beta.models.message_catalog_dto import MessageCatalogDto
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
    api_instance = sailpoint.beta.IAIMessageCatalogsApi(api_client)
    catalog_id = 'recommender' # str | The ID of the message catalog.

    try:
        # Get Message catalogs
        api_response = api_instance.get_message_catalogs(catalog_id)
        print("The response of IAIMessageCatalogsApi->get_message_catalogs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IAIMessageCatalogsApi->get_message_catalogs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog_id** | **str**| The ID of the message catalog. | 

### Return type

[**List[MessageCatalogDto]**](MessageCatalogDto.md)

### Authorization

[userAuth](../README.md#userAuth), [userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The message catalogs based on the request headers |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

