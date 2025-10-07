---
id: v2025-native-id-to-entitlement-ids-mapping
title: NativeIdToEntitlementIdsMapping
pagination_label: NativeIdToEntitlementIdsMapping
sidebar_label: NativeIdToEntitlementIdsMapping
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'NativeIdToEntitlementIdsMapping', 'V2025NativeIdToEntitlementIdsMapping'] 
slug: /tools/sdk/python/v2025/models/native-id-to-entitlement-ids-mapping
tags: ['SDK', 'Software Development Kit', 'NativeIdToEntitlementIdsMapping', 'V2025NativeIdToEntitlementIdsMapping']
---

# NativeIdToEntitlementIdsMapping

Native ID to Entitlement IDs mapping.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**native_id** | **str** | The native ID in the source system. | [required]
**entitlement_ids** | **[]str** | The list of entitlement IDs associated with the native ID in the source system. | [required]
}

## Example

```python
from sailpoint.v2025.models.native_id_to_entitlement_ids_mapping import NativeIdToEntitlementIdsMapping

native_id_to_entitlement_ids_mapping = NativeIdToEntitlementIdsMapping(
native_id='jdoe',
entitlement_ids=[
                    '2c91809773dee32014e13e122092014e'
                    ]
)

```
[[Back to top]](#) 

