---
id: create-status-change-action-request
title: CreateStatusChangeActionRequest
pagination_label: CreateStatusChangeActionRequest
sidebar_label: CreateStatusChangeActionRequest
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'CreateStatusChangeActionRequest', 'CreateStatusChangeActionRequest'] 
slug: /tools/sdk/python//models/create-status-change-action-request
tags: ['SDK', 'Software Development Kit', 'CreateStatusChangeActionRequest', 'CreateStatusChangeActionRequest']
---

# CreateStatusChangeActionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workflow_action** | [**StatusChangeAction**](status-change-action) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.create_status_change_action_request import CreateStatusChangeActionRequest

create_status_change_action_request = CreateStatusChangeActionRequest(
workflow_action=sailpoint.nerm.models.status_change_action.StatusChangeAction(
                    workflow_id = '33f072dd-13b4-41e1-8ea0-16f2a59b57c8', 
                    description = 'Changes the status of a non-employee.', 
                    new_status = 'Active', 
                    archived = False, )
)

```
[[Back to top]](#) 

