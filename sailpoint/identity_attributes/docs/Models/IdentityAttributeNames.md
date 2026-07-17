---
id: identity-attribute-names
title: IdentityAttributeNames
pagination_label: IdentityAttributeNames
sidebar_label: IdentityAttributeNames
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'IdentityAttributeNames', 'IdentityAttributeNames'] 
slug: /tools/sdk/python/identity-attributes/models/identity-attribute-names
tags: ['SDK', 'Software Development Kit', 'IdentityAttributeNames', 'IdentityAttributeNames']
---

# IdentityAttributeNames

Identity attribute IDs.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **[]str** | List of identity attributes' technical names. | [optional] 
}

## Example

```python
from sailpoint.identity_attributes.models.identity_attribute_names import IdentityAttributeNames

identity_attribute_names = IdentityAttributeNames(
ids=["name","displayName"]
)

```
[[Back to top]](#) 

