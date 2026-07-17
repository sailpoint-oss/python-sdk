---
id: public-identity-attribute-config
title: PublicIdentityAttributeConfig
pagination_label: PublicIdentityAttributeConfig
sidebar_label: PublicIdentityAttributeConfig
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'PublicIdentityAttributeConfig', 'PublicIdentityAttributeConfig'] 
slug: /tools/sdk/python/public-identities-config/models/public-identity-attribute-config
tags: ['SDK', 'Software Development Kit', 'PublicIdentityAttributeConfig', 'PublicIdentityAttributeConfig']
---

# PublicIdentityAttributeConfig

Used to map an attribute key for an Identity to its display name.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The attribute key | [optional] 
**name** | **str** | The attribute display name | [optional] 
}

## Example

```python
from sailpoint.public_identities_config.models.public_identity_attribute_config import PublicIdentityAttributeConfig

public_identity_attribute_config = PublicIdentityAttributeConfig(
key='country',
name='Country'
)

```
[[Back to top]](#) 

