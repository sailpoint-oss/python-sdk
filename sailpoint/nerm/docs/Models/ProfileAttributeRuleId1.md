---
id: profile-attribute-rule-id1
title: ProfileAttributeRuleId1
pagination_label: ProfileAttributeRuleId1
sidebar_label: ProfileAttributeRuleId1
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'ProfileAttributeRuleId1', 'ProfileAttributeRuleId1'] 
slug: /tools/sdk/python//models/profile-attribute-rule-id1
tags: ['SDK', 'Software Development Kit', 'ProfileAttributeRuleId1', 'ProfileAttributeRuleId1']
---

# ProfileAttributeRuleId1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** |  **Enum** [  'ProfileAttributeRule' ] |  | [required]
**condition_object_type** |  **Enum** [  'ProfileSelectAttribute',    'ProfileSearchAttribute',    'OwnerSelectAttribute',    'OwnerSearchAttribute',    'ContributorSelectAttribute',    'ContributorSearchAttribute' ] |  | [required]
**condition_object_id** | **str** |  | [required]
**comparison_operator** |  **Enum** [  'include?',    'exclude?' ] |  | [required]
**value** | **str** |  | [required]
}

## Example

```python
from sailpoint.nerm.models.profile_attribute_rule_id1 import ProfileAttributeRuleId1

profile_attribute_rule_id1 = ProfileAttributeRuleId1(
type='ProfileAttributeRule',
condition_object_type='ProfileSelectAttribute',
condition_object_id='',
comparison_operator='include?',
value=''
)

```
[[Back to top]](#) 

