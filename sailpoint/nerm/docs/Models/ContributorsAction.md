---
id: contributors-action
title: ContributorsAction
pagination_label: ContributorsAction
sidebar_label: ContributorsAction
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'ContributorsAction', 'ContributorsAction'] 
slug: /tools/sdk/python//models/contributors-action
tags: ['SDK', 'Software Development Kit', 'ContributorsAction', 'ContributorsAction']
---

# ContributorsAction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workflow_id** | **str** | The workflow the workflow action belongs to. | [required]
**description** | **str** | The description of the workflow action. | [required]
**owner** |  **Enum** [  'true',    'false' ] | If the assignment option should be an owner.  Owner, Contributors, or Roles must be chosen. | [optional] 
**contributors** |  **Enum** [  'true',    'false' ] | If the assignment option should be contributors. Owner, Contributors, or Roles must be chosen. | [optional] 
**roles** |  **Enum** [  'true',    'false' ] | If the assignment option should be roles. Owner, Contributors, or Roles must be chosen. | [optional] 
**archived** | **bool** | If the workflow action is archived or not. | [optional] [default to False]
}

## Example

```python
from sailpoint.nerm.models.contributors_action import ContributorsAction

contributors_action = ContributorsAction(
workflow_id='33f072dd-13b4-41e1-8ea0-16f2a59b57c8',
description='Have the requester determine the contributors or owner of the profile.',
owner='true',
contributors='true',
roles='true',
archived=False
)

```
[[Back to top]](#) 

