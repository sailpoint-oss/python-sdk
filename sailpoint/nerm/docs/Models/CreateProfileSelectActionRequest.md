---
id: create-profile-select-action-request
title: CreateProfileSelectActionRequest
pagination_label: CreateProfileSelectActionRequest
sidebar_label: CreateProfileSelectActionRequest
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'CreateProfileSelectActionRequest', 'CreateProfileSelectActionRequest'] 
slug: /tools/sdk/python//models/create-profile-select-action-request
tags: ['SDK', 'Software Development Kit', 'CreateProfileSelectActionRequest', 'CreateProfileSelectActionRequest']
---

# CreateProfileSelectActionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workflow_action** | [**ProfileSelectAction**](profile-select-action) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.create_profile_select_action_request import CreateProfileSelectActionRequest

create_profile_select_action_request = CreateProfileSelectActionRequest(
workflow_action=sailpoint.nerm.models.profile_select_action.ProfileSelectAction(
                    workflow_id = '33f072dd-13b4-41e1-8ea0-16f2a59b57c8', 
                    description = 'Select the profiles that you want to run this workflow for.', 
                    archived = False, )
)

```
[[Back to top]](#) 

