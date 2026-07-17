---
id: entitlement-connection-bulk-update-item
title: EntitlementConnectionBulkUpdateItem
pagination_label: EntitlementConnectionBulkUpdateItem
sidebar_label: EntitlementConnectionBulkUpdateItem
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'EntitlementConnectionBulkUpdateItem', 'EntitlementConnectionBulkUpdateItem'] 
slug: /tools/sdk/python/entitlement-connections/models/entitlement-connection-bulk-update-item
tags: ['SDK', 'Software Development Kit', 'EntitlementConnectionBulkUpdateItem', 'EntitlementConnectionBulkUpdateItem']
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
from sailpoint.entitlement_connections.models.entitlement_connection_bulk_update_item import EntitlementConnectionBulkUpdateItem

entitlement_connection_bulk_update_item = EntitlementConnectionBulkUpdateItem(
connection_id='d532fa5cb15748e2873c6a01e5923ec4',
type='JIT'
)

```
[[Back to top]](#) 

