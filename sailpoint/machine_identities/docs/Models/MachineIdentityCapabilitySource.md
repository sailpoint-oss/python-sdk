---
id: machine-identity-capability-source
title: MachineIdentityCapabilitySource
pagination_label: MachineIdentityCapabilitySource
sidebar_label: MachineIdentityCapabilitySource
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'MachineIdentityCapabilitySource', 'MachineIdentityCapabilitySource'] 
slug: /tools/sdk/python/machine-identities/models/machine-identity-capability-source
tags: ['SDK', 'Software Development Kit', 'MachineIdentityCapabilitySource', 'MachineIdentityCapabilitySource']
---

# MachineIdentityCapabilitySource

The source the capability was aggregated from.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **DtoType** |  | [optional] 
**id** | **str** | ID of the object to which this reference applies | [optional] 
**name** | **str** | Human-readable display name of the object to which this reference applies | [optional] 
}

## Example

```python
from sailpoint.machine_identities.models.machine_identity_capability_source import MachineIdentityCapabilitySource

machine_identity_capability_source = MachineIdentityCapabilitySource(
type='IDENTITY',
id='2c91808568c529c60168cca6f90c1313',
name='William Wilson'
)

```
[[Back to top]](#) 

