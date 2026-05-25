---
id: v2026-intel-machine-source
title: IntelMachineSource
pagination_label: IntelMachineSource
sidebar_label: IntelMachineSource
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'IntelMachineSource', 'V2026IntelMachineSource'] 
slug: /tools/sdk/python/v2026/models/intel-machine-source
tags: ['SDK', 'Software Development Kit', 'IntelMachineSource', 'V2026IntelMachineSource']
---

# IntelMachineSource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the correlated source in Identity Security Cloud. | [optional] 
**name** | **str** | Display name of the source as configured in Identity Security Cloud. | [optional] 
**type** | **str** | Connector or source type classification for the backing system. | [optional] 
}

## Example

```python
from sailpoint.v2026.models.intel_machine_source import IntelMachineSource

intel_machine_source = IntelMachineSource(
id='2c9180835d2e5168015d32f890301e89',
name='Active Directory',
type='LDAP'
)

```
[[Back to top]](#) 

