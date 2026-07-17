---
id: machine-identity-v2-source
title: MachineIdentityV2Source
pagination_label: MachineIdentityV2Source
sidebar_label: MachineIdentityV2Source
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'MachineIdentityV2Source', 'MachineIdentityV2Source'] 
slug: /tools/sdk/python/machine-identities/models/machine-identity-v2-source
tags: ['SDK', 'Software Development Kit', 'MachineIdentityV2Source', 'MachineIdentityV2Source']
---

# MachineIdentityV2Source

The source of the machine identity.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **DtoType** |  | [optional] 
**id** | **str** | ID of the object to which this reference applies | [optional] 
**name** | **str** | Human-readable display name of the object to which this reference applies | [optional] 
}

## Example

```python
from sailpoint.machine_identities.models.machine_identity_v2_source import MachineIdentityV2Source

machine_identity_v2_source = MachineIdentityV2Source(
type='IDENTITY',
id='2c91808568c529c60168cca6f90c1313',
name='William Wilson'
)

```
[[Back to top]](#) 

