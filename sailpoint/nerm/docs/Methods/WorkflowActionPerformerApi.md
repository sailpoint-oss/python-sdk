---
id: workflow-action-performer
title: Workflow_action_performer
pagination_label: workflow_action_performer
sidebar_label: workflow_action_performer
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'workflow_action_performer', 'workflow_action_performer'] 
slug: /tools/sdk/python//methods/workflow-action-performer
tags: ['SDK', 'Software Development Kit', 'workflow_action_performer', 'workflow_action_performer']
---

# sailpoint.nerm.WorkflowActionPerformerApi
   
All URIs are relative to *https://acmeco.nonemployee.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create-workflow-action-performer**](#create-workflow-action-performer) | **POST** `/workflow_action_performers` | Create a workflow action performer


## create-workflow-action-performer
Create a workflow action performer
Create a workflow action performer for an existing workflow action

[API Spec](https://developer.sailpoint.com/docs/api//create-workflow-action-performer)

### Parameters 

Param Type | Name | Data Type | Required  | Description
------------- | ------------- | ------------- | ------------- | ------------- 
 Body  | create_workflow_action_performer_request | [**CreateWorkflowActionPerformerRequest**](../models/create-workflow-action-performer-request) | True  | 

### Return type
[**CreateWorkflowActionPerformer200Response**](../models/create-workflow-action-performer200-response)

### Responses
Code | Description  | Data Type | Response headers |
------------- | ------------- | ------------- |------------------|
200 | Expected response to a valid request | CreateWorkflowActionPerformer200Response |  -  |
400 | Bad Request - unable to complete. | GetAttributes400Response |  -  |
500 | Internal Server Error - returned on unhandled exceptions. | GetAttributes500Response |  -  |

### HTTP request headers
 - **Content-Type**: application/json
 - **Accept**: application/json

### Example

```python
from sailpoint.nerm.api.workflow_action_performer_api import WorkflowActionPerformerApi
from sailpoint.nerm.api_client import ApiClient
from sailpoint.nerm.models.create_workflow_action_performer200_response import CreateWorkflowActionPerformer200Response
from sailpoint.nerm.models.create_workflow_action_performer_request import CreateWorkflowActionPerformerRequest
from sailpoint.configuration import Configuration
configuration = Configuration()


with ApiClient(configuration) as api_client:
    create_workflow_action_performer_request = '''sailpoint.nerm.CreateWorkflowActionPerformerRequest()''' # CreateWorkflowActionPerformerRequest | 

    try:
        # Create a workflow action performer
        new_create_workflow_action_performer_request = CreateWorkflowActionPerformerRequest.from_json(create_workflow_action_performer_request)
        results = WorkflowActionPerformerApi(api_client).create_workflow_action_performer(create_workflow_action_performer_request=new_create_workflow_action_performer_request)
        # Below is a request that includes all optional parameters
        # results = WorkflowActionPerformerApi(api_client).create_workflow_action_performer(new_create_workflow_action_performer_request)
        print("The response of WorkflowActionPerformerApi->create_workflow_action_performer:\n")
        print(results.model_dump_json(by_alias=True, indent=4))
    except Exception as e:
        print("Exception when calling WorkflowActionPerformerApi->create_workflow_action_performer: %s\n" % e)
```



[[Back to top]](#) 



