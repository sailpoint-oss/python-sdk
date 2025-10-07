---
id: source-id-and-native-id-to-entitlement-ids-mapping
title: SourceIdAndNativeIdToEntitlementIdsMapping
pagination_label: SourceIdAndNativeIdToEntitlementIdsMapping
sidebar_label: SourceIdAndNativeIdToEntitlementIdsMapping
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'SourceIdAndNativeIdToEntitlementIdsMapping', 'SourceIdAndNativeIdToEntitlementIdsMapping'] 
slug: /tools/sdk/python/v3/models/source-id-and-native-id-to-entitlement-ids-mapping
tags: ['SDK', 'Software Development Kit', 'SourceIdAndNativeIdToEntitlementIdsMapping', 'SourceIdAndNativeIdToEntitlementIdsMapping']
---

# SourceIdAndNativeIdToEntitlementIdsMapping

Source ID and Native ID to Entitlement IDs mapping.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_id** | **str** | The ID of the source system. | [required]
**native_id_to_entitlement_ids_mappings** | [**[]NativeIdToEntitlementIdsMapping**](native-id-to-entitlement-ids-mapping) | The native ID and entitlement IDs mapping in the source system. | [required]
}

## Example

```python
from sailpoint.v3.models.source_id_and_native_id_to_entitlement_ids_mapping import SourceIdAndNativeIdToEntitlementIdsMapping

source_id_and_native_id_to_entitlement_ids_mapping = SourceIdAndNativeIdToEntitlementIdsMapping(
source_id='2c91809773dee32014e13e122092014e',
native_id_to_entitlement_ids_mappings=[
                    sailpoint.v3.models.native_id_to_entitlement_ids_mapping.NativeIdToEntitlementIdsMapping(
                        native_id = 'jdoe', 
                        entitlement_ids = [
                            '2c91809773dee32014e13e122092014e'
                            ], )
                    ]
)

```
[[Back to top]](#) 

