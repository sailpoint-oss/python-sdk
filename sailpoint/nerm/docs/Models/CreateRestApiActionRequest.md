---
id: create-rest-api-action-request
title: CreateRestApiActionRequest
pagination_label: CreateRestApiActionRequest
sidebar_label: CreateRestApiActionRequest
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'CreateRestApiActionRequest', 'CreateRestApiActionRequest'] 
slug: /tools/sdk/python//models/create-rest-api-action-request
tags: ['SDK', 'Software Development Kit', 'CreateRestApiActionRequest', 'CreateRestApiActionRequest']
---

# CreateRestApiActionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workflow_action** | [**RestApiAction**](rest-api-action) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.create_rest_api_action_request import CreateRestApiActionRequest

create_rest_api_action_request = CreateRestApiActionRequest(
workflow_action=sailpoint.nerm.models.rest_api_action.RestApiAction(
                    workflow_id = '33f072dd-13b4-41e1-8ea0-16f2a59b57c8', 
                    description = 'Makes a request to a Restful API.', 
                    archived = False, )
)

```
[[Back to top]](#) 

