---
id: profile-type-rule
title: ProfileTypeRule
pagination_label: ProfileTypeRule
sidebar_label: ProfileTypeRule
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'ProfileTypeRule', 'ProfileTypeRule'] 
slug: /tools/sdk/python//models/profile-type-rule
tags: ['SDK', 'Software Development Kit', 'ProfileTypeRule', 'ProfileTypeRule']
---

# ProfileTypeRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**uid** | **str** |  | [optional] [readonly] 
**type** |  **Enum** [  'ProfileTypeRule' ] |  | [required]
**comparison_operator** |  **Enum** [  '==',    '!=' ] |  | [optional] 
**value** | **str** |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.profile_type_rule import ProfileTypeRule

profile_type_rule = ProfileTypeRule(
id='',
uid='',
type='ProfileTypeRule',
comparison_operator='==',
value=''
)

```
[[Back to top]](#) 

