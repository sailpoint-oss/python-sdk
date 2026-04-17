---
id: update-profile-action
title: UpdateProfileAction
pagination_label: UpdateProfileAction
sidebar_label: UpdateProfileAction
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'UpdateProfileAction', 'UpdateProfileAction'] 
slug: /tools/sdk/python//models/update-profile-action
tags: ['SDK', 'Software Development Kit', 'UpdateProfileAction', 'UpdateProfileAction']
---

# UpdateProfileAction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workflow_id** | **str** | The workflow the workflow action belongs to. | [required]
**description** | **str** | The description of the workflow action. | [required]
**archived** | **bool** | If the workflow action is archived or not. | [optional] [default to False]
}

## Example

```python
from sailpoint.nerm.models.update_profile_action import UpdateProfileAction

update_profile_action = UpdateProfileAction(
workflow_id='33f072dd-13b4-41e1-8ea0-16f2a59b57c8',
description='Updates a profile with all attributes collected during the workflow.',
archived=False
)

```
[[Back to top]](#) 

