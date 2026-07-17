---
id: role-metadata-bulk-update-by-id-request-values-inner
title: RoleMetadataBulkUpdateByIdRequestValuesInner
pagination_label: RoleMetadataBulkUpdateByIdRequestValuesInner
sidebar_label: RoleMetadataBulkUpdateByIdRequestValuesInner
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'RoleMetadataBulkUpdateByIdRequestValuesInner', 'RoleMetadataBulkUpdateByIdRequestValuesInner'] 
slug: /tools/sdk/python/roles/models/role-metadata-bulk-update-by-id-request-values-inner
tags: ['SDK', 'Software Development Kit', 'RoleMetadataBulkUpdateByIdRequestValuesInner', 'RoleMetadataBulkUpdateByIdRequestValuesInner']
---

# RoleMetadataBulkUpdateByIdRequestValuesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute** | **str** | the key of metadata attribute | [required]
**values** | **[]str** | the values of attribute to be updated | [required]
}

## Example

```python
from sailpoint.roles.models.role_metadata_bulk_update_by_id_request_values_inner import RoleMetadataBulkUpdateByIdRequestValuesInner

role_metadata_bulk_update_by_id_request_values_inner = RoleMetadataBulkUpdateByIdRequestValuesInner(
attribute='iscFederalClassifications',
values=["secret"]
)

```
[[Back to top]](#) 

