---
id: v2025-additional-owner-ref
title: AdditionalOwnerRef
pagination_label: AdditionalOwnerRef
sidebar_label: AdditionalOwnerRef
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'AdditionalOwnerRef', 'V2025AdditionalOwnerRef'] 
slug: /tools/sdk/python/v2025/models/additional-owner-ref
tags: ['SDK', 'Software Development Kit', 'AdditionalOwnerRef', 'V2025AdditionalOwnerRef']
---

# AdditionalOwnerRef

Reference to an additional owner (identity or governance group).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** |  **Enum** [  'IDENTITY',    'GOVERNANCE_GROUP' ] | Type of the additional owner; IDENTITY for an identity, GOVERNANCE_GROUP for a governance group. | [optional] 
**id** | **str** | ID of the identity or governance group. | [optional] 
**name** | **str** | Display name. It may be left null or omitted on input. If set, it must match the current display name of the identity or governance group, otherwise a 400 Bad Request error may result. | [optional] 
}

## Example

```python
from sailpoint.v2025.models.additional_owner_ref import AdditionalOwnerRef

additional_owner_ref = AdditionalOwnerRef(
type='IDENTITY',
id='2c9180a46faadee4016fb4e018c20639',
name='support'
)

```
[[Back to top]](#) 

