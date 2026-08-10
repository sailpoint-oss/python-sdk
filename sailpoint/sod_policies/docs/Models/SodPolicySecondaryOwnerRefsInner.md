---
id: sod-policy-secondary-owner-refs-inner
title: SodPolicySecondaryOwnerRefsInner
pagination_label: SodPolicySecondaryOwnerRefsInner
sidebar_label: SodPolicySecondaryOwnerRefsInner
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'SodPolicySecondaryOwnerRefsInner', 'SodPolicySecondaryOwnerRefsInner'] 
slug: /tools/sdk/python/sod-policies/models/sod-policy-secondary-owner-refs-inner
tags: ['SDK', 'Software Development Kit', 'SodPolicySecondaryOwnerRefsInner', 'SodPolicySecondaryOwnerRefsInner']
---

# SodPolicySecondaryOwnerRefsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** |  **Enum** [  'IDENTITY',    'GOVERNANCE_GROUP' ] | Secondary Owner Type | [optional] 
**id** | **str** | Secondary Owner ID | [optional] 
**name** | **str** | Secondary Owner Name | [optional] 
}

## Example

```python
from sailpoint.sod_policies.models.sod_policy_secondary_owner_refs_inner import SodPolicySecondaryOwnerRefsInner

sod_policy_secondary_owner_refs_inner = SodPolicySecondaryOwnerRefsInner(
type='IDENTITY',
id='2c9180a46faadee4016fb4e018c20639',
name='Support'
)

```
[[Back to top]](#) 

