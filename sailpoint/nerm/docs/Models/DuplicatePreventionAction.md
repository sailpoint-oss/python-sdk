---
id: duplicate-prevention-action
title: DuplicatePreventionAction
pagination_label: DuplicatePreventionAction
sidebar_label: DuplicatePreventionAction
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'DuplicatePreventionAction', 'DuplicatePreventionAction'] 
slug: /tools/sdk/python//models/duplicate-prevention-action
tags: ['SDK', 'Software Development Kit', 'DuplicatePreventionAction', 'DuplicatePreventionAction']
---

# DuplicatePreventionAction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workflow_id** | **str** | The workflow the workflow action belongs to. | [required]
**description** | **str** | The description of the workflow action. | [required]
**search_scope** |  **Enum** [  'all',    'current' ] | The search scope of the profiles to check against. | [required]
**ne_attribute_ids** | **[]str** | An array of ne_attribute_ids. | [optional] 
**handle_id** | **str** | The handle id. | [optional] 
**archived** | **bool** | If the workflow action is archived or not. | [optional] [default to False]
}

## Example

```python
from sailpoint.nerm.models.duplicate_prevention_action import DuplicatePreventionAction

duplicate_prevention_action = DuplicatePreventionAction(
workflow_id='33f072dd-13b4-41e1-8ea0-16f2a59b57c8',
description='Allows a user to select an already existing profile, or create a new one for the request.',
search_scope='current',
ne_attribute_ids=[33f072dd-13b4-41e1-8ea0-16f2a59b57c8],
handle_id='33f072dd-13b4-41e1-8ea0-16f2a59b57c8',
archived=False
)

```
[[Back to top]](#) 

