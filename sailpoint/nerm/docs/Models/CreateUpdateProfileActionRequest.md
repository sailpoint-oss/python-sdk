---
id: create-update-profile-action-request
title: CreateUpdateProfileActionRequest
pagination_label: CreateUpdateProfileActionRequest
sidebar_label: CreateUpdateProfileActionRequest
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'CreateUpdateProfileActionRequest', 'CreateUpdateProfileActionRequest'] 
slug: /tools/sdk/python//models/create-update-profile-action-request
tags: ['SDK', 'Software Development Kit', 'CreateUpdateProfileActionRequest', 'CreateUpdateProfileActionRequest']
---

# CreateUpdateProfileActionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workflow_action** | [**UpdateProfileAction**](update-profile-action) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.create_update_profile_action_request import CreateUpdateProfileActionRequest

create_update_profile_action_request = CreateUpdateProfileActionRequest(
workflow_action=sailpoint.nerm.models.update_profile_action.UpdateProfileAction(
                    workflow_id = '33f072dd-13b4-41e1-8ea0-16f2a59b57c8', 
                    description = 'Updates a profile with all attributes collected during the workflow.', 
                    archived = False, )
)

```
[[Back to top]](#) 

