---
id: v2025-account-source-reference-owner
title: AccountSourceReferenceOwner
pagination_label: AccountSourceReferenceOwner
sidebar_label: AccountSourceReferenceOwner
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'AccountSourceReferenceOwner', 'V2025AccountSourceReferenceOwner'] 
slug: /tools/sdk/python/v2025/models/account-source-reference-owner
tags: ['SDK', 'Software Development Kit', 'AccountSourceReferenceOwner', 'V2025AccountSourceReferenceOwner']
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
from sailpoint.v2025.models.account_source_reference_owner import AccountSourceReferenceOwner

account_source_reference_owner = AccountSourceReferenceOwner(
id='owner-123',
name='owner-name'
)

```
[[Back to top]](#) 

