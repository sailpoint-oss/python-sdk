---
id: workflow-action
title: WorkflowAction
pagination_label: WorkflowAction
sidebar_label: WorkflowAction
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'WorkflowAction', 'WorkflowAction'] 
slug: /tools/sdk/python//models/workflow-action
tags: ['SDK', 'Software Development Kit', 'WorkflowAction', 'WorkflowAction']
---

# WorkflowAction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workflow_id** | **str** | The workflow the workflow action belongs to. | [required]
**description** | **str** | The description of the workflow action. | [optional] 
**page_id** | **str** | The page the workflow action should render. | [required]
**add_requester_as_owner** | **bool** | If the requester should be added as the owner of the profile to be created. | [optional] [default to True]
**email_attribute_id** | **str** | The attribute storing the email address for the workflow action. | [optional] 
**email_addresses** | **[]str** | The email addresses for the workflow action. | [optional] 
**new_status** | **str** | The new status for the Status Change workflow action. | [optional] 
**archived** | **bool** | If the workflow action is archived or not. | [optional] [default to False]
**skippable** | **bool** | If the workflow action is skippable or not. | [optional] [default to False]
**requires_comment** | **bool** | If the workflow action requires a comment or not. | [optional] [default to False]
}

## Example

```python
from sailpoint.nerm.models.workflow_action import WorkflowAction

workflow_action = WorkflowAction(
workflow_id='33f072dd-13b4-41e1-8ea0-16f2a59b57c8',
description='Require approval from another user or a group of users with a specific role.',
page_id='33f072dd-13b4-41e1-8ea0-16f2a59b57c8',
add_requester_as_owner=True,
email_attribute_id='33f072dd-13b4-41e1-8ea0-16f2a59b57c8',
email_addresses=[johndoe@gmail.com, janedoe@gmail.com],
new_status='Active, Inactive, On Leave, Terminated',
archived=False,
skippable=False,
requires_comment=False
)

```
[[Back to top]](#) 

