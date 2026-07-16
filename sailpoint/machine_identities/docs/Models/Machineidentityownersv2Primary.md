---
id: machineidentityownersv2-primary
title: Machineidentityownersv2Primary
pagination_label: Machineidentityownersv2Primary
sidebar_label: Machineidentityownersv2Primary
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Machineidentityownersv2Primary', 'Machineidentityownersv2Primary'] 
slug: /tools/sdk/python/machine-identities/models/machineidentityownersv2-primary
tags: ['SDK', 'Software Development Kit', 'Machineidentityownersv2Primary', 'Machineidentityownersv2Primary']
---

# Machineidentityownersv2Primary

The identity selected as the primary owner.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **Dtotype** |  | [optional] 
**id** | **str** | ID of the object to which this reference applies | [optional] 
**name** | **str** | Human-readable display name of the object to which this reference applies | [optional] 
}

## Example

```python
from sailpoint.machine_identities.models.machineidentityownersv2_primary import Machineidentityownersv2Primary

machineidentityownersv2_primary = Machineidentityownersv2Primary(
type='IDENTITY',
id='2c91808568c529c60168cca6f90c1313',
name='William Wilson'
)

```
[[Back to top]](#) 

