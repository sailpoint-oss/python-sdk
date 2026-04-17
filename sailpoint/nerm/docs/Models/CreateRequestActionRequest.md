---
id: create-request-action-request
title: CreateRequestActionRequest
pagination_label: CreateRequestActionRequest
sidebar_label: CreateRequestActionRequest
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'CreateRequestActionRequest', 'CreateRequestActionRequest'] 
slug: /tools/sdk/python//models/create-request-action-request
tags: ['SDK', 'Software Development Kit', 'CreateRequestActionRequest', 'CreateRequestActionRequest']
---

# CreateRequestActionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workflow_action** | [**RequestAction**](request-action) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.create_request_action_request import CreateRequestActionRequest

create_request_action_request = CreateRequestActionRequest(
workflow_action=sailpoint.nerm.models.request_action.RequestAction(
                    workflow_id = '33f072dd-13b4-41e1-8ea0-16f2a59b57c8', 
                    description = 'Provides the requester a page with forms.', 
                    page_id = '33f072dd-13b4-41e1-8ea0-16f2a59b57c8', 
                    archived = False, 
                    requires_comment = False, )
)

```
[[Back to top]](#) 

