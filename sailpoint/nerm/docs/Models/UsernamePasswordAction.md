---
id: username-password-action
title: UsernamePasswordAction
pagination_label: UsernamePasswordAction
sidebar_label: UsernamePasswordAction
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'UsernamePasswordAction', 'UsernamePasswordAction'] 
slug: /tools/sdk/python//models/username-password-action
tags: ['SDK', 'Software Development Kit', 'UsernamePasswordAction', 'UsernamePasswordAction']
---

# UsernamePasswordAction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workflow_id** | **str** | The workflow the workflow action belongs to. | [required]
**description** | **str** | The description of the workflow action. | [required]
**archived** | **bool** | If the workflow action is archived or not. | [optional] [default to False]
}

## Example

```python
from sailpoint.nerm.models.username_password_action import UsernamePasswordAction

username_password_action = UsernamePasswordAction(
workflow_id='33f072dd-13b4-41e1-8ea0-16f2a59b57c8',
description='Prompt the user for their username and password.',
archived=False
)

```
[[Back to top]](#) 

