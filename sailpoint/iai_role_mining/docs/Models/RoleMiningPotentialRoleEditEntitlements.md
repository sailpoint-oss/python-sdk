---
id: role-mining-potential-role-edit-entitlements
title: RoleMiningPotentialRoleEditEntitlements
pagination_label: RoleMiningPotentialRoleEditEntitlements
sidebar_label: RoleMiningPotentialRoleEditEntitlements
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'RoleMiningPotentialRoleEditEntitlements', 'RoleMiningPotentialRoleEditEntitlements'] 
slug: /tools/sdk/python/iai-role-mining/models/role-mining-potential-role-edit-entitlements
tags: ['SDK', 'Software Development Kit', 'RoleMiningPotentialRoleEditEntitlements', 'RoleMiningPotentialRoleEditEntitlements']
---

# RoleMiningPotentialRoleEditEntitlements


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **[]str** | The list of entitlement ids to be edited | [optional] 
**exclude** | **bool** | If true, add ids to be exclusion list. If false, remove ids from the exclusion list. | [optional] 
}

## Example

```python
from sailpoint.iai_role_mining.models.role_mining_potential_role_edit_entitlements import RoleMiningPotentialRoleEditEntitlements

role_mining_potential_role_edit_entitlements = RoleMiningPotentialRoleEditEntitlements(
ids=[
                    ''
                    ],
exclude=True
)

```
[[Back to top]](#) 

