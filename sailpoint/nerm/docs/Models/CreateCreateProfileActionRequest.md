---
id: create-create-profile-action-request
title: CreateCreateProfileActionRequest
pagination_label: CreateCreateProfileActionRequest
sidebar_label: CreateCreateProfileActionRequest
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'CreateCreateProfileActionRequest', 'CreateCreateProfileActionRequest'] 
slug: /tools/sdk/python//models/create-create-profile-action-request
tags: ['SDK', 'Software Development Kit', 'CreateCreateProfileActionRequest', 'CreateCreateProfileActionRequest']
---

# CreateCreateProfileActionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workflow_action** | [**CreateProfileAction**](create-profile-action) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.create_create_profile_action_request import CreateCreateProfileActionRequest

create_create_profile_action_request = CreateCreateProfileActionRequest(
workflow_action=sailpoint.nerm.models.create_profile_action.CreateProfileAction(
                    workflow_id = '33f072dd-13b4-41e1-8ea0-16f2a59b57c8', 
                    description = 'Creates a profile with all attributes collected during the workflow.', 
                    add_requester_as_owner = True, 
                    archived = False, )
)

```
[[Back to top]](#) 

