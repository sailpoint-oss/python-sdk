---
id: create-close-session-action-request
title: CreateCloseSessionActionRequest
pagination_label: CreateCloseSessionActionRequest
sidebar_label: CreateCloseSessionActionRequest
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'CreateCloseSessionActionRequest', 'CreateCloseSessionActionRequest'] 
slug: /tools/sdk/python//models/create-close-session-action-request
tags: ['SDK', 'Software Development Kit', 'CreateCloseSessionActionRequest', 'CreateCloseSessionActionRequest']
---

# CreateCloseSessionActionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workflow_action** | [**CloseSessionAction**](close-session-action) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.create_close_session_action_request import CreateCloseSessionActionRequest

create_close_session_action_request = CreateCloseSessionActionRequest(
workflow_action=sailpoint.nerm.models.close_session_action.CloseSessionAction(
                    workflow_id = '33f072dd-13b4-41e1-8ea0-16f2a59b57c8', 
                    description = 'Closes the current workflow session.', 
                    archived = False, )
)

```
[[Back to top]](#) 

