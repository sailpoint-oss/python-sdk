---
id: email-verification-action
title: EmailVerificationAction
pagination_label: EmailVerificationAction
sidebar_label: EmailVerificationAction
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'EmailVerificationAction', 'EmailVerificationAction'] 
slug: /tools/sdk/python//models/email-verification-action
tags: ['SDK', 'Software Development Kit', 'EmailVerificationAction', 'EmailVerificationAction']
---

# EmailVerificationAction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workflow_id** | **str** | The workflow the workflow action belongs to. | [required]
**description** | **str** | The description of the workflow action. | [required]
**email_expiration** | **int** | The email expiration time, in minutes. | [required]
**token_expiration** | **int** | The token expiration time, coordinates with token_expiration_type. | [required]
**token_expiration_type** |  **Enum** [  'hours',    'days',    'login attempts',    'always' ] | The token expiration type, coordinates with token_expiration. | [required]
**archived** | **bool** | If the workflow action is archived or not. | [optional] [default to False]
}

## Example

```python
from sailpoint.nerm.models.email_verification_action import EmailVerificationAction

email_verification_action = EmailVerificationAction(
workflow_id='33f072dd-13b4-41e1-8ea0-16f2a59b57c8',
description='Have the user verify their email address.',
email_expiration=20,
token_expiration=1,
token_expiration_type='days',
archived=False
)

```
[[Back to top]](#) 

