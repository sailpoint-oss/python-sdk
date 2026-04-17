---
id: create-update-workflow-request
title: CreateUpdateWorkflowRequest
pagination_label: CreateUpdateWorkflowRequest
sidebar_label: CreateUpdateWorkflowRequest
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'CreateUpdateWorkflowRequest', 'CreateUpdateWorkflowRequest'] 
slug: /tools/sdk/python//models/create-update-workflow-request
tags: ['SDK', 'Software Development Kit', 'CreateUpdateWorkflowRequest', 'CreateUpdateWorkflowRequest']
---

# CreateUpdateWorkflowRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workflow** | [**UpdateWorkflow**](update-workflow) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.create_update_workflow_request import CreateUpdateWorkflowRequest

create_update_workflow_request = CreateUpdateWorkflowRequest(
workflow=sailpoint.nerm.models.update_workflow.UpdateWorkflow(
                    profile_type_id = '33f072dd-13b4-41e1-8ea0-16f2a59b57c8', 
                    status = 'Enabled', 
                    uid = 'my_uid', 
                    name = 'my_workflow', 
                    profile_status = 'active', 
                    disable_failure_email_notifications = False, )
)

```
[[Back to top]](#) 

