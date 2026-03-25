---
id: v2026-machine-identity-aggregation-response-target
title: MachineIdentityAggregationResponseTarget
pagination_label: MachineIdentityAggregationResponseTarget
sidebar_label: MachineIdentityAggregationResponseTarget
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'MachineIdentityAggregationResponseTarget', 'V2026MachineIdentityAggregationResponseTarget'] 
slug: /tools/sdk/python/v2026/models/machine-identity-aggregation-response-target
tags: ['SDK', 'Software Development Kit', 'MachineIdentityAggregationResponseTarget', 'V2026MachineIdentityAggregationResponseTarget']
---

# MachineIdentityAggregationResponseTarget

The target(source) of the aggregation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**DtoType**](dto-type) |  | [optional] 
**id** | **str** | ID of the object to which this reference applies | [optional] 
**name** | **str** | Human-readable display name of the object to which this reference applies | [optional] 
}

## Example

```python
from sailpoint.v2026.models.machine_identity_aggregation_response_target import MachineIdentityAggregationResponseTarget

machine_identity_aggregation_response_target = MachineIdentityAggregationResponseTarget(
type='IDENTITY',
id='2c91808568c529c60168cca6f90c1313',
name='William Wilson'
)

```
[[Back to top]](#) 

