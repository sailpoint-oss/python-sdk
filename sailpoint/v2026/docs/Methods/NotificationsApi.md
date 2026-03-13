---
id: v2026-notifications
title: Notifications
pagination_label: Notifications
sidebar_label: Notifications
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Notifications', 'V2026Notifications'] 
slug: /tools/sdk/python/v2026/methods/notifications
tags: ['SDK', 'Software Development Kit', 'Notifications', 'V2026Notifications']
---

# sailpoint.v2026.NotificationsApi
   
All URIs are relative to *https://sailpoint.api.identitynow.com/v2026*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get-notification-template-variables**](#get-notification-template-variables) | **GET** `/notification-template-variables/{key}/{medium}` | Get notification template variables


## get-notification-template-variables
Get notification template variables
Returns global variables and template-specific variables for a given notification template key and medium.
Use these variable names in template content; they are replaced at send time with the corresponding values.
Variable lists can be sorted by key, type, or description via the sorters query parameter (default ascending by key).


[API Spec](https://developer.sailpoint.com/docs/api/v2026/get-notification-template-variables)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | key | **str** | True  | The notification template key. Valid keys (and key/medium pairs) are available from the list notification templates operation. 
Path   | medium | **str** | True  | The notification template medium (e.g. EMAIL, SLACK, TEAMS). Valid key/medium pairs are available from the list notification templates operation. 
  Query | sorters | **str** |   (optional) | Sort results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#sorting-results)  Sorting is supported for the following fields: **key, type, description**

### Return type
[**TemplateVariablesDto**](../models/template-variables-dto)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Global and template-specific variables for the given key and medium. | TemplateVariablesDto |  -  |
400 | Client Error - Returned if the request body is invalid. | ErrorResponseDto |  -  |
401 | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. | GetAccessRequestConfig401Response |  -  |
403 | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. | ErrorResponseDto |  -  |
404 | Not Found - returned if the request URL refers to a resource or object that does not exist | ErrorResponseDto |  -  |
429 | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. | GetAccessRequestConfig429Response |  -  |
500 | Internal Server Error - Returned if there is an unexpected error. | ErrorResponseDto |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.v2026.api.notifications_api import NotificationsApi
from sailpoint.v2026.api_client import ApiClient
from sailpoint.v2026.models.template_variables_dto import TemplateVariablesDto
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    key = 'approval_request_notification' # str | The notification template key. Valid keys (and key/medium pairs) are available from the list notification templates operation.  # str | The notification template key. Valid keys (and key/medium pairs) are available from the list notification templates operation. 
    medium = 'EMAIL' # str | The notification template medium (e.g. EMAIL, SLACK, TEAMS). Valid key/medium pairs are available from the list notification templates operation.  # str | The notification template medium (e.g. EMAIL, SLACK, TEAMS). Valid key/medium pairs are available from the list notification templates operation. 
    sorters = '-description' # str | Sort results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#sorting-results)  Sorting is supported for the following fields: **key, type, description** (optional) # str | Sort results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#sorting-results)  Sorting is supported for the following fields: **key, type, description** (optional)

    try:
        # Get notification template variables
        
        results = NotificationsApi(api_client).get_notification_template_variables(key=key, medium=medium)
        # Below is a request that includes all optional parameters
        # results = NotificationsApi(api_client).get_notification_template_variables(key, medium, sorters)
        print("The response of NotificationsApi->get_notification_template_variables:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling NotificationsApi->get_notification_template_variables: %s\n" % e)
```



[[Back to top]](#) 



