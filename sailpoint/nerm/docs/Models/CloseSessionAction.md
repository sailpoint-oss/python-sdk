---
id: close-session-action
title: CloseSessionAction
pagination_label: CloseSessionAction
sidebar_label: CloseSessionAction
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'CloseSessionAction', 'CloseSessionAction'] 
slug: /tools/sdk/python//models/close-session-action
tags: ['SDK', 'Software Development Kit', 'CloseSessionAction', 'CloseSessionAction']
---

# CloseSessionAction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workflow_id** | **str** | The workflow the workflow action belongs to. | [required]
**description** | **str** | The description of the workflow action. | [required]
**archived** | **bool** | If the workflow action is archived or not. | [optional] [default to False]
}

## Example

```python
from sailpoint.nerm.models.close_session_action import CloseSessionAction

close_session_action = CloseSessionAction(
workflow_id='33f072dd-13b4-41e1-8ea0-16f2a59b57c8',
description='Closes the current workflow session.',
archived=False
)

```
[[Back to top]](#) 

