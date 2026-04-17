---
id: identity-proofing-action
title: IdentityProofingAction
pagination_label: IdentityProofingAction
sidebar_label: IdentityProofingAction
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'IdentityProofingAction', 'IdentityProofingAction'] 
slug: /tools/sdk/python//models/identity-proofing-action
tags: ['SDK', 'Software Development Kit', 'IdentityProofingAction', 'IdentityProofingAction']
---

# IdentityProofingAction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workflow_id** | **str** | The workflow the workflow action belongs to. | [required]
**description** | **str** | The description of the workflow action. | [required]
**archived** | **bool** | If the workflow action is archived or not. | [optional] [default to False]
}

## Example

```python
from sailpoint.nerm.models.identity_proofing_action import IdentityProofingAction

identity_proofing_action = IdentityProofingAction(
workflow_id='33f072dd-13b4-41e1-8ea0-16f2a59b57c8',
description='Have the user account associated with this profile validate the identity data.',
archived=False
)

```
[[Back to top]](#) 

