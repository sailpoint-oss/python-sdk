---
id: audits
title: Audits
pagination_label: audits
sidebar_label: audits
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'audits', 'audits'] 
slug: /tools/sdk/python//methods/audits
tags: ['SDK', 'Software Development Kit', 'audits', 'audits']
---

# sailpoint.nerm.AuditsApi
   
All URIs are relative to *https://acmeco.nonemployee.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search**](#search) | **POST** `/audit_events/query` | Query for Audit events


## search
Query for Audit events
This endpoint provides a search engine for Audit Events by optionally combining subject_type, type, and subject_id to narrow down the audit events. A Subject Type of Profile links up to the AuditableProfile types. An Subject Type of WorkflowSession links up to the AuditableWorkflow types. An Subject Type of Get/Post/Patch/Delete links up to the AuditableApi types. The remaining Subject Types link up to the ActiveRecord types (configuration changes).

- Any workflow audit event created as of 10/11/2024 will be able to be queried by workflow name, workflow uid, or workflow profile type.
- Any profile audit event created as of 10/11/2024 will be able to be queried by profile type.
- The entity_type parameter has been updated to subject_type, which now matches what is in the response object.
- With the additional query filters added, there is a max of 5 filter parameters at one time (aside from pagination parameters)

To accommodate these changes, an API contract change was required.  Please read the updated API documentation for the new request syntax.

[API Spec](https://developer.sailpoint.com/docs/api//search)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
 Body  | search_request | [**SearchRequest**](../models/search-request) | True  | 

### Return type
[**Search200Response**](../models/search200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | AuditEvents | Search200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.audits_api import AuditsApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.search200_response import Search200Response
from sailpoint.nerm.models.search_request import SearchRequest
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    search_request = '''sailpoint.nerm.SearchRequest()''' # SearchRequest | 

    try:
        # Query for Audit events
        new_search_request = SearchRequest.from_json(search_request)
        results = AuditsApi(api_client).search(search_request=new_search_request)
        # Below is a request that includes all optional parameters
        # results = AuditsApi(api_client).search(new_search_request)
        print("The response of AuditsApi->search:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling AuditsApi->search: %s\n" % e)
```



[[Back to top]](#) 



