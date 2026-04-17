---
id: create-unassign-action-request
title: CreateUnassignActionRequest
pagination_label: CreateUnassignActionRequest
sidebar_label: CreateUnassignActionRequest
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'CreateUnassignActionRequest', 'CreateUnassignActionRequest'] 
slug: /tools/sdk/python//models/create-unassign-action-request
tags: ['SDK', 'Software Development Kit', 'CreateUnassignActionRequest', 'CreateUnassignActionRequest']
---

# CreateUnassignActionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workflow_action** | [**UnassignAction**](unassign-action) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.create_unassign_action_request import CreateUnassignActionRequest

create_unassign_action_request = CreateUnassignActionRequest(
workflow_action=sailpoint.nerm.models.unassign_action.UnassignAction(
                    workflow_id = '33f072dd-13b4-41e1-8ea0-16f2a59b57c8', 
                    description = 'Un-assigns roles from a profile.', 
                    archived = False, )
)

```
[[Back to top]](#) 

