---
id: request-action
title: RequestAction
pagination_label: RequestAction
sidebar_label: RequestAction
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'RequestAction', 'RequestAction'] 
slug: /tools/sdk/python//models/request-action
tags: ['SDK', 'Software Development Kit', 'RequestAction', 'RequestAction']
---

# RequestAction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workflow_id** | **str** | The workflow the workflow action belongs to. | [required]
**description** | **str** | The description of the workflow action. | [required]
**page_id** | **str** | The page the workflow action should render. | [optional] 
**archived** | **bool** | If the workflow action is archived or not. | [optional] [default to False]
**requires_comment** | **bool** | If the workflow action requires a comment or not. | [optional] [default to False]
}

## Example

```python
from sailpoint.nerm.models.request_action import RequestAction

request_action = RequestAction(
workflow_id='33f072dd-13b4-41e1-8ea0-16f2a59b57c8',
description='Provides the requester a page with forms.',
page_id='33f072dd-13b4-41e1-8ea0-16f2a59b57c8',
archived=False,
requires_comment=False
)

```
[[Back to top]](#) 

