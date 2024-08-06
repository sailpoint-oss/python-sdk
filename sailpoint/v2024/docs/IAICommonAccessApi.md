# sailpoint.v2024.IAICommonAccessApi

All URIs are relative to *https://sailpoint.api.identitynow.com/v2024*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_common_access**](IAICommonAccessApi.md#create_common_access) | **POST** /common-access | Create common access items
[**get_common_access**](IAICommonAccessApi.md#get_common_access) | **GET** /common-access | Get a paginated list of common access
[**update_common_access_status_in_bulk**](IAICommonAccessApi.md#update_common_access_status_in_bulk) | **POST** /common-access/update-status | Bulk update common access status


# **create_common_access**
> CommonAccessItemResponse create_common_access(x_sail_point_experimental, common_access_item_request)

Create common access items

This API is used to add roles/access profiles to the list of common access for a customer. Requires authorization scope of iai:access-modeling:create

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.v2024
from sailpoint.v2024.models.common_access_item_request import CommonAccessItemRequest
from sailpoint.v2024.models.common_access_item_response import CommonAccessItemResponse
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
    api_instance = sailpoint.v2024.IAICommonAccessApi(api_client)
    x_sail_point_experimental = 'true' # str | Use this header to enable this experimental API. (default to 'true')
    common_access_item_request = sailpoint.v2024.CommonAccessItemRequest() # CommonAccessItemRequest | 

    try:
        # Create common access items
        api_response = api_instance.create_common_access(x_sail_point_experimental, common_access_item_request)
        print("The response of IAICommonAccessApi->create_common_access:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IAICommonAccessApi->create_common_access: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_sail_point_experimental** | **str**| Use this header to enable this experimental API. | [default to &#39;true&#39;]
 **common_access_item_request** | [**CommonAccessItemRequest**](CommonAccessItemRequest.md)|  | 

### Return type

[**CommonAccessItemResponse**](CommonAccessItemResponse.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Returns details of the common access classification request. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_common_access**
> List[CommonAccessResponse] get_common_access(x_sail_point_experimental, offset=offset, limit=limit, count=count, filters=filters, sorters=sorters)

Get a paginated list of common access

This endpoint returns the current common access for a customer. The returned items can be filtered and sorted. Requires authorization scope of iai:access-modeling:read

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.v2024
from sailpoint.v2024.models.common_access_response import CommonAccessResponse
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
    api_instance = sailpoint.v2024.IAICommonAccessApi(api_client)
    x_sail_point_experimental = 'true' # str | Use this header to enable this experimental API. (default to 'true')
    offset = 0 # int | Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 0)
    limit = 250 # int | Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 250)
    count = False # bool | If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count=true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to False)
    filters = 'access.type eq \"ROLE\"' # str | Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **status**: *eq, sw*  **reviewedByUser** *eq*  **access.id**: *eq, sw*  **access.type**: *eq*  **access.name**: *sw, eq*  **access.description**: *sw, eq* (optional)
    sorters = 'access.name' # str | Sort results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#sorting-results)  Sorting is supported for the following fields: **access.name, status**  By default the common access items are sorted by name, ascending. (optional)

    try:
        # Get a paginated list of common access
        api_response = api_instance.get_common_access(x_sail_point_experimental, offset=offset, limit=limit, count=count, filters=filters, sorters=sorters)
        print("The response of IAICommonAccessApi->get_common_access:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IAICommonAccessApi->get_common_access: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_sail_point_experimental** | **str**| Use this header to enable this experimental API. | [default to &#39;true&#39;]
 **offset** | **int**| Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to 0]
 **limit** | **int**| Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to 250]
 **count** | **bool**| If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count&#x3D;true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to False]
 **filters** | **str**| Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **status**: *eq, sw*  **reviewedByUser** *eq*  **access.id**: *eq, sw*  **access.type**: *eq*  **access.name**: *sw, eq*  **access.description**: *sw, eq* | [optional] 
 **sorters** | **str**| Sort results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#sorting-results)  Sorting is supported for the following fields: **access.name, status**  By default the common access items are sorted by name, ascending. | [optional] 

### Return type

[**List[CommonAccessResponse]**](CommonAccessResponse.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Succeeded. Returns a list of common access for a customer. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_common_access_status_in_bulk**
> object update_common_access_status_in_bulk(x_sail_point_experimental, common_access_id_status)

Bulk update common access status

This submits an update request to the common access application. At this time there are no parameters. Requires authorization scope of iai:access-modeling:update

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.v2024
from sailpoint.v2024.models.common_access_id_status import CommonAccessIDStatus
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
    api_instance = sailpoint.v2024.IAICommonAccessApi(api_client)
    x_sail_point_experimental = 'true' # str | Use this header to enable this experimental API. (default to 'true')
    common_access_id_status = [sailpoint.v2024.CommonAccessIDStatus()] # List[CommonAccessIDStatus] | Confirm or deny in bulk the common access ids that are (or aren't) common access

    try:
        # Bulk update common access status
        api_response = api_instance.update_common_access_status_in_bulk(x_sail_point_experimental, common_access_id_status)
        print("The response of IAICommonAccessApi->update_common_access_status_in_bulk:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IAICommonAccessApi->update_common_access_status_in_bulk: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_sail_point_experimental** | **str**| Use this header to enable this experimental API. | [default to &#39;true&#39;]
 **common_access_id_status** | [**List[CommonAccessIDStatus]**](CommonAccessIDStatus.md)| Confirm or deny in bulk the common access ids that are (or aren&#39;t) common access | 

### Return type

**object**

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted - Returned if the request was successfully accepted into the system. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

