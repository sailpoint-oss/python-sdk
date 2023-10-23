# v3.AccountActivitiesApi

All URIs are relative to *https://sailpoint.api.identitynow.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_account_activity**](AccountActivitiesApi.md#get_account_activity) | **GET** /account-activities/{id} | Get an Account Activity
[**list_account_activities**](AccountActivitiesApi.md#list_account_activities) | **GET** /account-activities | List Account Activities


# **get_account_activity**
> AccountActivity get_account_activity(id)

Get an Account Activity

This gets a single account activity by its id.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import v3
from v3.models.account_activity import AccountActivity
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
    api_instance = v3.AccountActivitiesApi(api_client)
    id = 'ef38f94347e94562b5bb8424a56397d8' # str | The account activity id

    try:
        # Get an Account Activity
        api_response = api_instance.get_account_activity(id)
        print("The response of AccountActivitiesApi->get_account_activity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountActivitiesApi->get_account_activity: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The account activity id | 

### Return type

[**AccountActivity**](AccountActivity.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An account activity object |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_account_activities**
> List[AccountActivity] list_account_activities(requested_for=requested_for, requested_by=requested_by, regarding_identity=regarding_identity, limit=limit, offset=offset, count=count, filters=filters, sorters=sorters)

List Account Activities

This gets a collection of account activities that satisfy the given query parameters.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import v3
from v3.models.account_activity import AccountActivity
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
    api_instance = v3.AccountActivitiesApi(api_client)
    requested_for = '2c91808568c529c60168cca6f90c1313' # str | The identity that the activity was requested for. *me* indicates the current user. Mutually exclusive with *regarding-identity*. (optional)
    requested_by = '2c91808568c529c60168cca6f90c1313' # str | The identity that requested the activity. *me* indicates the current user. Mutually exclusive with *regarding-identity*. (optional)
    regarding_identity = '2c91808568c529c60168cca6f90c1313' # str | The specified identity will be either the requester or target of the account activity. *me* indicates the current user. Mutually exclusive with *requested-for* and *requested-by*. (optional)
    limit = 250 # int | Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 250)
    offset = 0 # int | Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 0)
    count = False # bool | If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count=true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to False)
    filters = 'type eq \"Identity Refresh\"' # str | Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results).  Filtering is supported for the following fields and operators:  **type**: *eq, in* (See the `type` property in the response schema for possible values)  **created**: *gt, lt, ge, le*  **modified**: *gt, lt, ge, le* (optional)
    sorters = 'created' # str | Sort results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#sorting-results) Sorting is supported for the following fields: **type, created, modified** (optional)

    try:
        # List Account Activities
        api_response = api_instance.list_account_activities(requested_for=requested_for, requested_by=requested_by, regarding_identity=regarding_identity, limit=limit, offset=offset, count=count, filters=filters, sorters=sorters)
        print("The response of AccountActivitiesApi->list_account_activities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountActivitiesApi->list_account_activities: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **requested_for** | **str**| The identity that the activity was requested for. *me* indicates the current user. Mutually exclusive with *regarding-identity*. | [optional] 
 **requested_by** | **str**| The identity that requested the activity. *me* indicates the current user. Mutually exclusive with *regarding-identity*. | [optional] 
 **regarding_identity** | **str**| The specified identity will be either the requester or target of the account activity. *me* indicates the current user. Mutually exclusive with *requested-for* and *requested-by*. | [optional] 
 **limit** | **int**| Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to 250]
 **offset** | **int**| Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to 0]
 **count** | **bool**| If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count&#x3D;true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to False]
 **filters** | **str**| Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results).  Filtering is supported for the following fields and operators:  **type**: *eq, in* (See the &#x60;type&#x60; property in the response schema for possible values)  **created**: *gt, lt, ge, le*  **modified**: *gt, lt, ge, le* | [optional] 
 **sorters** | **str**| Sort results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#sorting-results) Sorting is supported for the following fields: **type, created, modified** | [optional] 

### Return type

[**List[AccountActivity]**](AccountActivity.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of account activities |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

