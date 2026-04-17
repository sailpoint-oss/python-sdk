---
id: create-create-workflow-request
title: CreateCreateWorkflowRequest
pagination_label: CreateCreateWorkflowRequest
sidebar_label: CreateCreateWorkflowRequest
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'CreateCreateWorkflowRequest', 'CreateCreateWorkflowRequest'] 
slug: /tools/sdk/python//models/create-create-workflow-request
tags: ['SDK', 'Software Development Kit', 'CreateCreateWorkflowRequest', 'CreateCreateWorkflowRequest']
---

# CreateCreateWorkflowRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workflow** | [**CreateWorkflow**](create-workflow) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.create_create_workflow_request import CreateCreateWorkflowRequest

create_create_workflow_request = CreateCreateWorkflowRequest(
workflow=sailpoint.nerm.models.create_workflow.CreateWorkflow(
                    profile_type_id = '33f072dd-13b4-41e1-8ea0-16f2a59b57c8', 
                    status = 'Enabled', 
                    uid = 'my_uid', 
                    name = 'my_workflow', 
                    disable_failure_email_notifications = False, )
)

```
[[Back to top]](#) 

