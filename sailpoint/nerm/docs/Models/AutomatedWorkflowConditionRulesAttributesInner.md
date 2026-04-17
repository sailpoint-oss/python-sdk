---
id: automated-workflow-condition-rules-attributes-inner
title: AutomatedWorkflowConditionRulesAttributesInner
pagination_label: AutomatedWorkflowConditionRulesAttributesInner
sidebar_label: AutomatedWorkflowConditionRulesAttributesInner
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'AutomatedWorkflowConditionRulesAttributesInner', 'AutomatedWorkflowConditionRulesAttributesInner'] 
slug: /tools/sdk/python//models/automated-workflow-condition-rules-attributes-inner
tags: ['SDK', 'Software Development Kit', 'AutomatedWorkflowConditionRulesAttributesInner', 'AutomatedWorkflowConditionRulesAttributesInner']
---

# AutomatedWorkflowConditionRulesAttributesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**logical_operator** |  **Enum** [  'AND',    'OR' ] | The type of condition rule. | [required]
**comparison_operator** |  **Enum** [  '<',    '>',    '==',    'before',    'include?',    'absent?',    'after' ] | The operator used by the condition rule. | [required]
**condition_object_id** | **str** | UUID for object targeted by the condition. | [optional] 
**condition_object_type** | **str** | Type of object targeted by the condition. | [required]
**secondary_value** | **str** | Used for time_frame comparison. | [optional] 
**tertiary_value** | **str** | Represents the days of a temporal comparison. | [optional] 
**value** | **str** | The value being compared against. | [optional] 
**order** | **int** | If there are multiple rules against one workflow, this is the order that they are ran in. | [optional] 
**type** |  **Enum** [  'RiskRule',    'ProfileIdRule',    'ProfileTypeRule',    'ProfileExistsRule',    'ProfileStatusRule',    'SessionAttributeRule',    'ProfileAttributeRule',    'ProfileDoesNotExistRule',    'IdentityProofingRule' ] | The type of condition rule. | [required]
}

## Example

```python
from sailpoint.nerm.models.automated_workflow_condition_rules_attributes_inner import AutomatedWorkflowConditionRulesAttributesInner

automated_workflow_condition_rules_attributes_inner = AutomatedWorkflowConditionRulesAttributesInner(
logical_operator='AND',
comparison_operator='==',
condition_object_id='cc844e99-9895-43d0-9d17-8f606b2158ba',
condition_object_type='DateAttribute',
secondary_value='before',
tertiary_value='before',
value='true',
order=1,
type='ProfileTypeRule'
)

```
[[Back to top]](#) 

