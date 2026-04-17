---
id: create-identity-proofing-action-request
title: CreateIdentityProofingActionRequest
pagination_label: CreateIdentityProofingActionRequest
sidebar_label: CreateIdentityProofingActionRequest
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'CreateIdentityProofingActionRequest', 'CreateIdentityProofingActionRequest'] 
slug: /tools/sdk/python//models/create-identity-proofing-action-request
tags: ['SDK', 'Software Development Kit', 'CreateIdentityProofingActionRequest', 'CreateIdentityProofingActionRequest']
---

# CreateIdentityProofingActionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workflow_action** | [**IdentityProofingAction**](identity-proofing-action) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.create_identity_proofing_action_request import CreateIdentityProofingActionRequest

create_identity_proofing_action_request = CreateIdentityProofingActionRequest(
workflow_action=sailpoint.nerm.models.identity_proofing_action.IdentityProofingAction(
                    workflow_id = '33f072dd-13b4-41e1-8ea0-16f2a59b57c8', 
                    description = 'Have the user account associated with this profile validate the identity data.', 
                    archived = False, )
)

```
[[Back to top]](#) 

