# sailpoint.v2024.CertificationCampaignFiltersApi

All URIs are relative to *https://sailpoint.api.identitynow.com/v2024*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_campaign_filter**](CertificationCampaignFiltersApi.md#create_campaign_filter) | **POST** /campaign-filters | Create Campaign Filter
[**delete_campaign_filters**](CertificationCampaignFiltersApi.md#delete_campaign_filters) | **POST** /campaign-filters/delete | Deletes Campaign Filters
[**get_campaign_filter_by_id**](CertificationCampaignFiltersApi.md#get_campaign_filter_by_id) | **GET** /campaign-filters/{id} | Get Campaign Filter by ID
[**list_campaign_filters**](CertificationCampaignFiltersApi.md#list_campaign_filters) | **GET** /campaign-filters | List Campaign Filters
[**update_campaign_filter**](CertificationCampaignFiltersApi.md#update_campaign_filter) | **POST** /campaign-filters/{id} | Updates a Campaign Filter


# **create_campaign_filter**
> CampaignFilterDetails create_campaign_filter(campaign_filter_details)

Create Campaign Filter

Use this API to create a campaign filter based on filter details and criteria.

### Example

* OAuth Authentication (userAuth):
* OAuth Authentication (userAuth):

```python
import sailpoint.v2024
from sailpoint.v2024.models.campaign_filter_details import CampaignFilterDetails
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
    api_instance = sailpoint.v2024.CertificationCampaignFiltersApi(api_client)
    campaign_filter_details = sailpoint.v2024.CampaignFilterDetails() # CampaignFilterDetails | 

    try:
        # Create Campaign Filter
        api_response = api_instance.create_campaign_filter(campaign_filter_details)
        print("The response of CertificationCampaignFiltersApi->create_campaign_filter:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CertificationCampaignFiltersApi->create_campaign_filter: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_filter_details** | [**CampaignFilterDetails**](CampaignFilterDetails.md)|  | 

### Return type

[**CampaignFilterDetails**](CampaignFilterDetails.md)

### Authorization

[userAuth](../README.md#userAuth), [userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Created successfully. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_campaign_filters**
> delete_campaign_filters(request_body)

Deletes Campaign Filters

Deletes campaign filters whose Ids are specified in the provided list of campaign filter Ids. Authorized callers must be an ORG_ADMIN or a CERT_ADMIN.

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
    api_instance = sailpoint.v2024.CertificationCampaignFiltersApi(api_client)
    request_body = ['request_body_example'] # List[str] | A json list of IDs of campaign filters to delete.

    try:
        # Deletes Campaign Filters
        api_instance.delete_campaign_filters(request_body)
    except Exception as e:
        print("Exception when calling CertificationCampaignFiltersApi->delete_campaign_filters: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[str]**](str.md)| A json list of IDs of campaign filters to delete. | 

### Return type

void (empty response body)

### Authorization

[userAuth](../README.md#userAuth), [userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No content - indicates the request was successful but there is no content to be returned in the response. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_campaign_filter_by_id**
> List[CampaignFilterDetails] get_campaign_filter_by_id(id)

Get Campaign Filter by ID

Retrieves information for an existing campaign filter using the filter's ID.

### Example

* OAuth Authentication (userAuth):
* OAuth Authentication (userAuth):

```python
import sailpoint.v2024
from sailpoint.v2024.models.campaign_filter_details import CampaignFilterDetails
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
    api_instance = sailpoint.v2024.CertificationCampaignFiltersApi(api_client)
    id = 'e9f9a1397b842fd5a65842087040d3ac' # str | The ID of the campaign filter to be retrieved.

    try:
        # Get Campaign Filter by ID
        api_response = api_instance.get_campaign_filter_by_id(id)
        print("The response of CertificationCampaignFiltersApi->get_campaign_filter_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CertificationCampaignFiltersApi->get_campaign_filter_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the campaign filter to be retrieved. | 

### Return type

[**List[CampaignFilterDetails]**](CampaignFilterDetails.md)

### Authorization

[userAuth](../README.md#userAuth), [userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A campaign filter object. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_campaign_filters**
> ListCampaignFilters200Response list_campaign_filters(limit=limit, start=start, include_system_filters=include_system_filters)

List Campaign Filters

Use this API to list all campaign filters. You can reduce scope with standard V3 query parameters.

### Example

* OAuth Authentication (userAuth):
* OAuth Authentication (userAuth):

```python
import sailpoint.v2024
from sailpoint.v2024.models.list_campaign_filters200_response import ListCampaignFilters200Response
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
    api_instance = sailpoint.v2024.CertificationCampaignFiltersApi(api_client)
    limit = 250 # int | Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 250)
    start = 0 # int | Start/Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 0)
    include_system_filters = True # bool | If this is true, the API includes system filters in the count and results. Otherwise it excludes them. If no value is provided, the default is true.  (optional) (default to True)

    try:
        # List Campaign Filters
        api_response = api_instance.list_campaign_filters(limit=limit, start=start, include_system_filters=include_system_filters)
        print("The response of CertificationCampaignFiltersApi->list_campaign_filters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CertificationCampaignFiltersApi->list_campaign_filters: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to 250]
 **start** | **int**| Start/Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to 0]
 **include_system_filters** | **bool**| If this is true, the API includes system filters in the count and results. Otherwise it excludes them. If no value is provided, the default is true.  | [optional] [default to True]

### Return type

[**ListCampaignFilters200Response**](ListCampaignFilters200Response.md)

### Authorization

[userAuth](../README.md#userAuth), [userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of campaign filter objects. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_campaign_filter**
> CampaignFilterDetails update_campaign_filter(filter_id, campaign_filter_details)

Updates a Campaign Filter

Updates an existing campaign filter using the filter's ID.

### Example

* OAuth Authentication (userAuth):
* OAuth Authentication (userAuth):

```python
import sailpoint.v2024
from sailpoint.v2024.models.campaign_filter_details import CampaignFilterDetails
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
    api_instance = sailpoint.v2024.CertificationCampaignFiltersApi(api_client)
    filter_id = 'e9f9a1397b842fd5a65842087040d3ac' # str | The ID of the campaign filter being modified.
    campaign_filter_details = sailpoint.v2024.CampaignFilterDetails() # CampaignFilterDetails | A campaign filter details with updated field values.

    try:
        # Updates a Campaign Filter
        api_response = api_instance.update_campaign_filter(filter_id, campaign_filter_details)
        print("The response of CertificationCampaignFiltersApi->update_campaign_filter:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CertificationCampaignFiltersApi->update_campaign_filter: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_id** | **str**| The ID of the campaign filter being modified. | 
 **campaign_filter_details** | [**CampaignFilterDetails**](CampaignFilterDetails.md)| A campaign filter details with updated field values. | 

### Return type

[**CampaignFilterDetails**](CampaignFilterDetails.md)

### Authorization

[userAuth](../README.md#userAuth), [userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Created successfully. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

