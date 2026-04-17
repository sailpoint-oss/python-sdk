---
id: login-workflow
title: LoginWorkflow
pagination_label: LoginWorkflow
sidebar_label: LoginWorkflow
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'LoginWorkflow', 'LoginWorkflow'] 
slug: /tools/sdk/python//models/login-workflow
tags: ['SDK', 'Software Development Kit', 'LoginWorkflow', 'LoginWorkflow']
---

# LoginWorkflow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile_type_id** | **str** | The profile type the workflow effects. | [required]
**status** |  **Enum** [  'Enabled',    'Disabled' ] | Whether or not the workflow is enabled or disabled. | [required]
**uid** | **str** | The user-specified identifier of the workflow. | [required]
**name** | **str** | Name of the workflow | [required]
**options** | [**LoginWorkflowOptions**](login-workflow-options) |  | [optional] 
**disable_failure_email_notifications** | **bool** | When honored at runtime, suppresses failure email notifications for this workflow's sessions. | [optional] 
}

## Example

```python
from sailpoint.nerm.models.login_workflow import LoginWorkflow

login_workflow = LoginWorkflow(
profile_type_id='33f072dd-13b4-41e1-8ea0-16f2a59b57c8',
status='Enabled',
uid='my_uid',
name='my_workflow',
options=sailpoint.nerm.models.login_workflow_options.LoginWorkflow_options(
                    expiration_time = 1, ),
disable_failure_email_notifications=False
)

```
[[Back to top]](#) 

