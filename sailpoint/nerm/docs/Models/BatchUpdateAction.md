---
id: batch-update-action
title: BatchUpdateAction
pagination_label: BatchUpdateAction
sidebar_label: BatchUpdateAction
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'BatchUpdateAction', 'BatchUpdateAction'] 
slug: /tools/sdk/python//models/batch-update-action
tags: ['SDK', 'Software Development Kit', 'BatchUpdateAction', 'BatchUpdateAction']
---

# BatchUpdateAction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workflow_id** | **str** | The workflow the workflow action belongs to. | [required]
**description** | **str** | The description of the workflow action. | [required]
**archived** | **bool** | If the workflow action is archived or not. | [optional] [default to False]
}

## Example

```python
from sailpoint.nerm.models.batch_update_action import BatchUpdateAction

batch_update_action = BatchUpdateAction(
workflow_id='33f072dd-13b4-41e1-8ea0-16f2a59b57c8',
description='Updates a batch of profiles with all attributes collected during the workflow.',
archived=False
)

```
[[Back to top]](#) 

