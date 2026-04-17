---
id: create-notification-action-request
title: CreateNotificationActionRequest
pagination_label: CreateNotificationActionRequest
sidebar_label: CreateNotificationActionRequest
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'CreateNotificationActionRequest', 'CreateNotificationActionRequest'] 
slug: /tools/sdk/python//models/create-notification-action-request
tags: ['SDK', 'Software Development Kit', 'CreateNotificationActionRequest', 'CreateNotificationActionRequest']
---

# CreateNotificationActionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workflow_action** | [**NotificationAction**](notification-action) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.create_notification_action_request import CreateNotificationActionRequest

create_notification_action_request = CreateNotificationActionRequest(
workflow_action=sailpoint.nerm.models.notification_action.NotificationAction(
                    workflow_id = '33f072dd-13b4-41e1-8ea0-16f2a59b57c8', 
                    description = 'Send a notification to a group of users.', 
                    email_attribute_id = '33f072dd-13b4-41e1-8ea0-16f2a59b57c8', 
                    email_addresses = [johndoe@gmail.com, janedoe@gmail.com], 
                    archived = False, 
                    workflow_action_email_attributes = sailpoint.nerm.models.notification_action_workflow_action_email_attributes.NotificationAction_workflow_action_email_attributes(
                        id = '33f072dd-13b4-41e1-8ea0-16f2a59b57c8', 
                        workflow_action_id = '33f072dd-13b4-41e1-8ea0-16f2a59b57c8', 
                        email_id = '33f072dd-13b4-41e1-8ea0-16f2a59b57c8', 
                        type = 'StandardEmail', ), )
)

```
[[Back to top]](#) 

