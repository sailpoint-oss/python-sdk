---
id: resource-v2
title: ResourceV2
pagination_label: ResourceV2
sidebar_label: ResourceV2
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'ResourceV2', 'ResourceV2'] 
slug: /tools/sdk/python/machine-identities/models/resource-v2
tags: ['SDK', 'Software Development Kit', 'ResourceV2', 'ResourceV2']
---

# ResourceV2

The source resource a machine identity is derived from.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The source resource identifier. | [optional] 
**type** | **str** | The type of the source resource. | [optional] 
**name** | **str** | The display name of the source resource. | [optional] 
**features** | **[]str** | The set of features supported by the source resource. | [optional] 
}

## Example

```python
from sailpoint.machine_identities.models.resource_v2 import ResourceV2

resource_v2 = ResourceV2(
id='8886e5e3-63d0-462f-a195-d98da885b8dc',
type='aws:iam-role',
name='nightly-batch-role',
features=["PROVISIONING","AUTHENTICATION"]
)

```
[[Back to top]](#) 

