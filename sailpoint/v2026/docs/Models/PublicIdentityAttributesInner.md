---
id: v2026-public-identity-attributes-inner
title: PublicIdentityAttributesInner
pagination_label: PublicIdentityAttributesInner
sidebar_label: PublicIdentityAttributesInner
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'PublicIdentityAttributesInner', 'V2026PublicIdentityAttributesInner'] 
slug: /tools/sdk/python/v2026/models/public-identity-attributes-inner
tags: ['SDK', 'Software Development Kit', 'PublicIdentityAttributesInner', 'V2026PublicIdentityAttributesInner']
---

# PublicIdentityAttributesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The attribute key | [optional] 
**name** | **str** | Human-readable display name of the attribute | [optional] 
**value** | **str** | The attribute value | [optional] 
}

## Example

```python
from sailpoint.v2026.models.public_identity_attributes_inner import PublicIdentityAttributesInner

public_identity_attributes_inner = PublicIdentityAttributesInner(
key='country',
name='Country',
value='US'
)

```
[[Back to top]](#) 

