---
id: v2026-machine-identity-user-entitlement-response-entitlement
title: MachineIdentityUserEntitlementResponseEntitlement
pagination_label: MachineIdentityUserEntitlementResponseEntitlement
sidebar_label: MachineIdentityUserEntitlementResponseEntitlement
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'MachineIdentityUserEntitlementResponseEntitlement', 'V2026MachineIdentityUserEntitlementResponseEntitlement'] 
slug: /tools/sdk/python/v2026/models/machine-identity-user-entitlement-response-entitlement
tags: ['SDK', 'Software Development Kit', 'MachineIdentityUserEntitlementResponseEntitlement', 'V2026MachineIdentityUserEntitlementResponseEntitlement']
---

# MachineIdentityUserEntitlementResponseEntitlement

The user entitlement

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**DtoType**](dto-type) |  | [optional] 
**id** | **str** | ID of the object to which this reference applies | [optional] 
**name** | **str** | Human-readable display name of the object to which this reference applies | [optional] 
}

## Example

```python
from sailpoint.v2026.models.machine_identity_user_entitlement_response_entitlement import MachineIdentityUserEntitlementResponseEntitlement

machine_identity_user_entitlement_response_entitlement = MachineIdentityUserEntitlementResponseEntitlement(
type='IDENTITY',
id='2c91808568c529c60168cca6f90c1313',
name='William Wilson'
)

```
[[Back to top]](#) 

