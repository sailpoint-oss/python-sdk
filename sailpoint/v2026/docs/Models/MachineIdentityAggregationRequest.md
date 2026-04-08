---
id: v2026-machine-identity-aggregation-request
title: MachineIdentityAggregationRequest
pagination_label: MachineIdentityAggregationRequest
sidebar_label: MachineIdentityAggregationRequest
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'MachineIdentityAggregationRequest', 'V2026MachineIdentityAggregationRequest'] 
slug: /tools/sdk/python/v2026/models/machine-identity-aggregation-request
tags: ['SDK', 'Software Development Kit', 'MachineIdentityAggregationRequest', 'V2026MachineIdentityAggregationRequest']
---

# MachineIdentityAggregationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataset_ids** | **[]str** | List of dataset Ids to aggregate machine identities | [required]
**disable_optimization** | **bool** | Flag to disable optimization for the aggregation. Defaults to false when not provided. When set to true, it disables aggregation optimizations and may increase processing time. | [optional] [default to False]
}

## Example

```python
from sailpoint.v2026.models.machine_identity_aggregation_request import MachineIdentityAggregationRequest

machine_identity_aggregation_request = MachineIdentityAggregationRequest(
dataset_ids=[
                    'source:datasetId12345'
                    ],
disable_optimization=False
)

```
[[Back to top]](#) 

