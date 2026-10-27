---
id: target-attributes
title: TargetAttributes
pagination_label: TargetAttributes
sidebar_label: TargetAttributes
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'TargetAttributes', 'TargetAttributes'] 
slug: /tools/sdk/python/machine-mapping-metadata/models/target-attributes
tags: ['SDK', 'Software Development Kit', 'TargetAttributes', 'TargetAttributes']
---

# TargetAttributes

The attribute names a machine mapping can target.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | **[]str** | The target attribute names. | [optional] 
}

## Example

```python
from sailpoint.machine_mapping_metadata.models.target_attributes import TargetAttributes

target_attributes = TargetAttributes(
attributes=["name","nativeIdentity"]
)

```
[[Back to top]](#) 

