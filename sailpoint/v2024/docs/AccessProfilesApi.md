# sailpoint.v2024.AccessProfilesApi

All URIs are relative to *https://sailpoint.api.identitynow.com/v2024*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_access_profile**](AccessProfilesApi.md#create_access_profile) | **POST** /access-profiles | Create Access Profile
[**delete_access_profile**](AccessProfilesApi.md#delete_access_profile) | **DELETE** /access-profiles/{id} | Delete the specified Access Profile
[**delete_access_profiles_in_bulk**](AccessProfilesApi.md#delete_access_profiles_in_bulk) | **POST** /access-profiles/bulk-delete | Delete Access Profile(s)
[**get_access_profile**](AccessProfilesApi.md#get_access_profile) | **GET** /access-profiles/{id} | Get an Access Profile
[**get_access_profile_entitlements**](AccessProfilesApi.md#get_access_profile_entitlements) | **GET** /access-profiles/{id}/entitlements | List Access Profile&#39;s Entitlements
[**list_access_profiles**](AccessProfilesApi.md#list_access_profiles) | **GET** /access-profiles | List Access Profiles
[**patch_access_profile**](AccessProfilesApi.md#patch_access_profile) | **PATCH** /access-profiles/{id} | Patch a specified Access Profile
[**update_access_profiles_in_bulk**](AccessProfilesApi.md#update_access_profiles_in_bulk) | **POST** /access-profiles/bulk-update-requestable | Update Access Profile(s) requestable field.


# **create_access_profile**
> AccessProfile create_access_profile(access_profile)

Create Access Profile

Use this API to create an access profile. A user with only ROLE_SUBADMIN or SOURCE_SUBADMIN authority must be associated with the access profile's Source. The maximum supported length for the description field is 2000 characters. Longer descriptions will be preserved for existing access profiles. However, any new access profiles as well as any updates to existing descriptions are limited to 2000 characters.

### Example

* OAuth Authentication (userAuth):
* OAuth Authentication (userAuth):
* OAuth Authentication (applicationAuth):

```python
import sailpoint.v2024
from sailpoint.v2024.models.access_profile import AccessProfile
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.v2024.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.v2024.AccessProfilesApi(api_client)
    access_profile = sailpoint.v2024.AccessProfile() # AccessProfile | 

    try:
        # Create Access Profile
        api_response = api_instance.create_access_profile(access_profile)
        print("The response of AccessProfilesApi->create_access_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccessProfilesApi->create_access_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_profile** | [**AccessProfile**](AccessProfile.md)|  | 

### Return type

[**AccessProfile**](AccessProfile.md)

### Authorization

[userAuth](../README.md#userAuth), [userAuth](../README.md#userAuth), [applicationAuth](../README.md#applicationAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Access profile created. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_access_profile**
> delete_access_profile(id)

Delete the specified Access Profile

This API deletes an existing Access Profile.  The Access Profile must not be in use, for example, Access Profile can not be deleted if they belong to an Application, Life Cycle State or a Role. If it is, a 400 error is returned.  A user with SOURCE_SUBADMIN must be able to administer the Source associated with the Access Profile.

### Example

* OAuth Authentication (userAuth):
* OAuth Authentication (userAuth):
* OAuth Authentication (applicationAuth):

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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.v2024.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.v2024.AccessProfilesApi(api_client)
    id = '2c91808a7813090a017814121919ecca' # str | ID of the Access Profile to delete

    try:
        # Delete the specified Access Profile
        api_instance.delete_access_profile(id)
    except Exception as e:
        print("Exception when calling AccessProfilesApi->delete_access_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the Access Profile to delete | 

### Return type

void (empty response body)

### Authorization

[userAuth](../README.md#userAuth), [userAuth](../README.md#userAuth), [applicationAuth](../README.md#applicationAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No content - indicates the request was successful but there is no content to be returned in the response. |  -  |
**400** | Returned when an access profile cannot be deleted as it&#39;s being used. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_access_profiles_in_bulk**
> AccessProfileBulkDeleteResponse delete_access_profiles_in_bulk(access_profile_bulk_delete_request)

Delete Access Profile(s)

This endpoint initiates a bulk deletion of one or more access profiles. When the request is successful, the endpoint returns the bulk delete's task result ID.  To follow the task, you can use [Get Task Status by ID](https://developer.sailpoint.com/docs/api/beta/get-task-status), which will return the task result's status and information.  This endpoint can only bulk delete up to a limit of 50 access profiles per request.  By default, if any of the indicated access profiles are in use, no deletions will be performed and the **inUse** field of the response indicates the usages that must be removed first. If the request field **bestEffortOnly** is **true**, however, usages are reported in the **inUse** response field but all other indicated access profiles will be deleted. A SOURCE_SUBADMIN user can only use this endpoint to delete access profiles associated with sources they're able to administer.

### Example

* OAuth Authentication (userAuth):
* OAuth Authentication (userAuth):
* OAuth Authentication (applicationAuth):

```python
import sailpoint.v2024
from sailpoint.v2024.models.access_profile_bulk_delete_request import AccessProfileBulkDeleteRequest
from sailpoint.v2024.models.access_profile_bulk_delete_response import AccessProfileBulkDeleteResponse
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.v2024.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.v2024.AccessProfilesApi(api_client)
    access_profile_bulk_delete_request = {bestEffortOnly=true, accessProfileIds=[2c91808876438bb2017668b91919ecca, 2c91808876438ba801766e129f151816]} # AccessProfileBulkDeleteRequest | 

    try:
        # Delete Access Profile(s)
        api_response = api_instance.delete_access_profiles_in_bulk(access_profile_bulk_delete_request)
        print("The response of AccessProfilesApi->delete_access_profiles_in_bulk:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccessProfilesApi->delete_access_profiles_in_bulk: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_profile_bulk_delete_request** | [**AccessProfileBulkDeleteRequest**](AccessProfileBulkDeleteRequest.md)|  | 

### Return type

[**AccessProfileBulkDeleteResponse**](AccessProfileBulkDeleteResponse.md)

### Authorization

[userAuth](../README.md#userAuth), [userAuth](../README.md#userAuth), [applicationAuth](../README.md#applicationAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returned only if **bestEffortOnly** is **false**, and one or more Access Profiles are in use. |  -  |
**202** | Returned if at least one deletion will be performed. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_access_profile**
> AccessProfile get_access_profile(id)

Get an Access Profile

This API returns an Access Profile by its ID.

### Example

* OAuth Authentication (userAuth):
* OAuth Authentication (userAuth):
* OAuth Authentication (applicationAuth):

```python
import sailpoint.v2024
from sailpoint.v2024.models.access_profile import AccessProfile
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.v2024.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.v2024.AccessProfilesApi(api_client)
    id = '2c9180837ca6693d017ca8d097500149' # str | ID of the Access Profile

    try:
        # Get an Access Profile
        api_response = api_instance.get_access_profile(id)
        print("The response of AccessProfilesApi->get_access_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccessProfilesApi->get_access_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the Access Profile | 

### Return type

[**AccessProfile**](AccessProfile.md)

### Authorization

[userAuth](../README.md#userAuth), [userAuth](../README.md#userAuth), [applicationAuth](../README.md#applicationAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An AccessProfile |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_access_profile_entitlements**
> List[Entitlement] get_access_profile_entitlements(id, limit=limit, offset=offset, count=count, filters=filters, sorters=sorters)

List Access Profile's Entitlements

Use this API to get a list of an access profile's entitlements.  A SOURCE_SUBADMIN user must have access to the source associated with the specified access profile. >**Note:** When you filter for access profiles that have the '+' symbol in their names, the response is blank. 

### Example

* OAuth Authentication (userAuth):
* OAuth Authentication (userAuth):
* OAuth Authentication (applicationAuth):

```python
import sailpoint.v2024
from sailpoint.v2024.models.entitlement import Entitlement
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.v2024.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.v2024.AccessProfilesApi(api_client)
    id = '2c91808a7813090a017814121919ecca' # str | ID of the access profile containing the entitlements.
    limit = 250 # int | Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 250)
    offset = 0 # int | Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 0)
    count = False # bool | If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count=true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to False)
    filters = 'attribute eq \"memberOf\"' # str | Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **id**: *eq, in*  **name**: *eq, sw*  **attribute**: *eq, sw*  **value**: *eq, sw*  **created**: *gt, lt, ge, le*  **modified**: *gt, lt, ge, le*  **owner.id**: *eq, in*  **source.id**: *eq, in*  Filtering is not supported for access profiles and entitlements that have the '+' symbol in their names.  (optional)
    sorters = 'name,-modified' # str | Sort results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#sorting-results)  Sorting is supported for the following fields: **name, attribute, value, created, modified** (optional)

    try:
        # List Access Profile's Entitlements
        api_response = api_instance.get_access_profile_entitlements(id, limit=limit, offset=offset, count=count, filters=filters, sorters=sorters)
        print("The response of AccessProfilesApi->get_access_profile_entitlements:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccessProfilesApi->get_access_profile_entitlements: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the access profile containing the entitlements. | 
 **limit** | **int**| Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to 250]
 **offset** | **int**| Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to 0]
 **count** | **bool**| If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count&#x3D;true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to False]
 **filters** | **str**| Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **id**: *eq, in*  **name**: *eq, sw*  **attribute**: *eq, sw*  **value**: *eq, sw*  **created**: *gt, lt, ge, le*  **modified**: *gt, lt, ge, le*  **owner.id**: *eq, in*  **source.id**: *eq, in*  Filtering is not supported for access profiles and entitlements that have the &#39;+&#39; symbol in their names.  | [optional] 
 **sorters** | **str**| Sort results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#sorting-results)  Sorting is supported for the following fields: **name, attribute, value, created, modified** | [optional] 

### Return type

[**List[Entitlement]**](Entitlement.md)

### Authorization

[userAuth](../README.md#userAuth), [userAuth](../README.md#userAuth), [applicationAuth](../README.md#applicationAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of entitlements. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_access_profiles**
> List[AccessProfile] list_access_profiles(for_subadmin=for_subadmin, limit=limit, offset=offset, count=count, filters=filters, sorters=sorters, for_segment_ids=for_segment_ids, include_unsegmented=include_unsegmented)

List Access Profiles

Use this API to get a list of access profiles. >**Note:** When you filter for access profiles that have the '+' symbol in their names, the response is blank. 

### Example

* OAuth Authentication (userAuth):
* OAuth Authentication (userAuth):
* OAuth Authentication (applicationAuth):

```python
import sailpoint.v2024
from sailpoint.v2024.models.access_profile import AccessProfile
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.v2024.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.v2024.AccessProfilesApi(api_client)
    for_subadmin = '8c190e6787aa4ed9a90bd9d5344523fb' # str | If provided, filters the returned list according to what is visible to the indicated ROLE_SUBADMIN or SOURCE_SUBADMIN identity. The value of the parameter is either an identity ID, or the special value **me**, which is shorthand for the calling identity's ID.  A 400 Bad Request error is returned if the **for-subadmin** parameter is specified for an identity that is not a subadmin. (optional)
    limit = 50 # int | Note that for this API the maximum value for limit is 50. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 50)
    offset = 0 # int | Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 0)
    count = False # bool | If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count=true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to False)
    filters = 'name eq \"SailPoint Support\"' # str | Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **id**: *eq, in*  **name**: *eq, sw*  **created**: *gt, lt, ge, le*  **modified**: *gt, lt, ge, le*  **owner.id**: *eq, in*  **requestable**: *eq*  **source.id**: *eq, in*  Composite operators supported: *and, or*  Filtering is not supported for access profiles and entitlements that have the '+' symbol in their names.  (optional)
    sorters = 'name,-modified' # str | Sort results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#sorting-results)  Sorting is supported for the following fields: **name, created, modified** (optional)
    for_segment_ids = '0b5c9f25-83c6-4762-9073-e38f7bb2ae26,2e8d8180-24bc-4d21-91c6-7affdb473b0d' # str | If present and not empty, additionally filters access profiles to those which are assigned to the segment(s) with the specified IDs.  If segmentation is currently unavailable, specifying this parameter results in an error. (optional)
    include_unsegmented = True # bool | Indicates whether the response list should contain unsegmented access profiles. If *for-segment-ids* is absent or empty, specifying *include-unsegmented* as false results in an error. (optional) (default to True)

    try:
        # List Access Profiles
        api_response = api_instance.list_access_profiles(for_subadmin=for_subadmin, limit=limit, offset=offset, count=count, filters=filters, sorters=sorters, for_segment_ids=for_segment_ids, include_unsegmented=include_unsegmented)
        print("The response of AccessProfilesApi->list_access_profiles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccessProfilesApi->list_access_profiles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **for_subadmin** | **str**| If provided, filters the returned list according to what is visible to the indicated ROLE_SUBADMIN or SOURCE_SUBADMIN identity. The value of the parameter is either an identity ID, or the special value **me**, which is shorthand for the calling identity&#39;s ID.  A 400 Bad Request error is returned if the **for-subadmin** parameter is specified for an identity that is not a subadmin. | [optional] 
 **limit** | **int**| Note that for this API the maximum value for limit is 50. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to 50]
 **offset** | **int**| Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to 0]
 **count** | **bool**| If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count&#x3D;true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to False]
 **filters** | **str**| Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **id**: *eq, in*  **name**: *eq, sw*  **created**: *gt, lt, ge, le*  **modified**: *gt, lt, ge, le*  **owner.id**: *eq, in*  **requestable**: *eq*  **source.id**: *eq, in*  Composite operators supported: *and, or*  Filtering is not supported for access profiles and entitlements that have the &#39;+&#39; symbol in their names.  | [optional] 
 **sorters** | **str**| Sort results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#sorting-results)  Sorting is supported for the following fields: **name, created, modified** | [optional] 
 **for_segment_ids** | **str**| If present and not empty, additionally filters access profiles to those which are assigned to the segment(s) with the specified IDs.  If segmentation is currently unavailable, specifying this parameter results in an error. | [optional] 
 **include_unsegmented** | **bool**| Indicates whether the response list should contain unsegmented access profiles. If *for-segment-ids* is absent or empty, specifying *include-unsegmented* as false results in an error. | [optional] [default to True]

### Return type

[**List[AccessProfile]**](AccessProfile.md)

### Authorization

[userAuth](../README.md#userAuth), [userAuth](../README.md#userAuth), [applicationAuth](../README.md#applicationAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of access profiles. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_access_profile**
> AccessProfile patch_access_profile(id, json_patch_operation)

Patch a specified Access Profile

This API updates an existing Access Profile. The following fields are patchable:  **name**  **description**  **enabled**  **owner**  **requestable**  **accessRequestConfig**  **revokeRequestConfig**  **segments**  **entitlements**  **provisioningCriteria**  **source** (must be updated with entitlements belonging to new source in the same API call)  If you need to change the `source` of the access profile, you can do so only if you update the `entitlements` in the same API call.  The new entitlements can only come from the target source that you want to change to.  Look for the example \"Replace Source\" in the examples dropdown.  A user with SOURCE_SUBADMIN may only use this API to patch Access Profiles which are associated with Sources they are able to administer. >  The maximum supported length for the description field is 2000 characters. Longer descriptions will be preserved for existing access profiles, however, any new access profiles as well as any updates to existing descriptions will be limited to 2000 characters.  > You can only add or replace **entitlements** that exist on the source that the access profile is attached to. You can use the **list entitlements** endpoint with the **filters** query parameter to get a list of available entitlements on the access profile's source.

### Example

* OAuth Authentication (userAuth):
* OAuth Authentication (userAuth):
* OAuth Authentication (applicationAuth):

```python
import sailpoint.v2024
from sailpoint.v2024.models.access_profile import AccessProfile
from sailpoint.v2024.models.json_patch_operation import JsonPatchOperation
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.v2024.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.v2024.AccessProfilesApi(api_client)
    id = '2c91808a7813090a017814121919ecca' # str | ID of the Access Profile to patch
    json_patch_operation = [{op=add, path=/entitlements, value=[{id=2c9180857725c14301772a93bb77242d, type=ENTITLEMENT, name=AD User Group}]}] # List[JsonPatchOperation] | 

    try:
        # Patch a specified Access Profile
        api_response = api_instance.patch_access_profile(id, json_patch_operation)
        print("The response of AccessProfilesApi->patch_access_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccessProfilesApi->patch_access_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the Access Profile to patch | 
 **json_patch_operation** | [**List[JsonPatchOperation]**](JsonPatchOperation.md)|  | 

### Return type

[**AccessProfile**](AccessProfile.md)

### Authorization

[userAuth](../README.md#userAuth), [userAuth](../README.md#userAuth), [applicationAuth](../README.md#applicationAuth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Responds with the Access Profile as updated. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_access_profiles_in_bulk**
> List[AccessProfileUpdateItem] update_access_profiles_in_bulk(x_sail_point_experimental, access_profile_bulk_update_request_inner)

Update Access Profile(s) requestable field.

This API initiates a bulk update of field requestable for one or more Access Profiles.  >  If any of the indicated Access Profiles is exists in Organization,then those Access Profiles will be added in **updated**     list of the response.Requestable field of these Access Profiles marked as **true** or **false**.  >  If any of the indicated Access Profiles is not does not exists in Organization,then those Access Profiles will be added in **notFound** list of the response. Access Profiles marked as **notFound** will not be updated.  A SOURCE_SUBADMIN may only use this API to update Access Profiles which are associated with Sources they are able to administer.

### Example

* OAuth Authentication (userAuth):
* OAuth Authentication (userAuth):

```python
import sailpoint.v2024
from sailpoint.v2024.models.access_profile_bulk_update_request_inner import AccessProfileBulkUpdateRequestInner
from sailpoint.v2024.models.access_profile_update_item import AccessProfileUpdateItem
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
    api_instance = sailpoint.v2024.AccessProfilesApi(api_client)
    x_sail_point_experimental = 'true' # str | Use this header to enable this experimental API. (default to 'true')
    access_profile_bulk_update_request_inner = [{id=464ae7bf-791e-49fd-b746-06a2e4a89635, requestable=false}] # List[AccessProfileBulkUpdateRequestInner] | 

    try:
        # Update Access Profile(s) requestable field.
        api_response = api_instance.update_access_profiles_in_bulk(x_sail_point_experimental, access_profile_bulk_update_request_inner)
        print("The response of AccessProfilesApi->update_access_profiles_in_bulk:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccessProfilesApi->update_access_profiles_in_bulk: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_sail_point_experimental** | **str**| Use this header to enable this experimental API. | [default to &#39;true&#39;]
 **access_profile_bulk_update_request_inner** | [**List[AccessProfileBulkUpdateRequestInner]**](AccessProfileBulkUpdateRequestInner.md)|  | 

### Return type

[**List[AccessProfileUpdateItem]**](AccessProfileUpdateItem.md)

### Authorization

[userAuth](../README.md#userAuth), [userAuth](../README.md#userAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**207** | List of updated and not updated Access Profiles. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**412** | Precondition Failed - Returned in response if API/Feature not enabled for an organization. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

