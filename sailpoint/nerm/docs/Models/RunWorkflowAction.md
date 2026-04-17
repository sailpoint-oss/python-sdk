---
id: run-workflow-action
title: RunWorkflowAction
pagination_label: RunWorkflowAction
sidebar_label: RunWorkflowAction
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'RunWorkflowAction', 'RunWorkflowAction'] 
slug: /tools/sdk/python//models/run-workflow-action
tags: ['SDK', 'Software Development Kit', 'RunWorkflowAction', 'RunWorkflowAction']
---

# RunWorkflowAction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workflow_id** | **str** | The workflow the workflow action belongs to. | [required]
**description** | **str** | The description of the workflow action. | [required]
**archived** | **bool** | If the workflow action is archived or not. | [optional] [default to False]
**configuration_attributes** | [**RunWorkflowActionConfigurationAttributes**](run-workflow-action-configuration-attributes) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.run_workflow_action import RunWorkflowAction

run_workflow_action = RunWorkflowAction(
workflow_id='33f072dd-13b4-41e1-8ea0-16f2a59b57c8',
description='Runs another workflow with the ability to pass data in between.',
archived=False,
configuration_attributes=sailpoint.nerm.models.run_workflow_action_configuration_attributes.RunWorkflowAction_configuration_attributes(
                    id = '33f072dd-13b4-41e1-8ea0-16f2a59b57c8', 
                    workflow_id = '33f072dd-13b4-41e1-8ea0-16f2a59b57c8', 
                    wait_for_completion = False, 
                    profile_to_send = 'current', 
                    return_profile = False, 
                    run_workflow_action_id = '33f072dd-13b4-41e1-8ea0-16f2a59b57c8', 
                    profile_type_id = '33f072dd-13b4-41e1-8ea0-16f2a59b57c8', )
)

```
[[Back to top]](#) 

