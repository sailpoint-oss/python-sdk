---
id: rest-api-action
title: RestApiAction
pagination_label: RestApiAction
sidebar_label: RestApiAction
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'RestApiAction', 'RestApiAction'] 
slug: /tools/sdk/python//models/rest-api-action
tags: ['SDK', 'Software Development Kit', 'RestApiAction', 'RestApiAction']
---

# RestApiAction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workflow_id** | **str** | The workflow the workflow action belongs to. | [required]
**description** | **str** | The description of the workflow action. | [required]
**archived** | **bool** | If the workflow action is archived or not. | [optional] [default to False]
}

## Example

```python
from sailpoint.nerm.models.rest_api_action import RestApiAction

rest_api_action = RestApiAction(
workflow_id='33f072dd-13b4-41e1-8ea0-16f2a59b57c8',
description='Makes a request to a Restful API.',
archived=False
)

```
[[Back to top]](#) 

