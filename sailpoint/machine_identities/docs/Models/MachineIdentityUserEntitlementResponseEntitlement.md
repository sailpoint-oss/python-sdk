---
id: machine-identity-user-entitlement-response-entitlement
title: MachineIdentityUserEntitlementResponseEntitlement
pagination_label: MachineIdentityUserEntitlementResponseEntitlement
sidebar_label: MachineIdentityUserEntitlementResponseEntitlement
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'MachineIdentityUserEntitlementResponseEntitlement', 'MachineIdentityUserEntitlementResponseEntitlement'] 
slug: /tools/sdk/python/machine-identities/models/machine-identity-user-entitlement-response-entitlement
tags: ['SDK', 'Software Development Kit', 'MachineIdentityUserEntitlementResponseEntitlement', 'MachineIdentityUserEntitlementResponseEntitlement']
---

# MachineIdentityUserEntitlementResponseEntitlement

The user entitlement

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **DtoType** |  | [optional] 
**id** | **str** | ID of the object to which this reference applies | [optional] 
**name** | **str** | Human-readable display name of the object to which this reference applies | [optional] 
}

## Example

```python
from sailpoint.machine_identities.models.machine_identity_user_entitlement_response_entitlement import MachineIdentityUserEntitlementResponseEntitlement

machine_identity_user_entitlement_response_entitlement = MachineIdentityUserEntitlementResponseEntitlement(
type='IDENTITY',
id='2c91808568c529c60168cca6f90c1313',
name='William Wilson'
)

```
[[Back to top]](#) 

