---
id: v2026-identity-reference
title: IdentityReference
pagination_label: IdentityReference
sidebar_label: IdentityReference
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'IdentityReference', 'V2026IdentityReference'] 
slug: /tools/sdk/python/v2026/models/identity-reference
tags: ['SDK', 'Software Development Kit', 'IdentityReference', 'V2026IdentityReference']
---

# IdentityReference

Contains detailed information about an identity, including unique identifier, name, email address, and registration status.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of identity | [optional] 
**name** | **str** | Name of Identity | [optional] 
**email** | **str** | mail id of identity | [optional] 
**status** | **str** | status of identity UNREGISTERED/REGISTERED | [optional] 
}

## Example

```python
from sailpoint.v2026.models.identity_reference import IdentityReference

identity_reference = IdentityReference(
id='117e169acf21f4ae28e8a06198ce7f69',
name='Alfred',
email='alfred@testmail.identitysoon.com',
status='UNREGISTERED'
)

```
[[Back to top]](#) 

