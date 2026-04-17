---
id: create-set-security-question-action-request
title: CreateSetSecurityQuestionActionRequest
pagination_label: CreateSetSecurityQuestionActionRequest
sidebar_label: CreateSetSecurityQuestionActionRequest
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'CreateSetSecurityQuestionActionRequest', 'CreateSetSecurityQuestionActionRequest'] 
slug: /tools/sdk/python//models/create-set-security-question-action-request
tags: ['SDK', 'Software Development Kit', 'CreateSetSecurityQuestionActionRequest', 'CreateSetSecurityQuestionActionRequest']
---

# CreateSetSecurityQuestionActionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workflow_action** | [**SetSecurityQuestionAction**](set-security-question-action) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.create_set_security_question_action_request import CreateSetSecurityQuestionActionRequest

create_set_security_question_action_request = CreateSetSecurityQuestionActionRequest(
workflow_action=sailpoint.nerm.models.set_security_question_action.SetSecurityQuestionAction(
                    workflow_id = '33f072dd-13b4-41e1-8ea0-16f2a59b57c8', 
                    description = 'Prompt the user to provide some personal security questions and answers.', 
                    archived = False, 
                    number_of_questions = 1, )
)

```
[[Back to top]](#) 

