---
id: invitation-action-workflow-action-email-attributes
title: InvitationActionWorkflowActionEmailAttributes
pagination_label: InvitationActionWorkflowActionEmailAttributes
sidebar_label: InvitationActionWorkflowActionEmailAttributes
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'InvitationActionWorkflowActionEmailAttributes', 'InvitationActionWorkflowActionEmailAttributes'] 
slug: /tools/sdk/python//models/invitation-action-workflow-action-email-attributes
tags: ['SDK', 'Software Development Kit', 'InvitationActionWorkflowActionEmailAttributes', 'InvitationActionWorkflowActionEmailAttributes']
---

# InvitationActionWorkflowActionEmailAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | the id. | [optional] 
**workflow_action_id** | **str** | the id of the workflow action. | [optional] 
**email_id** | **str** | the id of the email. | [optional] 
**type** |  **Enum** [  'StandardEmail',    'PerformerNotificationEmail',    'ApprovalEmail',    'RejectionEmail' ] | the type of email. | [optional] 
}

## Example

```python
from sailpoint.nerm.models.invitation_action_workflow_action_email_attributes import InvitationActionWorkflowActionEmailAttributes

invitation_action_workflow_action_email_attributes = InvitationActionWorkflowActionEmailAttributes(
id='33f072dd-13b4-41e1-8ea0-16f2a59b57c8',
workflow_action_id='33f072dd-13b4-41e1-8ea0-16f2a59b57c8',
email_id='33f072dd-13b4-41e1-8ea0-16f2a59b57c8',
type='StandardEmail'
)

```
[[Back to top]](#) 

