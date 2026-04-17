---
id: review-action
title: ReviewAction
pagination_label: ReviewAction
sidebar_label: ReviewAction
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'ReviewAction', 'ReviewAction'] 
slug: /tools/sdk/python//models/review-action
tags: ['SDK', 'Software Development Kit', 'ReviewAction', 'ReviewAction']
---

# ReviewAction


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
from sailpoint.nerm.models.review_action import ReviewAction

review_action = ReviewAction(
workflow_id='33f072dd-13b4-41e1-8ea0-16f2a59b57c8',
description='Allows the requester to review.',
page_id='33f072dd-13b4-41e1-8ea0-16f2a59b57c8',
archived=False,
requires_comment=False
)

```
[[Back to top]](#) 

