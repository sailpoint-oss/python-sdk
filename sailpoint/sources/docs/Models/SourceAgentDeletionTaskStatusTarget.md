---
id: source-agent-deletion-task-status-target
title: SourceAgentDeletionTaskStatusTarget
pagination_label: SourceAgentDeletionTaskStatusTarget
sidebar_label: SourceAgentDeletionTaskStatusTarget
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'SourceAgentDeletionTaskStatusTarget', 'SourceAgentDeletionTaskStatusTarget'] 
slug: /tools/sdk/python/sources/models/source-agent-deletion-task-status-target
tags: ['SDK', 'Software Development Kit', 'SourceAgentDeletionTaskStatusTarget', 'SourceAgentDeletionTaskStatusTarget']
---

# SourceAgentDeletionTaskStatusTarget

The source that AI agents are deleted from.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **DtoType** |  | [optional] 
**id** | **str** | ID of the object to which this reference applies | [optional] 
**name** | **str** | Human-readable display name of the object to which this reference applies | [optional] 
}

## Example

```python
from sailpoint.sources.models.source_agent_deletion_task_status_target import SourceAgentDeletionTaskStatusTarget

source_agent_deletion_task_status_target = SourceAgentDeletionTaskStatusTarget(
type='IDENTITY',
id='2c91808568c529c60168cca6f90c1313',
name='William Wilson'
)

```
[[Back to top]](#) 

