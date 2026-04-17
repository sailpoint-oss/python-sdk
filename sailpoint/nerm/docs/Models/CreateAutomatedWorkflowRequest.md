---
id: create-automated-workflow-request
title: CreateAutomatedWorkflowRequest
pagination_label: CreateAutomatedWorkflowRequest
sidebar_label: CreateAutomatedWorkflowRequest
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'CreateAutomatedWorkflowRequest', 'CreateAutomatedWorkflowRequest'] 
slug: /tools/sdk/python//models/create-automated-workflow-request
tags: ['SDK', 'Software Development Kit', 'CreateAutomatedWorkflowRequest', 'CreateAutomatedWorkflowRequest']
---

# CreateAutomatedWorkflowRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workflow** | [**AutomatedWorkflow**](automated-workflow) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.create_automated_workflow_request import CreateAutomatedWorkflowRequest

create_automated_workflow_request = CreateAutomatedWorkflowRequest(
workflow=sailpoint.nerm.models.automated_workflow.AutomatedWorkflow(
                    profile_type_id = '33f072dd-13b4-41e1-8ea0-16f2a59b57c8', 
                    status = 'Enabled', 
                    uid = 'my_uid', 
                    name = 'my_workflow', 
                    disable_failure_email_notifications = False, 
                    condition_rules_attributes = [{type=ProfileTypeRule, condition_object_type=DateAttribute, comparison_operator===, logical_operator=AND, value=true}], )
)

```
[[Back to top]](#) 

