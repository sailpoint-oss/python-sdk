---
id: profile-check-action
title: ProfileCheckAction
pagination_label: ProfileCheckAction
sidebar_label: ProfileCheckAction
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'ProfileCheckAction', 'ProfileCheckAction'] 
slug: /tools/sdk/python//models/profile-check-action
tags: ['SDK', 'Software Development Kit', 'ProfileCheckAction', 'ProfileCheckAction']
---

# ProfileCheckAction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workflow_id** | **str** | The workflow the workflow action belongs to. | [required]
**description** | **str** | The description of the workflow action. | [required]
**archived** | **bool** | If the workflow action is archived or not. | [optional] [default to False]
**ne_attribute_ids** | **[]str** | An array of ne_attribute_ids. | [optional] 
**handle_type** |  **Enum** [  'session',    'attribute' ] | The handle type for what should happen if an existing profile is found. | [optional] 
**handle_id** | **str** | The handle id.  When handle type is session, this is the session id. | [optional] 
}

## Example

```python
from sailpoint.nerm.models.profile_check_action import ProfileCheckAction

profile_check_action = ProfileCheckAction(
workflow_id='33f072dd-13b4-41e1-8ea0-16f2a59b57c8',
description='Finds a profile based on selected attributes and values found in the session.',
archived=False,
ne_attribute_ids=[33f072dd-13b4-41e1-8ea0-16f2a59b57c8],
handle_type='session',
handle_id='33f072dd-13b4-41e1-8ea0-16f2a59b57c8'
)

```
[[Back to top]](#) 

