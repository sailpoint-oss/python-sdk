---
id: create-ask-security-question-action-request
title: CreateAskSecurityQuestionActionRequest
pagination_label: CreateAskSecurityQuestionActionRequest
sidebar_label: CreateAskSecurityQuestionActionRequest
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'CreateAskSecurityQuestionActionRequest', 'CreateAskSecurityQuestionActionRequest'] 
slug: /tools/sdk/python//models/create-ask-security-question-action-request
tags: ['SDK', 'Software Development Kit', 'CreateAskSecurityQuestionActionRequest', 'CreateAskSecurityQuestionActionRequest']
---

# CreateAskSecurityQuestionActionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workflow_action** | [**AskSecurityQuestionAction**](ask-security-question-action) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.create_ask_security_question_action_request import CreateAskSecurityQuestionActionRequest

create_ask_security_question_action_request = CreateAskSecurityQuestionActionRequest(
workflow_action=sailpoint.nerm.models.ask_security_question_action.AskSecurityQuestionAction(
                    workflow_id = '33f072dd-13b4-41e1-8ea0-16f2a59b57c8', 
                    description = 'Prompt the user to answer some personal security questions.', 
                    number_of_questions = 1, 
                    token_expiration = 1, 
                    token_expiration_type = 'days', 
                    archived = False, )
)

```
[[Back to top]](#) 

