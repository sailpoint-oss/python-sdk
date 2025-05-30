---
id: v2025-vendor-connector-mapping-deleted-by
title: VendorConnectorMappingDeletedBy
pagination_label: VendorConnectorMappingDeletedBy
sidebar_label: VendorConnectorMappingDeletedBy
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'VendorConnectorMappingDeletedBy', 'V2025VendorConnectorMappingDeletedBy'] 
slug: /tools/sdk/python/v2025/models/vendor-connector-mapping-deleted-by
tags: ['SDK', 'Software Development Kit', 'VendorConnectorMappingDeletedBy', 'V2025VendorConnectorMappingDeletedBy']
---

# VendorConnectorMappingDeletedBy

An object representing the nullable identifier of the user who deleted the mapping.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**string** | **str** | The identifier of the user who deleted the mapping, if applicable. | [optional] 
**valid** | **bool** | A flag indicating if the 'String' field is set and valid, i.e., if the mapping has been deleted. | [optional] [default to False]
}

## Example

```python
from sailpoint.v2025.models.vendor_connector_mapping_deleted_by import VendorConnectorMappingDeletedBy

vendor_connector_mapping_deleted_by = VendorConnectorMappingDeletedBy(
string='',
valid=False
)

```
[[Back to top]](#) 

