---
id: v2025-machine-identity-updated-user-entitlement-changes
title: MachineIdentityUpdatedUserEntitlementChanges
pagination_label: MachineIdentityUpdatedUserEntitlementChanges
sidebar_label: MachineIdentityUpdatedUserEntitlementChanges
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'MachineIdentityUpdatedUserEntitlementChanges', 'V2025MachineIdentityUpdatedUserEntitlementChanges'] 
slug: /tools/sdk/python/v2025/models/machine-identity-updated-user-entitlement-changes
tags: ['SDK', 'Software Development Kit', 'MachineIdentityUpdatedUserEntitlementChanges', 'V2025MachineIdentityUpdatedUserEntitlementChanges']
---

# MachineIdentityUpdatedUserEntitlementChanges

Changes to user entitlements.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute_name** | **str** | Name of the attribute that changed. | [optional] 
**added** | [**[]MachineIdentityUserEntitlements**](machine-identity-user-entitlements) | User entitlements that were added. | [optional] 
**removed** | [**[]MachineIdentityUserEntitlements**](machine-identity-user-entitlements) | User entitlements that were removed. | [optional] 
}

## Example

```python
from sailpoint.v2025.models.machine_identity_updated_user_entitlement_changes import MachineIdentityUpdatedUserEntitlementChanges

machine_identity_updated_user_entitlement_changes = MachineIdentityUpdatedUserEntitlementChanges(
attribute_name='userEntitlements',
added=[
                    {entitlementId=2509f650c20a3ab5956be70f6f136fbc, displayName=CN=Engineering-test-org3,OU=megapod-useast1-test-org3,OU=org-data-service,DC=TestAutomationAD,DC=local, source={type=SOURCE, id=7443d0ffb1304bbcbdf4c07b5c09d4f2, name=ODS-AD-Source}}
                    ],
removed=[
                    {entitlementId=2509f650c20a3ab5956be70f6f136fbc, displayName=CN=Engineering-test-org3,OU=megapod-useast1-test-org3,OU=org-data-service,DC=TestAutomationAD,DC=local, source={type=SOURCE, id=7443d0ffb1304bbcbdf4c07b5c09d4f2, name=ODS-AD-Source}}
                    ]
)

```
[[Back to top]](#) 

