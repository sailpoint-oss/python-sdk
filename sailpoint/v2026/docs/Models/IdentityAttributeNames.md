---
id: v2026-identity-attribute-names
title: IdentityAttributeNames
pagination_label: IdentityAttributeNames
sidebar_label: IdentityAttributeNames
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'IdentityAttributeNames', 'V2026IdentityAttributeNames'] 
slug: /tools/sdk/python/v2026/models/identity-attribute-names
tags: ['SDK', 'Software Development Kit', 'IdentityAttributeNames', 'V2026IdentityAttributeNames']
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
from sailpoint.v2026.models.identity_attribute_names import IdentityAttributeNames

identity_attribute_names = IdentityAttributeNames(
ids=[name, displayName]
)

```
[[Back to top]](#) 

