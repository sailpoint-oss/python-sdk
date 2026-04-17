---
id: batch-workflow
title: BatchWorkflow
pagination_label: BatchWorkflow
sidebar_label: BatchWorkflow
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'BatchWorkflow', 'BatchWorkflow'] 
slug: /tools/sdk/python//models/batch-workflow
tags: ['SDK', 'Software Development Kit', 'BatchWorkflow', 'BatchWorkflow']
---

# BatchWorkflow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile_type_id** | **str** | The profile type the workflow effects. | [required]
**status** |  **Enum** [  'Enabled',    'Disabled' ] | Whether or not the workflow is enabled or disabled. | [required]
**uid** | **str** | The user-specified identifier of the workflow. | [required]
**name** | **str** | Name of the workflow | [required]
**options** | [**BatchWorkflowOptions**](batch-workflow-options) |  | [optional] 
**disable_failure_email_notifications** | **bool** | When honored at runtime, suppresses failure email notifications for this workflow's sessions. | [optional] 
}

## Example

```python
from sailpoint.nerm.models.batch_workflow import BatchWorkflow

batch_workflow = BatchWorkflow(
profile_type_id='33f072dd-13b4-41e1-8ea0-16f2a59b57c8',
status='Enabled',
uid='my_uid',
name='my_workflow',
options=sailpoint.nerm.models.batch_workflow_options.BatchWorkflow_options(
                    all_profiles = 'true', 
                    multiple_requests = 'false', ),
disable_failure_email_notifications=False
)

```
[[Back to top]](#) 

