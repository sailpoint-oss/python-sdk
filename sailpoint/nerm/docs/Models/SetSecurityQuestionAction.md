---
id: set-security-question-action
title: SetSecurityQuestionAction
pagination_label: SetSecurityQuestionAction
sidebar_label: SetSecurityQuestionAction
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'SetSecurityQuestionAction', 'SetSecurityQuestionAction'] 
slug: /tools/sdk/python//models/set-security-question-action
tags: ['SDK', 'Software Development Kit', 'SetSecurityQuestionAction', 'SetSecurityQuestionAction']
---

# SetSecurityQuestionAction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workflow_id** | **str** | The workflow the workflow action belongs to. | [required]
**description** | **str** | The description of the workflow action. | [required]
**archived** | **bool** | If the workflow action is archived or not. | [optional] [default to False]
**number_of_questions** | **int** | The number of questions the user should answer upon login. | [required]
}

## Example

```python
from sailpoint.nerm.models.set_security_question_action import SetSecurityQuestionAction

set_security_question_action = SetSecurityQuestionAction(
workflow_id='33f072dd-13b4-41e1-8ea0-16f2a59b57c8',
description='Prompt the user to provide some personal security questions and answers.',
archived=False,
number_of_questions=1
)

```
[[Back to top]](#) 

