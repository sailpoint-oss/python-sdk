---
id: profile-type-rule1
title: ProfileTypeRule1
pagination_label: ProfileTypeRule1
sidebar_label: ProfileTypeRule1
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'ProfileTypeRule1', 'ProfileTypeRule1'] 
slug: /tools/sdk/python//models/profile-type-rule1
tags: ['SDK', 'Software Development Kit', 'ProfileTypeRule1', 'ProfileTypeRule1']
---

# ProfileTypeRule1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** |  **Enum** [  'ProfileTypeRule' ] |  | [required]
**comparison_operator** |  **Enum** [  '==',    '!=' ] |  | [required]
**value** | **str** |  | [required]
}

## Example

```python
from sailpoint.nerm.models.profile_type_rule1 import ProfileTypeRule1

profile_type_rule1 = ProfileTypeRule1(
type='ProfileTypeRule',
comparison_operator='==',
value=''
)

```
[[Back to top]](#) 

