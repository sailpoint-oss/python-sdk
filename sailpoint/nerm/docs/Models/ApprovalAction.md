---
id: approval-action
title: ApprovalAction
pagination_label: ApprovalAction
sidebar_label: ApprovalAction
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'ApprovalAction', 'ApprovalAction'] 
slug: /tools/sdk/python//models/approval-action
tags: ['SDK', 'Software Development Kit', 'ApprovalAction', 'ApprovalAction']
---

# ApprovalAction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workflow_id** | **str** | The workflow the workflow action belongs to. | [required]
**description** | **str** | The description of the workflow action. | [optional] 
**page_id** | **str** | The page the workflow action should render. | [required]
**archived** | **bool** | If the workflow action is archived or not. | [optional] [default to False]
**skippable** | **bool** | If the workflow action is skippable or not. | [optional] [default to False]
**requires_comment** | **bool** | If the workflow action requires a comment or not. | [optional] [default to False]
}

## Example

```python
from sailpoint.nerm.models.approval_action import ApprovalAction

approval_action = ApprovalAction(
workflow_id='33f072dd-13b4-41e1-8ea0-16f2a59b57c8',
description='Require approval from another user or a group of users with a specific role.',
page_id='33f072dd-13b4-41e1-8ea0-16f2a59b57c8',
archived=False,
skippable=False,
requires_comment=False
)

```
[[Back to top]](#) 

