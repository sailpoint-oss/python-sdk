---
id: profile-select-action
title: ProfileSelectAction
pagination_label: ProfileSelectAction
sidebar_label: ProfileSelectAction
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'ProfileSelectAction', 'ProfileSelectAction'] 
slug: /tools/sdk/python//models/profile-select-action
tags: ['SDK', 'Software Development Kit', 'ProfileSelectAction', 'ProfileSelectAction']
---

# ProfileSelectAction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workflow_id** | **str** | The workflow the workflow action belongs to. | [required]
**description** | **str** | The description of the workflow action. | [required]
**archived** | **bool** | If the workflow action is archived or not. | [optional] [default to False]
}

## Example

```python
from sailpoint.nerm.models.profile_select_action import ProfileSelectAction

profile_select_action = ProfileSelectAction(
workflow_id='33f072dd-13b4-41e1-8ea0-16f2a59b57c8',
description='Select the profiles that you want to run this workflow for.',
archived=False
)

```
[[Back to top]](#) 

