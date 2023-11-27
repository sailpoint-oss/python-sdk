# sailpoint.v2.GovernanceGroupsApi

All URIs are relative to *https://sailpoint.api.identitynow.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_delete_work_groups**](GovernanceGroupsApi.md#bulk_delete_work_groups) | **POST** /workgroups/bulk-delete | Bulk delete work groups
[**create_workgroup**](GovernanceGroupsApi.md#create_workgroup) | **POST** /workgroups | Create Work Group
[**delete_workgroup**](GovernanceGroupsApi.md#delete_workgroup) | **DELETE** /workgroups/{workgroupId} | Delete Work Group By Id
[**get_workgroup**](GovernanceGroupsApi.md#get_workgroup) | **GET** /workgroups/{workgroupId} | Get Work Group By Id
[**list_workgroup_connections**](GovernanceGroupsApi.md#list_workgroup_connections) | **GET** /workgroups/{workgroupId}/connections | List Work Group Connections
[**list_workgroup_members**](GovernanceGroupsApi.md#list_workgroup_members) | **GET** /workgroups/{workgroupId}/members | List Work Group Members
[**list_workgroups**](GovernanceGroupsApi.md#list_workgroups) | **GET** /workgroups | List Work Groups
[**modify_workgroup_members**](GovernanceGroupsApi.md#modify_workgroup_members) | **POST** /workgroups/{workgroupId}/members | Modify Work Group Members
[**update_workgroup**](GovernanceGroupsApi.md#update_workgroup) | **PATCH** /workgroups/{workgroupId} | Update Work Group By Id


# **bulk_delete_work_groups**
> BulkDeleteWorkGroups200Response bulk_delete_work_groups(bulk_delete_work_groups_request)

Bulk delete work groups

This API allows you to bulk-delete work groups

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import sailpoint.v2
from sailpoint.v2.models.bulk_delete_work_groups200_response import BulkDeleteWorkGroups200Response
from sailpoint.v2.models.bulk_delete_work_groups_request import BulkDeleteWorkGroupsRequest
from sailpoint.v2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.v2.Configuration(
    host = "https://sailpoint.api.identitynow.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.v2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.v2.GovernanceGroupsApi(api_client)
    bulk_delete_work_groups_request = sailpoint.v2.BulkDeleteWorkGroupsRequest() # BulkDeleteWorkGroupsRequest | Work group ids to delete

    try:
        # Bulk delete work groups
        api_response = api_instance.bulk_delete_work_groups(bulk_delete_work_groups_request)
        print("The response of GovernanceGroupsApi->bulk_delete_work_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GovernanceGroupsApi->bulk_delete_work_groups: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bulk_delete_work_groups_request** | [**BulkDeleteWorkGroupsRequest**](BulkDeleteWorkGroupsRequest.md)| Work group ids to delete | 

### Return type

[**BulkDeleteWorkGroups200Response**](BulkDeleteWorkGroups200Response.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of work group objects |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_workgroup**
> List[ListWorkgroups200ResponseInner] create_workgroup(create_workgroup_request)

Create Work Group

This API allows you to create a work group

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import sailpoint.v2
from sailpoint.v2.models.create_workgroup_request import CreateWorkgroupRequest
from sailpoint.v2.models.list_workgroups200_response_inner import ListWorkgroups200ResponseInner
from sailpoint.v2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.v2.Configuration(
    host = "https://sailpoint.api.identitynow.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.v2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.v2.GovernanceGroupsApi(api_client)
    create_workgroup_request = sailpoint.v2.CreateWorkgroupRequest() # CreateWorkgroupRequest | Work group to create.

    try:
        # Create Work Group
        api_response = api_instance.create_workgroup(create_workgroup_request)
        print("The response of GovernanceGroupsApi->create_workgroup:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GovernanceGroupsApi->create_workgroup: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_workgroup_request** | [**CreateWorkgroupRequest**](CreateWorkgroupRequest.md)| Work group to create. | 

### Return type

[**List[ListWorkgroups200ResponseInner]**](ListWorkgroups200ResponseInner.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of work group objects |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_workgroup**
> delete_workgroup(workgroup_id)

Delete Work Group By Id

This API deletes a single workgroup based on the ID

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import sailpoint.v2
from sailpoint.v2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.v2.Configuration(
    host = "https://sailpoint.api.identitynow.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.v2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.v2.GovernanceGroupsApi(api_client)
    workgroup_id = 'ef38f94347e94562b5bb8424a56397d8' # str | The workgroup ID

    try:
        # Delete Work Group By Id
        api_instance.delete_workgroup(workgroup_id)
    except Exception as e:
        print("Exception when calling GovernanceGroupsApi->delete_workgroup: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workgroup_id** | **str**| The workgroup ID | 

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
**204** | Empty response on successful deletion |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workgroup**
> ListWorkgroups200ResponseInner get_workgroup(workgroup_id)

Get Work Group By Id

This API returns the details for a single workgroup based on the ID

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import sailpoint.v2
from sailpoint.v2.models.list_workgroups200_response_inner import ListWorkgroups200ResponseInner
from sailpoint.v2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.v2.Configuration(
    host = "https://sailpoint.api.identitynow.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.v2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.v2.GovernanceGroupsApi(api_client)
    workgroup_id = 'ef38f94347e94562b5bb8424a56397d8' # str | The workgroup ID

    try:
        # Get Work Group By Id
        api_response = api_instance.get_workgroup(workgroup_id)
        print("The response of GovernanceGroupsApi->get_workgroup:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GovernanceGroupsApi->get_workgroup: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workgroup_id** | **str**| The workgroup ID | 

### Return type

[**ListWorkgroups200ResponseInner**](ListWorkgroups200ResponseInner.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Workgroup object |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_workgroup_connections**
> List[ListWorkgroupConnections200ResponseInner] list_workgroup_connections(workgroup_id)

List Work Group Connections

This API returns the connections of a work group

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import sailpoint.v2
from sailpoint.v2.models.list_workgroup_connections200_response_inner import ListWorkgroupConnections200ResponseInner
from sailpoint.v2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.v2.Configuration(
    host = "https://sailpoint.api.identitynow.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.v2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.v2.GovernanceGroupsApi(api_client)
    workgroup_id = 'ef38f94347e94562b5bb8424a56397d8' # str | The workgroup ID

    try:
        # List Work Group Connections
        api_response = api_instance.list_workgroup_connections(workgroup_id)
        print("The response of GovernanceGroupsApi->list_workgroup_connections:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GovernanceGroupsApi->list_workgroup_connections: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workgroup_id** | **str**| The workgroup ID | 

### Return type

[**List[ListWorkgroupConnections200ResponseInner]**](ListWorkgroupConnections200ResponseInner.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of work group connection objects |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_workgroup_members**
> List[ListWorkgroupMembers200ResponseInner] list_workgroup_members(workgroup_id, limit=limit, offset=offset, filters=filters)

List Work Group Members

This API returns the members of a work group

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import sailpoint.v2
from sailpoint.v2.models.list_workgroup_members200_response_inner import ListWorkgroupMembers200ResponseInner
from sailpoint.v2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.v2.Configuration(
    host = "https://sailpoint.api.identitynow.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.v2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.v2.GovernanceGroupsApi(api_client)
    workgroup_id = 'ef38f94347e94562b5bb8424a56397d8' # str | The workgroup ID
    limit = 250 # int | Max number of results to return (optional) (default to 250)
    offset = 0 # int | Offset into the full result set. Usually specified with *limit* to paginate through the results. (optional) (default to 0)
    filters = 'filters_example' # str | Filter results using the following syntax. [{property:name, value: \"Tyler\", operation: EQ}] (optional)

    try:
        # List Work Group Members
        api_response = api_instance.list_workgroup_members(workgroup_id, limit=limit, offset=offset, filters=filters)
        print("The response of GovernanceGroupsApi->list_workgroup_members:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GovernanceGroupsApi->list_workgroup_members: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workgroup_id** | **str**| The workgroup ID | 
 **limit** | **int**| Max number of results to return | [optional] [default to 250]
 **offset** | **int**| Offset into the full result set. Usually specified with *limit* to paginate through the results. | [optional] [default to 0]
 **filters** | **str**| Filter results using the following syntax. [{property:name, value: \&quot;Tyler\&quot;, operation: EQ}] | [optional] 

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
**200** | List of work group member objects |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_workgroups**
> List[ListWorkgroups200ResponseInner] list_workgroups(limit=limit, offset=offset, filters=filters)

List Work Groups

This API returns a list of work groups

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import sailpoint.v2
from sailpoint.v2.models.list_workgroups200_response_inner import ListWorkgroups200ResponseInner
from sailpoint.v2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.v2.Configuration(
    host = "https://sailpoint.api.identitynow.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.v2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.v2.GovernanceGroupsApi(api_client)
    limit = 250 # int | Max number of results to return (optional) (default to 250)
    offset = 0 # int | Offset into the full result set. Usually specified with *limit* to paginate through the results. (optional) (default to 0)
    filters = 'filters_example' # str | Filter results using the following syntax. [{property:name, value: \"Tyler\", operation: EQ}] (optional)

    try:
        # List Work Groups
        api_response = api_instance.list_workgroups(limit=limit, offset=offset, filters=filters)
        print("The response of GovernanceGroupsApi->list_workgroups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GovernanceGroupsApi->list_workgroups: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Max number of results to return | [optional] [default to 250]
 **offset** | **int**| Offset into the full result set. Usually specified with *limit* to paginate through the results. | [optional] [default to 0]
 **filters** | **str**| Filter results using the following syntax. [{property:name, value: \&quot;Tyler\&quot;, operation: EQ}] | [optional] 

### Return type

[**List[ListWorkgroups200ResponseInner]**](ListWorkgroups200ResponseInner.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of work group objects |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_workgroup_members**
> modify_workgroup_members(workgroup_id, modify_workgroup_members_request)

Modify Work Group Members

This API allows you to modify the members of a work group

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import sailpoint.v2
from sailpoint.v2.models.modify_workgroup_members_request import ModifyWorkgroupMembersRequest
from sailpoint.v2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.v2.Configuration(
    host = "https://sailpoint.api.identitynow.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.v2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.v2.GovernanceGroupsApi(api_client)
    workgroup_id = 'ef38f94347e94562b5bb8424a56397d8' # str | The workgroup ID
    modify_workgroup_members_request = sailpoint.v2.ModifyWorkgroupMembersRequest() # ModifyWorkgroupMembersRequest | Add/Remove workgroup member ids.

    try:
        # Modify Work Group Members
        api_instance.modify_workgroup_members(workgroup_id, modify_workgroup_members_request)
    except Exception as e:
        print("Exception when calling GovernanceGroupsApi->modify_workgroup_members: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workgroup_id** | **str**| The workgroup ID | 
 **modify_workgroup_members_request** | [**ModifyWorkgroupMembersRequest**](ModifyWorkgroupMembersRequest.md)| Add/Remove workgroup member ids. | 

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
**204** | Empty response on successful deletion |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_workgroup**
> ListWorkgroups200ResponseInner update_workgroup(workgroup_id, create_workgroup_request)

Update Work Group By Id

This API updates and returns the details for a single workgroup based on the ID

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import sailpoint.v2
from sailpoint.v2.models.create_workgroup_request import CreateWorkgroupRequest
from sailpoint.v2.models.list_workgroups200_response_inner import ListWorkgroups200ResponseInner
from sailpoint.v2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.v2.Configuration(
    host = "https://sailpoint.api.identitynow.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.v2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.v2.GovernanceGroupsApi(api_client)
    workgroup_id = 'ef38f94347e94562b5bb8424a56397d8' # str | The workgroup ID
    create_workgroup_request = sailpoint.v2.CreateWorkgroupRequest() # CreateWorkgroupRequest | Work group to modify.

    try:
        # Update Work Group By Id
        api_response = api_instance.update_workgroup(workgroup_id, create_workgroup_request)
        print("The response of GovernanceGroupsApi->update_workgroup:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GovernanceGroupsApi->update_workgroup: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workgroup_id** | **str**| The workgroup ID | 
 **create_workgroup_request** | [**CreateWorkgroupRequest**](CreateWorkgroupRequest.md)| Work group to modify. | 

### Return type

[**ListWorkgroups200ResponseInner**](ListWorkgroups200ResponseInner.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Workgroup object |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

