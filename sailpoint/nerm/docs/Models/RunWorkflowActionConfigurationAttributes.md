---
id: run-workflow-action-configuration-attributes
title: RunWorkflowActionConfigurationAttributes
pagination_label: RunWorkflowActionConfigurationAttributes
sidebar_label: RunWorkflowActionConfigurationAttributes
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'RunWorkflowActionConfigurationAttributes', 'RunWorkflowActionConfigurationAttributes'] 
slug: /tools/sdk/python//models/run-workflow-action-configuration-attributes
tags: ['SDK', 'Software Development Kit', 'RunWorkflowActionConfigurationAttributes', 'RunWorkflowActionConfigurationAttributes']
---

# RunWorkflowActionConfigurationAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | the id. | [optional] 
**workflow_id** | **str** | the id of the workflow. | [optional] 
**wait_for_completion** | **bool** | If the parent workflow should wait for the child to complete. | [optional] 
**profile_to_send** |  **Enum** [  'none',    'current',    'attribute',    'profile_type' ] | the profile the parent should send to the child workflow. | [optional] 
**return_profile** | **bool** | if the child workflow should return a profile. | [optional] 
**run_workflow_action_id** | **str** | the id of the child workflow to run. | [optional] 
**profile_type_id** | **str** | the id of the profile type. | [optional] 
}

## Example

```python
from sailpoint.nerm.models.run_workflow_action_configuration_attributes import RunWorkflowActionConfigurationAttributes

run_workflow_action_configuration_attributes = RunWorkflowActionConfigurationAttributes(
id='33f072dd-13b4-41e1-8ea0-16f2a59b57c8',
workflow_id='33f072dd-13b4-41e1-8ea0-16f2a59b57c8',
wait_for_completion=False,
profile_to_send='current',
return_profile=False,
run_workflow_action_id='33f072dd-13b4-41e1-8ea0-16f2a59b57c8',
profile_type_id='33f072dd-13b4-41e1-8ea0-16f2a59b57c8'
)

```
[[Back to top]](#) 

