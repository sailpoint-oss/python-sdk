---
id: v2024-task-status-message
title: TaskStatusMessage
pagination_label: TaskStatusMessage
sidebar_label: TaskStatusMessage
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'TaskStatusMessage', 'V2024TaskStatusMessage'] 
slug: /tools/sdk/python/v2024/models/task-status-message
tags: ['SDK', 'Software Development Kit', 'TaskStatusMessage', 'V2024TaskStatusMessage']
---

# TaskStatusMessage

TaskStatus Message

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** |  **Enum** [  'INFO',    'WARN',    'ERROR' ] | Type of the message | [required]
**localized_text** | [**LocalizedMessage**](localized-message) |  | [required]
**key** | **str** | Key of the message | [required]
**parameters** | [**[]TaskStatusMessageParametersInner**](task-status-message-parameters-inner) | Message parameters for internationalization | [required]
}

## Example

```python
from sailpoint.v2024.models.task_status_message import TaskStatusMessage

task_status_message = TaskStatusMessage(
type='INFO',
localized_text=sailpoint.v2024.models.localized_message.LocalizedMessage(
                    locale = 'An error has occurred!', 
                    message = 'Error has occurred!', ),
key='akey',
parameters=[{name=value}]
)

```
[[Back to top]](#) 

