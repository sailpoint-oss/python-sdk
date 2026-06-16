---
id: v2026-entitlement-connection-bulk-update-item
title: EntitlementConnectionBulkUpdateItem
pagination_label: EntitlementConnectionBulkUpdateItem
sidebar_label: EntitlementConnectionBulkUpdateItem
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'EntitlementConnectionBulkUpdateItem', 'V2026EntitlementConnectionBulkUpdateItem'] 
slug: /tools/sdk/python/v2026/models/entitlement-connection-bulk-update-item
tags: ['SDK', 'Software Development Kit', 'EntitlementConnectionBulkUpdateItem', 'V2026EntitlementConnectionBulkUpdateItem']
---

# EntitlementConnectionBulkUpdateItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection_id** | **str** | Connection ID to update. | [required]
**type** |  **Enum** [  'JIT',    'STANDING' ] | Target connection type. | [required]
}

## Example

```python
from sailpoint.v2026.models.entitlement_connection_bulk_update_item import EntitlementConnectionBulkUpdateItem

entitlement_connection_bulk_update_item = EntitlementConnectionBulkUpdateItem(
connection_id='d532fa5cb15748e2873c6a01e5923ec4',
type='JIT'
)

```
[[Back to top]](#) 

