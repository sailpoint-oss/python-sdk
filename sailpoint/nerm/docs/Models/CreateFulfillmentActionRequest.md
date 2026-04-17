---
id: create-fulfillment-action-request
title: CreateFulfillmentActionRequest
pagination_label: CreateFulfillmentActionRequest
sidebar_label: CreateFulfillmentActionRequest
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'CreateFulfillmentActionRequest', 'CreateFulfillmentActionRequest'] 
slug: /tools/sdk/python//models/create-fulfillment-action-request
tags: ['SDK', 'Software Development Kit', 'CreateFulfillmentActionRequest', 'CreateFulfillmentActionRequest']
---

# CreateFulfillmentActionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workflow_action** | [**FulfillmentAction**](fulfillment-action) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.create_fulfillment_action_request import CreateFulfillmentActionRequest

create_fulfillment_action_request = CreateFulfillmentActionRequest(
workflow_action=sailpoint.nerm.models.fulfillment_action.FulfillmentAction(
                    workflow_id = '33f072dd-13b4-41e1-8ea0-16f2a59b57c8', 
                    description = 'Have another user or group provide information for the profile.', 
                    page_id = '33f072dd-13b4-41e1-8ea0-16f2a59b57c8', 
                    archived = False, 
                    requires_comment = False, )
)

```
[[Back to top]](#) 

