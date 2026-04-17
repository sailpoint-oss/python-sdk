---
id: password-reset-action
title: PasswordResetAction
pagination_label: PasswordResetAction
sidebar_label: PasswordResetAction
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'PasswordResetAction', 'PasswordResetAction'] 
slug: /tools/sdk/python//models/password-reset-action
tags: ['SDK', 'Software Development Kit', 'PasswordResetAction', 'PasswordResetAction']
---

# PasswordResetAction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workflow_id** | **str** | The workflow the workflow action belongs to. | [required]
**description** | **str** | The description of the workflow action. | [required]
**archived** | **bool** | If the workflow action is archived or not. | [optional] [default to False]
}

## Example

```python
from sailpoint.nerm.models.password_reset_action import PasswordResetAction

password_reset_action = PasswordResetAction(
workflow_id='33f072dd-13b4-41e1-8ea0-16f2a59b57c8',
description='Prompt the user to reset their password.',
archived=False
)

```
[[Back to top]](#) 

