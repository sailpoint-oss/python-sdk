---
id: profile-attribute-rule-id
title: ProfileAttributeRuleId
pagination_label: ProfileAttributeRuleId
sidebar_label: ProfileAttributeRuleId
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'ProfileAttributeRuleId', 'ProfileAttributeRuleId'] 
slug: /tools/sdk/python//models/profile-attribute-rule-id
tags: ['SDK', 'Software Development Kit', 'ProfileAttributeRuleId', 'ProfileAttributeRuleId']
---

# ProfileAttributeRuleId


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**uid** | **str** |  | [optional] [readonly] 
**type** |  **Enum** [  'ProfileAttributeRule' ] |  | [required]
**condition_object_type** |  **Enum** [  'ProfileSelectAttribute',    'ProfileSearchAttribute',    'OwnerSelectAttribute',    'OwnerSearchAttribute',    'ContributorSelectAttribute',    'ContributorSearchAttribute' ] |  | [required]
**condition_object_id** | **str** |  | [required]
**comparison_operator** |  **Enum** [  'include?',    'exclude?' ] |  | [required]
**value** | **str** |  | [required]
}

## Example

```python
from sailpoint.nerm.models.profile_attribute_rule_id import ProfileAttributeRuleId

profile_attribute_rule_id = ProfileAttributeRuleId(
id='',
uid='',
type='ProfileAttributeRule',
condition_object_type='ProfileSelectAttribute',
condition_object_id='',
comparison_operator='include?',
value=''
)

```
[[Back to top]](#) 

