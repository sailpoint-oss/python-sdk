# sailpoint.beta.GovernanceGroupsApi

All URIs are relative to *https://sailpoint.api.identitynow.com/beta*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_workgroup**](GovernanceGroupsApi.md#create_workgroup) | **POST** /workgroups | Create a new Governance Group.
[**delete_workgroup**](GovernanceGroupsApi.md#delete_workgroup) | **DELETE** /workgroups/{id} | Delete a Governance Group
[**delete_workgroup_members**](GovernanceGroupsApi.md#delete_workgroup_members) | **POST** /workgroups/{workgroupId}/members/bulk-delete | Remove members from Governance Group
[**delete_workgroups_in_bulk**](GovernanceGroupsApi.md#delete_workgroups_in_bulk) | **POST** /workgroups/bulk-delete | Delete Governance Group(s)
[**get_workgroup**](GovernanceGroupsApi.md#get_workgroup) | **GET** /workgroups/{id} | Get Governance Group by Id
[**list_connections**](GovernanceGroupsApi.md#list_connections) | **GET** /workgroups/{workgroupId}/connections | List connections for Governance Group
[**list_workgroup_members**](GovernanceGroupsApi.md#list_workgroup_members) | **GET** /workgroups/{workgroupId}/members | List Governance Group Members
[**list_workgroups**](GovernanceGroupsApi.md#list_workgroups) | **GET** /workgroups | List Governance Groups
[**patch_workgroup**](GovernanceGroupsApi.md#patch_workgroup) | **PATCH** /workgroups/{id} | Patch a Governance Group
[**update_workgroup_members**](GovernanceGroupsApi.md#update_workgroup_members) | **POST** /workgroups/{workgroupId}/members/bulk-add | Add members to Governance Group


# **create_workgroup**
> WorkgroupDto create_workgroup(workgroup_dto)

Create a new Governance Group.

This API creates a new Governance Group.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.beta
from sailpoint.beta.models.workgroup_dto import WorkgroupDto
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
    api_instance = sailpoint.beta.GovernanceGroupsApi(api_client)
    workgroup_dto = sailpoint.beta.WorkgroupDto() # WorkgroupDto | 

    try:
        # Create a new Governance Group.
        api_response = api_instance.create_workgroup(workgroup_dto)
        print("The response of GovernanceGroupsApi->create_workgroup:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GovernanceGroupsApi->create_workgroup: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workgroup_dto** | [**WorkgroupDto**](WorkgroupDto.md)|  | 

### Return type

[**WorkgroupDto**](WorkgroupDto.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Governance Group object created. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_workgroup**
> delete_workgroup(id)

Delete a Governance Group

This API deletes a Governance Group by its ID.

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
    api_instance = sailpoint.beta.GovernanceGroupsApi(api_client)
    id = '2c9180837ca6693d017ca8d097500149' # str | ID of the Governance Group

    try:
        # Delete a Governance Group
        api_instance.delete_workgroup(id)
    except Exception as e:
        print("Exception when calling GovernanceGroupsApi->delete_workgroup: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the Governance Group | 

### Return type

void (empty response body)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **delete_workgroup_members**
> List[WorkgroupMemberDeleteItem] delete_workgroup_members(workgroup_id, bulk_workgroup_members_request_inner)

Remove members from Governance Group

This API removes one or more  members from a Governance Group.  A token with API, ORG_ADMIN authority is required to call this API.  >  **Following field of Identity is an optional field in the request.**  >  **name**

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.beta
from sailpoint.beta.models.bulk_workgroup_members_request_inner import BulkWorkgroupMembersRequestInner
from sailpoint.beta.models.workgroup_member_delete_item import WorkgroupMemberDeleteItem
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
    api_instance = sailpoint.beta.GovernanceGroupsApi(api_client)
    workgroup_id = '2c91808a7813090a017814121919ecca' # str | ID of the Governance Group.
    bulk_workgroup_members_request_inner = [sailpoint.beta.BulkWorkgroupMembersRequestInner()] # List[BulkWorkgroupMembersRequestInner] | List of identities to be removed from  a Governance Group members list.

    try:
        # Remove members from Governance Group
        api_response = api_instance.delete_workgroup_members(workgroup_id, bulk_workgroup_members_request_inner)
        print("The response of GovernanceGroupsApi->delete_workgroup_members:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GovernanceGroupsApi->delete_workgroup_members: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workgroup_id** | **str**| ID of the Governance Group. | 
 **bulk_workgroup_members_request_inner** | [**List[BulkWorkgroupMembersRequestInner]**](BulkWorkgroupMembersRequestInner.md)| List of identities to be removed from  a Governance Group members list. | 

### Return type

[**List[WorkgroupMemberDeleteItem]**](WorkgroupMemberDeleteItem.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**207** | List of deleted and not deleted identities from Governance Group members list. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_workgroups_in_bulk**
> List[WorkgroupDeleteItem] delete_workgroups_in_bulk(workgroup_bulk_delete_request)

Delete Governance Group(s)

 This API initiates a bulk deletion of one or more Governance Groups.  >  If any of the indicated Governance Groups have one or more connections associated with it,then those Governance Groups will be added in  **inUse** list of the response. Governance Group(s) marked as **inUse** can not be deleted.  >  If any of the indicated Governance Groups is not does not exists in Organization,then those Governance Groups will be added in **notFound** list of the response. Governance Groups marked as **notFound** will not be deleted.  >  If any of the indicated Governance Groups does not have any connections associated with it,then those Governance Groups will be added in **deleted** list of the response. A Governance Group marked as **deleted** will be deleted from current Organization.  >  If the request contains any **inUse** or **notFound** Governance Group IDs then it skips only these Governance Groups for deletion and deletes the rest of Governance Groups which have no connections associated with it.   >  **This API has limit number of Governance Groups can be deleted at one time. If the request contains more then 100 Governance Groups IDs to be deleted then the API will throw an exception.**

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.beta
from sailpoint.beta.models.workgroup_bulk_delete_request import WorkgroupBulkDeleteRequest
from sailpoint.beta.models.workgroup_delete_item import WorkgroupDeleteItem
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
    api_instance = sailpoint.beta.GovernanceGroupsApi(api_client)
    workgroup_bulk_delete_request = {ids=[567a697e-885b-495a-afc5-d55e1c23a302, c7b0f7b2-1e78-4063-b294-a555333dacd2]} # WorkgroupBulkDeleteRequest | 

    try:
        # Delete Governance Group(s)
        api_response = api_instance.delete_workgroups_in_bulk(workgroup_bulk_delete_request)
        print("The response of GovernanceGroupsApi->delete_workgroups_in_bulk:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GovernanceGroupsApi->delete_workgroups_in_bulk: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workgroup_bulk_delete_request** | [**WorkgroupBulkDeleteRequest**](WorkgroupBulkDeleteRequest.md)|  | 

### Return type

[**List[WorkgroupDeleteItem]**](WorkgroupDeleteItem.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**207** | Governance Group bulk delete response. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workgroup**
> WorkgroupDto get_workgroup(id)

Get Governance Group by Id

This API returns a Governance Groups by its ID.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.beta
from sailpoint.beta.models.workgroup_dto import WorkgroupDto
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
    api_instance = sailpoint.beta.GovernanceGroupsApi(api_client)
    id = '2c9180837ca6693d017ca8d097500149' # str | ID of the Governance Group

    try:
        # Get Governance Group by Id
        api_response = api_instance.get_workgroup(id)
        print("The response of GovernanceGroupsApi->get_workgroup:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GovernanceGroupsApi->get_workgroup: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the Governance Group | 

### Return type

[**WorkgroupDto**](WorkgroupDto.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A Governance Group |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_connections**
> List[WorkgroupConnectionDto] list_connections(workgroup_id, offset=offset, limit=limit, count=count, sorters=sorters)

List connections for Governance Group

This API returns list of connections associated with a Governance Group.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.beta
from sailpoint.beta.models.workgroup_connection_dto import WorkgroupConnectionDto
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
    api_instance = sailpoint.beta.GovernanceGroupsApi(api_client)
    workgroup_id = '2c91808a7813090a017814121919ecca' # str | ID of the Governance Group.
    offset = 0 # int | Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 0)
    limit = 50 # int | Note that for this API the maximum value for limit is 50. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 50)
    count = False # bool | If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count=true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to False)
    sorters = 'name,-modified' # str | Sort results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#sorting-results)  Sorting is supported for the following fields: **name, created, modified** (optional)

    try:
        # List connections for Governance Group
        api_response = api_instance.list_connections(workgroup_id, offset=offset, limit=limit, count=count, sorters=sorters)
        print("The response of GovernanceGroupsApi->list_connections:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GovernanceGroupsApi->list_connections: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workgroup_id** | **str**| ID of the Governance Group. | 
 **offset** | **int**| Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to 0]
 **limit** | **int**| Note that for this API the maximum value for limit is 50. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to 50]
 **count** | **bool**| If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count&#x3D;true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to False]
 **sorters** | **str**| Sort results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#sorting-results)  Sorting is supported for the following fields: **name, created, modified** | [optional] 

### Return type

[**List[WorkgroupConnectionDto]**](WorkgroupConnectionDto.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List all connections associated with a Governance Group. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_workgroup_members**
> List[ListWorkgroupMembers200ResponseInner] list_workgroup_members(workgroup_id, offset=offset, limit=limit, count=count, sorters=sorters)

List Governance Group Members

This API returns list of members associated with a Governance Group.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.beta
from sailpoint.beta.models.list_workgroup_members200_response_inner import ListWorkgroupMembers200ResponseInner
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
    api_instance = sailpoint.beta.GovernanceGroupsApi(api_client)
    workgroup_id = '2c91808a7813090a017814121919ecca' # str | ID of the Governance Group.
    offset = 0 # int | Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 0)
    limit = 50 # int | Note that for this API the maximum value for limit is 50. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 50)
    count = False # bool | If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count=true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to False)
    sorters = 'name,-modified' # str | Sort results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#sorting-results)  Sorting is supported for the following fields: **name, created, modified** (optional)

    try:
        # List Governance Group Members
        api_response = api_instance.list_workgroup_members(workgroup_id, offset=offset, limit=limit, count=count, sorters=sorters)
        print("The response of GovernanceGroupsApi->list_workgroup_members:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GovernanceGroupsApi->list_workgroup_members: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workgroup_id** | **str**| ID of the Governance Group. | 
 **offset** | **int**| Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to 0]
 **limit** | **int**| Note that for this API the maximum value for limit is 50. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to 50]
 **count** | **bool**| If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count&#x3D;true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to False]
 **sorters** | **str**| Sort results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#sorting-results)  Sorting is supported for the following fields: **name, created, modified** | [optional] 

### Return type

[**List[ListWorkgroupMembers200ResponseInner]**](ListWorkgroupMembers200ResponseInner.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List all members associated with a Governance Group. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_workgroups**
> List[WorkgroupDto] list_workgroups(offset=offset, limit=limit, count=count, filters=filters, sorters=sorters)

List Governance Groups

This API returns list of Governance Groups

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.beta
from sailpoint.beta.models.workgroup_dto import WorkgroupDto
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
    api_instance = sailpoint.beta.GovernanceGroupsApi(api_client)
    offset = 0 # int | Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 0)
    limit = 50 # int | Note that for this API the maximum value for limit is 50. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 50)
    count = False # bool | If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count=true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to False)
    filters = 'name sw \"Test\"' # str | Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **id**: *eq, in, sw*  **name**: *eq, sw, in*  **memberships.identityId**: *eq, in* (optional)
    sorters = 'name,-modified' # str | Sort results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#sorting-results)  Sorting is supported for the following fields: **name, created, modified, id, description** (optional)

    try:
        # List Governance Groups
        api_response = api_instance.list_workgroups(offset=offset, limit=limit, count=count, filters=filters, sorters=sorters)
        print("The response of GovernanceGroupsApi->list_workgroups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GovernanceGroupsApi->list_workgroups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to 0]
 **limit** | **int**| Note that for this API the maximum value for limit is 50. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to 50]
 **count** | **bool**| If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count&#x3D;true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to False]
 **filters** | **str**| Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **id**: *eq, in, sw*  **name**: *eq, sw, in*  **memberships.identityId**: *eq, in* | [optional] 
 **sorters** | **str**| Sort results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#sorting-results)  Sorting is supported for the following fields: **name, created, modified, id, description** | [optional] 

### Return type

[**List[WorkgroupDto]**](WorkgroupDto.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of Governance Groups |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_workgroup**
> WorkgroupDto patch_workgroup(id, json_patch_operation=json_patch_operation)

Patch a Governance Group

This API updates an existing governance group by ID.  The following fields and objects are patchable:   * name   * description   * owner  A token with API or ORG_ADMIN authority is required to call this API.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.beta
from sailpoint.beta.models.json_patch_operation import JsonPatchOperation
from sailpoint.beta.models.workgroup_dto import WorkgroupDto
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
    api_instance = sailpoint.beta.GovernanceGroupsApi(api_client)
    id = '2c9180837ca6693d017ca8d097500149' # str | ID of the Governance Group
    json_patch_operation = [{op=replace, path=/description, value=Governance Group new description.}] # List[JsonPatchOperation] |  (optional)

    try:
        # Patch a Governance Group
        api_response = api_instance.patch_workgroup(id, json_patch_operation=json_patch_operation)
        print("The response of GovernanceGroupsApi->patch_workgroup:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GovernanceGroupsApi->patch_workgroup: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the Governance Group | 
 **json_patch_operation** | [**List[JsonPatchOperation]**](JsonPatchOperation.md)|  | [optional] 

### Return type

[**WorkgroupDto**](WorkgroupDto.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A Governance Group. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_workgroup_members**
> List[WorkgroupMemberAddItem] update_workgroup_members(workgroup_id, bulk_workgroup_members_request_inner)

Add members to Governance Group

This API adds one or more members to a Governance Group.  A token with API, ORG_ADMIN authority is required to call this API.  >  **Following field of Identity is an optional field in the request.**  >  **name**

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.beta
from sailpoint.beta.models.bulk_workgroup_members_request_inner import BulkWorkgroupMembersRequestInner
from sailpoint.beta.models.workgroup_member_add_item import WorkgroupMemberAddItem
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
    api_instance = sailpoint.beta.GovernanceGroupsApi(api_client)
    workgroup_id = '2c91808a7813090a017814121919ecca' # str | ID of the Governance Group.
    bulk_workgroup_members_request_inner = [sailpoint.beta.BulkWorkgroupMembersRequestInner()] # List[BulkWorkgroupMembersRequestInner] | List of identities to be added to a Governance Group members list.

    try:
        # Add members to Governance Group
        api_response = api_instance.update_workgroup_members(workgroup_id, bulk_workgroup_members_request_inner)
        print("The response of GovernanceGroupsApi->update_workgroup_members:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GovernanceGroupsApi->update_workgroup_members: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workgroup_id** | **str**| ID of the Governance Group. | 
 **bulk_workgroup_members_request_inner** | [**List[BulkWorkgroupMembersRequestInner]**](BulkWorkgroupMembersRequestInner.md)| List of identities to be added to a Governance Group members list. | 

### Return type

[**List[WorkgroupMemberAddItem]**](WorkgroupMemberAddItem.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**207** | List of added and not added identities into  Governance Group members list. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

