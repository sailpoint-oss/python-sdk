---
id: create-email-verification-action-request
title: CreateEmailVerificationActionRequest
pagination_label: CreateEmailVerificationActionRequest
sidebar_label: CreateEmailVerificationActionRequest
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'CreateEmailVerificationActionRequest', 'CreateEmailVerificationActionRequest'] 
slug: /tools/sdk/python//models/create-email-verification-action-request
tags: ['SDK', 'Software Development Kit', 'CreateEmailVerificationActionRequest', 'CreateEmailVerificationActionRequest']
---

# CreateEmailVerificationActionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workflow_action** | [**EmailVerificationAction**](email-verification-action) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.create_email_verification_action_request import CreateEmailVerificationActionRequest

create_email_verification_action_request = CreateEmailVerificationActionRequest(
workflow_action=sailpoint.nerm.models.email_verification_action.EmailVerificationAction(
                    workflow_id = '33f072dd-13b4-41e1-8ea0-16f2a59b57c8', 
                    description = 'Have the user verify their email address.', 
                    email_expiration = 20, 
                    token_expiration = 1, 
                    token_expiration_type = 'days', 
                    archived = False, )
)

```
[[Back to top]](#) 

