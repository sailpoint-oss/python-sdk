---
id: workflow-action-performers
title: WorkflowActionPerformers
pagination_label: WorkflowActionPerformers
sidebar_label: WorkflowActionPerformers
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'WorkflowActionPerformers', 'WorkflowActionPerformers'] 
slug: /tools/sdk/python//models/workflow-action-performers
tags: ['SDK', 'Software Development Kit', 'WorkflowActionPerformers', 'WorkflowActionPerformers']
---

# WorkflowActionPerformers


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The id of the workflow action performer that was created. | [optional] 
**contributor_attribute_id** | **str** | The id of the user attribute to perform the action. | [optional] 
**contributors** | **bool** | Set to allow profile contributor to perform the action. | [optional] [default to False]
**contributors_manager_attribute_id** | **str** | The id of the user attribute to perform the action. | [optional] 
**owner** | **bool** | Set to allow profile owner to perform the action. | [optional] [default to False]
**profiles_contributors_attribute_id** | **str** | The id of the profile attribute to perform the action. | [optional] 
**requester** | **bool** | Set to allow requester from the request to perform the action. | [optional] [default to False]
**requesters_manager** | **bool** | Set to allow the requester's manager from the request to perform the action. | [optional] [default to False]
**workflow_action_id** | **str** | The id of the workflow action. | [optional] 
}

## Example

```python
from sailpoint.nerm.models.workflow_action_performers import WorkflowActionPerformers

workflow_action_performers = WorkflowActionPerformers(
id='e6905f25-489a-43cd-a758-bdacaf60dcab',
contributor_attribute_id='e6905f25-489a-43cd-a758-bdacaf60dcab',
contributors=True,
contributors_manager_attribute_id='e6905f25-489a-43cd-a758-bdacaf60dcab',
owner=True,
profiles_contributors_attribute_id='e6905f25-489a-43cd-a758-bdacaf60dcab',
requester=True,
requesters_manager=True,
workflow_action_id='e6905f25-489a-43cd-a758-bdacaf60dcab'
)

```
[[Back to top]](#) 

