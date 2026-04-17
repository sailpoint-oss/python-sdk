---
id: create-workflow
title: CreateWorkflow
pagination_label: CreateWorkflow
sidebar_label: CreateWorkflow
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'CreateWorkflow', 'CreateWorkflow'] 
slug: /tools/sdk/python//models/create-workflow
tags: ['SDK', 'Software Development Kit', 'CreateWorkflow', 'CreateWorkflow']
---

# CreateWorkflow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile_type_id** | **str** | The profile type the workflow effects. | [required]
**status** |  **Enum** [  'Enabled',    'Disabled' ] | Whether or not the workflow is enabled or disabled. | [required]
**uid** | **str** | The user-specified identifier of the workflow. | [required]
**name** | **str** | Name of the workflow | [required]
**disable_failure_email_notifications** | **bool** | When honored at runtime, suppresses failure email notifications for this workflow's sessions. | [optional] 
}

## Example

```python
from sailpoint.nerm.models.create_workflow import CreateWorkflow

create_workflow = CreateWorkflow(
profile_type_id='33f072dd-13b4-41e1-8ea0-16f2a59b57c8',
status='Enabled',
uid='my_uid',
name='my_workflow',
disable_failure_email_notifications=False
)

```
[[Back to top]](#) 

