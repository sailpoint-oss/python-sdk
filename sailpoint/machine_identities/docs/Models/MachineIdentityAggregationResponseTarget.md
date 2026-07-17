---
id: machine-identity-aggregation-response-target
title: MachineIdentityAggregationResponseTarget
pagination_label: MachineIdentityAggregationResponseTarget
sidebar_label: MachineIdentityAggregationResponseTarget
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'MachineIdentityAggregationResponseTarget', 'MachineIdentityAggregationResponseTarget'] 
slug: /tools/sdk/python/machine-identities/models/machine-identity-aggregation-response-target
tags: ['SDK', 'Software Development Kit', 'MachineIdentityAggregationResponseTarget', 'MachineIdentityAggregationResponseTarget']
---

# MachineIdentityAggregationResponseTarget

The target(source) of the aggregation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **DtoType** |  | [optional] 
**id** | **str** | ID of the object to which this reference applies | [optional] 
**name** | **str** | Human-readable display name of the object to which this reference applies | [optional] 
}

## Example

```python
from sailpoint.machine_identities.models.machine_identity_aggregation_response_target import MachineIdentityAggregationResponseTarget

machine_identity_aggregation_response_target = MachineIdentityAggregationResponseTarget(
type='IDENTITY',
id='2c91808568c529c60168cca6f90c1313',
name='William Wilson'
)

```
[[Back to top]](#) 

