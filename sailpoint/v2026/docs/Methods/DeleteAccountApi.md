---
id: v2026-delete-account
title: Delete_account
pagination_label: Delete_account
sidebar_label: Delete_account
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Delete_account', 'V2026Delete_account'] 
slug: /tools/sdk/python/v2026/methods/delete-account
tags: ['SDK', 'Software Development Kit', 'Delete_account', 'V2026Delete_account']
---

# sailpoint.v2026.DeleteAccountApi
   
All URIs are relative to *https://sailpoint.api.identitynow.com/v2026*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete-account-request**](#delete-account-request) | **POST** `/account-requests/account/{accountId}/delete` | Delete account


## delete-account-request
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
Delete account
Initiates an account deletion request for the specified account.
This method validates the input data, processes the deletion request,
and generates an asynchronous result containing a tracking ID. 
>**NOTE: You can only delete accounts from sources of the "Connected" type. which supports account deletion**

[API Spec](https://developer.sailpoint.com/docs/api/v2026/delete-account-request)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
   | x_sail_point_experimental | **str** | True  (default to 'true') | Use this header to enable this experimental API.
Path   | account_id | **str** | True  | Account ID.
 Body  | account_delete_request_input | [**AccountDeleteRequestInput**](../models/account-delete-request-input) |   (optional) | 

### Return type
[**AccountDeleteAsyncResult**](../models/account-delete-async-result)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
202 | Account deletion request details. | AccountDeleteAsyncResult |  -  |
400 | Client Error - Returned if the request body is invalid. | ErrorResponseDto |  -  |
401 | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. | GetTaskStatus401Response |  -  |
403 | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. | ErrorResponseDto |  -  |
404 | Not Found - returned if the request URL refers to a resource or object that does not exist | ErrorResponseDto |  -  |
429 | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. | GetTaskStatus429Response |  -  |
500 | Internal Server Error - Returned if there is an unexpected error. | ErrorResponseDto |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.v2026.api.delete_account_api import DeleteAccountApi
from sailpoint.v2026.api_client import ApiClient
from sailpoint.v2026.models.account_delete_async_result import AccountDeleteAsyncResult
from sailpoint.v2026.models.account_delete_request_input import AccountDeleteRequestInput
from sailpoint.configuration import Configuration
configuration = Configuration()

configuration.experimental = True

with ApiClient(configuration) as api_client:
    x_sail_point_experimental = 'true' # str | Use this header to enable this experimental API. (default to 'true') # str | Use this header to enable this experimental API. (default to 'true')
    account_id = 'ef38f94347e94562b5bb8424a56498d8' # str | Account ID. # str | Account ID.
    account_delete_request_input = '''{
          "comments" : "Requesting account deletion request"
        }''' # AccountDeleteRequestInput |  (optional)

    try:
        # Delete account
        
        results = DeleteAccountApi(api_client).delete_account_request(x_sail_point_experimental=x_sail_point_experimental, account_id=account_id)
        # Below is a request that includes all optional parameters
        # results = DeleteAccountApi(api_client).delete_account_request(x_sail_point_experimental, account_id, new_account_delete_request_input)
        print("The response of DeleteAccountApi->delete_account_request:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling DeleteAccountApi->delete_account_request: %s\n" % e)
```



[[Back to top]](#) 



