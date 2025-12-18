---
id: v2025-identity-reference1
title: IdentityReference1
pagination_label: IdentityReference1
sidebar_label: IdentityReference1
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'IdentityReference1', 'V2025IdentityReference1'] 
slug: /tools/sdk/python/v2025/models/identity-reference1
tags: ['SDK', 'Software Development Kit', 'IdentityReference1', 'V2025IdentityReference1']
---

# IdentityReference1

Details about the identity correlated with the account.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the identity that is correlated with this account. | [required]
**name** | **str** | The name of the identity that is correlated with this account. | [required]
**alias** | **str** | The alias of the identity. | [required]
**email** | **str** | The email of the identity. | [required]
}

## Example

```python
from sailpoint.v2025.models.identity_reference1 import IdentityReference1

identity_reference1 = IdentityReference1(
id='ee769173319b41d19ccec6c235423237b',
name='john.doe',
alias='jdoe',
email='john.doe@email.com'
)

```
[[Back to top]](#) 

