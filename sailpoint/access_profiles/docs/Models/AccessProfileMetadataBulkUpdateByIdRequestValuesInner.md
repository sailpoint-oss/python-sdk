---
id: access-profile-metadata-bulk-update-by-id-request-values-inner
title: AccessProfileMetadataBulkUpdateByIdRequestValuesInner
pagination_label: AccessProfileMetadataBulkUpdateByIdRequestValuesInner
sidebar_label: AccessProfileMetadataBulkUpdateByIdRequestValuesInner
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'AccessProfileMetadataBulkUpdateByIdRequestValuesInner', 'AccessProfileMetadataBulkUpdateByIdRequestValuesInner'] 
slug: /tools/sdk/python/access-profiles/models/access-profile-metadata-bulk-update-by-id-request-values-inner
tags: ['SDK', 'Software Development Kit', 'AccessProfileMetadataBulkUpdateByIdRequestValuesInner', 'AccessProfileMetadataBulkUpdateByIdRequestValuesInner']
---

# AccessProfileMetadataBulkUpdateByIdRequestValuesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute** | **str** | The technical name of the metadata attribute. | [required]
**values** | **[]str** | The values of the attribute to be updated. | [required]
**object_type** | **str** | The type of the metadata attribute. Set to `custom` for custom metadata attributes, which require a suite license. | [optional] 
}

## Example

```python
from sailpoint.access_profiles.models.access_profile_metadata_bulk_update_by_id_request_values_inner import AccessProfileMetadataBulkUpdateByIdRequestValuesInner

access_profile_metadata_bulk_update_by_id_request_values_inner = AccessProfileMetadataBulkUpdateByIdRequestValuesInner(
attribute='iscFederalClassifications',
values=["secret"],
object_type='custom'
)

```
[[Back to top]](#) 

