---
id: machine-identity-user-entitlement-response-source
title: MachineIdentityUserEntitlementResponseSource
pagination_label: MachineIdentityUserEntitlementResponseSource
sidebar_label: MachineIdentityUserEntitlementResponseSource
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'MachineIdentityUserEntitlementResponseSource', 'MachineIdentityUserEntitlementResponseSource'] 
slug: /tools/sdk/python/machine-identities/models/machine-identity-user-entitlement-response-source
tags: ['SDK', 'Software Development Kit', 'MachineIdentityUserEntitlementResponseSource', 'MachineIdentityUserEntitlementResponseSource']
---

# MachineIdentityUserEntitlementResponseSource

The source of the user entitlement

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **DtoType** |  | [optional] 
**id** | **str** | ID of the object to which this reference applies | [optional] 
**name** | **str** | Human-readable display name of the object to which this reference applies | [optional] 
}

## Example

```python
from sailpoint.machine_identities.models.machine_identity_user_entitlement_response_source import MachineIdentityUserEntitlementResponseSource

machine_identity_user_entitlement_response_source = MachineIdentityUserEntitlementResponseSource(
type='IDENTITY',
id='2c91808568c529c60168cca6f90c1313',
name='William Wilson'
)

```
[[Back to top]](#) 

