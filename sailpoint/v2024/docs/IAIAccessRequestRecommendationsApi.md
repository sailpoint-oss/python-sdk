# sailpoint.v2024.IAIAccessRequestRecommendationsApi

All URIs are relative to *https://sailpoint.api.identitynow.com/v2024*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_access_request_recommendations_ignored_item**](IAIAccessRequestRecommendationsApi.md#add_access_request_recommendations_ignored_item) | **POST** /ai-access-request-recommendations/ignored-items | Notification of Ignored Access Request Recommendations
[**add_access_request_recommendations_requested_item**](IAIAccessRequestRecommendationsApi.md#add_access_request_recommendations_requested_item) | **POST** /ai-access-request-recommendations/requested-items | Notification of Requested Access Request Recommendations
[**add_access_request_recommendations_viewed_item**](IAIAccessRequestRecommendationsApi.md#add_access_request_recommendations_viewed_item) | **POST** /ai-access-request-recommendations/viewed-items | Notification of Viewed Access Request Recommendations
[**add_access_request_recommendations_viewed_items**](IAIAccessRequestRecommendationsApi.md#add_access_request_recommendations_viewed_items) | **POST** /ai-access-request-recommendations/viewed-items/bulk-create | Notification of Viewed Access Request Recommendations in Bulk
[**get_access_request_recommendations**](IAIAccessRequestRecommendationsApi.md#get_access_request_recommendations) | **GET** /ai-access-request-recommendations | Identity Access Request Recommendations
[**get_access_request_recommendations_ignored_items**](IAIAccessRequestRecommendationsApi.md#get_access_request_recommendations_ignored_items) | **GET** /ai-access-request-recommendations/ignored-items | List of Ignored Access Request Recommendations
[**get_access_request_recommendations_requested_items**](IAIAccessRequestRecommendationsApi.md#get_access_request_recommendations_requested_items) | **GET** /ai-access-request-recommendations/requested-items | List of Requested Access Request Recommendations
[**get_access_request_recommendations_viewed_items**](IAIAccessRequestRecommendationsApi.md#get_access_request_recommendations_viewed_items) | **GET** /ai-access-request-recommendations/viewed-items | List of Viewed Access Request Recommendations


# **add_access_request_recommendations_ignored_item**
> AccessRequestRecommendationActionItemResponseDto add_access_request_recommendations_ignored_item(x_sail_point_experimental, access_request_recommendation_action_item_dto)

Notification of Ignored Access Request Recommendations

This API ignores a recommended access request item. Once an item is ignored, it will be marked as ignored=true if it is still a recommended item. The consumer can decide to hide ignored recommendations.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.v2024
from sailpoint.v2024.models.access_request_recommendation_action_item_dto import AccessRequestRecommendationActionItemDto
from sailpoint.v2024.models.access_request_recommendation_action_item_response_dto import AccessRequestRecommendationActionItemResponseDto
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
    api_instance = sailpoint.v2024.IAIAccessRequestRecommendationsApi(api_client)
    x_sail_point_experimental = 'true' # str | Use this header to enable this experimental API. (default to 'true')
    access_request_recommendation_action_item_dto = sailpoint.v2024.AccessRequestRecommendationActionItemDto() # AccessRequestRecommendationActionItemDto | The recommended access item to ignore for an identity.

    try:
        # Notification of Ignored Access Request Recommendations
        api_response = api_instance.add_access_request_recommendations_ignored_item(x_sail_point_experimental, access_request_recommendation_action_item_dto)
        print("The response of IAIAccessRequestRecommendationsApi->add_access_request_recommendations_ignored_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IAIAccessRequestRecommendationsApi->add_access_request_recommendations_ignored_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_sail_point_experimental** | **str**| Use this header to enable this experimental API. | [default to &#39;true&#39;]
 **access_request_recommendation_action_item_dto** | [**AccessRequestRecommendationActionItemDto**](AccessRequestRecommendationActionItemDto.md)| The recommended access item to ignore for an identity. | 

### Return type

[**AccessRequestRecommendationActionItemResponseDto**](AccessRequestRecommendationActionItemResponseDto.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Recommendation successfully stored as ignored. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_access_request_recommendations_requested_item**
> AccessRequestRecommendationActionItemResponseDto add_access_request_recommendations_requested_item(x_sail_point_experimental, access_request_recommendation_action_item_dto)

Notification of Requested Access Request Recommendations

This API consumes a notification that a recommended access request item was requested. This API does not actually make the request, it is just a notification. This will help provide feedback in order to improve our recommendations.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.v2024
from sailpoint.v2024.models.access_request_recommendation_action_item_dto import AccessRequestRecommendationActionItemDto
from sailpoint.v2024.models.access_request_recommendation_action_item_response_dto import AccessRequestRecommendationActionItemResponseDto
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
    api_instance = sailpoint.v2024.IAIAccessRequestRecommendationsApi(api_client)
    x_sail_point_experimental = 'true' # str | Use this header to enable this experimental API. (default to 'true')
    access_request_recommendation_action_item_dto = sailpoint.v2024.AccessRequestRecommendationActionItemDto() # AccessRequestRecommendationActionItemDto | The recommended access item that was requested for an identity.

    try:
        # Notification of Requested Access Request Recommendations
        api_response = api_instance.add_access_request_recommendations_requested_item(x_sail_point_experimental, access_request_recommendation_action_item_dto)
        print("The response of IAIAccessRequestRecommendationsApi->add_access_request_recommendations_requested_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IAIAccessRequestRecommendationsApi->add_access_request_recommendations_requested_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_sail_point_experimental** | **str**| Use this header to enable this experimental API. | [default to &#39;true&#39;]
 **access_request_recommendation_action_item_dto** | [**AccessRequestRecommendationActionItemDto**](AccessRequestRecommendationActionItemDto.md)| The recommended access item that was requested for an identity. | 

### Return type

[**AccessRequestRecommendationActionItemResponseDto**](AccessRequestRecommendationActionItemResponseDto.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Notification successfully acknowledged. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_access_request_recommendations_viewed_item**
> AccessRequestRecommendationActionItemResponseDto add_access_request_recommendations_viewed_item(x_sail_point_experimental, access_request_recommendation_action_item_dto)

Notification of Viewed Access Request Recommendations

This API consumes a notification that a recommended access request item was viewed. Future recommendations with this item will be marked with viewed=true. This can be useful for the consumer to determine if there are any new/unviewed recommendations.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.v2024
from sailpoint.v2024.models.access_request_recommendation_action_item_dto import AccessRequestRecommendationActionItemDto
from sailpoint.v2024.models.access_request_recommendation_action_item_response_dto import AccessRequestRecommendationActionItemResponseDto
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
    api_instance = sailpoint.v2024.IAIAccessRequestRecommendationsApi(api_client)
    x_sail_point_experimental = 'true' # str | Use this header to enable this experimental API. (default to 'true')
    access_request_recommendation_action_item_dto = sailpoint.v2024.AccessRequestRecommendationActionItemDto() # AccessRequestRecommendationActionItemDto | The recommended access that was viewed for an identity.

    try:
        # Notification of Viewed Access Request Recommendations
        api_response = api_instance.add_access_request_recommendations_viewed_item(x_sail_point_experimental, access_request_recommendation_action_item_dto)
        print("The response of IAIAccessRequestRecommendationsApi->add_access_request_recommendations_viewed_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IAIAccessRequestRecommendationsApi->add_access_request_recommendations_viewed_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_sail_point_experimental** | **str**| Use this header to enable this experimental API. | [default to &#39;true&#39;]
 **access_request_recommendation_action_item_dto** | [**AccessRequestRecommendationActionItemDto**](AccessRequestRecommendationActionItemDto.md)| The recommended access that was viewed for an identity. | 

### Return type

[**AccessRequestRecommendationActionItemResponseDto**](AccessRequestRecommendationActionItemResponseDto.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Recommendation successfully stored as viewed. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_access_request_recommendations_viewed_items**
> List[AccessRequestRecommendationActionItemResponseDto] add_access_request_recommendations_viewed_items(x_sail_point_experimental, access_request_recommendation_action_item_dto)

Notification of Viewed Access Request Recommendations in Bulk

This API consumes a notification that a set of recommended access request item were viewed. Future recommendations with these items will be marked with viewed=true. This can be useful for the consumer to determine if there are any new/unviewed recommendations.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.v2024
from sailpoint.v2024.models.access_request_recommendation_action_item_dto import AccessRequestRecommendationActionItemDto
from sailpoint.v2024.models.access_request_recommendation_action_item_response_dto import AccessRequestRecommendationActionItemResponseDto
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
    api_instance = sailpoint.v2024.IAIAccessRequestRecommendationsApi(api_client)
    x_sail_point_experimental = 'true' # str | Use this header to enable this experimental API. (default to 'true')
    access_request_recommendation_action_item_dto = [sailpoint.v2024.AccessRequestRecommendationActionItemDto()] # List[AccessRequestRecommendationActionItemDto] | The recommended access items that were viewed for an identity.

    try:
        # Notification of Viewed Access Request Recommendations in Bulk
        api_response = api_instance.add_access_request_recommendations_viewed_items(x_sail_point_experimental, access_request_recommendation_action_item_dto)
        print("The response of IAIAccessRequestRecommendationsApi->add_access_request_recommendations_viewed_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IAIAccessRequestRecommendationsApi->add_access_request_recommendations_viewed_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_sail_point_experimental** | **str**| Use this header to enable this experimental API. | [default to &#39;true&#39;]
 **access_request_recommendation_action_item_dto** | [**List[AccessRequestRecommendationActionItemDto]**](AccessRequestRecommendationActionItemDto.md)| The recommended access items that were viewed for an identity. | 

### Return type

[**List[AccessRequestRecommendationActionItemResponseDto]**](AccessRequestRecommendationActionItemResponseDto.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Recommendations successfully stored as viewed. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_access_request_recommendations**
> List[AccessRequestRecommendationItemDetail] get_access_request_recommendations(x_sail_point_experimental, identity_id=identity_id, limit=limit, offset=offset, count=count, include_translation_messages=include_translation_messages, filters=filters, sorters=sorters)

Identity Access Request Recommendations

This API returns the access request recommendations for the specified identity. The default identity is *me* which indicates the current user.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.v2024
from sailpoint.v2024.models.access_request_recommendation_item_detail import AccessRequestRecommendationItemDetail
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
    api_instance = sailpoint.v2024.IAIAccessRequestRecommendationsApi(api_client)
    x_sail_point_experimental = 'true' # str | Use this header to enable this experimental API. (default to 'true')
    identity_id = 'me' # str | Get access request recommendations for an identityId. *me* indicates the current user. (optional) (default to 'me')
    limit = 15 # int | Max number of results to return. (optional) (default to 15)
    offset = 0 # int | Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 0)
    count = False # bool | If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count=true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to False)
    include_translation_messages = False # bool | If *true* it will populate a list of translation messages in the response. (optional) (default to False)
    filters = 'access.name co \"admin\"' # str | Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **access.name**: *co*  **access.type**: *eq, in*  **access.description**: *co, eq, in* (optional)
    sorters = 'sorters_example' # str | Sort results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#sorting-results)  Sorting is supported for the following fields: **access.name, access.type**  By default the recommendations are sorted by highest confidence first. (optional)

    try:
        # Identity Access Request Recommendations
        api_response = api_instance.get_access_request_recommendations(x_sail_point_experimental, identity_id=identity_id, limit=limit, offset=offset, count=count, include_translation_messages=include_translation_messages, filters=filters, sorters=sorters)
        print("The response of IAIAccessRequestRecommendationsApi->get_access_request_recommendations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IAIAccessRequestRecommendationsApi->get_access_request_recommendations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_sail_point_experimental** | **str**| Use this header to enable this experimental API. | [default to &#39;true&#39;]
 **identity_id** | **str**| Get access request recommendations for an identityId. *me* indicates the current user. | [optional] [default to &#39;me&#39;]
 **limit** | **int**| Max number of results to return. | [optional] [default to 15]
 **offset** | **int**| Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to 0]
 **count** | **bool**| If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count&#x3D;true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to False]
 **include_translation_messages** | **bool**| If *true* it will populate a list of translation messages in the response. | [optional] [default to False]
 **filters** | **str**| Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **access.name**: *co*  **access.type**: *eq, in*  **access.description**: *co, eq, in* | [optional] 
 **sorters** | **str**| Sort results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#sorting-results)  Sorting is supported for the following fields: **access.name, access.type**  By default the recommendations are sorted by highest confidence first. | [optional] 

### Return type

[**List[AccessRequestRecommendationItemDetail]**](AccessRequestRecommendationItemDetail.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of access request recommendations for the identityId |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_access_request_recommendations_ignored_items**
> List[AccessRequestRecommendationActionItemResponseDto] get_access_request_recommendations_ignored_items(x_sail_point_experimental, limit=limit, offset=offset, count=count, filters=filters, sorters=sorters)

List of Ignored Access Request Recommendations

This API returns the list of ignored access request recommendations.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.v2024
from sailpoint.v2024.models.access_request_recommendation_action_item_response_dto import AccessRequestRecommendationActionItemResponseDto
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
    api_instance = sailpoint.v2024.IAIAccessRequestRecommendationsApi(api_client)
    x_sail_point_experimental = 'true' # str | Use this header to enable this experimental API. (default to 'true')
    limit = 250 # int | Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 250)
    offset = 0 # int | Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 0)
    count = False # bool | If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count=true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to False)
    filters = 'identityId eq \"2c9180846b0a0583016b299f210c1314\"' # str | Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **access.id**: *eq, in*  **access.type**: *eq, in*  **identityId**: *eq, in* (optional)
    sorters = 'access.id' # str | Sort results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#sorting-results)  Sorting is supported for the following fields: **access.id, access.type, identityId, timestamp** (optional)

    try:
        # List of Ignored Access Request Recommendations
        api_response = api_instance.get_access_request_recommendations_ignored_items(x_sail_point_experimental, limit=limit, offset=offset, count=count, filters=filters, sorters=sorters)
        print("The response of IAIAccessRequestRecommendationsApi->get_access_request_recommendations_ignored_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IAIAccessRequestRecommendationsApi->get_access_request_recommendations_ignored_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_sail_point_experimental** | **str**| Use this header to enable this experimental API. | [default to &#39;true&#39;]
 **limit** | **int**| Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to 250]
 **offset** | **int**| Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to 0]
 **count** | **bool**| If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count&#x3D;true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to False]
 **filters** | **str**| Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **access.id**: *eq, in*  **access.type**: *eq, in*  **identityId**: *eq, in* | [optional] 
 **sorters** | **str**| Sort results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#sorting-results)  Sorting is supported for the following fields: **access.id, access.type, identityId, timestamp** | [optional] 

### Return type

[**List[AccessRequestRecommendationActionItemResponseDto]**](AccessRequestRecommendationActionItemResponseDto.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns list of ignored access request recommendations. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_access_request_recommendations_requested_items**
> List[AccessRequestRecommendationActionItemResponseDto] get_access_request_recommendations_requested_items(x_sail_point_experimental, limit=limit, offset=offset, count=count, filters=filters, sorters=sorters)

List of Requested Access Request Recommendations

This API returns a list of requested access request recommendations.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.v2024
from sailpoint.v2024.models.access_request_recommendation_action_item_response_dto import AccessRequestRecommendationActionItemResponseDto
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
    api_instance = sailpoint.v2024.IAIAccessRequestRecommendationsApi(api_client)
    x_sail_point_experimental = 'true' # str | Use this header to enable this experimental API. (default to 'true')
    limit = 250 # int | Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 250)
    offset = 0 # int | Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 0)
    count = False # bool | If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count=true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to False)
    filters = 'access.id eq \"2c9180846b0a0583016b299f210c1314\"' # str | Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **access.id**: *eq, in*  **access.type**: *eq, in*  **identityId**: *eq, in* (optional)
    sorters = 'sorters_example' # str | Sort results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#sorting-results)  Sorting is supported for the following fields: **access.id, access.type, identityId, timestamp** (optional)

    try:
        # List of Requested Access Request Recommendations
        api_response = api_instance.get_access_request_recommendations_requested_items(x_sail_point_experimental, limit=limit, offset=offset, count=count, filters=filters, sorters=sorters)
        print("The response of IAIAccessRequestRecommendationsApi->get_access_request_recommendations_requested_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IAIAccessRequestRecommendationsApi->get_access_request_recommendations_requested_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_sail_point_experimental** | **str**| Use this header to enable this experimental API. | [default to &#39;true&#39;]
 **limit** | **int**| Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to 250]
 **offset** | **int**| Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to 0]
 **count** | **bool**| If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count&#x3D;true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to False]
 **filters** | **str**| Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **access.id**: *eq, in*  **access.type**: *eq, in*  **identityId**: *eq, in* | [optional] 
 **sorters** | **str**| Sort results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#sorting-results)  Sorting is supported for the following fields: **access.id, access.type, identityId, timestamp** | [optional] 

### Return type

[**List[AccessRequestRecommendationActionItemResponseDto]**](AccessRequestRecommendationActionItemResponseDto.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the list of requested access request recommendations. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_access_request_recommendations_viewed_items**
> List[AccessRequestRecommendationActionItemResponseDto] get_access_request_recommendations_viewed_items(x_sail_point_experimental, limit=limit, offset=offset, count=count, filters=filters, sorters=sorters)

List of Viewed Access Request Recommendations

This API returns the list of viewed access request recommendations.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.v2024
from sailpoint.v2024.models.access_request_recommendation_action_item_response_dto import AccessRequestRecommendationActionItemResponseDto
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
    api_instance = sailpoint.v2024.IAIAccessRequestRecommendationsApi(api_client)
    x_sail_point_experimental = 'true' # str | Use this header to enable this experimental API. (default to 'true')
    limit = 250 # int | Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 250)
    offset = 0 # int | Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 0)
    count = False # bool | If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count=true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to False)
    filters = 'access.id eq \"2c9180846b0a0583016b299f210c1314\"' # str | Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **access.id**: *eq, in*  **access.type**: *eq, in*  **identityId**: *eq, in* (optional)
    sorters = 'sorters_example' # str | Sort results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#sorting-results)  Sorting is supported for the following fields: **access.id, access.type, identityId, timestamp** (optional)

    try:
        # List of Viewed Access Request Recommendations
        api_response = api_instance.get_access_request_recommendations_viewed_items(x_sail_point_experimental, limit=limit, offset=offset, count=count, filters=filters, sorters=sorters)
        print("The response of IAIAccessRequestRecommendationsApi->get_access_request_recommendations_viewed_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IAIAccessRequestRecommendationsApi->get_access_request_recommendations_viewed_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_sail_point_experimental** | **str**| Use this header to enable this experimental API. | [default to &#39;true&#39;]
 **limit** | **int**| Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to 250]
 **offset** | **int**| Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to 0]
 **count** | **bool**| If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count&#x3D;true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to False]
 **filters** | **str**| Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **access.id**: *eq, in*  **access.type**: *eq, in*  **identityId**: *eq, in* | [optional] 
 **sorters** | **str**| Sort results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#sorting-results)  Sorting is supported for the following fields: **access.id, access.type, identityId, timestamp** | [optional] 

### Return type

[**List[AccessRequestRecommendationActionItemResponseDto]**](AccessRequestRecommendationActionItemResponseDto.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns list of viewed access request recommendations. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

