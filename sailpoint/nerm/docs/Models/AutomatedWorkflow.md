---
id: automated-workflow
title: AutomatedWorkflow
pagination_label: AutomatedWorkflow
sidebar_label: AutomatedWorkflow
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'AutomatedWorkflow', 'AutomatedWorkflow'] 
slug: /tools/sdk/python//models/automated-workflow
tags: ['SDK', 'Software Development Kit', 'AutomatedWorkflow', 'AutomatedWorkflow']
---

# AutomatedWorkflow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile_type_id** | **str** | The profile type the workflow effects. | [required]
**status** |  **Enum** [  'Enabled',    'Disabled' ] | Whether or not the workflow is enabled or disabled. | [required]
**uid** | **str** | The user-specified identifier of the workflow. | [required]
**name** | **str** | Name of the workflow | [required]
**disable_failure_email_notifications** | **bool** | When honored at runtime, suppresses failure email notifications for this workflow's sessions. | [optional] 
**condition_rules_attributes** | [**[]AutomatedWorkflowConditionRulesAttributesInner**](automated-workflow-condition-rules-attributes-inner) | The ProfileTypeRule this workflow will be working with. | [required]
}

## Example

```python
from sailpoint.nerm.models.automated_workflow import AutomatedWorkflow

automated_workflow = AutomatedWorkflow(
profile_type_id='33f072dd-13b4-41e1-8ea0-16f2a59b57c8',
status='Enabled',
uid='my_uid',
name='my_workflow',
disable_failure_email_notifications=False,
condition_rules_attributes=[{type=ProfileTypeRule, condition_object_type=DateAttribute, comparison_operator===, logical_operator=AND, value=true}]
)

```
[[Back to top]](#) 

