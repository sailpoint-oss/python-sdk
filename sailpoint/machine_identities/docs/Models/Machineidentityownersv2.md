---
id: machineidentityownersv2
title: Machineidentityownersv2
pagination_label: Machineidentityownersv2
sidebar_label: Machineidentityownersv2
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Machineidentityownersv2', 'Machineidentityownersv2'] 
slug: /tools/sdk/python/machine-identities/models/machineidentityownersv2
tags: ['SDK', 'Software Development Kit', 'Machineidentityownersv2', 'Machineidentityownersv2']
---

# Machineidentityownersv2

Owner configuration for a machine identity. A single primary (human IDENTITY) owner plus additional owners that are either up to ten human (IDENTITY) references or exactly one GOVERNANCE_GROUP reference - not both.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**primary** | [**Machineidentityownersv2Primary**](machineidentityownersv2-primary) |  | [optional] 
**secondary** | [**[]Basereferencedto**](basereferencedto) | Additional owners. Entries are either up to ten human (IDENTITY) references or exactly one GOVERNANCE_GROUP reference - not both. Governance-group owners appear here with type GOVERNANCE_GROUP. | [optional] 
}

## Example

```python
from sailpoint.machine_identities.models.machineidentityownersv2 import Machineidentityownersv2

machineidentityownersv2 = Machineidentityownersv2(
primary=,
secondary=[{"id":"2c9180858082150f0180893dbaf44202","name":"Jane Doe","type":"IDENTITY"}]
)

```
[[Back to top]](#) 

