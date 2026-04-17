---
id: create-password-reset-action-request
title: CreatePasswordResetActionRequest
pagination_label: CreatePasswordResetActionRequest
sidebar_label: CreatePasswordResetActionRequest
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'CreatePasswordResetActionRequest', 'CreatePasswordResetActionRequest'] 
slug: /tools/sdk/python//models/create-password-reset-action-request
tags: ['SDK', 'Software Development Kit', 'CreatePasswordResetActionRequest', 'CreatePasswordResetActionRequest']
---

# CreatePasswordResetActionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workflow_action** | [**PasswordResetAction**](password-reset-action) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.create_password_reset_action_request import CreatePasswordResetActionRequest

create_password_reset_action_request = CreatePasswordResetActionRequest(
workflow_action=sailpoint.nerm.models.password_reset_action.PasswordResetAction(
                    workflow_id = '33f072dd-13b4-41e1-8ea0-16f2a59b57c8', 
                    description = 'Prompt the user to reset their password.', 
                    archived = False, )
)

```
[[Back to top]](#) 

