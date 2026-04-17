---
id: create-workflow-action-performer-request
title: CreateWorkflowActionPerformerRequest
pagination_label: CreateWorkflowActionPerformerRequest
sidebar_label: CreateWorkflowActionPerformerRequest
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'CreateWorkflowActionPerformerRequest', 'CreateWorkflowActionPerformerRequest'] 
slug: /tools/sdk/python//models/create-workflow-action-performer-request
tags: ['SDK', 'Software Development Kit', 'CreateWorkflowActionPerformerRequest', 'CreateWorkflowActionPerformerRequest']
---

# CreateWorkflowActionPerformerRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workflow_action_performers** | [**WorkflowActionPerformers1**](workflow-action-performers1) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.create_workflow_action_performer_request import CreateWorkflowActionPerformerRequest

create_workflow_action_performer_request = CreateWorkflowActionPerformerRequest(
workflow_action_performers=sailpoint.nerm.models.workflow_action_performers_1.WorkflowActionPerformers_1(
                    contributor_attribute_id = 'e6905f25-489a-43cd-a758-bdacaf60dcab', 
                    contributors = True, 
                    contributors_manager_attribute_id = 'e6905f25-489a-43cd-a758-bdacaf60dcab', 
                    owner = True, 
                    profiles_contributors_attribute_id = 'e6905f25-489a-43cd-a758-bdacaf60dcab', 
                    requester = True, 
                    requesters_manager = True, 
                    workflow_action_id = 'e6905f25-489a-43cd-a758-bdacaf60dcab', )
)

```
[[Back to top]](#) 

