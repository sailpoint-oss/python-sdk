---
id: profile-attribute-rule-string1
title: ProfileAttributeRuleString1
pagination_label: ProfileAttributeRuleString1
sidebar_label: ProfileAttributeRuleString1
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'ProfileAttributeRuleString1', 'ProfileAttributeRuleString1'] 
slug: /tools/sdk/python//models/profile-attribute-rule-string1
tags: ['SDK', 'Software Development Kit', 'ProfileAttributeRuleString1', 'ProfileAttributeRuleString1']
---

# ProfileAttributeRuleString1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** |  **Enum** [  'ProfileAttributeRule' ] |  | [required]
**condition_object_type** |  **Enum** [  'TextFieldAttribute',    'TextAreaAttribute' ] |  | [required]
**condition_object_id** | **str** |  | [required]
**comparison_operator** |  **Enum** [  '==',    '!=',    '>',    '<',    'start_with?',    'end_with?',    'include?' ] |  | [required]
**value** | **str** |  | [required]
}

## Example

```python
from sailpoint.nerm.models.profile_attribute_rule_string1 import ProfileAttributeRuleString1

profile_attribute_rule_string1 = ProfileAttributeRuleString1(
type='ProfileAttributeRule',
condition_object_type='TextFieldAttribute',
condition_object_id='',
comparison_operator='==',
value='Some value'
)

```
[[Back to top]](#) 

