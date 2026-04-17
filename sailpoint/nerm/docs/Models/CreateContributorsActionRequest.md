---
id: create-contributors-action-request
title: CreateContributorsActionRequest
pagination_label: CreateContributorsActionRequest
sidebar_label: CreateContributorsActionRequest
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'CreateContributorsActionRequest', 'CreateContributorsActionRequest'] 
slug: /tools/sdk/python//models/create-contributors-action-request
tags: ['SDK', 'Software Development Kit', 'CreateContributorsActionRequest', 'CreateContributorsActionRequest']
---

# CreateContributorsActionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workflow_action** | [**ContributorsAction**](contributors-action) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.create_contributors_action_request import CreateContributorsActionRequest

create_contributors_action_request = CreateContributorsActionRequest(
workflow_action=sailpoint.nerm.models.contributors_action.ContributorsAction(
                    workflow_id = '33f072dd-13b4-41e1-8ea0-16f2a59b57c8', 
                    description = 'Have the requester determine the contributors or owner of the profile.', 
                    owner = 'true', 
                    contributors = 'true', 
                    roles = 'true', 
                    archived = False, )
)

```
[[Back to top]](#) 

