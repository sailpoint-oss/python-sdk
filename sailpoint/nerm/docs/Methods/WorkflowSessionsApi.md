---
id: workflow-sessions
title: Workflow_sessions
pagination_label: workflow_sessions
sidebar_label: workflow_sessions
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'workflow_sessions', 'workflow_sessions'] 
slug: /tools/sdk/python//methods/workflow-sessions
tags: ['SDK', 'Software Development Kit', 'workflow_sessions', 'workflow_sessions']
---

# sailpoint.nerm.WorkflowSessionsApi
   
All URIs are relative to *https://acmeco.nonemployee.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get-workflow-session**](#get-workflow-session) | **GET** `/workflow_sessions/{id}` | Find workflow session
[**get-workflow-session-upload**](#get-workflow-session-upload) | **GET** `/workflow_sessions/{id}/upload/{attribute_id}` | Retrieves workflow session attachment URL
[**get-workflow-sessions**](#get-workflow-sessions) | **GET** `/workflow_sessions` | Get workflow sessions
[**patch-workflow-session**](#patch-workflow-session) | **PATCH** `/workflow_sessions/{id}` | Update a workflow session
[**submit-workflow-session**](#submit-workflow-session) | **POST** `/workflow_sessions` | Create a workflow session
[**submit-workflow-session-upload**](#submit-workflow-session-upload) | **POST** `/workflow_sessions/{id}/upload/{attribute_id}` | Uploads workflow session attachment


## get-workflow-session
Find workflow session
Find workflow session by id

[API Spec](https://developer.sailpoint.com/docs/api//get-workflow-session)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | id | **str** | True  | ID of the object to retrieve, update, or delete

### Return type
[**SubmitWorkflowSession200Response**](../models/submit-workflow-session200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | SubmitWorkflowSession200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.workflow_sessions_api import WorkflowSessionsApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.submit_workflow_session200_response import SubmitWorkflowSession200Response
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    id = '1246d8b3-ac29-4015-8154-dea4434a73fa' # str | ID of the object to retrieve, update, or delete # str | ID of the object to retrieve, update, or delete

    try:
        # Find workflow session
        
        results = WorkflowSessionsApi(api_client).get_workflow_session(id=id)
        # Below is a request that includes all optional parameters
        # results = WorkflowSessionsApi(api_client).get_workflow_session(id)
        print("The response of WorkflowSessionsApi->get_workflow_session:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling WorkflowSessionsApi->get_workflow_session: %s\n" % e)
```



[[Back to top]](#) 

## get-workflow-session-upload
Retrieves workflow session attachment URL
Retrieves the URL of an attachment attribute value from a workflow session

[API Spec](https://developer.sailpoint.com/docs/api//get-workflow-session-upload)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | id | **str** | True  | ID of the object to retrieve, update, or delete
Path   | attribute_id | **str** | True  | The id of the attachment attribute

### Return type
[**Url**](../models/url)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | Url |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.workflow_sessions_api import WorkflowSessionsApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.url import Url
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    id = '1246d8b3-ac29-4015-8154-dea4434a73fa' # str | ID of the object to retrieve, update, or delete # str | ID of the object to retrieve, update, or delete
    attribute_id = '1246d8b3-ac29-4015-8154-dea4434a73fa' # str | The id of the attachment attribute # str | The id of the attachment attribute

    try:
        # Retrieves workflow session attachment URL
        
        results = WorkflowSessionsApi(api_client).get_workflow_session_upload(id=id, attribute_id=attribute_id)
        # Below is a request that includes all optional parameters
        # results = WorkflowSessionsApi(api_client).get_workflow_session_upload(id, attribute_id)
        print("The response of WorkflowSessionsApi->get_workflow_session_upload:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling WorkflowSessionsApi->get_workflow_session_upload: %s\n" % e)
```



[[Back to top]](#) 

## get-workflow-sessions
Get workflow sessions
Get workflow sessions

[API Spec](https://developer.sailpoint.com/docs/api//get-workflow-sessions)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
  Query | limit | **int** |   (optional) | The maximum number of items to return.
  Query | offset | **int** |   (optional) | The number of items to skip before starting to collect the result set.
  Query | order | **str** |   (optional) | The field to order results by.
  Query | profile_id | **str** |   (optional) | Profile ID to filter by
Path   | uid | **str** |   (optional) | UID of the object to retrieve, update, or delete.  A UID or \"specified identifier\" is a string typically in \"snake_case\" format that provides a human-readable description of the record.  They are commonly used to ensure sandbox, qa, staging and production tenants have the identical configuration items loaded.  Every record has a UID assigned when persisted. When not specified the system assigns one by default.  A default value looks like a 32 character string of random hexadecimal characters.
  Query | workflow_id | **str** |   (optional) | Workflow ID for filtering
  Query | requester_id | **str** |   (optional) | Requester ID for filtering
  Query | status | **str** |   (optional) | filter by workflow session status
  Query | metadata | **bool** |   (optional) (default to False) | Returns batching metadata in the response. This includes `total` as the total quantity, `next` as the path of the following query url, `limit` and `after_id` (if requested) with the next following id (null if it is the last \"page\").

### Return type
[**GetWorkflowSessions200Response**](../models/get-workflow-sessions200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | GetWorkflowSessions200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: Not defined
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.workflow_sessions_api import WorkflowSessionsApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.get_workflow_sessions200_response import GetWorkflowSessions200Response
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    limit = 5 # int | The maximum number of items to return. (optional) # int | The maximum number of items to return. (optional)
    offset = 5 # int | The number of items to skip before starting to collect the result set. (optional) # int | The number of items to skip before starting to collect the result set. (optional)
    order = 'created_at' # str | The field to order results by. (optional) # str | The field to order results by. (optional)
    profile_id = '4e480441-451d-47d9-87c2-9a0f0fe135eb' # str | Profile ID to filter by (optional) # str | Profile ID to filter by (optional)
    uid = 'middle_initial_attribute' # str | UID of the object to retrieve, update, or delete.  A UID or \"specified identifier\" is a string typically in \"snake_case\" format that provides a human-readable description of the record.  They are commonly used to ensure sandbox, qa, staging and production tenants have the identical configuration items loaded.  Every record has a UID assigned when persisted. When not specified the system assigns one by default.  A default value looks like a 32 character string of random hexadecimal characters. (optional) # str | UID of the object to retrieve, update, or delete.  A UID or \"specified identifier\" is a string typically in \"snake_case\" format that provides a human-readable description of the record.  They are commonly used to ensure sandbox, qa, staging and production tenants have the identical configuration items loaded.  Every record has a UID assigned when persisted. When not specified the system assigns one by default.  A default value looks like a 32 character string of random hexadecimal characters. (optional)
    workflow_id = 'bba9cfb2-96c1-4acb-ac79-a21732527265' # str | Workflow ID for filtering (optional) # str | Workflow ID for filtering (optional)
    requester_id = 'c5e1dd38-7e29-464f-a0da-0c0d886d022a' # str | Requester ID for filtering (optional) # str | Requester ID for filtering (optional)
    status = 'pending approval' # str | filter by workflow session status (optional) # str | filter by workflow session status (optional)
    metadata = False # bool | Returns batching metadata in the response. This includes `total` as the total quantity, `next` as the path of the following query url, `limit` and `after_id` (if requested) with the next following id (null if it is the last \"page\"). (optional) (default to False) # bool | Returns batching metadata in the response. This includes `total` as the total quantity, `next` as the path of the following query url, `limit` and `after_id` (if requested) with the next following id (null if it is the last \"page\"). (optional) (default to False)

    try:
        # Get workflow sessions
        
        results = WorkflowSessionsApi(api_client).get_workflow_sessions()
        # Below is a request that includes all optional parameters
        # results = WorkflowSessionsApi(api_client).get_workflow_sessions(limit, offset, order, profile_id, uid, workflow_id, requester_id, status, metadata)
        print("The response of WorkflowSessionsApi->get_workflow_sessions:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling WorkflowSessionsApi->get_workflow_sessions: %s\n" % e)
```



[[Back to top]](#) 

## patch-workflow-session
Update a workflow session
Update a workflow session by id

[API Spec](https://developer.sailpoint.com/docs/api//patch-workflow-session)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | id | **str** | True  | ID of the object to retrieve, update, or delete
 Body  | submit_workflow_session_request | [**SubmitWorkflowSessionRequest**](../models/submit-workflow-session-request) | True  | 
  Query | run | **bool** |   (optional) (default to False) | Will run the created/updated workflow session if successful

### Return type
[**SubmitWorkflowSession200Response**](../models/submit-workflow-session200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | SubmitWorkflowSession200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.workflow_sessions_api import WorkflowSessionsApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.submit_workflow_session200_response import SubmitWorkflowSession200Response
from sailpoint.nerm.models.submit_workflow_session_request import SubmitWorkflowSessionRequest
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    id = '1246d8b3-ac29-4015-8154-dea4434a73fa' # str | ID of the object to retrieve, update, or delete # str | ID of the object to retrieve, update, or delete
    submit_workflow_session_request = '''sailpoint.nerm.SubmitWorkflowSessionRequest()''' # SubmitWorkflowSessionRequest | 
    run = False # bool | Will run the created/updated workflow session if successful (optional) (default to False) # bool | Will run the created/updated workflow session if successful (optional) (default to False)

    try:
        # Update a workflow session
        new_submit_workflow_session_request = SubmitWorkflowSessionRequest.from_json(submit_workflow_session_request)
        results = WorkflowSessionsApi(api_client).patch_workflow_session(id=id, submit_workflow_session_request=new_submit_workflow_session_request)
        # Below is a request that includes all optional parameters
        # results = WorkflowSessionsApi(api_client).patch_workflow_session(id, new_submit_workflow_session_request, run)
        print("The response of WorkflowSessionsApi->patch_workflow_session:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling WorkflowSessionsApi->patch_workflow_session: %s\n" % e)
```



[[Back to top]](#) 

## submit-workflow-session
Create a workflow session
Create a workflow session

[API Spec](https://developer.sailpoint.com/docs/api//submit-workflow-session)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
 Body  | submit_workflow_session_request | [**SubmitWorkflowSessionRequest**](../models/submit-workflow-session-request) | True  | 
  Query | run | **bool** |   (optional) (default to False) | Will run the created/updated workflow session if successful

### Return type
[**SubmitWorkflowSession200Response**](../models/submit-workflow-session200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | SubmitWorkflowSession200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.workflow_sessions_api import WorkflowSessionsApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.submit_workflow_session200_response import SubmitWorkflowSession200Response
from sailpoint.nerm.models.submit_workflow_session_request import SubmitWorkflowSessionRequest
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    submit_workflow_session_request = '''sailpoint.nerm.SubmitWorkflowSessionRequest()''' # SubmitWorkflowSessionRequest | 
    run = False # bool | Will run the created/updated workflow session if successful (optional) (default to False) # bool | Will run the created/updated workflow session if successful (optional) (default to False)

    try:
        # Create a workflow session
        new_submit_workflow_session_request = SubmitWorkflowSessionRequest.from_json(submit_workflow_session_request)
        results = WorkflowSessionsApi(api_client).submit_workflow_session(submit_workflow_session_request=new_submit_workflow_session_request)
        # Below is a request that includes all optional parameters
        # results = WorkflowSessionsApi(api_client).submit_workflow_session(new_submit_workflow_session_request, run)
        print("The response of WorkflowSessionsApi->submit_workflow_session:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling WorkflowSessionsApi->submit_workflow_session: %s\n" % e)
```



[[Back to top]](#) 

## submit-workflow-session-upload
Uploads workflow session attachment
Uploads a new attachment attribute value to a workflow session. The upload must be a FORM data type; this is not a JSON API. The upload must include the binary content of the payload under the 'file' named form element. The upload must not attempt to include the file name or its content type as a other form or JSON as parameters. The upload must not attempt to upload the file body as the POST body payload; it has to arrive as a FORM parameter. Do not use a `File/Binary` payload type for the POST operation in your API client.


[API Spec](https://developer.sailpoint.com/docs/api//submit-workflow-session-upload)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
Path   | id | **str** | True  | ID of the object to retrieve, update, or delete
Path   | attribute_id | **str** | True  | The id of the attachment attribute
   | file | **bytearray** |   (optional) | 

### Return type
[**Url**](../models/url)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | Url |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.workflow_sessions_api import WorkflowSessionsApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.url import Url
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    id = '1246d8b3-ac29-4015-8154-dea4434a73fa' # str | ID of the object to retrieve, update, or delete # str | ID of the object to retrieve, update, or delete
    attribute_id = '1246d8b3-ac29-4015-8154-dea4434a73fa' # str | The id of the attachment attribute # str | The id of the attachment attribute
    file = None # bytearray |  (optional) # bytearray |  (optional)

    try:
        # Uploads workflow session attachment
        
        results = WorkflowSessionsApi(api_client).submit_workflow_session_upload(id=id, attribute_id=attribute_id)
        # Below is a request that includes all optional parameters
        # results = WorkflowSessionsApi(api_client).submit_workflow_session_upload(id, attribute_id, file)
        print("The response of WorkflowSessionsApi->submit_workflow_session_upload:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling WorkflowSessionsApi->submit_workflow_session_upload: %s\n" % e)
```



[[Back to top]](#) 



