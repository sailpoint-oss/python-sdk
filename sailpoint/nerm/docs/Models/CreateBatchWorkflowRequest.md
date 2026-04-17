---
id: create-batch-workflow-request
title: CreateBatchWorkflowRequest
pagination_label: CreateBatchWorkflowRequest
sidebar_label: CreateBatchWorkflowRequest
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'CreateBatchWorkflowRequest', 'CreateBatchWorkflowRequest'] 
slug: /tools/sdk/python//models/create-batch-workflow-request
tags: ['SDK', 'Software Development Kit', 'CreateBatchWorkflowRequest', 'CreateBatchWorkflowRequest']
---

# CreateBatchWorkflowRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workflow** | [**BatchWorkflow**](batch-workflow) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.create_batch_workflow_request import CreateBatchWorkflowRequest

create_batch_workflow_request = CreateBatchWorkflowRequest(
workflow=sailpoint.nerm.models.batch_workflow.BatchWorkflow(
                    profile_type_id = '33f072dd-13b4-41e1-8ea0-16f2a59b57c8', 
                    status = 'Enabled', 
                    uid = 'my_uid', 
                    name = 'my_workflow', 
                    options = sailpoint.nerm.models.batch_workflow_options.BatchWorkflow_options(
                        all_profiles = 'true', 
                        multiple_requests = 'false', ), 
                    disable_failure_email_notifications = False, )
)

```
[[Back to top]](#) 

