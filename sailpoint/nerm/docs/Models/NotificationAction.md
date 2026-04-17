---
id: notification-action
title: NotificationAction
pagination_label: NotificationAction
sidebar_label: NotificationAction
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'NotificationAction', 'NotificationAction'] 
slug: /tools/sdk/python//models/notification-action
tags: ['SDK', 'Software Development Kit', 'NotificationAction', 'NotificationAction']
---

# NotificationAction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workflow_id** | **str** | The workflow the workflow action belongs to. | [required]
**description** | **str** | The description of the workflow action. | [required]
**email_attribute_id** | **str** | The attribute storing the email address for the workflow action. | [optional] 
**email_addresses** | **[]str** | The email addresses for the workflow action. | [optional] 
**archived** | **bool** | If the workflow action is archived or not. | [optional] [default to False]
**workflow_action_email_attributes** | [**NotificationActionWorkflowActionEmailAttributes**](notification-action-workflow-action-email-attributes) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.notification_action import NotificationAction

notification_action = NotificationAction(
workflow_id='33f072dd-13b4-41e1-8ea0-16f2a59b57c8',
description='Send a notification to a group of users.',
email_attribute_id='33f072dd-13b4-41e1-8ea0-16f2a59b57c8',
email_addresses=[johndoe@gmail.com, janedoe@gmail.com],
archived=False,
workflow_action_email_attributes=sailpoint.nerm.models.notification_action_workflow_action_email_attributes.NotificationAction_workflow_action_email_attributes(
                    id = '33f072dd-13b4-41e1-8ea0-16f2a59b57c8', 
                    workflow_action_id = '33f072dd-13b4-41e1-8ea0-16f2a59b57c8', 
                    email_id = '33f072dd-13b4-41e1-8ea0-16f2a59b57c8', 
                    type = 'StandardEmail', )
)

```
[[Back to top]](#) 

