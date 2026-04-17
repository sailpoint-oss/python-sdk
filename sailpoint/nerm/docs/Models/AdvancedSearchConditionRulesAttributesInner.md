---
id: advanced-search-condition-rules-attributes-inner
title: AdvancedSearchConditionRulesAttributesInner
pagination_label: AdvancedSearchConditionRulesAttributesInner
sidebar_label: AdvancedSearchConditionRulesAttributesInner
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'AdvancedSearchConditionRulesAttributesInner', 'AdvancedSearchConditionRulesAttributesInner'] 
slug: /tools/sdk/python//models/advanced-search-condition-rules-attributes-inner
tags: ['SDK', 'Software Development Kit', 'AdvancedSearchConditionRulesAttributesInner', 'AdvancedSearchConditionRulesAttributesInner']
---

# AdvancedSearchConditionRulesAttributesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**uid** | **str** |  | [optional] [readonly] 
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
from sailpoint.nerm.models.advanced_search_condition_rules_attributes_inner import AdvancedSearchConditionRulesAttributesInner

advanced_search_condition_rules_attributes_inner = AdvancedSearchConditionRulesAttributesInner(
id='',
uid='',
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

