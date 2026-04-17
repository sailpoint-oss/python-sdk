---
id: advanced-search1-condition-rules-attributes-inner
title: AdvancedSearch1ConditionRulesAttributesInner
pagination_label: AdvancedSearch1ConditionRulesAttributesInner
sidebar_label: AdvancedSearch1ConditionRulesAttributesInner
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'AdvancedSearch1ConditionRulesAttributesInner', 'AdvancedSearch1ConditionRulesAttributesInner'] 
slug: /tools/sdk/python//models/advanced-search1-condition-rules-attributes-inner
tags: ['SDK', 'Software Development Kit', 'AdvancedSearch1ConditionRulesAttributesInner', 'AdvancedSearch1ConditionRulesAttributesInner']
---

# AdvancedSearch1ConditionRulesAttributesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** |  **Enum** [  'ProfileTypeRule',    'ProfileStatusRule',    'ProfileAttributeRule',    'RiskRule' ] |  | [required]
**comparison_operator** |  **Enum** [  '==',    '>',    '<' ] |  | [required]
**value** | **str** |  | [required]
**condition_object_type** |  **Enum** [  'ProfileSelectAttribute',    'ProfileSearchAttribute',    'OwnerSelectAttribute',    'OwnerSearchAttribute',    'ContributorSelectAttribute',    'ContributorSearchAttribute' ] |  | [required]
**condition_object_id** | **str** |  | [required]
**secondary_attribute_type** |  **Enum** [  'DateAttribute' ] |  | [optional] 
**secondary_attribute_id** | **str** |  | [optional] 
**secondary_value** |  **Enum** [  'OverallRisk' ] |  | [required]
**tertiary_value** | **str** |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.advanced_search1_condition_rules_attributes_inner import AdvancedSearch1ConditionRulesAttributesInner

advanced_search1_condition_rules_attributes_inner = AdvancedSearch1ConditionRulesAttributesInner(
type='ProfileTypeRule',
comparison_operator='==',
value='',
condition_object_type='ProfileSelectAttribute',
condition_object_id='',
secondary_attribute_type='DateAttribute',
secondary_attribute_id='',
secondary_value='OverallRisk',
tertiary_value='30'
)

```
[[Back to top]](#) 

