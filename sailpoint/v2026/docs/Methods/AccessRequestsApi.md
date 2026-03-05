---
id: v2026-access-requests
title: Access_Requests
pagination_label: Access_Requests
sidebar_label: Access_Requests
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Access_Requests', 'V2026Access_Requests'] 
slug: /tools/sdk/python/v2026/methods/access-requests
tags: ['SDK', 'Software Development Kit', 'Access_Requests', 'V2026Access_Requests']
---

# sailpoint.v2026.AccessRequestsApi
   
All URIs are relative to *https://sailpoint.api.identitynow.com/v2026*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get-access-request-config**](#get-access-request-config) | **GET** `/access-request-config` | Get access request configuration
[**set-access-request-config**](#set-access-request-config) | **PUT** `/access-request-config` | Update access request configuration


## get-access-request-config
Get access request configuration
This endpoint returns the current access-request configuration.

[API Spec](https://developer.sailpoint.com/docs/api/v2026/get-access-request-config)

### Parameters 
This endpoint does not need any parameter. 

### Return type
[**AccessRequestConfig**](../models/access-request-config)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Access Request Configuration Details. | AccessRequestConfig |  -  |
400 | Client Error - Returned if the request body is invalid. | ErrorResponseDto |  -  |
401 | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. | GetAccessRequestConfig401Response |  -  |
403 | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. | ErrorResponseDto |  -  |
429 | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. | GetAccessRequestConfig429Response |  -  |
500 | Internal Server Error - Returned if there is an unexpected error. | ErrorResponseDto |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.v2026.api.access_requests_api import AccessRequestsApi
from sailpoint.v2026.api_client import ApiClient
from sailpoint.v2026.models.access_request_config import AccessRequestConfig
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:

    try:
        # Get access request configuration
        
        results = AccessRequestsApi(api_client).get_access_request_config()
        # Below is a request that includes all optional parameters
        # results = AccessRequestsApi(api_client).get_access_request_config()
        print("The response of AccessRequestsApi->get_access_request_config:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling AccessRequestsApi->get_access_request_config: %s\n" % e)
```



[[Back to top]](#) 

## set-access-request-config
Update access request configuration
This endpoint replaces the current access-request configuration.

[API Spec](https://developer.sailpoint.com/docs/api/v2026/set-access-request-config)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
 Body  | access_request_config | [**AccessRequestConfig**](../models/access-request-config) | True  | 

### Return type
[**AccessRequestConfig**](../models/access-request-config)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Access Request Configuration Details. | AccessRequestConfig |  -  |
400 | Client Error - Returned if the request body is invalid. | ErrorResponseDto |  -  |
401 | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. | GetAccessRequestConfig401Response |  -  |
403 | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. | ErrorResponseDto |  -  |
429 | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. | GetAccessRequestConfig429Response |  -  |
500 | Internal Server Error - Returned if there is an unexpected error. | ErrorResponseDto |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.v2026.api.access_requests_api import AccessRequestsApi
from sailpoint.v2026.api_client import ApiClient
from sailpoint.v2026.models.access_request_config import AccessRequestConfig
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    access_request_config = '''{
          "govGroupVisibilityEnabled" : true,
          "requestOnBehalfOfConfig" : {
            "allowRequestOnBehalfOfEmployeeByManager" : true,
            "allowRequestOnBehalfOfAnyoneByAnyone" : true
          },
          "autoApprovalEnabled" : true,
          "entitlementRequestConfig" : {
            "accessRequestConfig" : {
              "denialCommentRequired" : false,
              "approvalSchemes" : [ {
                "approverId" : "e3eab852-8315-467f-9de7-70eda97f63c8",
                "approverType" : "GOVERNANCE_GROUP"
              }, {
                "approverId" : "e3eab852-8315-467f-9de7-70eda97f63c8",
                "approverType" : "GOVERNANCE_GROUP"
              } ],
              "reauthorizationRequired" : false,
              "requestCommentRequired" : true,
              "requireEndDate" : true,
              "maxPermittedAccessDuration" : {
                "value" : 5,
                "timeUnit" : "DAYS"
              }
            },
            "revocationRequestConfig" : {
              "approvalSchemes" : [ {
                "approverId" : "e3eab852-8315-467f-9de7-70eda97f63c8",
                "approverType" : "GOVERNANCE_GROUP"
              }, {
                "approverId" : "e3eab852-8315-467f-9de7-70eda97f63c8",
                "approverType" : "GOVERNANCE_GROUP"
              } ]
            }
          },
          "reauthorizationEnabled" : true,
          "approvalsMustBeExternal" : true
        }''' # AccessRequestConfig | 

    try:
        # Update access request configuration
        new_access_request_config = AccessRequestConfig.from_json(access_request_config)
        results = AccessRequestsApi(api_client).set_access_request_config(access_request_config=new_access_request_config)
        # Below is a request that includes all optional parameters
        # results = AccessRequestsApi(api_client).set_access_request_config(new_access_request_config)
        print("The response of AccessRequestsApi->set_access_request_config:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling AccessRequestsApi->set_access_request_config: %s\n" % e)
```



[[Back to top]](#) 



