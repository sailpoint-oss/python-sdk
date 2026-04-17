---
id: auto-assign-action
title: AutoAssignAction
pagination_label: AutoAssignAction
sidebar_label: AutoAssignAction
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'AutoAssignAction', 'AutoAssignAction'] 
slug: /tools/sdk/python//models/auto-assign-action
tags: ['SDK', 'Software Development Kit', 'AutoAssignAction', 'AutoAssignAction']
---

# AutoAssignAction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workflow_id** | **str** | The workflow the workflow action belongs to. | [required]
**description** | **str** | The description of the workflow action. | [required]
**archived** | **bool** | If the workflow action is archived or not. | [optional] [default to False]
**contributor_attr** | **str** | The id of the contributor attribute for contributors from another profile. If workflow_action_roles are not associated to this object, this is required. | [optional] 
}

## Example

```python
from sailpoint.nerm.models.auto_assign_action import AutoAssignAction

auto_assign_action = AutoAssignAction(
workflow_id='33f072dd-13b4-41e1-8ea0-16f2a59b57c8',
description='Automatically assigns contributors to this profile.',
archived=False,
contributor_attr='33f072dd-13b4-41e1-8ea0-16f2a59b57c8'
)

```
[[Back to top]](#) 

