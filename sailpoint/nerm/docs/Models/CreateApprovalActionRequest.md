---
id: create-approval-action-request
title: CreateApprovalActionRequest
pagination_label: CreateApprovalActionRequest
sidebar_label: CreateApprovalActionRequest
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'CreateApprovalActionRequest', 'CreateApprovalActionRequest'] 
slug: /tools/sdk/python//models/create-approval-action-request
tags: ['SDK', 'Software Development Kit', 'CreateApprovalActionRequest', 'CreateApprovalActionRequest']
---

# CreateApprovalActionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workflow_action** | [**ApprovalAction**](approval-action) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.create_approval_action_request import CreateApprovalActionRequest

create_approval_action_request = CreateApprovalActionRequest(
workflow_action=sailpoint.nerm.models.approval_action.ApprovalAction(
                    workflow_id = '33f072dd-13b4-41e1-8ea0-16f2a59b57c8', 
                    description = 'Require approval from another user or a group of users with a specific role.', 
                    page_id = '33f072dd-13b4-41e1-8ea0-16f2a59b57c8', 
                    archived = False, 
                    skippable = False, 
                    requires_comment = False, )
)

```
[[Back to top]](#) 

