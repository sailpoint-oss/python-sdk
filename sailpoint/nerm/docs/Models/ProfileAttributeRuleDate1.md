---
id: profile-attribute-rule-date1
title: ProfileAttributeRuleDate1
pagination_label: ProfileAttributeRuleDate1
sidebar_label: ProfileAttributeRuleDate1
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'ProfileAttributeRuleDate1', 'ProfileAttributeRuleDate1'] 
slug: /tools/sdk/python//models/profile-attribute-rule-date1
tags: ['SDK', 'Software Development Kit', 'ProfileAttributeRuleDate1', 'ProfileAttributeRuleDate1']
---

# ProfileAttributeRuleDate1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
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
from sailpoint.nerm.models.profile_attribute_rule_date1 import ProfileAttributeRuleDate1

profile_attribute_rule_date1 = ProfileAttributeRuleDate1(
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

