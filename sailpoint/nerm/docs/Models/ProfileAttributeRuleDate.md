---
id: profile-attribute-rule-date
title: ProfileAttributeRuleDate
pagination_label: ProfileAttributeRuleDate
sidebar_label: ProfileAttributeRuleDate
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'ProfileAttributeRuleDate', 'ProfileAttributeRuleDate'] 
slug: /tools/sdk/python//models/profile-attribute-rule-date
tags: ['SDK', 'Software Development Kit', 'ProfileAttributeRuleDate', 'ProfileAttributeRuleDate']
---

# ProfileAttributeRuleDate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**uid** | **str** |  | [optional] [readonly] 
**type** |  **Enum** [  'ProfileAttributeRule' ] |  | [required]
**condition_object_type** |  **Enum** [  'DateAttribute' ] |  | [required]
**condition_object_id** | **str** |  | [optional] 
**secondary_attribute_type** |  **Enum** [  'DateAttribute' ] |  | [optional] 
**secondary_attribute_id** | **str** |  | [optional] 
**comparison_operator** |  **Enum** [  '>',    '<',    'after',    'before' ] |  | [optional] 
**value** |  **Enum** [  'Today',    '<uid>' ] |  | [required]
**secondary_value** |  **Enum** [  'after',    'before' ] |  | [optional] 
**tertiary_value** | **str** |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.profile_attribute_rule_date import ProfileAttributeRuleDate

profile_attribute_rule_date = ProfileAttributeRuleDate(
id='',
uid='',
type='ProfileAttributeRule',
condition_object_type='DateAttribute',
condition_object_id='',
secondary_attribute_type='DateAttribute',
secondary_attribute_id='',
comparison_operator='>',
value='Today',
secondary_value='after',
tertiary_value='30'
)

```
[[Back to top]](#) 

