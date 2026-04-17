---
id: status-change-action
title: StatusChangeAction
pagination_label: StatusChangeAction
sidebar_label: StatusChangeAction
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'StatusChangeAction', 'StatusChangeAction'] 
slug: /tools/sdk/python//models/status-change-action
tags: ['SDK', 'Software Development Kit', 'StatusChangeAction', 'StatusChangeAction']
---

# StatusChangeAction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workflow_id** | **str** | The workflow the workflow action belongs to. | [required]
**description** | **str** | The description of the workflow action. | [required]
**new_status** |  **Enum** [  'Active',    'Inactive',    'On Leave',    'Terminated' ] | The new status for the Status Change workflow action. | [optional] 
**archived** | **bool** | If the workflow action is archived or not. | [optional] [default to False]
}

## Example

```python
from sailpoint.nerm.models.status_change_action import StatusChangeAction

status_change_action = StatusChangeAction(
workflow_id='33f072dd-13b4-41e1-8ea0-16f2a59b57c8',
description='Changes the status of a non-employee.',
new_status='Active',
archived=False
)

```
[[Back to top]](#) 

