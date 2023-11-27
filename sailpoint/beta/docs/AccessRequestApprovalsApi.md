# sailpoint.beta.AccessRequestApprovalsApi

All URIs are relative to *https://sailpoint.api.identitynow.com/beta*

Method | HTTP request | Description
------------- | ------------- | -------------
[**approve_access_request**](AccessRequestApprovalsApi.md#approve_access_request) | **POST** /access-request-approvals/{approvalId}/approve | Approves an access request approval.
[**forward_access_request**](AccessRequestApprovalsApi.md#forward_access_request) | **POST** /access-request-approvals/{approvalId}/forward | Forwards an access request approval to a new owner.
[**get_access_request_approval_summary**](AccessRequestApprovalsApi.md#get_access_request_approval_summary) | **GET** /access-request-approvals/approval-summary | Get the number of pending, approved and rejected access requests approvals
[**list_completed_approvals**](AccessRequestApprovalsApi.md#list_completed_approvals) | **GET** /access-request-approvals/completed | Completed Access Request Approvals List
[**list_pending_approvals**](AccessRequestApprovalsApi.md#list_pending_approvals) | **GET** /access-request-approvals/pending | Pending Access Request Approvals List
[**reject_access_request**](AccessRequestApprovalsApi.md#reject_access_request) | **POST** /access-request-approvals/{approvalId}/reject | Rejects an access request approval.


# **approve_access_request**
> object approve_access_request(approval_id, comment_dto=comment_dto)

Approves an access request approval.

This endpoint approves an access request approval. Only the owner of the approval and ORG_ADMIN users are allowed to perform this action.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import sailpoint.beta
from sailpoint.beta.models.comment_dto import CommentDto
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
    api_instance = sailpoint.beta.AccessRequestApprovalsApi(api_client)
    approval_id = '2c91808b7294bea301729568c68c002e' # str | The id of the approval.
    comment_dto = sailpoint.beta.CommentDto() # CommentDto | Reviewer's comment. (optional)

    try:
        # Approves an access request approval.
        api_response = api_instance.approve_access_request(approval_id, comment_dto=comment_dto)
        print("The response of AccessRequestApprovalsApi->approve_access_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccessRequestApprovalsApi->approve_access_request: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **approval_id** | **str**| The id of the approval. | 
 **comment_dto** | [**CommentDto**](CommentDto.md)| Reviewer&#39;s comment. | [optional] 

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
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **forward_access_request**
> object forward_access_request(approval_id, forward_approval_dto)

Forwards an access request approval to a new owner.

This endpoint forwards an access request approval. Only the owner of the approval and ORG_ADMIN users are allowed to perform this action.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import sailpoint.beta
from sailpoint.beta.models.forward_approval_dto import ForwardApprovalDto
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
    api_instance = sailpoint.beta.AccessRequestApprovalsApi(api_client)
    approval_id = '2c91808b7294bea301729568c68c002e' # str | The id of the approval.
    forward_approval_dto = sailpoint.beta.ForwardApprovalDto() # ForwardApprovalDto | Information about the forwarded approval.

    try:
        # Forwards an access request approval to a new owner.
        api_response = api_instance.forward_access_request(approval_id, forward_approval_dto)
        print("The response of AccessRequestApprovalsApi->forward_access_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccessRequestApprovalsApi->forward_access_request: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **approval_id** | **str**| The id of the approval. | 
 **forward_approval_dto** | [**ForwardApprovalDto**](ForwardApprovalDto.md)| Information about the forwarded approval. | 

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
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_access_request_approval_summary**
> ApprovalSummary get_access_request_approval_summary(owner_id=owner_id, from_date=from_date)

Get the number of pending, approved and rejected access requests approvals

This endpoint returns the number of pending, approved and rejected access requests approvals. See \"owner-id\" query parameter below for authorization info.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import sailpoint.beta
from sailpoint.beta.models.approval_summary import ApprovalSummary
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
    api_instance = sailpoint.beta.AccessRequestApprovalsApi(api_client)
    owner_id = 'owner_id_example' # str | The id of the owner or approver identity of the approvals. If present, the value returns approval summary for the specified identity.    * ORG_ADMIN users can call this with any identity ID value.    * ORG_ADMIN user can also fetch all the approvals in the org, when owner-id is not used.    * Non ORG_ADMIN users can only specify *me* or pass their own identity ID value. (optional)
    from_date = 'from_date_example' # str | From date is the date and time from which the results will be shown. It should be in a valid ISO-8601 format  example: from-date=2020-03-19T19:59:11Z (optional)

    try:
        # Get the number of pending, approved and rejected access requests approvals
        api_response = api_instance.get_access_request_approval_summary(owner_id=owner_id, from_date=from_date)
        print("The response of AccessRequestApprovalsApi->get_access_request_approval_summary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccessRequestApprovalsApi->get_access_request_approval_summary: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_id** | **str**| The id of the owner or approver identity of the approvals. If present, the value returns approval summary for the specified identity.    * ORG_ADMIN users can call this with any identity ID value.    * ORG_ADMIN user can also fetch all the approvals in the org, when owner-id is not used.    * Non ORG_ADMIN users can only specify *me* or pass their own identity ID value. | [optional] 
 **from_date** | **str**| From date is the date and time from which the results will be shown. It should be in a valid ISO-8601 format  example: from-date&#x3D;2020-03-19T19:59:11Z | [optional] 

### Return type

[**ApprovalSummary**](ApprovalSummary.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Number of pending, approved, rejected access request approvals. |  -  |
**400** | Client Error - Returned if the query parameter is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_completed_approvals**
> List[CompletedApproval] list_completed_approvals(owner_id=owner_id, limit=limit, offset=offset, count=count, filters=filters, sorters=sorters)

Completed Access Request Approvals List

This endpoint returns list of completed approvals. See *owner-id* query parameter below for authorization info.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import sailpoint.beta
from sailpoint.beta.models.completed_approval import CompletedApproval
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
    api_instance = sailpoint.beta.AccessRequestApprovalsApi(api_client)
    owner_id = 'owner_id_example' # str | If present, the value returns only completed approvals for the specified identity.    * ORG_ADMIN users can call this with any identity ID value.    * ORG_ADMIN users can also fetch all the approvals in the org, when owner-id is not used.    * Non-ORG_ADMIN users can only specify *me* or pass their own identity ID value. (optional)
    limit = 250 # int | Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 250)
    offset = 0 # int | Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 0)
    count = False # bool | If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count=true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to False)
    filters = 'filters_example' # str | Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **id**: *eq, in, co, ge, gt, le, lt, ne, isnull, sw*  **requestedFor.id**: *eq, in, co, ge, gt, le, lt, ne, isnull, sw*  **modified**: *gt, lt, ge, le, co, eq, in, ne, sw* (optional)
    sorters = 'sorters_example' # str | Sort results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#sorting-results)  Sorting is supported for the following fields: **created, modified** (optional)

    try:
        # Completed Access Request Approvals List
        api_response = api_instance.list_completed_approvals(owner_id=owner_id, limit=limit, offset=offset, count=count, filters=filters, sorters=sorters)
        print("The response of AccessRequestApprovalsApi->list_completed_approvals:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccessRequestApprovalsApi->list_completed_approvals: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_id** | **str**| If present, the value returns only completed approvals for the specified identity.    * ORG_ADMIN users can call this with any identity ID value.    * ORG_ADMIN users can also fetch all the approvals in the org, when owner-id is not used.    * Non-ORG_ADMIN users can only specify *me* or pass their own identity ID value. | [optional] 
 **limit** | **int**| Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to 250]
 **offset** | **int**| Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to 0]
 **count** | **bool**| If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count&#x3D;true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to False]
 **filters** | **str**| Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **id**: *eq, in, co, ge, gt, le, lt, ne, isnull, sw*  **requestedFor.id**: *eq, in, co, ge, gt, le, lt, ne, isnull, sw*  **modified**: *gt, lt, ge, le, co, eq, in, ne, sw* | [optional] 
 **sorters** | **str**| Sort results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#sorting-results)  Sorting is supported for the following fields: **created, modified** | [optional] 

### Return type

[**List[CompletedApproval]**](CompletedApproval.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of Completed Approvals. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_pending_approvals**
> List[PendingApproval] list_pending_approvals(owner_id=owner_id, limit=limit, offset=offset, count=count, filters=filters, sorters=sorters)

Pending Access Request Approvals List

This endpoint returns a list of pending approvals. See \"owner-id\" query parameter below for authorization info.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import sailpoint.beta
from sailpoint.beta.models.pending_approval import PendingApproval
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
    api_instance = sailpoint.beta.AccessRequestApprovalsApi(api_client)
    owner_id = 'owner_id_example' # str | If present, the value returns only pending approvals for the specified identity.    * ORG_ADMIN users can call this with any identity ID value.    * ORG_ADMIN users can also fetch all the approvals in the org, when owner-id is not used.    * Non-ORG_ADMIN users can only specify *me* or pass their own identity ID value. (optional)
    limit = 250 # int | Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 250)
    offset = 0 # int | Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 0)
    count = False # bool | If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count=true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to False)
    filters = 'filters_example' # str | Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **id**: *eq, in*  **requestedFor.id**: *eq, in*  **modified**: *gt, lt, ge, le, eq, in* (optional)
    sorters = 'sorters_example' # str | Sort results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#sorting-results)  Sorting is supported for the following fields: **created, modified** (optional)

    try:
        # Pending Access Request Approvals List
        api_response = api_instance.list_pending_approvals(owner_id=owner_id, limit=limit, offset=offset, count=count, filters=filters, sorters=sorters)
        print("The response of AccessRequestApprovalsApi->list_pending_approvals:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccessRequestApprovalsApi->list_pending_approvals: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_id** | **str**| If present, the value returns only pending approvals for the specified identity.    * ORG_ADMIN users can call this with any identity ID value.    * ORG_ADMIN users can also fetch all the approvals in the org, when owner-id is not used.    * Non-ORG_ADMIN users can only specify *me* or pass their own identity ID value. | [optional] 
 **limit** | **int**| Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to 250]
 **offset** | **int**| Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to 0]
 **count** | **bool**| If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count&#x3D;true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to False]
 **filters** | **str**| Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **id**: *eq, in*  **requestedFor.id**: *eq, in*  **modified**: *gt, lt, ge, le, eq, in* | [optional] 
 **sorters** | **str**| Sort results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#sorting-results)  Sorting is supported for the following fields: **created, modified** | [optional] 

### Return type

[**List[PendingApproval]**](PendingApproval.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of Pending Approvals. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reject_access_request**
> object reject_access_request(approval_id, comment_dto=comment_dto)

Rejects an access request approval.

This endpoint rejects an access request approval. Only the owner of the approval and admin users are allowed to perform this action.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):
```python
import time
import os
import sailpoint.beta
from sailpoint.beta.models.comment_dto import CommentDto
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
    api_instance = sailpoint.beta.AccessRequestApprovalsApi(api_client)
    approval_id = '2c91808b7294bea301729568c68c002e' # str | The id of the approval.
    comment_dto = sailpoint.beta.CommentDto() # CommentDto | Reviewer's comment. (optional)

    try:
        # Rejects an access request approval.
        api_response = api_instance.reject_access_request(approval_id, comment_dto=comment_dto)
        print("The response of AccessRequestApprovalsApi->reject_access_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccessRequestApprovalsApi->reject_access_request: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **approval_id** | **str**| The id of the approval. | 
 **comment_dto** | [**CommentDto**](CommentDto.md)| Reviewer&#39;s comment. | [optional] 

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
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

