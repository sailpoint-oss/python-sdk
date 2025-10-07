---
id: v2025-identity-with-new-access
title: IdentityWithNewAccess
pagination_label: IdentityWithNewAccess
sidebar_label: IdentityWithNewAccess
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'IdentityWithNewAccess', 'V2025IdentityWithNewAccess'] 
slug: /tools/sdk/python/v2025/models/identity-with-new-access
tags: ['SDK', 'Software Development Kit', 'IdentityWithNewAccess', 'V2025IdentityWithNewAccess']
---

# IdentityWithNewAccess

An identity with a set of access to be added

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identity_id** | **str** | Identity id to be checked. | [required]
**access_refs** | [**[]IdentityWithNewAccessAccessRefsInner**](identity-with-new-access-access-refs-inner) | The list of entitlements to consider for possible violations in a preventive check. | [required]
**source_id_and_native_id_to_entitlement_ids_mappings** | [**[]SourceIdAndNativeIdToEntitlementIdsMapping**](source-id-and-native-id-to-entitlement-ids-mapping) | Mappings between sourceId and nativeId to entitlement IDs for which access is requested. This is only being used for ARM analysis in case of user having multiple accounts on the same source on which entitlement is requested. Optional parameter that helps identify which account the entitlement is requested on. For scenarios where users have a single account on the source and do not provide this field, the available account is chosen. | [optional] 
}

## Example

```python
from sailpoint.v2025.models.identity_with_new_access import IdentityWithNewAccess

identity_with_new_access = IdentityWithNewAccess(
identity_id='2c91808568c529c60168cca6f90c1313',
access_refs=[{type=ENTITLEMENT, id=2c918087682f9a86016839c050861ab1}, {type=ENTITLEMENT, id=2c918087682f9a86016839c0509c1ab2}],
source_id_and_native_id_to_entitlement_ids_mappings=[
                    sailpoint.v2025.models.source_id_and_native_id_to_entitlement_ids_mapping.SourceIdAndNativeIdToEntitlementIdsMapping(
                        source_id = '2c91809773dee32014e13e122092014e', 
                        native_id_to_entitlement_ids_mappings = [
                            sailpoint.v2025.models.native_id_to_entitlement_ids_mapping.NativeIdToEntitlementIdsMapping(
                                native_id = 'jdoe', 
                                entitlement_ids = [
                                    '2c91809773dee32014e13e122092014e'
                                    ], )
                            ], )
                    ]
)

```
[[Back to top]](#) 

