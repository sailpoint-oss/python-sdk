---
id: beta-sod-policy-owner-ref
title: SodPolicyOwnerRef
pagination_label: SodPolicyOwnerRef
sidebar_label: SodPolicyOwnerRef
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'SodPolicyOwnerRef', 'BetaSodPolicyOwnerRef'] 
slug: /tools/sdk/python/beta/models/sod-policy-owner-ref
tags: ['SDK', 'Software Development Kit', 'SodPolicyOwnerRef', 'BetaSodPolicyOwnerRef']
---

# SodPolicyOwnerRef

The owner of the SOD policy.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** |  **Enum** [  'IDENTITY',    'GOVERNANCE_GROUP' ] | Owner type. | [optional] 
**id** | **str** | Owner's ID. | [optional] 
**name** | **str** | Owner's name. | [optional] 
}

## Example

```python
from sailpoint.beta.models.sod_policy_owner_ref import SodPolicyOwnerRef

sod_policy_owner_ref = SodPolicyOwnerRef(
type='IDENTITY',
id='2c9180a46faadee4016fb4e018c20639',
name='Support'
)

```
[[Back to top]](#) 

