---
id: ask-security-question-action
title: AskSecurityQuestionAction
pagination_label: AskSecurityQuestionAction
sidebar_label: AskSecurityQuestionAction
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'AskSecurityQuestionAction', 'AskSecurityQuestionAction'] 
slug: /tools/sdk/python//models/ask-security-question-action
tags: ['SDK', 'Software Development Kit', 'AskSecurityQuestionAction', 'AskSecurityQuestionAction']
---

# AskSecurityQuestionAction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workflow_id** | **str** | The workflow the workflow action belongs to. | [required]
**description** | **str** | The description of the workflow action. | [required]
**number_of_questions** | **int** | The number of questions the user should answer upon login. | [required]
**token_expiration** | **int** | The token expiration time, coordinates with token_expiration_type. | [required]
**token_expiration_type** |  **Enum** [  'hours',    'days',    'login attempts',    'always' ] | The token expiration type, coordinates with token_expiration. | [required]
**archived** | **bool** | If the workflow action is archived or not. | [optional] [default to False]
}

## Example

```python
from sailpoint.nerm.models.ask_security_question_action import AskSecurityQuestionAction

ask_security_question_action = AskSecurityQuestionAction(
workflow_id='33f072dd-13b4-41e1-8ea0-16f2a59b57c8',
description='Prompt the user to answer some personal security questions.',
number_of_questions=1,
token_expiration=1,
token_expiration_type='days',
archived=False
)

```
[[Back to top]](#) 

