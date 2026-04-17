---
id: create-set-attributes-action-request
title: CreateSetAttributesActionRequest
pagination_label: CreateSetAttributesActionRequest
sidebar_label: CreateSetAttributesActionRequest
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'CreateSetAttributesActionRequest', 'CreateSetAttributesActionRequest'] 
slug: /tools/sdk/python//models/create-set-attributes-action-request
tags: ['SDK', 'Software Development Kit', 'CreateSetAttributesActionRequest', 'CreateSetAttributesActionRequest']
---

# CreateSetAttributesActionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workflow_action** | [**SetAttributesAction**](set-attributes-action) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.create_set_attributes_action_request import CreateSetAttributesActionRequest

create_set_attributes_action_request = CreateSetAttributesActionRequest(
workflow_action=sailpoint.nerm.models.set_attributes_action.SetAttributesAction(
                    workflow_id = '33f072dd-13b4-41e1-8ea0-16f2a59b57c8', 
                    description = 'Set attribute(s) to a specific value.', 
                    archived = False, )
)

```
[[Back to top]](#) 

