---
id: create-username-password-action-request
title: CreateUsernamePasswordActionRequest
pagination_label: CreateUsernamePasswordActionRequest
sidebar_label: CreateUsernamePasswordActionRequest
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'CreateUsernamePasswordActionRequest', 'CreateUsernamePasswordActionRequest'] 
slug: /tools/sdk/python//models/create-username-password-action-request
tags: ['SDK', 'Software Development Kit', 'CreateUsernamePasswordActionRequest', 'CreateUsernamePasswordActionRequest']
---

# CreateUsernamePasswordActionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workflow_action** | [**UsernamePasswordAction**](username-password-action) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.create_username_password_action_request import CreateUsernamePasswordActionRequest

create_username_password_action_request = CreateUsernamePasswordActionRequest(
workflow_action=sailpoint.nerm.models.username_password_action.UsernamePasswordAction(
                    workflow_id = '33f072dd-13b4-41e1-8ea0-16f2a59b57c8', 
                    description = 'Prompt the user for their username and password.', 
                    archived = False, )
)

```
[[Back to top]](#) 

