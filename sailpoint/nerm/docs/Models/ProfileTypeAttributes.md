---
id: profile-type-attributes
title: ProfileTypeAttributes
pagination_label: ProfileTypeAttributes
sidebar_label: ProfileTypeAttributes
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'ProfileTypeAttributes', 'ProfileTypeAttributes'] 
slug: /tools/sdk/python//models/profile-type-attributes
tags: ['SDK', 'Software Development Kit', 'ProfileTypeAttributes', 'ProfileTypeAttributes']
---

# ProfileTypeAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | How many ne attribute records exist | [optional] 
**records** | [**[]ProfileTypeAttribute**](profile-type-attribute) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.profile_type_attributes import ProfileTypeAttributes

profile_type_attributes = ProfileTypeAttributes(
count=5,
records=[
                    sailpoint.nerm.models.profile_type_attribute.ProfileTypeAttribute(
                        id = '1246d8b3-ac29-4015-8154-dea4434a73fa', 
                        uid = '1246d8b3-ac29-4015-8154-dea4434a73fa', 
                        label = 'object', 
                        synced = '1246d8b3-ac29-4015-8154-dea4434a73fa', )
                    ]
)

```
[[Back to top]](#) 

