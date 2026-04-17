---
id: create-duplicate-prevention-action-request
title: CreateDuplicatePreventionActionRequest
pagination_label: CreateDuplicatePreventionActionRequest
sidebar_label: CreateDuplicatePreventionActionRequest
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'CreateDuplicatePreventionActionRequest', 'CreateDuplicatePreventionActionRequest'] 
slug: /tools/sdk/python//models/create-duplicate-prevention-action-request
tags: ['SDK', 'Software Development Kit', 'CreateDuplicatePreventionActionRequest', 'CreateDuplicatePreventionActionRequest']
---

# CreateDuplicatePreventionActionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workflow_action** | [**DuplicatePreventionAction**](duplicate-prevention-action) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.create_duplicate_prevention_action_request import CreateDuplicatePreventionActionRequest

create_duplicate_prevention_action_request = CreateDuplicatePreventionActionRequest(
workflow_action=sailpoint.nerm.models.duplicate_prevention_action.DuplicatePreventionAction(
                    workflow_id = '33f072dd-13b4-41e1-8ea0-16f2a59b57c8', 
                    description = 'Allows a user to select an already existing profile, or create a new one for the request.', 
                    search_scope = 'current', 
                    ne_attribute_ids = [33f072dd-13b4-41e1-8ea0-16f2a59b57c8], 
                    handle_id = '33f072dd-13b4-41e1-8ea0-16f2a59b57c8', 
                    archived = False, )
)

```
[[Back to top]](#) 

