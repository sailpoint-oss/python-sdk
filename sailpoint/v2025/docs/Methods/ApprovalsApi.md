---
id: v2025-approvals
title: Approvals
pagination_label: Approvals
sidebar_label: Approvals
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Approvals', 'V2025Approvals'] 
slug: /tools/sdk/python/v2025/methods/approvals
tags: ['SDK', 'Software Development Kit', 'Approvals', 'V2025Approvals']
---

# sailpoint.v2025.ApprovalsApi
  Use this API to implement approval functionality. With this functionality in place, you can get generic approvals and modify them. 

The main advantages this API has vs [Access Request Approvals](https://developer.sailpoint.com/docs/api/v2025/access-request-approvals) are that you can use it to get generic approvals individually or in batches and make changes to those approvals. 
 
All URIs are relative to *https://sailpoint.api.identitynow.com/v2025*

Method | HTTP request | Description
------------- | ------------- | -------------
[**approve-approval**](#approve-approval) | **POST** `/generic-approvals/{id}/approve` | Post Approvals Approve
[**approve-approval-0**](#approve-approval-0) | **POST** `/generic-approvals/bulk-approve` | Post Bulk Approve Approvals
[**cancel-approval**](#cancel-approval) | **POST** `/generic-approvals/bulk-cancel` | Post Bulk Cancel Approvals
[**get-approval**](#get-approval) | **GET** `/generic-approvals/{id}` | Get an approval
[**get-approvals**](#get-approvals) | **GET** `/generic-approvals` | Get approvals
[**get-approvals-config-id-type**](#get-approvals-config-id-type) | **GET** `/generic-approvals/config` | Get Approval Config Type
[**move-approval**](#move-approval) | **POST** `/generic-approvals/bulk-reassign` | Post Bulk Reassign Approvals
[**put-approvals-config-type**](#put-approvals-config-type) | **PUT** `/generic-approvals/config` | Put Approval Config Type
[**reject-approval**](#reject-approval) | **POST** `/generic-approvals/{id}/reject` | Post Approvals Reject
[**reject-approval-0**](#reject-approval-0) | **POST** `/generic-approvals/bulk-reject` | Post Bulk Reject Approvals
[**update-approvals-attributes**](#update-approvals-attributes) | **POST** `/generic-approvals/{id}/attributes` | Post Approvals Attributes
[**update-approvals-comments**](#update-approvals-comments) | **POST** `/generic-approvals/{id}/comments` | Post Approvals Comments
[**update-approvals-reassign**](#update-approvals-reassign) | **POST** `/generic-approvals/{id}/reassign` | Post Approvals Reassign


## approve-approval
Post Approvals Approve
Currently this endpoint only supports Entitlement Description Approvals.
Approves a specified approval request on behalf of the caller. This endpoint is for generic approvals, unlike the access-request-approval endpoint, and does not include access-request-approvals. The approval request must be in a state that allows it to be approved.
If called by an admin and the admin is not listed as an approver, the approval request will be reassigned from a random approver to the admin user.

[API Spec](https://developer.sailpoint.com/docs/api/v2025/approve-approval)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | id | **str** | True  | Approval ID that correlates to an existing approval request that a user wants to approve
 Body  | approval_approve_request | [**ApprovalApproveRequest**](../models/approval-approve-request) |   (optional) | 

### Return type
[**Approval**](../models/approval)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Approval object | Approval |  -  |
400 | Client Error - Returned if the request body is invalid. | ErrorResponseDto |  -  |
401 | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. | ListAccessProfiles401Response |  -  |
403 | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. | ErrorResponseDto |  -  |
404 | Not Found - returned if the request URL refers to a resource or object that does not exist | ErrorResponseDto |  -  |
429 | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. | ListAccessProfiles429Response |  -  |
500 | Internal Server Error - Returned if there is an unexpected error. | ErrorResponseDto |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.v2025.api.approvals_api import ApprovalsApi
from sailpoint.v2025.api_client import ApiClient
from sailpoint.v2025.models.approval import Approval
from sailpoint.v2025.models.approval_approve_request import ApprovalApproveRequest
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    id = '38453251-6be2-5f8f-df93-5ce19e295837' # str | Approval ID that correlates to an existing approval request that a user wants to approve # str | Approval ID that correlates to an existing approval request that a user wants to approve
    approval_approve_request = '''{
          "comment" : "comment",
          "additionalAttributes" : {
            "additionalProp1" : "string",
            "additionalProp2" : "string",
            "additionalProp3" : "string"
          }
        }''' # ApprovalApproveRequest |  (optional)

    try:
        # Post Approvals Approve
        
        results = ApprovalsApi(api_client).approve_approval(id=id)
        # Below is a request that includes all optional parameters
        # results = ApprovalsApi(api_client).approve_approval(id, new_approval_approve_request)
        print("The response of ApprovalsApi->approve_approval:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling ApprovalsApi->approve_approval: %s\n" % e)
```



[[Back to top]](#) 

## approve-approval-0
Post Bulk Approve Approvals
Bulk Approves specified approval requests on behalf of the caller

[API Spec](https://developer.sailpoint.com/docs/api/v2025/approve-approval-0)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
 Body  | bulk_approve_request_dto | [**BulkApproveRequestDTO**](../models/bulk-approve-request-dto) | True  | 

### Return type
**object**

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
202 | Accepted - Returned if the request was successfully accepted into the system. | object |  -  |
400 | Client Error - Returned if the request body is invalid. | ErrorResponseDto |  -  |
401 | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. | ListAccessProfiles401Response |  -  |
403 | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. | ErrorResponseDto |  -  |
404 | Not Found - returned if the request URL refers to a resource or object that does not exist | ErrorResponseDto |  -  |
429 | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. | ListAccessProfiles429Response |  -  |
500 | Internal Server Error - Returned if there is an unexpected error. | ErrorResponseDto |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.v2025.api.approvals_api import ApprovalsApi
from sailpoint.v2025.api_client import ApiClient
from sailpoint.v2025.models.bulk_approve_request_dto import BulkApproveRequestDTO
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    bulk_approve_request_dto = '''{
          "comment" : "Bulk approved by admin for monthly review",
          "approvalIds" : [ "38453251-6be2-5f8f-df93-5ce19e295837", "38453251-6be2-5f8f-df93-5ce19e295838" ],
          "additionalAttributes" : {
            "source" : "automation",
            "urgency" : "high"
          }
        }''' # BulkApproveRequestDTO | 

    try:
        # Post Bulk Approve Approvals
        new_bulk_approve_request_dto = BulkApproveRequestDto.from_json(bulk_approve_request_dto)
        results = ApprovalsApi(api_client).approve_approval_0(bulk_approve_request_dto=new_bulk_approve_request_dto)
        # Below is a request that includes all optional parameters
        # results = ApprovalsApi(api_client).approve_approval_0(new_bulk_approve_request_dto)
        print("The response of ApprovalsApi->approve_approval_0:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling ApprovalsApi->approve_approval_0: %s\n" % e)
```



[[Back to top]](#) 

## cancel-approval
Post Bulk Cancel Approvals
Bulk cancels specified approval requests on behalf of the caller

[API Spec](https://developer.sailpoint.com/docs/api/v2025/cancel-approval)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
 Body  | bulk_cancel_request_dto | [**BulkCancelRequestDTO**](../models/bulk-cancel-request-dto) | True  | 

### Return type
**object**

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
202 | Accepted - Returned if the request was successfully accepted into the system. | object |  -  |
400 | Client Error - Returned if the request body is invalid. | ErrorResponseDto |  -  |
401 | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. | ListAccessProfiles401Response |  -  |
403 | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. | ErrorResponseDto |  -  |
404 | Not Found - returned if the request URL refers to a resource or object that does not exist | ErrorResponseDto |  -  |
429 | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. | ListAccessProfiles429Response |  -  |
500 | Internal Server Error - Returned if there is an unexpected error. | ErrorResponseDto |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.v2025.api.approvals_api import ApprovalsApi
from sailpoint.v2025.api_client import ApiClient
from sailpoint.v2025.models.bulk_cancel_request_dto import BulkCancelRequestDTO
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    bulk_cancel_request_dto = '''{
          "comment" : "Bulk cancellation by admin",
          "approvalIds" : [ "38453251-6be2-5f8f-df93-5ce19e295837", "38453251-6be2-5f8f-df93-5ce19e295838" ]
        }''' # BulkCancelRequestDTO | 

    try:
        # Post Bulk Cancel Approvals
        new_bulk_cancel_request_dto = BulkCancelRequestDto.from_json(bulk_cancel_request_dto)
        results = ApprovalsApi(api_client).cancel_approval(bulk_cancel_request_dto=new_bulk_cancel_request_dto)
        # Below is a request that includes all optional parameters
        # results = ApprovalsApi(api_client).cancel_approval(new_bulk_cancel_request_dto)
        print("The response of ApprovalsApi->cancel_approval:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling ApprovalsApi->cancel_approval: %s\n" % e)
```



[[Back to top]](#) 

## get-approval
:::warning experimental 
This API is currently in an experimental state. The API is subject to change based on feedback and further testing. You must include the X-SailPoint-Experimental header and set it to `true` to use this endpoint.
:::
:::tip setting x-sailpoint-experimental header
 on the configuration object you can set the `x-sailpoint-experimental` header to `true' to enable all experimantl endpoints within the SDK.
 Example:
 ```python
   configuration = Configuration()
   configuration.experimental = True
 ```
:::
Get an approval
Currently this endpoint only supports Entitlement Description Approvals.
Retrieve a single approval for a given approval ID. This endpoint is for generic approvals, different than the access-request-approval endpoint and does not include access-request-approvals.

[API Spec](https://developer.sailpoint.com/docs/api/v2025/get-approval)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | id | **str** | True  | ID of the approval that is to be returned
   | x_sail_point_experimental | **str** | True  (default to 'true') | Use this header to enable this experimental API.

### Return type
[**Approval**](../models/approval)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Approval object | Approval |  -  |
400 | Client Error - Returned if the request body is invalid. | ErrorResponseDto |  -  |
401 | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. | ListAccessProfiles401Response |  -  |
403 | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. | ErrorResponseDto |  -  |
429 | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. | ListAccessProfiles429Response |  -  |
500 | Internal Server Error - Returned if there is an unexpected error. | ErrorResponseDto |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.v2025.api.approvals_api import ApprovalsApi
from sailpoint.v2025.api_client import ApiClient
from sailpoint.v2025.models.approval import Approval
from sailpoint.configuration import Configuration
configuration = Configuration()

configuration.experimental = True

with ApiClient(configuration) as api_client:
    id = '38453251-6be2-5f8f-df93-5ce19e295837' # str | ID of the approval that is to be returned # str | ID of the approval that is to be returned
    x_sail_point_experimental = 'true' # str | Use this header to enable this experimental API. (default to 'true') # str | Use this header to enable this experimental API. (default to 'true')

    try:
        # Get an approval
        
        results = ApprovalsApi(api_client).get_approval(id=id, x_sail_point_experimental=x_sail_point_experimental)
        # Below is a request that includes all optional parameters
        # results = ApprovalsApi(api_client).get_approval(id, x_sail_point_experimental)
        print("The response of ApprovalsApi->get_approval:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling ApprovalsApi->get_approval: %s\n" % e)
```



[[Back to top]](#) 

## get-approvals
Get approvals
Currently this endpoint only supports Entitlement Description Approvals.
Get a list of approvals. This endpoint is for generic approvals, unlike the access-request-approval endpoint, and does not include access-request-approvals. 
Absence of all query parameters for non admins will will default to mine=true. Admin will default to mine=false.
Absence of all query parameters for admins will return all approvals in the org.

[API Spec](https://developer.sailpoint.com/docs/api/v2025/get-approvals)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
  Query | mine | **bool** |   (optional) (default to False) | Returns the list of approvals for the current caller. Defaults to false if admin, true otherwise.
  Query | requester_id | **str** |   (optional) | Returns the list of approvals for a given requester ID. Must match the calling user's identity ID unless they are an admin.
  Query | requestee_id | **str** |   (optional) | Returns the list of approvals for a given requesteeId ID. Must match the calling user's identity ID unless they are an admin.
  Query | approver_id | **str** |   (optional) | Returns the list of approvals for a given approverId ID. Must match the calling user's identity ID unless they are an admin.
  Query | count | **bool** |   (optional) (default to False) | Adds X-Total-Count to the header to give the amount of total approvals returned from the query.
  Query | count_only | **bool** |   (optional) (default to False) | Adds X-Total-Count to the header to give the amount of total approvals returned from the query. Only returns the count and no approval objects.
  Query | include_comments | **bool** |   (optional) (default to False) | If set to true in the query, the approval requests returned will include comments.
  Query | include_approvers | **bool** |   (optional) (default to False) | If set to true in the query, the approval requests returned will include approvers.
  Query | include_batch_info | **bool** |   (optional) (default to False) | If set to true in the query, the approval requests returned will include batch information.
  Query | filters | **str** |   (optional) | Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **status**: *eq, ne, in, co, sw*  **referenceType**: *eq, ne, in, co, sw*  **name**: *eq, ne, in, co, sw*  **priority**: *eq, ne, in, co, sw*  **type**: *eq, ne, in, co, sw*  **medium**: *eq, ne, in, co, sw*  **description**: *eq, ne, in, co, sw*  **batchId**: *eq, ne, in, co, sw*  **approvalId**: *eq, ne, in, co, sw*  **tenantId**: *eq, ne, in, co, sw*  **createdDate**: *eq, ne, in, co, sw, gt, ge, lt, le*  **dueDate**: *eq, ne, in, co, sw, gt, ge, lt, le*  **completedDate**: *eq, ne, in, co, sw, gt, ge, lt, le*  **search**: *eq, ne, in, co, sw*  **referenceId**: *eq, ne, in, co, sw*  **referenceName**: *eq, ne, in, co, sw*  **requestedTargetType**: *eq, ne, in, co, sw*  **requestedTargetRequestType**: *eq, ne, in, co, sw*  **requestedTargetId**: *eq, ne, in, co, sw*  **modifiedDate**: *eq, ne, in, co, sw, gt, ge, lt, le*  **requesterId**: *eq, ne, in, co, sw*  **requesteeId**: *eq, ne, in, co, sw*  **approverId**: *eq, ne, in, co, sw*  **decisionDate**: *eq, ne, in, co, sw, gt, ge, lt, le*
  Query | limit | **int** |   (optional) (default to 250) | Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information.
  Query | offset | **int** |   (optional) (default to 0) | Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information.

### Return type
[**List[Approval]**](../models/approval)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | List of approvals. | List[Approval] |  -  |
400 | Client Error - Returned if the request body is invalid. | ErrorResponseDto |  -  |
401 | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. | ListAccessProfiles401Response |  -  |
403 | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. | ErrorResponseDto |  -  |
429 | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. | ListAccessProfiles429Response |  -  |
500 | Internal Server Error - Returned if there is an unexpected error. | ErrorResponseDto |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.v2025.api.approvals_api import ApprovalsApi
from sailpoint.v2025.api_client import ApiClient
from sailpoint.v2025.models.approval import Approval
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    mine = False # bool | Returns the list of approvals for the current caller. Defaults to false if admin, true otherwise. (optional) (default to False) # bool | Returns the list of approvals for the current caller. Defaults to false if admin, true otherwise. (optional) (default to False)
    requester_id = '17e633e7d57e481569df76323169deb6a' # str | Returns the list of approvals for a given requester ID. Must match the calling user's identity ID unless they are an admin. (optional) # str | Returns the list of approvals for a given requester ID. Must match the calling user's identity ID unless they are an admin. (optional)
    requestee_id = '27e6334g757e481569df76323169db9sc' # str | Returns the list of approvals for a given requesteeId ID. Must match the calling user's identity ID unless they are an admin. (optional) # str | Returns the list of approvals for a given requesteeId ID. Must match the calling user's identity ID unless they are an admin. (optional)
    approver_id = '37e6334g557e481569df7g2d3169db9sb' # str | Returns the list of approvals for a given approverId ID. Must match the calling user's identity ID unless they are an admin. (optional) # str | Returns the list of approvals for a given approverId ID. Must match the calling user's identity ID unless they are an admin. (optional)
    count = False # bool | Adds X-Total-Count to the header to give the amount of total approvals returned from the query. (optional) (default to False) # bool | Adds X-Total-Count to the header to give the amount of total approvals returned from the query. (optional) (default to False)
    count_only = False # bool | Adds X-Total-Count to the header to give the amount of total approvals returned from the query. Only returns the count and no approval objects. (optional) (default to False) # bool | Adds X-Total-Count to the header to give the amount of total approvals returned from the query. Only returns the count and no approval objects. (optional) (default to False)
    include_comments = False # bool | If set to true in the query, the approval requests returned will include comments. (optional) (default to False) # bool | If set to true in the query, the approval requests returned will include comments. (optional) (default to False)
    include_approvers = False # bool | If set to true in the query, the approval requests returned will include approvers. (optional) (default to False) # bool | If set to true in the query, the approval requests returned will include approvers. (optional) (default to False)
    include_batch_info = False # bool | If set to true in the query, the approval requests returned will include batch information. (optional) (default to False) # bool | If set to true in the query, the approval requests returned will include batch information. (optional) (default to False)
    filters = 'filters=status eq PENDING' # str | Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **status**: *eq, ne, in, co, sw*  **referenceType**: *eq, ne, in, co, sw*  **name**: *eq, ne, in, co, sw*  **priority**: *eq, ne, in, co, sw*  **type**: *eq, ne, in, co, sw*  **medium**: *eq, ne, in, co, sw*  **description**: *eq, ne, in, co, sw*  **batchId**: *eq, ne, in, co, sw*  **approvalId**: *eq, ne, in, co, sw*  **tenantId**: *eq, ne, in, co, sw*  **createdDate**: *eq, ne, in, co, sw, gt, ge, lt, le*  **dueDate**: *eq, ne, in, co, sw, gt, ge, lt, le*  **completedDate**: *eq, ne, in, co, sw, gt, ge, lt, le*  **search**: *eq, ne, in, co, sw*  **referenceId**: *eq, ne, in, co, sw*  **referenceName**: *eq, ne, in, co, sw*  **requestedTargetType**: *eq, ne, in, co, sw*  **requestedTargetRequestType**: *eq, ne, in, co, sw*  **requestedTargetId**: *eq, ne, in, co, sw*  **modifiedDate**: *eq, ne, in, co, sw, gt, ge, lt, le*  **requesterId**: *eq, ne, in, co, sw*  **requesteeId**: *eq, ne, in, co, sw*  **approverId**: *eq, ne, in, co, sw*  **decisionDate**: *eq, ne, in, co, sw, gt, ge, lt, le* (optional) # str | Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **status**: *eq, ne, in, co, sw*  **referenceType**: *eq, ne, in, co, sw*  **name**: *eq, ne, in, co, sw*  **priority**: *eq, ne, in, co, sw*  **type**: *eq, ne, in, co, sw*  **medium**: *eq, ne, in, co, sw*  **description**: *eq, ne, in, co, sw*  **batchId**: *eq, ne, in, co, sw*  **approvalId**: *eq, ne, in, co, sw*  **tenantId**: *eq, ne, in, co, sw*  **createdDate**: *eq, ne, in, co, sw, gt, ge, lt, le*  **dueDate**: *eq, ne, in, co, sw, gt, ge, lt, le*  **completedDate**: *eq, ne, in, co, sw, gt, ge, lt, le*  **search**: *eq, ne, in, co, sw*  **referenceId**: *eq, ne, in, co, sw*  **referenceName**: *eq, ne, in, co, sw*  **requestedTargetType**: *eq, ne, in, co, sw*  **requestedTargetRequestType**: *eq, ne, in, co, sw*  **requestedTargetId**: *eq, ne, in, co, sw*  **modifiedDate**: *eq, ne, in, co, sw, gt, ge, lt, le*  **requesterId**: *eq, ne, in, co, sw*  **requesteeId**: *eq, ne, in, co, sw*  **approverId**: *eq, ne, in, co, sw*  **decisionDate**: *eq, ne, in, co, sw, gt, ge, lt, le* (optional)
    limit = 250 # int | Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 250) # int | Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 250)
    offset = 0 # int | Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 0) # int | Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 0)

    try:
        # Get approvals
        
        results = ApprovalsApi(api_client).get_approvals()
        # Below is a request that includes all optional parameters
        # results = ApprovalsApi(api_client).get_approvals(mine, requester_id, requestee_id, approver_id, count, count_only, include_comments, include_approvers, include_batch_info, filters, limit, offset)
        print("The response of ApprovalsApi->get_approvals:\n")
        for item in results:
            print(item.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling ApprovalsApi->get_approvals: %s\n" % e)
```



[[Back to top]](#) 

## get-approvals-config-id-type
Get Approval Config Type
Currently this endpoint only supports Entitlement Description Approvals.
Retrieves a singular approval configuration that matches the given ID

[API Spec](https://developer.sailpoint.com/docs/api/v2025/get-approvals-config-id-type)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | id | **str** | True  | ID the ID defined by the scope field, this could the approval ID (uuid), specific domain object ID (uuid), approval type (role/application/access_request/entitlement/source), tenant ID (uuid)

### Return type
[**ApprovalConfig**](../models/approval-config)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Approval object | ApprovalConfig |  -  |
400 | Client Error - Returned if the request body is invalid. | ErrorResponseDto |  -  |
401 | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. | ListAccessProfiles401Response |  -  |
403 | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. | ErrorResponseDto |  -  |
429 | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. | ListAccessProfiles429Response |  -  |
500 | Internal Server Error - Returned if there is an unexpected error. | ErrorResponseDto |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.v2025.api.approvals_api import ApprovalsApi
from sailpoint.v2025.api_client import ApiClient
from sailpoint.v2025.models.approval_config import ApprovalConfig
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    id = '38453251-6be2-5f8f-df93-5ce19e295837' # str | ID the ID defined by the scope field, this could the approval ID (uuid), specific domain object ID (uuid), approval type (role/application/access_request/entitlement/source), tenant ID (uuid) # str | ID the ID defined by the scope field, this could the approval ID (uuid), specific domain object ID (uuid), approval type (role/application/access_request/entitlement/source), tenant ID (uuid)

    try:
        # Get Approval Config Type
        
        results = ApprovalsApi(api_client).get_approvals_config_id_type(id=id)
        # Below is a request that includes all optional parameters
        # results = ApprovalsApi(api_client).get_approvals_config_id_type(id)
        print("The response of ApprovalsApi->get_approvals_config_id_type:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling ApprovalsApi->get_approvals_config_id_type: %s\n" % e)
```



[[Back to top]](#) 

## move-approval
Post Bulk Reassign Approvals
Bulk reassigns specified approval requests on behalf of the caller

[API Spec](https://developer.sailpoint.com/docs/api/v2025/move-approval)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
 Body  | bulk_reassign_request_dto | [**BulkReassignRequestDTO**](../models/bulk-reassign-request-dto) | True  | 

### Return type
**object**

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
202 | Accepted - Returned if the request was successfully accepted into the system. | object |  -  |
400 | Client Error - Returned if the request body is invalid. | ErrorResponseDto |  -  |
401 | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. | ListAccessProfiles401Response |  -  |
403 | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. | ErrorResponseDto |  -  |
404 | Not Found - returned if the request URL refers to a resource or object that does not exist | ErrorResponseDto |  -  |
429 | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. | ListAccessProfiles429Response |  -  |
500 | Internal Server Error - Returned if there is an unexpected error. | ErrorResponseDto |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.v2025.api.approvals_api import ApprovalsApi
from sailpoint.v2025.api_client import ApiClient
from sailpoint.v2025.models.bulk_reassign_request_dto import BulkReassignRequestDTO
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    bulk_reassign_request_dto = '''{
          "reassignTo" : "32454251-6ce2-5d8f-df93-5ce19e295238",
          "comment" : "Bulk reassignment by admin",
          "reassignFrom" : "12353251-6be2-5f8f-df93-5ce19b6e5837",
          "approvalIds" : [ "38453251-6be2-5f8f-df93-5ce19e295837", "38453251-6be2-5f8f-df93-5ce19e295838" ]
        }''' # BulkReassignRequestDTO | 

    try:
        # Post Bulk Reassign Approvals
        new_bulk_reassign_request_dto = BulkReassignRequestDto.from_json(bulk_reassign_request_dto)
        results = ApprovalsApi(api_client).move_approval(bulk_reassign_request_dto=new_bulk_reassign_request_dto)
        # Below is a request that includes all optional parameters
        # results = ApprovalsApi(api_client).move_approval(new_bulk_reassign_request_dto)
        print("The response of ApprovalsApi->move_approval:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling ApprovalsApi->move_approval: %s\n" % e)
```



[[Back to top]](#) 

## put-approvals-config-type
Put Approval Config Type
Upserts a singular approval configuration that matches the given configID and configScope

[API Spec](https://developer.sailpoint.com/docs/api/v2025/put-approvals-config-type)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
  Query | id | **str** | True  | The ID defined by the scope field, where [[id]]:[[scope]] is the following: [[approvalID]]:APPROVAL_REQUEST [[roleID]]:ROLE [[entitlementID]]:ENTITLEMENT [[accessProfileID]]:ACCESS_PROFILE [[sourceID]]:SOURCE [[applicationID]]:APPLICATION ENTITLEMENT_DESCRIPTIONS:APPROVAL_TYPE CUSTOM_ACCESS_REQUEST_APPROVAL:APPROVAL_TYPE GENERIC_APPROVAL:APPROVAL_TYPE [[tenantID]]:TENANT 
  Query | scope | **str** | True  | The scope of the field, where [[id]]:[[scope]] is the following: [[approvalID]]:APPROVAL_REQUEST [[roleID]]:ROLE [[entitlementID]]:ENTITLEMENT [[accessProfileID]]:ACCESS_PROFILE [[sourceID]]:SOURCE [[applicationID]]:APPLICATION ENTITLEMENT_DESCRIPTIONS:APPROVAL_TYPE CUSTOM_ACCESS_REQUEST_APPROVAL:APPROVAL_TYPE GENERIC_APPROVAL:APPROVAL_TYPE [[tenantID]]:TENANT 
 Body  | approval_config | [**ApprovalConfig**](../models/approval-config) | True  | 

### Return type
[**ApprovalConfig**](../models/approval-config)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Verified Email Status | ApprovalConfig |  -  |
400 | Client Error - Returned if the request body is invalid. | ErrorResponseDto |  -  |
401 | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. | ListAccessProfiles401Response |  -  |
403 | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. | ErrorResponseDto |  -  |
404 | Not Found - returned if the request URL refers to a resource or object that does not exist | ErrorResponseDto |  -  |
429 | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. | ListAccessProfiles429Response |  -  |
500 | Internal Server Error - Returned if there is an unexpected error. | ErrorResponseDto |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.v2025.api.approvals_api import ApprovalsApi
from sailpoint.v2025.api_client import ApiClient
from sailpoint.v2025.models.approval_config import ApprovalConfig
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    id = '38453251-6be2-5f8f-df93-5ce19e295837' # str | The ID defined by the scope field, where [[id]]:[[scope]] is the following: [[approvalID]]:APPROVAL_REQUEST [[roleID]]:ROLE [[entitlementID]]:ENTITLEMENT [[accessProfileID]]:ACCESS_PROFILE [[sourceID]]:SOURCE [[applicationID]]:APPLICATION ENTITLEMENT_DESCRIPTIONS:APPROVAL_TYPE CUSTOM_ACCESS_REQUEST_APPROVAL:APPROVAL_TYPE GENERIC_APPROVAL:APPROVAL_TYPE [[tenantID]]:TENANT  # str | The ID defined by the scope field, where [[id]]:[[scope]] is the following: [[approvalID]]:APPROVAL_REQUEST [[roleID]]:ROLE [[entitlementID]]:ENTITLEMENT [[accessProfileID]]:ACCESS_PROFILE [[sourceID]]:SOURCE [[applicationID]]:APPLICATION ENTITLEMENT_DESCRIPTIONS:APPROVAL_TYPE CUSTOM_ACCESS_REQUEST_APPROVAL:APPROVAL_TYPE GENERIC_APPROVAL:APPROVAL_TYPE [[tenantID]]:TENANT 
    scope = 'ROLE' # str | The scope of the field, where [[id]]:[[scope]] is the following: [[approvalID]]:APPROVAL_REQUEST [[roleID]]:ROLE [[entitlementID]]:ENTITLEMENT [[accessProfileID]]:ACCESS_PROFILE [[sourceID]]:SOURCE [[applicationID]]:APPLICATION ENTITLEMENT_DESCRIPTIONS:APPROVAL_TYPE CUSTOM_ACCESS_REQUEST_APPROVAL:APPROVAL_TYPE GENERIC_APPROVAL:APPROVAL_TYPE [[tenantID]]:TENANT  # str | The scope of the field, where [[id]]:[[scope]] is the following: [[approvalID]]:APPROVAL_REQUEST [[roleID]]:ROLE [[entitlementID]]:ENTITLEMENT [[accessProfileID]]:ACCESS_PROFILE [[sourceID]]:SOURCE [[applicationID]]:APPLICATION ENTITLEMENT_DESCRIPTIONS:APPROVAL_TYPE CUSTOM_ACCESS_REQUEST_APPROVAL:APPROVAL_TYPE GENERIC_APPROVAL:APPROVAL_TYPE [[tenantID]]:TENANT 
    approval_config = '''{
          "timeoutConfig" : {
            "daysUntilTimeout" : 2,
            "enabled" : true,
            "timeoutResult" : "EXPIRED"
          },
          "requiresComment" : "ALL",
          "cronTimezone" : {
            "offset" : "",
            "location" : "America/New_York"
          },
          "fallbackApprover" : {
            "identityID" : "17e633e7d57e481569df76323169deb6a",
            "members" : [ {
              "name" : "Bob Neil",
              "id" : "17e633e7d57e481569df76323169deb6a",
              "type" : "IDENTITY",
              "email" : "mail@mail.com"
            }, {
              "name" : "Bob Neil",
              "id" : "17e633e7d57e481569df76323169deb6a",
              "type" : "IDENTITY",
              "email" : "mail@mail.com"
            } ],
            "name" : "Jim Bob",
            "ownerOf" : [ {
              "name" : "Access Request App",
              "id" : "string",
              "type" : "APPLICATION"
            }, {
              "name" : "Access Request App",
              "id" : "string",
              "type" : "APPLICATION"
            } ],
            "serialOrder" : 0,
            "type" : "IDENTITY",
            "email" : "mail@mail.com"
          },
          "reminderConfig" : {
            "reminderCronSchedule" : "1 1 1 1 1",
            "daysUntilFirstReminder" : 0,
            "maxReminders" : 5,
            "enabled" : false
          },
          "scope" : "APPROVAL_REQUEST",
          "tenantId" : "d3c10266-1a31-4acc-b01e-44a3d1c56615",
          "escalationConfig" : {
            "escalationCronSchedule" : "*/5 * * * *",
            "escalationChain" : [ {
              "tier" : 1,
              "chainId" : "ef85d1a8-41ef-433a-8153-0b1f59e7b26a",
              "identityType" : "IDENTITY",
              "identityId" : "fdfda352157d4cc79bb749953131b457"
            }, {
              "tier" : 1,
              "chainId" : "ef85d1a8-41ef-433a-8153-0b1f59e7b26a",
              "identityType" : "IDENTITY",
              "identityId" : "fdfda352157d4cc79bb749953131b457"
            } ],
            "daysUntilFirstEscalation" : 2,
            "enabled" : true
          },
          "id" : "5804e7d6-e04b-400f-9fb8-dff894419a2f",
          "serialChain" : [ {
            "tier" : 1,
            "chainId" : "23dc206e-2a9e-4f98-93db-8d6e342cca18",
            "identityType" : "IDENTITY",
            "identityId" : "2c9180858090ea8801809a0465e829da"
          }, {
            "tier" : 1,
            "chainId" : "23dc206e-2a9e-4f98-93db-8d6e342cca18",
            "identityType" : "IDENTITY",
            "identityId" : "2c9180858090ea8801809a0465e829da"
          } ],
          "autoApprove" : "false"
        }''' # ApprovalConfig | 

    try:
        # Put Approval Config Type
        new_approval_config = ApprovalConfig.from_json(approval_config)
        results = ApprovalsApi(api_client).put_approvals_config_type(id=id, scope=scope, approval_config=new_approval_config)
        # Below is a request that includes all optional parameters
        # results = ApprovalsApi(api_client).put_approvals_config_type(id, scope, new_approval_config)
        print("The response of ApprovalsApi->put_approvals_config_type:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling ApprovalsApi->put_approvals_config_type: %s\n" % e)
```



[[Back to top]](#) 

## reject-approval
Post Approvals Reject
Currently this endpoint only supports Entitlement Description Approvals.
Rejects a specified approval request on behalf of the caller.
If called by an admin and the admin is not listed as an approver, the approval request will be reassigned from a random approver to the admin user.

[API Spec](https://developer.sailpoint.com/docs/api/v2025/reject-approval)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | id | **str** | True  | Approval ID that correlates to an existing approval request that a user wants to reject.
 Body  | approval_reject_request | [**ApprovalRejectRequest**](../models/approval-reject-request) |   (optional) | 

### Return type
 (empty response body)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
204 | No content - indicates the request was successful but there is no content to be returned in the response. |  |  -  |
400 | Client Error - Returned if the request body is invalid. | ErrorResponseDto |  -  |
401 | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. | ListAccessProfiles401Response |  -  |
403 | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. | ErrorResponseDto |  -  |
404 | Not Found - returned if the request URL refers to a resource or object that does not exist | ErrorResponseDto |  -  |
429 | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. | ListAccessProfiles429Response |  -  |
500 | Internal Server Error - Returned if there is an unexpected error. | ErrorResponseDto |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.v2025.api.approvals_api import ApprovalsApi
from sailpoint.v2025.api_client import ApiClient
from sailpoint.v2025.models.approval_reject_request import ApprovalRejectRequest
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    id = '38453251-6be2-5f8f-df93-5ce19e295837' # str | Approval ID that correlates to an existing approval request that a user wants to reject. # str | Approval ID that correlates to an existing approval request that a user wants to reject.
    approval_reject_request = '''{
          "comment" : "string"
        }''' # ApprovalRejectRequest |  (optional)

    try:
        # Post Approvals Reject
        
        ApprovalsApi(api_client).reject_approval(id=id)
        # Below is a request that includes all optional parameters
        # ApprovalsApi(api_client).reject_approval(id, new_approval_reject_request)
    except Exception as e:
        print("Exception when calling ApprovalsApi->reject_approval: %s\n" % e)
```



[[Back to top]](#) 

## reject-approval-0
Post Bulk Reject Approvals
Bulk reject specified approval requests on behalf of the caller

[API Spec](https://developer.sailpoint.com/docs/api/v2025/reject-approval-0)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
 Body  | bulk_reject_request_dto | [**BulkRejectRequestDTO**](../models/bulk-reject-request-dto) | True  | 

### Return type
**object**

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
202 | Accepted - Returned if the request was successfully accepted into the system. | object |  -  |
400 | Client Error - Returned if the request body is invalid. | ErrorResponseDto |  -  |
401 | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. | ListAccessProfiles401Response |  -  |
403 | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. | ErrorResponseDto |  -  |
404 | Not Found - returned if the request URL refers to a resource or object that does not exist | ErrorResponseDto |  -  |
429 | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. | ListAccessProfiles429Response |  -  |
500 | Internal Server Error - Returned if there is an unexpected error. | ErrorResponseDto |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.v2025.api.approvals_api import ApprovalsApi
from sailpoint.v2025.api_client import ApiClient
from sailpoint.v2025.models.bulk_reject_request_dto import BulkRejectRequestDTO
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    bulk_reject_request_dto = '''{
          "comment" : "Bulk reject by admin",
          "approvalIds" : [ "38453251-6be2-5f8f-df93-5ce19e295837", "38453251-6be2-5f8f-df93-5ce19e295838" ]
        }''' # BulkRejectRequestDTO | 

    try:
        # Post Bulk Reject Approvals
        new_bulk_reject_request_dto = BulkRejectRequestDto.from_json(bulk_reject_request_dto)
        results = ApprovalsApi(api_client).reject_approval_0(bulk_reject_request_dto=new_bulk_reject_request_dto)
        # Below is a request that includes all optional parameters
        # results = ApprovalsApi(api_client).reject_approval_0(new_bulk_reject_request_dto)
        print("The response of ApprovalsApi->reject_approval_0:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling ApprovalsApi->reject_approval_0: %s\n" % e)
```



[[Back to top]](#) 

## update-approvals-attributes
Post Approvals Attributes
Currently this endpoint only supports Entitlement Description Approvals.
Allows for the edit/addition/removal of the key/value pair additional attributes map for an existing approval request.

[API Spec](https://developer.sailpoint.com/docs/api/v2025/update-approvals-attributes)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | id | **str** | True  | Approval ID that correlates to an existing approval request that a user wants to change the attributes of.
 Body  | approval_attributes_request | [**ApprovalAttributesRequest**](../models/approval-attributes-request) | True  | 

### Return type
[**Approval**](../models/approval)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Approval object | Approval |  -  |
400 | Client Error - Returned if the request body is invalid. | ErrorResponseDto |  -  |
401 | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. | ListAccessProfiles401Response |  -  |
403 | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. | ErrorResponseDto |  -  |
404 | Not Found - returned if the request URL refers to a resource or object that does not exist | ErrorResponseDto |  -  |
429 | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. | ListAccessProfiles429Response |  -  |
500 | Internal Server Error - Returned if there is an unexpected error. | ErrorResponseDto |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.v2025.api.approvals_api import ApprovalsApi
from sailpoint.v2025.api_client import ApiClient
from sailpoint.v2025.models.approval import Approval
from sailpoint.v2025.models.approval_attributes_request import ApprovalAttributesRequest
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    id = '38453251-6be2-5f8f-df93-5ce19e295837' # str | Approval ID that correlates to an existing approval request that a user wants to change the attributes of. # str | Approval ID that correlates to an existing approval request that a user wants to change the attributes of.
    approval_attributes_request = '''{
          "removeAttributeKeys" : [ "string" ],
          "comment" : "comment",
          "additionalAttributes" : {
            "additionalProp1" : "string",
            "additionalProp2" : "string",
            "additionalProp3" : "string"
          }
        }''' # ApprovalAttributesRequest | 

    try:
        # Post Approvals Attributes
        new_approval_attributes_request = ApprovalAttributesRequest.from_json(approval_attributes_request)
        results = ApprovalsApi(api_client).update_approvals_attributes(id=id, approval_attributes_request=new_approval_attributes_request)
        # Below is a request that includes all optional parameters
        # results = ApprovalsApi(api_client).update_approvals_attributes(id, new_approval_attributes_request)
        print("The response of ApprovalsApi->update_approvals_attributes:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling ApprovalsApi->update_approvals_attributes: %s\n" % e)
```



[[Back to top]](#) 

## update-approvals-comments
Post Approvals Comments
Currently this endpoint only supports Entitlement Description Approvals.
Adds comments to a specified approval request.

[API Spec](https://developer.sailpoint.com/docs/api/v2025/update-approvals-comments)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | id | **str** | True  | Approval ID that correlates to an existing approval request that a user wants to add a comment to.
 Body  | approval_comments_request | [**ApprovalCommentsRequest**](../models/approval-comments-request) | True  | 

### Return type
[**Approval**](../models/approval)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Approval object | Approval |  -  |
400 | Client Error - Returned if the request body is invalid. | ErrorResponseDto |  -  |
401 | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. | ListAccessProfiles401Response |  -  |
403 | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. | ErrorResponseDto |  -  |
404 | Not Found - returned if the request URL refers to a resource or object that does not exist | ErrorResponseDto |  -  |
429 | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. | ListAccessProfiles429Response |  -  |
500 | Internal Server Error - Returned if there is an unexpected error. | ErrorResponseDto |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.v2025.api.approvals_api import ApprovalsApi
from sailpoint.v2025.api_client import ApiClient
from sailpoint.v2025.models.approval import Approval
from sailpoint.v2025.models.approval_comments_request import ApprovalCommentsRequest
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    id = '38453251-6be2-5f8f-df93-5ce19e295837' # str | Approval ID that correlates to an existing approval request that a user wants to add a comment to. # str | Approval ID that correlates to an existing approval request that a user wants to add a comment to.
    approval_comments_request = '''{
          "comment" : "Approval comment."
        }''' # ApprovalCommentsRequest | 

    try:
        # Post Approvals Comments
        new_approval_comments_request = ApprovalCommentsRequest.from_json(approval_comments_request)
        results = ApprovalsApi(api_client).update_approvals_comments(id=id, approval_comments_request=new_approval_comments_request)
        # Below is a request that includes all optional parameters
        # results = ApprovalsApi(api_client).update_approvals_comments(id, new_approval_comments_request)
        print("The response of ApprovalsApi->update_approvals_comments:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling ApprovalsApi->update_approvals_comments: %s\n" % e)
```



[[Back to top]](#) 

## update-approvals-reassign
Post Approvals Reassign
Currently this endpoint only supports Entitlement Description Approvals.
Reassigns an approval request to another identity resulting in that identity being added as an authorized approver.

[API Spec](https://developer.sailpoint.com/docs/api/v2025/update-approvals-reassign)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | id | **str** | True  | Approval ID that correlates to an existing approval request that a user wants to reassign.
 Body  | approval_reassign_request | [**ApprovalReassignRequest**](../models/approval-reassign-request) | True  | 

### Return type
 (empty response body)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
204 | No content - indicates the request was successful but there is no content to be returned in the response. |  |  -  |
400 | Client Error - Returned if the request body is invalid. | ErrorResponseDto |  -  |
401 | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. | ListAccessProfiles401Response |  -  |
403 | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. | ErrorResponseDto |  -  |
404 | Not Found - returned if the request URL refers to a resource or object that does not exist | ErrorResponseDto |  -  |
429 | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. | ListAccessProfiles429Response |  -  |
500 | Internal Server Error - Returned if there is an unexpected error. | ErrorResponseDto |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.v2025.api.approvals_api import ApprovalsApi
from sailpoint.v2025.api_client import ApiClient
from sailpoint.v2025.models.approval_reassign_request import ApprovalReassignRequest
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    id = '38453251-6be2-5f8f-df93-5ce19e295837' # str | Approval ID that correlates to an existing approval request that a user wants to reassign. # str | Approval ID that correlates to an existing approval request that a user wants to reassign.
    approval_reassign_request = '''{
          "reassignTo" : "152354832eb6f8f539fd738592e19ec5",
          "comment" : "comment",
          "reassignFrom" : "384532516be25f8fdf935ce19e295837"
        }''' # ApprovalReassignRequest | 

    try:
        # Post Approvals Reassign
        new_approval_reassign_request = ApprovalReassignRequest.from_json(approval_reassign_request)
        ApprovalsApi(api_client).update_approvals_reassign(id=id, approval_reassign_request=new_approval_reassign_request)
        # Below is a request that includes all optional parameters
        # ApprovalsApi(api_client).update_approvals_reassign(id, new_approval_reassign_request)
    except Exception as e:
        print("Exception when calling ApprovalsApi->update_approvals_reassign: %s\n" % e)
```



[[Back to top]](#) 



