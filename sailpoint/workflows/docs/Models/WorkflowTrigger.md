---
id: workflow-trigger
title: WorkflowTrigger
pagination_label: WorkflowTrigger
sidebar_label: WorkflowTrigger
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'WorkflowTrigger', 'WorkflowTrigger'] 
slug: /tools/sdk/python/workflows/models/workflow-trigger
tags: ['SDK', 'Software Development Kit', 'WorkflowTrigger', 'WorkflowTrigger']
---

# WorkflowTrigger

The trigger that starts the workflow

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** |  **Enum** [  'EVENT',    'EXTERNAL',    'SCHEDULED',    '' ] | The trigger type | [required]
**display_name** | **str** | The trigger display name | [optional] 
**attributes** | **object** | Workflow Trigger Attributes. | [required]
}

## Example

```python
from sailpoint.workflows.models.workflow_trigger import WorkflowTrigger

workflow_trigger = WorkflowTrigger(
type='EVENT',
display_name='',
attributes=None
)

```
[[Back to top]](#) 

