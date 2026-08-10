---
id: public-machine-identity-owner
title: PublicMachineIdentityOwner
pagination_label: PublicMachineIdentityOwner
sidebar_label: PublicMachineIdentityOwner
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'PublicMachineIdentityOwner', 'PublicMachineIdentityOwner'] 
slug: /tools/sdk/python/public-machine-identities/models/public-machine-identity-owner
tags: ['SDK', 'Software Development Kit', 'PublicMachineIdentityOwner', 'PublicMachineIdentityOwner']
---

# PublicMachineIdentityOwner

Primary owner of a machine identity exposed by the public list endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Identity id of the primary owner. | [optional] 
**name** | **str** | Human-readable display name of the primary owner. | [optional] 
**email** | **str** | Email address of the primary owner. | [optional] 
}

## Example

```python
from sailpoint.public_machine_identities.models.public_machine_identity_owner import PublicMachineIdentityOwner

public_machine_identity_owner = PublicMachineIdentityOwner(
id='2c9180857182305e0171993735622948',
name='Alison Ferguso',
email='alison.ferguso@acme-solar.com'
)

```
[[Back to top]](#) 

