---
id: update-workflow
title: UpdateWorkflow
pagination_label: UpdateWorkflow
sidebar_label: UpdateWorkflow
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'UpdateWorkflow', 'UpdateWorkflow'] 
slug: /tools/sdk/python//models/update-workflow
tags: ['SDK', 'Software Development Kit', 'UpdateWorkflow', 'UpdateWorkflow']
---

# UpdateWorkflow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile_type_id** | **str** | The profile type the workflow effects. | [required]
**status** |  **Enum** [  'Enabled',    'Disabled' ] | Whether or not the workflow is enabled or disabled. | [required]
**uid** | **str** | The user-specified identifier of the workflow. | [required]
**name** | **str** | Name of the workflow | [required]
**profile_status** | **str** | The status of the profiles the workflow will effect. | [required]
**disable_failure_email_notifications** | **bool** | When honored at runtime, suppresses failure email notifications for this workflow's sessions. | [optional] 
}

## Example

```python
from sailpoint.nerm.models.update_workflow import UpdateWorkflow

update_workflow = UpdateWorkflow(
profile_type_id='33f072dd-13b4-41e1-8ea0-16f2a59b57c8',
status='Enabled',
uid='my_uid',
name='my_workflow',
profile_status='active',
disable_failure_email_notifications=False
)

```
[[Back to top]](#) 

