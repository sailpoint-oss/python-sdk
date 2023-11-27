# sailpoint.beta.RoleInsightsApi

All URIs are relative to *https://sailpoint.api.identitynow.com/beta*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_role_insight_requests**](RoleInsightsApi.md#create_role_insight_requests) | **POST** /role-insights/requests | Generate insights for roles
[**download_role_insights_entitlements_changes**](RoleInsightsApi.md#download_role_insights_entitlements_changes) | **GET** /role-insights/{insightId}/entitlement-changes/download | Download entitlement insights for a role
[**get_entitlement_changes_identities**](RoleInsightsApi.md#get_entitlement_changes_identities) | **GET** /role-insights/{insightId}/entitlement-changes/{entitlementId}/identities | Get identities for a suggested entitlement (for a role)
[**get_role_insight**](RoleInsightsApi.md#get_role_insight) | **GET** /role-insights/{insightId} | Get a single role insight
[**get_role_insights**](RoleInsightsApi.md#get_role_insights) | **GET** /role-insights | Get role insights
[**get_role_insights_current_entitlements**](RoleInsightsApi.md#get_role_insights_current_entitlements) | **GET** /role-insights/{insightId}/current-entitlements | Get current entitlement for a role
[**get_role_insights_entitlements_changes**](RoleInsightsApi.md#get_role_insights_entitlements_changes) | **GET** /role-insights/{insightId}/entitlement-changes | Get entitlement insights for a role
[**get_role_insights_requests**](RoleInsightsApi.md#get_role_insights_requests) | **GET** /role-insights/requests/{id} | Returns metadata from prior request.
[**get_role_insights_summary**](RoleInsightsApi.md#get_role_insights_summary) | **GET** /role-insights/summary | Get role insights summary information


# **create_role_insight_requests**
> RoleInsightsResponse create_role_insight_requests()

Generate insights for roles

Submits a create role insights request to the role insights application. At this time there are no parameters. All business roles will be processed for the customer.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import sailpoint.beta
from sailpoint.beta.models.role_insights_response import RoleInsightsResponse
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
    api_instance = sailpoint.beta.RoleInsightsApi(api_client)

    try:
        # Generate insights for roles
        api_response = api_instance.create_role_insight_requests()
        print("The response of RoleInsightsApi->create_role_insight_requests:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleInsightsApi->create_role_insight_requests: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**RoleInsightsResponse**](RoleInsightsResponse.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Submitted a role insights generation request |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_role_insights_entitlements_changes**
> str download_role_insights_entitlements_changes(insight_id, sorters=sorters, filters=filters)

Download entitlement insights for a role

This endpoint returns the entitlement insights for a role.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import sailpoint.beta
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
    api_instance = sailpoint.beta.RoleInsightsApi(api_client)
    insight_id = '8c190e67-87aa-4ed9-a90b-d9d5344523fb' # str | The role insight id
    sorters = 'identitiesWithAccess' # str | Sort results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#sorting-results)  Sorting is supported for the following fields: **identitiesWithAccess**  The default sort is **identitiesWithAccess** in descending order. (optional)
    filters = 'name sw \"r\"' # str | Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **name**: *sw*  **description**: *sw* (optional)

    try:
        # Download entitlement insights for a role
        api_response = api_instance.download_role_insights_entitlements_changes(insight_id, sorters=sorters, filters=filters)
        print("The response of RoleInsightsApi->download_role_insights_entitlements_changes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleInsightsApi->download_role_insights_entitlements_changes: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **insight_id** | **str**| The role insight id | 
 **sorters** | **str**| Sort results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#sorting-results)  Sorting is supported for the following fields: **identitiesWithAccess**  The default sort is **identitiesWithAccess** in descending order. | [optional] 
 **filters** | **str**| Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **name**: *sw*  **description**: *sw* | [optional] 

### Return type

**str**

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/csv, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Succeeded. Returns a csv file containing a list of entitlements to be added for a role. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_entitlement_changes_identities**
> List[RoleInsightsIdentities] get_entitlement_changes_identities(insight_id, entitlement_id, has_entitlement=has_entitlement, offset=offset, limit=limit, count=count, sorters=sorters, filters=filters)

Get identities for a suggested entitlement (for a role)

Role insights suggests entitlements to be added for a role. This endpoint returns a list of identities in the role, with or without the entitlements, for a suggested entitlement so that the user can see which identities would be affected if the suggested entitlement were to be added to the role.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import sailpoint.beta
from sailpoint.beta.models.role_insights_identities import RoleInsightsIdentities
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
    api_instance = sailpoint.beta.RoleInsightsApi(api_client)
    insight_id = '8c190e67-87aa-4ed9-a90b-d9d5344523fb' # str | The role insight id
    entitlement_id = '8c190e67-87aa-4ed9-a90b-d9d5344523fb' # str | The entitlement id
    has_entitlement = False # bool | Identity has this entitlement or not (optional) (default to False)
    offset = 0 # int | Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 0)
    limit = 250 # int | Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 250)
    count = False # bool | If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count=true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to False)
    sorters = 'name' # str | Sort results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#sorting-results)  Sorting is supported for the following fields: **name** (optional)
    filters = 'name sw \"Jan\"' # str | Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **name**: *sw* (optional)

    try:
        # Get identities for a suggested entitlement (for a role)
        api_response = api_instance.get_entitlement_changes_identities(insight_id, entitlement_id, has_entitlement=has_entitlement, offset=offset, limit=limit, count=count, sorters=sorters, filters=filters)
        print("The response of RoleInsightsApi->get_entitlement_changes_identities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleInsightsApi->get_entitlement_changes_identities: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **insight_id** | **str**| The role insight id | 
 **entitlement_id** | **str**| The entitlement id | 
 **has_entitlement** | **bool**| Identity has this entitlement or not | [optional] [default to False]
 **offset** | **int**| Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to 0]
 **limit** | **int**| Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to 250]
 **count** | **bool**| If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count&#x3D;true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to False]
 **sorters** | **str**| Sort results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#sorting-results)  Sorting is supported for the following fields: **name** | [optional] 
 **filters** | **str**| Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **name**: *sw* | [optional] 

### Return type

[**List[RoleInsightsIdentities]**](RoleInsightsIdentities.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Succeeded. Returns a list of identities with or without the entitlement. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_role_insight**
> RoleInsight get_role_insight(insight_id)

Get a single role insight

This endpoint gets role insights information for a role.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import sailpoint.beta
from sailpoint.beta.models.role_insight import RoleInsight
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
    api_instance = sailpoint.beta.RoleInsightsApi(api_client)
    insight_id = '8c190e67-87aa-4ed9-a90b-d9d5344523fb' # str | The role insight id

    try:
        # Get a single role insight
        api_response = api_instance.get_role_insight(insight_id)
        print("The response of RoleInsightsApi->get_role_insight:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleInsightsApi->get_role_insight: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **insight_id** | **str**| The role insight id | 

### Return type

[**RoleInsight**](RoleInsight.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Succeeded. Returns information about insights for a single role. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_role_insights**
> List[RoleInsight] get_role_insights(offset=offset, limit=limit, count=count, sorters=sorters, filters=filters)

Get role insights

This method returns detailed role insights for each role.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import sailpoint.beta
from sailpoint.beta.models.role_insight import RoleInsight
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
    api_instance = sailpoint.beta.RoleInsightsApi(api_client)
    offset = 0 # int | Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 0)
    limit = 250 # int | Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 250)
    count = False # bool | If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count=true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to False)
    sorters = 'numberOfUpdates' # str | Sort results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#sorting-results)  Sorting is supported for the following fields: **numberOfUpdates, identitiesWithAccess, totalNumberOfIdentities** (optional)
    filters = 'name sw \"John\"' # str | Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **name**: *sw*  **ownerName**: *sw*  **description**: *sw* (optional)

    try:
        # Get role insights
        api_response = api_instance.get_role_insights(offset=offset, limit=limit, count=count, sorters=sorters, filters=filters)
        print("The response of RoleInsightsApi->get_role_insights:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleInsightsApi->get_role_insights: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to 0]
 **limit** | **int**| Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to 250]
 **count** | **bool**| If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count&#x3D;true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to False]
 **sorters** | **str**| Sort results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#sorting-results)  Sorting is supported for the following fields: **numberOfUpdates, identitiesWithAccess, totalNumberOfIdentities** | [optional] 
 **filters** | **str**| Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **name**: *sw*  **ownerName**: *sw*  **description**: *sw* | [optional] 

### Return type

[**List[RoleInsight]**](RoleInsight.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Succeeded. Returns a list of roles with information about insights for each role. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_role_insights_current_entitlements**
> List[RoleInsightsEntitlement] get_role_insights_current_entitlements(insight_id, filters=filters)

Get current entitlement for a role

This endpoint gets the entitlements for a role. The term \"current\" is to distinguish from the entitlement(s) an insight might recommend adding.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import sailpoint.beta
from sailpoint.beta.models.role_insights_entitlement import RoleInsightsEntitlement
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
    api_instance = sailpoint.beta.RoleInsightsApi(api_client)
    insight_id = '8c190e67-87aa-4ed9-a90b-d9d5344523fb' # str | The role insight id
    filters = 'name sw \"r\"' # str | Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **name**: *sw*  **description**: *sw* (optional)

    try:
        # Get current entitlement for a role
        api_response = api_instance.get_role_insights_current_entitlements(insight_id, filters=filters)
        print("The response of RoleInsightsApi->get_role_insights_current_entitlements:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleInsightsApi->get_role_insights_current_entitlements: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **insight_id** | **str**| The role insight id | 
 **filters** | **str**| Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **name**: *sw*  **description**: *sw* | [optional] 

### Return type

[**List[RoleInsightsEntitlement]**](RoleInsightsEntitlement.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Succeeded. Returns a list of current or pre-existing entitlements for a role. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_role_insights_entitlements_changes**
> List[RoleInsightsEntitlementChanges] get_role_insights_entitlements_changes(insight_id, sorters=sorters, filters=filters)

Get entitlement insights for a role

This endpoint returns entitlement insights for a role.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import sailpoint.beta
from sailpoint.beta.models.role_insights_entitlement_changes import RoleInsightsEntitlementChanges
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
    api_instance = sailpoint.beta.RoleInsightsApi(api_client)
    insight_id = '8c190e67-87aa-4ed9-a90b-d9d5344523fb' # str | The role insight id
    sorters = 'sorters_example' # str | Sort results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#sorting-results)  Sorting is supported for the following fields: **identitiesWithAccess, name** (optional)
    filters = 'name sw \"Admin\"' # str | Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **name**: *sw*  **description**: *sw* (optional)

    try:
        # Get entitlement insights for a role
        api_response = api_instance.get_role_insights_entitlements_changes(insight_id, sorters=sorters, filters=filters)
        print("The response of RoleInsightsApi->get_role_insights_entitlements_changes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleInsightsApi->get_role_insights_entitlements_changes: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **insight_id** | **str**| The role insight id | 
 **sorters** | **str**| Sort results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#sorting-results)  Sorting is supported for the following fields: **identitiesWithAccess, name** | [optional] 
 **filters** | **str**| Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **name**: *sw*  **description**: *sw* | [optional] 

### Return type

[**List[RoleInsightsEntitlementChanges]**](RoleInsightsEntitlementChanges.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Succeeded. Returns a list of entitlements to be added for a role. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_role_insights_requests**
> RoleInsightsResponse get_role_insights_requests(id)

Returns metadata from prior request.

This endpoint returns details of a prior role insights request. 

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import sailpoint.beta
from sailpoint.beta.models.role_insights_response import RoleInsightsResponse
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
    api_instance = sailpoint.beta.RoleInsightsApi(api_client)
    id = '8c190e67-87aa-4ed9-a90b-d9d5344523fb' # str | The role insights request id

    try:
        # Returns metadata from prior request.
        api_response = api_instance.get_role_insights_requests(id)
        print("The response of RoleInsightsApi->get_role_insights_requests:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleInsightsApi->get_role_insights_requests: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The role insights request id | 

### Return type

[**RoleInsightsResponse**](RoleInsightsResponse.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Succeeded. Returns details of an earlier role insights request. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_role_insights_summary**
> RoleInsightsSummary get_role_insights_summary()

Get role insights summary information

This method returns high level summary information for role insights for a customer.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import sailpoint.beta
from sailpoint.beta.models.role_insights_summary import RoleInsightsSummary
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
    api_instance = sailpoint.beta.RoleInsightsApi(api_client)

    try:
        # Get role insights summary information
        api_response = api_instance.get_role_insights_summary()
        print("The response of RoleInsightsApi->get_role_insights_summary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleInsightsApi->get_role_insights_summary: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**RoleInsightsSummary**](RoleInsightsSummary.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Succeeded. Returns high level counts. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

