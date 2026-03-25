---
id: v2026-workflow-execution-history
title: WorkflowExecutionHistory
pagination_label: WorkflowExecutionHistory
sidebar_label: WorkflowExecutionHistory
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'WorkflowExecutionHistory', 'V2026WorkflowExecutionHistory'] 
slug: /tools/sdk/python/v2026/models/workflow-execution-history
tags: ['SDK', 'Software Development Kit', 'WorkflowExecutionHistory', 'V2026WorkflowExecutionHistory']
---

# WorkflowExecutionHistory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**definition** | **object** | The workflow definition for the workflow execution | [optional] 
**history** | **object** | List of workflow execution events for the given workflow execution | [optional] 
**trigger** | **object** | The trigger that initiated the workflow execution | [optional] 
}

## Example

```python
from sailpoint.v2026.models.workflow_execution_history import WorkflowExecutionHistory

workflow_execution_history = WorkflowExecutionHistory(
definition=None,
history=None,
trigger=None
)

```
[[Back to top]](#) 

