---
id: profile-attribute-rule-string
title: ProfileAttributeRuleString
pagination_label: ProfileAttributeRuleString
sidebar_label: ProfileAttributeRuleString
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'ProfileAttributeRuleString', 'ProfileAttributeRuleString'] 
slug: /tools/sdk/python//models/profile-attribute-rule-string
tags: ['SDK', 'Software Development Kit', 'ProfileAttributeRuleString', 'ProfileAttributeRuleString']
---

# ProfileAttributeRuleString


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**uid** | **str** |  | [optional] [readonly] 
**type** |  **Enum** [  'ProfileAttributeRule' ] |  | [required]
**condition_object_type** |  **Enum** [  'TextFieldAttribute',    'TextAreaAttribute' ] |  | [required]
**condition_object_id** | **str** |  | [required]
**comparison_operator** |  **Enum** [  '==',    '!=',    '>',    '<',    'start_with?',    'end_with?',    'include?' ] |  | [required]
**value** | **str** |  | [required]
}

## Example

```python
from sailpoint.nerm.models.profile_attribute_rule_string import ProfileAttributeRuleString

profile_attribute_rule_string = ProfileAttributeRuleString(
id='',
uid='',
type='ProfileAttributeRule',
condition_object_type='TextFieldAttribute',
condition_object_id='',
comparison_operator='==',
value='Some value'
)

```
[[Back to top]](#) 

