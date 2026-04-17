---
id: create-auto-assign-action-request
title: CreateAutoAssignActionRequest
pagination_label: CreateAutoAssignActionRequest
sidebar_label: CreateAutoAssignActionRequest
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'CreateAutoAssignActionRequest', 'CreateAutoAssignActionRequest'] 
slug: /tools/sdk/python//models/create-auto-assign-action-request
tags: ['SDK', 'Software Development Kit', 'CreateAutoAssignActionRequest', 'CreateAutoAssignActionRequest']
---

# CreateAutoAssignActionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workflow_action** | [**AutoAssignAction**](auto-assign-action) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.create_auto_assign_action_request import CreateAutoAssignActionRequest

create_auto_assign_action_request = CreateAutoAssignActionRequest(
workflow_action=sailpoint.nerm.models.auto_assign_action.AutoAssignAction(
                    workflow_id = '33f072dd-13b4-41e1-8ea0-16f2a59b57c8', 
                    description = 'Automatically assigns contributors to this profile.', 
                    archived = False, 
                    contributor_attr = '33f072dd-13b4-41e1-8ea0-16f2a59b57c8', )
)

```
[[Back to top]](#) 

