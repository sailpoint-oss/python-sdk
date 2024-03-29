# sailpoint.beta.EntitlementsApi

All URIs are relative to *https://sailpoint.api.identitynow.com/beta*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_entitlement**](EntitlementsApi.md#get_entitlement) | **GET** /entitlements/{id} | Get an entitlement
[**get_entitlement_request_config**](EntitlementsApi.md#get_entitlement_request_config) | **GET** /entitlements/{id}/entitlement-request-config | Get Entitlement Request Config
[**import_entitlements**](EntitlementsApi.md#import_entitlements) | **POST** /entitlements/aggregate/sources/{id} | Aggregate Entitlements
[**list_entitlement_children**](EntitlementsApi.md#list_entitlement_children) | **GET** /entitlements/{id}/children | List of entitlements children
[**list_entitlement_parents**](EntitlementsApi.md#list_entitlement_parents) | **GET** /entitlements/{id}/parents | List of entitlements parents
[**list_entitlements**](EntitlementsApi.md#list_entitlements) | **GET** /entitlements | Gets a list of entitlements.
[**patch_entitlement**](EntitlementsApi.md#patch_entitlement) | **PATCH** /entitlements/{id} | Patch an entitlement
[**put_entitlement_request_config**](EntitlementsApi.md#put_entitlement_request_config) | **PUT** /entitlements/{id}/entitlement-request-config | Replace Entitlement Request Config
[**reset_source_entitlements**](EntitlementsApi.md#reset_source_entitlements) | **POST** /entitlements/reset/sources/{id} | Reset Source Entitlements
[**update_entitlements_in_bulk**](EntitlementsApi.md#update_entitlements_in_bulk) | **POST** /entitlements/bulk-update | Bulk update an entitlement list


# **get_entitlement**
> Entitlement get_entitlement(id)

Get an entitlement

This API returns an entitlement by its ID.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.beta
from sailpoint.beta.models.entitlement import Entitlement
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
    api_instance = sailpoint.beta.EntitlementsApi(api_client)
    id = '2c91808874ff91550175097daaec161c' # str | The entitlement ID

    try:
        # Get an entitlement
        api_response = api_instance.get_entitlement(id)
        print("The response of EntitlementsApi->get_entitlement:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitlementsApi->get_entitlement: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The entitlement ID | 

### Return type

[**Entitlement**](Entitlement.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An entitlement |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_entitlement_request_config**
> EntitlementRequestConfig get_entitlement_request_config(id)

Get Entitlement Request Config

This API returns the entitlement request config for a specified entitlement.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.beta
from sailpoint.beta.models.entitlement_request_config import EntitlementRequestConfig
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
    api_instance = sailpoint.beta.EntitlementsApi(api_client)
    id = '2c91808874ff91550175097daaec161c' # str | Entitlement Id

    try:
        # Get Entitlement Request Config
        api_response = api_instance.get_entitlement_request_config(id)
        print("The response of EntitlementsApi->get_entitlement_request_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitlementsApi->get_entitlement_request_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Entitlement Id | 

### Return type

[**EntitlementRequestConfig**](EntitlementRequestConfig.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An Entitlement Request Config |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_entitlements**
> LoadEntitlementTask import_entitlements(id, csv_file)

Aggregate Entitlements

Starts an entitlement aggregation on the specified source.  If the target source is a direct connection, then the request body must be empty. You will also need to make sure the Content-Type header is not set. If you set the Content-Type header without specifying a body, then you will receive a 500 error. If the target source is a delimited file source, then the CSV file needs to be included in the request body. You will also need to set the Content-Type header to `multipart/form-data`.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.beta
from sailpoint.beta.models.load_entitlement_task import LoadEntitlementTask
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
    api_instance = sailpoint.beta.EntitlementsApi(api_client)
    id = 'ef38f94347e94562b5bb8424a56397d8' # str | Source Id
    csv_file = None # bytearray | 

    try:
        # Aggregate Entitlements
        api_response = api_instance.import_entitlements(id, csv_file)
        print("The response of EntitlementsApi->import_entitlements:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitlementsApi->import_entitlements: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Source Id | 
 **csv_file** | **bytearray**|  | 

### Return type

[**LoadEntitlementTask**](LoadEntitlementTask.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Aggregate Entitlements Task |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_entitlement_children**
> List[Entitlement] list_entitlement_children(id, limit=limit, offset=offset, count=count, sorters=sorters, filters=filters)

List of entitlements children

This API returns a list of all child entitlements of a given entitlement.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.beta
from sailpoint.beta.models.entitlement import Entitlement
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
    api_instance = sailpoint.beta.EntitlementsApi(api_client)
    id = '2c91808874ff91550175097daaec161c' # str | Entitlement Id
    limit = 250 # int | Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 250)
    offset = 0 # int | Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 0)
    count = False # bool | If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count=true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to False)
    sorters = 'name,-modified' # str | Sort results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#sorting-results)  Sorting is supported for the following fields: **id, name, created, modified, type, attribute, value, source.id** (optional)
    filters = 'attribute eq \"memberOf\"' # str | Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **id**: *eq, in*  **name**: *eq, in, sw*  **type**: *eq, in*  **attribute**: *eq, in*  **value**: *eq, in, sw*  **source.id**: *eq, in*  **requestable**: *eq*  **created**: *gt, lt, ge, le*  **modified**: *gt, lt, ge, le* (optional)

    try:
        # List of entitlements children
        api_response = api_instance.list_entitlement_children(id, limit=limit, offset=offset, count=count, sorters=sorters, filters=filters)
        print("The response of EntitlementsApi->list_entitlement_children:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitlementsApi->list_entitlement_children: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Entitlement Id | 
 **limit** | **int**| Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to 250]
 **offset** | **int**| Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to 0]
 **count** | **bool**| If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count&#x3D;true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to False]
 **sorters** | **str**| Sort results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#sorting-results)  Sorting is supported for the following fields: **id, name, created, modified, type, attribute, value, source.id** | [optional] 
 **filters** | **str**| Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **id**: *eq, in*  **name**: *eq, in, sw*  **type**: *eq, in*  **attribute**: *eq, in*  **value**: *eq, in, sw*  **source.id**: *eq, in*  **requestable**: *eq*  **created**: *gt, lt, ge, le*  **modified**: *gt, lt, ge, le* | [optional] 

### Return type

[**List[Entitlement]**](Entitlement.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of entitlements children from an entitlement |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_entitlement_parents**
> List[Entitlement] list_entitlement_parents(id, limit=limit, offset=offset, count=count, sorters=sorters, filters=filters)

List of entitlements parents

This API returns a list of all parent entitlements of a given entitlement.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.beta
from sailpoint.beta.models.entitlement import Entitlement
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
    api_instance = sailpoint.beta.EntitlementsApi(api_client)
    id = '2c91808c74ff913f0175097daa9d59cd' # str | Entitlement Id
    limit = 250 # int | Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 250)
    offset = 0 # int | Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 0)
    count = False # bool | If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count=true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to False)
    sorters = 'name,-modified' # str | Sort results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#sorting-results)  Sorting is supported for the following fields: **id, name, created, modified, type, attribute, value, source.id** (optional)
    filters = 'attribute eq \"memberOf\"' # str | Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **id**: *eq, in*  **name**: *eq, in, sw*  **type**: *eq, in*  **attribute**: *eq, in*  **value**: *eq, in, sw*  **source.id**: *eq, in*  **requestable**: *eq*  **created**: *gt, lt, ge, le*  **modified**: *gt, lt, ge, le* (optional)

    try:
        # List of entitlements parents
        api_response = api_instance.list_entitlement_parents(id, limit=limit, offset=offset, count=count, sorters=sorters, filters=filters)
        print("The response of EntitlementsApi->list_entitlement_parents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitlementsApi->list_entitlement_parents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Entitlement Id | 
 **limit** | **int**| Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to 250]
 **offset** | **int**| Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to 0]
 **count** | **bool**| If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count&#x3D;true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to False]
 **sorters** | **str**| Sort results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#sorting-results)  Sorting is supported for the following fields: **id, name, created, modified, type, attribute, value, source.id** | [optional] 
 **filters** | **str**| Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **id**: *eq, in*  **name**: *eq, in, sw*  **type**: *eq, in*  **attribute**: *eq, in*  **value**: *eq, in, sw*  **source.id**: *eq, in*  **requestable**: *eq*  **created**: *gt, lt, ge, le*  **modified**: *gt, lt, ge, le* | [optional] 

### Return type

[**List[Entitlement]**](Entitlement.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of entitlements parents from an entitlement |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_entitlements**
> List[Entitlement] list_entitlements(account_id=account_id, segmented_for_identity=segmented_for_identity, for_segment_ids=for_segment_ids, include_unsegmented=include_unsegmented, offset=offset, limit=limit, count=count, sorters=sorters, filters=filters)

Gets a list of entitlements.

This API returns a list of entitlements.  This API can be used in one of the two following ways: either getting entitlements for a specific **account-id**, or getting via use of **filters** (those two options are exclusive).  Any authenticated token can call this API.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.beta
from sailpoint.beta.models.entitlement import Entitlement
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
    api_instance = sailpoint.beta.EntitlementsApi(api_client)
    account_id = 'ef38f94347e94562b5bb8424a56397d8' # str | The account ID. If specified, returns only entitlements associated with the given Account. Cannot be specified with the **filters**, **segmented-for-identity**, **for-segment-ids**, or **include-unsegmented** param(s). (optional)
    segmented_for_identity = 'me' # str | If present and not empty, additionally filters Entitlements to those which are assigned to the Segment(s) which are visible to the Identity with the specified ID. By convention, the value **me** can stand in for the current user's Identity ID. Cannot be specified with the **account-id** or **for-segment-ids** param(s). It is also illegal to specify a value that refers to a different user's Identity. (optional)
    for_segment_ids = '041727d4-7d95-4779-b891-93cf41e98249,a378c9fa-bae5-494c-804e-a1e30f69f649' # str | If present and not empty, additionally filters Access Profiles to those which are assigned to the Segment(s) with the specified IDs. Cannot be specified with the **account-id** or **segmented-for-identity** param(s). (optional)
    include_unsegmented = True # bool | Whether or not the response list should contain unsegmented Entitlements. If **for-segment-ids** and **segmented-for-identity** are both absent or empty, specifying **include-unsegmented=false** results in an error. (optional) (default to True)
    offset = 0 # int | Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 0)
    limit = 250 # int | Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 250)
    count = False # bool | If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count=true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to False)
    sorters = 'name,-modified' # str | Sort results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#sorting-results)  Sorting is supported for the following fields: **id, name, created, modified, type, attribute, value, source.id, requestable** (optional)
    filters = 'attribute eq \"memberOf\"' # str | Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **id**: *eq, in*  **name**: *eq, in, sw*  **type**: *eq, in*  **attribute**: *eq, in*  **value**: *eq, in, sw*  **source.id**: *eq, in*  **requestable**: *eq*  **created**: *gt, lt, ge, le*  **modified**: *gt, lt, ge, le*  **owner.id**: *eq, in* (optional)

    try:
        # Gets a list of entitlements.
        api_response = api_instance.list_entitlements(account_id=account_id, segmented_for_identity=segmented_for_identity, for_segment_ids=for_segment_ids, include_unsegmented=include_unsegmented, offset=offset, limit=limit, count=count, sorters=sorters, filters=filters)
        print("The response of EntitlementsApi->list_entitlements:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitlementsApi->list_entitlements: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The account ID. If specified, returns only entitlements associated with the given Account. Cannot be specified with the **filters**, **segmented-for-identity**, **for-segment-ids**, or **include-unsegmented** param(s). | [optional] 
 **segmented_for_identity** | **str**| If present and not empty, additionally filters Entitlements to those which are assigned to the Segment(s) which are visible to the Identity with the specified ID. By convention, the value **me** can stand in for the current user&#39;s Identity ID. Cannot be specified with the **account-id** or **for-segment-ids** param(s). It is also illegal to specify a value that refers to a different user&#39;s Identity. | [optional] 
 **for_segment_ids** | **str**| If present and not empty, additionally filters Access Profiles to those which are assigned to the Segment(s) with the specified IDs. Cannot be specified with the **account-id** or **segmented-for-identity** param(s). | [optional] 
 **include_unsegmented** | **bool**| Whether or not the response list should contain unsegmented Entitlements. If **for-segment-ids** and **segmented-for-identity** are both absent or empty, specifying **include-unsegmented&#x3D;false** results in an error. | [optional] [default to True]
 **offset** | **int**| Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to 0]
 **limit** | **int**| Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to 250]
 **count** | **bool**| If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count&#x3D;true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to False]
 **sorters** | **str**| Sort results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#sorting-results)  Sorting is supported for the following fields: **id, name, created, modified, type, attribute, value, source.id, requestable** | [optional] 
 **filters** | **str**| Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **id**: *eq, in*  **name**: *eq, in, sw*  **type**: *eq, in*  **attribute**: *eq, in*  **value**: *eq, in, sw*  **source.id**: *eq, in*  **requestable**: *eq*  **created**: *gt, lt, ge, le*  **modified**: *gt, lt, ge, le*  **owner.id**: *eq, in* | [optional] 

### Return type

[**List[Entitlement]**](Entitlement.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of entitlements |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_entitlement**
> Entitlement patch_entitlement(id, json_patch_operation=json_patch_operation)

Patch an entitlement

This API updates an existing entitlement using [JSON Patch](https://tools.ietf.org/html/rfc6902) syntax.  The following fields are patchable: **requestable**, **privileged**, **segments**, **owner**, **name**, **description**, and **manuallyUpdatedFields**  When you're patching owner, only owner type and owner id must be provided. Owner name is optional, and it won't be modified. If the owner name is provided, it should correspond to the real name. The only owner type currently supported is IDENTITY.  A token with ORG_ADMIN or SOURCE_ADMIN authority is required to call this API.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.beta
from sailpoint.beta.models.entitlement import Entitlement
from sailpoint.beta.models.json_patch_operation import JsonPatchOperation
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
    api_instance = sailpoint.beta.EntitlementsApi(api_client)
    id = '2c91808a7813090a017814121e121518' # str | ID of the entitlement to patch
    json_patch_operation = [{op=replace, path=/requestable, value=true}, {op=replace, path=/privileged, value=true}] # List[JsonPatchOperation] |  (optional)

    try:
        # Patch an entitlement
        api_response = api_instance.patch_entitlement(id, json_patch_operation=json_patch_operation)
        print("The response of EntitlementsApi->patch_entitlement:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitlementsApi->patch_entitlement: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the entitlement to patch | 
 **json_patch_operation** | [**List[JsonPatchOperation]**](JsonPatchOperation.md)|  | [optional] 

### Return type

[**Entitlement**](Entitlement.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Responds with the entitlement as updated. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_entitlement_request_config**
> EntitlementRequestConfig put_entitlement_request_config(id, entitlement_request_config)

Replace Entitlement Request Config

This API replaces the entitlement request config for a specified entitlement.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.beta
from sailpoint.beta.models.entitlement_request_config import EntitlementRequestConfig
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
    api_instance = sailpoint.beta.EntitlementsApi(api_client)
    id = '2c91808a7813090a017814121e121518' # str | Entitlement ID
    entitlement_request_config = sailpoint.beta.EntitlementRequestConfig() # EntitlementRequestConfig | 

    try:
        # Replace Entitlement Request Config
        api_response = api_instance.put_entitlement_request_config(id, entitlement_request_config)
        print("The response of EntitlementsApi->put_entitlement_request_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitlementsApi->put_entitlement_request_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Entitlement ID | 
 **entitlement_request_config** | [**EntitlementRequestConfig**](EntitlementRequestConfig.md)|  | 

### Return type

[**EntitlementRequestConfig**](EntitlementRequestConfig.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Responds with the entitlement request config as updated. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_source_entitlements**
> EntitlementSourceResetBaseReferenceDto reset_source_entitlements(id)

Reset Source Entitlements

Removes all entitlements on a specific source.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.beta
from sailpoint.beta.models.entitlement_source_reset_base_reference_dto import EntitlementSourceResetBaseReferenceDto
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
    api_instance = sailpoint.beta.EntitlementsApi(api_client)
    id = '2c91808a7813090a017814121919ecca' # str | ID of source for the entitlement reset

    try:
        # Reset Source Entitlements
        api_response = api_instance.reset_source_entitlements(id)
        print("The response of EntitlementsApi->reset_source_entitlements:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitlementsApi->reset_source_entitlements: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of source for the entitlement reset | 

### Return type

[**EntitlementSourceResetBaseReferenceDto**](EntitlementSourceResetBaseReferenceDto.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Entitlement source reset task result |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_entitlements_in_bulk**
> update_entitlements_in_bulk(entitlement_bulk_update_request)

Bulk update an entitlement list

This API applies an update to every entitlement of the list.  The number of entitlements to update is limited to 50 items maximum.  The JsonPatch update follows the [JSON Patch](https://tools.ietf.org/html/rfc6902) standard. allowed operations : **{ \"op\": \"replace\", \"path\": \"/privileged\", \"value\": boolean }**  **{ \"op\": \"replace\", \"path\": \"/requestable\",\"value\": boolean }**   A token with ORG_ADMIN or API authority is required to call this API.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.beta
from sailpoint.beta.models.entitlement_bulk_update_request import EntitlementBulkUpdateRequest
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
    api_instance = sailpoint.beta.EntitlementsApi(api_client)
    entitlement_bulk_update_request = sailpoint.beta.EntitlementBulkUpdateRequest() # EntitlementBulkUpdateRequest | 

    try:
        # Bulk update an entitlement list
        api_instance.update_entitlements_in_bulk(entitlement_bulk_update_request)
    except Exception as e:
        print("Exception when calling EntitlementsApi->update_entitlements_in_bulk: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entitlement_bulk_update_request** | [**EntitlementBulkUpdateRequest**](EntitlementBulkUpdateRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

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
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

