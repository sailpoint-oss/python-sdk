---
id: create-profile-action
title: CreateProfileAction
pagination_label: CreateProfileAction
sidebar_label: CreateProfileAction
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'CreateProfileAction', 'CreateProfileAction'] 
slug: /tools/sdk/python//models/create-profile-action
tags: ['SDK', 'Software Development Kit', 'CreateProfileAction', 'CreateProfileAction']
---

# CreateProfileAction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workflow_id** | **str** | The workflow the workflow action belongs to. | [required]
**description** | **str** | The description of the workflow action. | [required]
**add_requester_as_owner** | **bool** | If the requester should be added as the owner of the profile to be created. | [optional] [default to True]
**archived** | **bool** | If the workflow action is archived or not. | [optional] [default to False]
}

## Example

```python
from sailpoint.nerm.models.create_profile_action import CreateProfileAction

create_profile_action = CreateProfileAction(
workflow_id='33f072dd-13b4-41e1-8ea0-16f2a59b57c8',
description='Creates a profile with all attributes collected during the workflow.',
add_requester_as_owner=True,
archived=False
)

```
[[Back to top]](#) 

