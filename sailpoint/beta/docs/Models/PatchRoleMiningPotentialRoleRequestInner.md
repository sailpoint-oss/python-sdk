---
id: beta-patch-role-mining-potential-role-request-inner
title: PatchRoleMiningPotentialRoleRequestInner
pagination_label: PatchRoleMiningPotentialRoleRequestInner
sidebar_label: PatchRoleMiningPotentialRoleRequestInner
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'PatchRoleMiningPotentialRoleRequestInner', 'BetaPatchRoleMiningPotentialRoleRequestInner'] 
slug: /tools/sdk/python/beta/models/patch-role-mining-potential-role-request-inner
tags: ['SDK', 'Software Development Kit', 'PatchRoleMiningPotentialRoleRequestInner', 'BetaPatchRoleMiningPotentialRoleRequestInner']
---

# PatchRoleMiningPotentialRoleRequestInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**op** |  **Enum** [  'remove',    'replace' ] | The operation to be performed | [optional] 
**path** | **str** | A string JSON Pointer representing the target path to an element to be affected by the operation | [required]
**value** | [**UpdateMultiHostSourcesRequestInnerValue**](update-multi-host-sources-request-inner-value) |  | [optional] 
}

## Example

```python
from sailpoint.beta.models.patch_role_mining_potential_role_request_inner import PatchRoleMiningPotentialRoleRequestInner

patch_role_mining_potential_role_request_inner = PatchRoleMiningPotentialRoleRequestInner(
op='replace',
path='/description',
value=New description
)

```
[[Back to top]](#) 

