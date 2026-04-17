---
id: create-profile-check-action-request
title: CreateProfileCheckActionRequest
pagination_label: CreateProfileCheckActionRequest
sidebar_label: CreateProfileCheckActionRequest
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'CreateProfileCheckActionRequest', 'CreateProfileCheckActionRequest'] 
slug: /tools/sdk/python//models/create-profile-check-action-request
tags: ['SDK', 'Software Development Kit', 'CreateProfileCheckActionRequest', 'CreateProfileCheckActionRequest']
---

# CreateProfileCheckActionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workflow_action** | [**ProfileCheckAction**](profile-check-action) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.create_profile_check_action_request import CreateProfileCheckActionRequest

create_profile_check_action_request = CreateProfileCheckActionRequest(
workflow_action=sailpoint.nerm.models.profile_check_action.ProfileCheckAction(
                    workflow_id = '33f072dd-13b4-41e1-8ea0-16f2a59b57c8', 
                    description = 'Finds a profile based on selected attributes and values found in the session.', 
                    archived = False, 
                    ne_attribute_ids = [33f072dd-13b4-41e1-8ea0-16f2a59b57c8], 
                    handle_type = 'session', 
                    handle_id = '33f072dd-13b4-41e1-8ea0-16f2a59b57c8', )
)

```
[[Back to top]](#) 

