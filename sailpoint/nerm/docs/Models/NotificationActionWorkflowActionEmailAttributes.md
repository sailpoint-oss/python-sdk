---
id: notification-action-workflow-action-email-attributes
title: NotificationActionWorkflowActionEmailAttributes
pagination_label: NotificationActionWorkflowActionEmailAttributes
sidebar_label: NotificationActionWorkflowActionEmailAttributes
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'NotificationActionWorkflowActionEmailAttributes', 'NotificationActionWorkflowActionEmailAttributes'] 
slug: /tools/sdk/python//models/notification-action-workflow-action-email-attributes
tags: ['SDK', 'Software Development Kit', 'NotificationActionWorkflowActionEmailAttributes', 'NotificationActionWorkflowActionEmailAttributes']
---

# NotificationActionWorkflowActionEmailAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | the id. | [optional] 
**workflow_action_id** | **str** | the id of the workflow action. | [optional] 
**email_id** | **str** | the id of the email. | [optional] 
**type** |  **Enum** [  'StandardEmail' ] | the type of email. | [optional] 
}

## Example

```python
from sailpoint.nerm.models.notification_action_workflow_action_email_attributes import NotificationActionWorkflowActionEmailAttributes

notification_action_workflow_action_email_attributes = NotificationActionWorkflowActionEmailAttributes(
id='33f072dd-13b4-41e1-8ea0-16f2a59b57c8',
workflow_action_id='33f072dd-13b4-41e1-8ea0-16f2a59b57c8',
email_id='33f072dd-13b4-41e1-8ea0-16f2a59b57c8',
type='StandardEmail'
)

```
[[Back to top]](#) 

