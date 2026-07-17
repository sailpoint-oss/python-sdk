---
id: account-source-reference-owner
title: AccountSourceReferenceOwner
pagination_label: AccountSourceReferenceOwner
sidebar_label: AccountSourceReferenceOwner
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'AccountSourceReferenceOwner', 'AccountSourceReferenceOwner'] 
slug: /tools/sdk/python/triggers/models/account-source-reference-owner
tags: ['SDK', 'Software Development Kit', 'AccountSourceReferenceOwner', 'AccountSourceReferenceOwner']
---

# AccountSourceReferenceOwner

Details about the owner of the source.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the source owner. | [required]
**name** | **str** | Name of the source owner. | [required]
}

## Example

```python
from sailpoint.triggers.models.account_source_reference_owner import AccountSourceReferenceOwner

account_source_reference_owner = AccountSourceReferenceOwner(
id='owner-123',
name='owner-name'
)

```
[[Back to top]](#) 

