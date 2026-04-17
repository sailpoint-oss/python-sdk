---
id: unassign-action
title: UnassignAction
pagination_label: UnassignAction
sidebar_label: UnassignAction
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'UnassignAction', 'UnassignAction'] 
slug: /tools/sdk/python//models/unassign-action
tags: ['SDK', 'Software Development Kit', 'UnassignAction', 'UnassignAction']
---

# UnassignAction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workflow_id** | **str** | The workflow the workflow action belongs to. | [required]
**description** | **str** | The description of the workflow action. | [required]
**archived** | **bool** | If the workflow action is archived or not. | [optional] [default to False]
}

## Example

```python
from sailpoint.nerm.models.unassign_action import UnassignAction

unassign_action = UnassignAction(
workflow_id='33f072dd-13b4-41e1-8ea0-16f2a59b57c8',
description='Un-assigns roles from a profile.',
archived=False
)

```
[[Back to top]](#) 

