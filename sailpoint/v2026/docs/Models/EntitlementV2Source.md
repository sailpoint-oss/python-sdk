---
id: v2026-entitlement-v2-source
title: EntitlementV2Source
pagination_label: EntitlementV2Source
sidebar_label: EntitlementV2Source
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'EntitlementV2Source', 'V2026EntitlementV2Source'] 
slug: /tools/sdk/python/v2026/models/entitlement-v2-source
tags: ['SDK', 'Software Development Kit', 'EntitlementV2Source', 'V2026EntitlementV2Source']
---

# EntitlementV2Source


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The source ID | [optional] 
**type** | **str** | The source type, will always be \"SOURCE\" | [optional] 
**name** | **str** | The source name | [optional] 
}

## Example

```python
from sailpoint.v2026.models.entitlement_v2_source import EntitlementV2Source

entitlement_v2_source = EntitlementV2Source(
id='2c9180827ca885d7017ca8ce28a000eb',
type='SOURCE',
name='ODS-AD-Source'
)

```
[[Back to top]](#) 

