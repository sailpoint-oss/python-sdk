---
id: set-attributes-action
title: SetAttributesAction
pagination_label: SetAttributesAction
sidebar_label: SetAttributesAction
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'SetAttributesAction', 'SetAttributesAction'] 
slug: /tools/sdk/python//models/set-attributes-action
tags: ['SDK', 'Software Development Kit', 'SetAttributesAction', 'SetAttributesAction']
---

# SetAttributesAction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workflow_id** | **str** | The workflow the workflow action belongs to. | [required]
**description** | **str** | The description of the workflow action. | [required]
**archived** | **bool** | If the workflow action is archived or not. | [optional] [default to False]
}

## Example

```python
from sailpoint.nerm.models.set_attributes_action import SetAttributesAction

set_attributes_action = SetAttributesAction(
workflow_id='33f072dd-13b4-41e1-8ea0-16f2a59b57c8',
description='Set attribute(s) to a specific value.',
archived=False
)

```
[[Back to top]](#) 

