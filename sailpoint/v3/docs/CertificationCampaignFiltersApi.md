# v3.CertificationCampaignFiltersApi

All URIs are relative to *https://sailpoint.api.identitynow.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_campaign_filter**](CertificationCampaignFiltersApi.md#create_campaign_filter) | **POST** /campaign-filters | Create a Campaign Filter
[**get_campaign_filter_by_id**](CertificationCampaignFiltersApi.md#get_campaign_filter_by_id) | **GET** /campaign-filters/{id} | Get Campaign Filter by ID


# **create_campaign_filter**
> CampaignFilterDetails create_campaign_filter(campaign_filter_details)

Create a Campaign Filter

Create a campaign Filter based on filter details and criteria.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import v3
from v3.models.campaign_filter_details import CampaignFilterDetails
from v3.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = v3.Configuration(
    host = "https://sailpoint.api.identitynow.com/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with v3.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = v3.CertificationCampaignFiltersApi(api_client)
    campaign_filter_details = v3.CampaignFilterDetails() # CampaignFilterDetails | 

    try:
        # Create a Campaign Filter
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

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

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

# **get_campaign_filter_by_id**
> List[CampaignFilterDetails] get_campaign_filter_by_id(filter_id)

Get Campaign Filter by ID

Retrieves information for an existing campaign filter using the filter's ID.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import v3
from v3.models.campaign_filter_details import CampaignFilterDetails
from v3.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = v3.Configuration(
    host = "https://sailpoint.api.identitynow.com/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with v3.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = v3.CertificationCampaignFiltersApi(api_client)
    filter_id = 'e9f9a1397b842fd5a65842087040d3ac' # str | The ID of the campaign filter to be retrieved.

    try:
        # Get Campaign Filter by ID
        api_response = api_instance.get_campaign_filter_by_id(filter_id)
        print("The response of CertificationCampaignFiltersApi->get_campaign_filter_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CertificationCampaignFiltersApi->get_campaign_filter_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_id** | **str**| The ID of the campaign filter to be retrieved. | 

### Return type

[**List[CampaignFilterDetails]**](CampaignFilterDetails.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

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

