---
id: workflow-action-performers1
title: WorkflowActionPerformers1
pagination_label: WorkflowActionPerformers1
sidebar_label: WorkflowActionPerformers1
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'WorkflowActionPerformers1', 'WorkflowActionPerformers1'] 
slug: /tools/sdk/python//models/workflow-action-performers1
tags: ['SDK', 'Software Development Kit', 'WorkflowActionPerformers1', 'WorkflowActionPerformers1']
---

# WorkflowActionPerformers1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contributor_attribute_id** | **str** | Specify the id of the user attribute to perform the action. | [optional] 
**contributors** | **bool** | Set to true to allow profile contributor to perform the action. | [optional] [default to False]
**contributors_manager_attribute_id** | **str** | Specify the id of the user attribute to perform the action. | [optional] 
**owner** | **bool** | Set to true to allow profile owner to perform the action. | [optional] [default to False]
**profiles_contributors_attribute_id** | **str** | Specify the id of the profile attribute to perform the action. | [optional] 
**requester** | **bool** | Set to true to allow requester from the request to perform the action. | [optional] [default to False]
**requesters_manager** | **bool** | Set to true to allow the requester's manager from the request to perform the action. | [optional] [default to False]
**workflow_action_id** | **str** | Specify the id of the workflow action you would like to create the workflow action performer/s for. | [optional] 
}

## Example

```python
from sailpoint.nerm.models.workflow_action_performers1 import WorkflowActionPerformers1

workflow_action_performers1 = WorkflowActionPerformers1(
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

