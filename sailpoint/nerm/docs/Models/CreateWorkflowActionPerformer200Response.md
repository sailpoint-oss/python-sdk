---
id: create-workflow-action-performer200-response
title: CreateWorkflowActionPerformer200Response
pagination_label: CreateWorkflowActionPerformer200Response
sidebar_label: CreateWorkflowActionPerformer200Response
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'CreateWorkflowActionPerformer200Response', 'CreateWorkflowActionPerformer200Response'] 
slug: /tools/sdk/python//models/create-workflow-action-performer200-response
tags: ['SDK', 'Software Development Kit', 'CreateWorkflowActionPerformer200Response', 'CreateWorkflowActionPerformer200Response']
---

# CreateWorkflowActionPerformer200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workflow_action_performer** | [**WorkflowActionPerformers**](workflow-action-performers) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.create_workflow_action_performer200_response import CreateWorkflowActionPerformer200Response

create_workflow_action_performer200_response = CreateWorkflowActionPerformer200Response(
workflow_action_performer=sailpoint.nerm.models.workflow_action_performers.WorkflowActionPerformers(
                    id = 'e6905f25-489a-43cd-a758-bdacaf60dcab', 
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

