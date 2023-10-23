# beta.IAIRecommendationsApi

All URIs are relative to *https://sailpoint.api.identitynow.com/beta*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_message_catalogs**](IAIRecommendationsApi.md#get_message_catalogs) | **GET** /translation-catalogs/{catalog-id} | Get Message catalogs
[**get_recommendations**](IAIRecommendationsApi.md#get_recommendations) | **POST** /recommendations/request | Returns a Recommendation Based on Object
[**get_recommendations_config**](IAIRecommendationsApi.md#get_recommendations_config) | **GET** /recommendations/config | Get certification recommendation config values
[**update_recommendations_config**](IAIRecommendationsApi.md#update_recommendations_config) | **PUT** /recommendations/config | Update certification recommendation config values


# **get_message_catalogs**
> List[MessageCatalogDto] get_message_catalogs(catalog_id)

Get Message catalogs

The getMessageCatalogs API returns message catalog based on the language headers in the requested object.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import beta
from beta.models.message_catalog_dto import MessageCatalogDto
from beta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/beta
# See configuration.py for a list of all supported configuration parameters.
configuration = beta.Configuration(
    host = "https://sailpoint.api.identitynow.com/beta"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with beta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = beta.IAIRecommendationsApi(api_client)
    catalog_id = 'catalog_id_example' # str | The ID of the message catalog.

    try:
        # Get Message catalogs
        api_response = api_instance.get_message_catalogs(catalog_id)
        print("The response of IAIRecommendationsApi->get_message_catalogs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IAIRecommendationsApi->get_message_catalogs: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog_id** | **str**| The ID of the message catalog. | 

### Return type

[**List[MessageCatalogDto]**](MessageCatalogDto.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

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

# **get_recommendations**
> RecommendationResponseDto get_recommendations(recommendation_request_dto)

Returns a Recommendation Based on Object

The getRecommendations API returns recommendations based on the requested object. The recommendations are invoked by IdentityIQ and IdentityNow plug-ins that retrieve recommendations based on the performed calculations.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import beta
from beta.models.recommendation_request_dto import RecommendationRequestDto
from beta.models.recommendation_response_dto import RecommendationResponseDto
from beta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/beta
# See configuration.py for a list of all supported configuration parameters.
configuration = beta.Configuration(
    host = "https://sailpoint.api.identitynow.com/beta"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with beta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = beta.IAIRecommendationsApi(api_client)
    recommendation_request_dto = beta.RecommendationRequestDto() # RecommendationRequestDto | 

    try:
        # Returns a Recommendation Based on Object
        api_response = api_instance.get_recommendations(recommendation_request_dto)
        print("The response of IAIRecommendationsApi->get_recommendations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IAIRecommendationsApi->get_recommendations: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recommendation_request_dto** | [**RecommendationRequestDto**](RecommendationRequestDto.md)|  | 

### Return type

[**RecommendationResponseDto**](RecommendationResponseDto.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The recommendations for a customer |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recommendations_config**
> RecommendationConfigDto get_recommendations_config()

Get certification recommendation config values

Retrieves configuration attributes used by certification recommendations.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import beta
from beta.models.recommendation_config_dto import RecommendationConfigDto
from beta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/beta
# See configuration.py for a list of all supported configuration parameters.
configuration = beta.Configuration(
    host = "https://sailpoint.api.identitynow.com/beta"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with beta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = beta.IAIRecommendationsApi(api_client)

    try:
        # Get certification recommendation config values
        api_response = api_instance.get_recommendations_config()
        print("The response of IAIRecommendationsApi->get_recommendations_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IAIRecommendationsApi->get_recommendations_config: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**RecommendationConfigDto**](RecommendationConfigDto.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Cert recommendation configuration attributes |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_recommendations_config**
> RecommendationConfigDto update_recommendations_config(recommendation_config_dto)

Update certification recommendation config values

Updates configuration attributes used by certification recommendations.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import beta
from beta.models.recommendation_config_dto import RecommendationConfigDto
from beta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/beta
# See configuration.py for a list of all supported configuration parameters.
configuration = beta.Configuration(
    host = "https://sailpoint.api.identitynow.com/beta"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with beta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = beta.IAIRecommendationsApi(api_client)
    recommendation_config_dto = beta.RecommendationConfigDto() # RecommendationConfigDto | 

    try:
        # Update certification recommendation config values
        api_response = api_instance.update_recommendations_config(recommendation_config_dto)
        print("The response of IAIRecommendationsApi->update_recommendations_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IAIRecommendationsApi->update_recommendations_config: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recommendation_config_dto** | [**RecommendationConfigDto**](RecommendationConfigDto.md)|  | 

### Return type

[**RecommendationConfigDto**](RecommendationConfigDto.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Cert recommendation configuration attributes after update |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

