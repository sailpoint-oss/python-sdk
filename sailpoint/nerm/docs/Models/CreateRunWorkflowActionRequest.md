---
id: create-run-workflow-action-request
title: CreateRunWorkflowActionRequest
pagination_label: CreateRunWorkflowActionRequest
sidebar_label: CreateRunWorkflowActionRequest
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'CreateRunWorkflowActionRequest', 'CreateRunWorkflowActionRequest'] 
slug: /tools/sdk/python//models/create-run-workflow-action-request
tags: ['SDK', 'Software Development Kit', 'CreateRunWorkflowActionRequest', 'CreateRunWorkflowActionRequest']
---

# CreateRunWorkflowActionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workflow_action** | [**RunWorkflowAction**](run-workflow-action) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.create_run_workflow_action_request import CreateRunWorkflowActionRequest

create_run_workflow_action_request = CreateRunWorkflowActionRequest(
workflow_action=sailpoint.nerm.models.run_workflow_action.RunWorkflowAction(
                    workflow_id = '33f072dd-13b4-41e1-8ea0-16f2a59b57c8', 
                    description = 'Runs another workflow with the ability to pass data in between.', 
                    archived = False, 
                    configuration_attributes = sailpoint.nerm.models.run_workflow_action_configuration_attributes.RunWorkflowAction_configuration_attributes(
                        id = '33f072dd-13b4-41e1-8ea0-16f2a59b57c8', 
                        workflow_id = '33f072dd-13b4-41e1-8ea0-16f2a59b57c8', 
                        wait_for_completion = False, 
                        profile_to_send = 'current', 
                        return_profile = False, 
                        run_workflow_action_id = '33f072dd-13b4-41e1-8ea0-16f2a59b57c8', 
                        profile_type_id = '33f072dd-13b4-41e1-8ea0-16f2a59b57c8', ), )
)

```
[[Back to top]](#) 

