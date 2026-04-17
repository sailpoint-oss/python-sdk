---
id: create-batch-update-action-request
title: CreateBatchUpdateActionRequest
pagination_label: CreateBatchUpdateActionRequest
sidebar_label: CreateBatchUpdateActionRequest
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'CreateBatchUpdateActionRequest', 'CreateBatchUpdateActionRequest'] 
slug: /tools/sdk/python//models/create-batch-update-action-request
tags: ['SDK', 'Software Development Kit', 'CreateBatchUpdateActionRequest', 'CreateBatchUpdateActionRequest']
---

# CreateBatchUpdateActionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workflow_action** | [**BatchUpdateAction**](batch-update-action) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.create_batch_update_action_request import CreateBatchUpdateActionRequest

create_batch_update_action_request = CreateBatchUpdateActionRequest(
workflow_action=sailpoint.nerm.models.batch_update_action.BatchUpdateAction(
                    workflow_id = '33f072dd-13b4-41e1-8ea0-16f2a59b57c8', 
                    description = 'Updates a batch of profiles with all attributes collected during the workflow.', 
                    archived = False, )
)

```
[[Back to top]](#) 

