---
id: v2025-machine-identity-user-entitlements
title: MachineIdentityUserEntitlements
pagination_label: MachineIdentityUserEntitlements
sidebar_label: MachineIdentityUserEntitlements
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'MachineIdentityUserEntitlements', 'V2025MachineIdentityUserEntitlements'] 
slug: /tools/sdk/python/v2025/models/machine-identity-user-entitlements
tags: ['SDK', 'Software Development Kit', 'MachineIdentityUserEntitlements', 'V2025MachineIdentityUserEntitlements']
---

# MachineIdentityUserEntitlements

Reference to a user entitlement.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entitlement_id** | **str** | Entitlement identifier. | [required]
**display_name** | **str** | Display name of the entitlement. | [required]
**source** | [**MachineIdentitySourceReference**](machine-identity-source-reference) |  | [required]
}

## Example

```python
from sailpoint.v2025.models.machine_identity_user_entitlements import MachineIdentityUserEntitlements

machine_identity_user_entitlements = MachineIdentityUserEntitlements(
entitlement_id='2509f650c20a3ab5956be70f6f136fbc',
display_name='CN=Engineering-test-org3,OU=megapod-useast1-test-org3,OU=org-data-service,DC=TestAutomationAD,DC=local',
source={type=SOURCE, id=c0201251a6ce4d268aba536cdd60a7f2, name=IdentityNow}
)

```
[[Back to top]](#) 

