---
id: entitlement-connection-bulk-update-result-item
title: EntitlementConnectionBulkUpdateResultItem
pagination_label: EntitlementConnectionBulkUpdateResultItem
sidebar_label: EntitlementConnectionBulkUpdateResultItem
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'EntitlementConnectionBulkUpdateResultItem', 'EntitlementConnectionBulkUpdateResultItem'] 
slug: /tools/sdk/python/entitlement-connections/models/entitlement-connection-bulk-update-result-item
tags: ['SDK', 'Software Development Kit', 'EntitlementConnectionBulkUpdateResultItem', 'EntitlementConnectionBulkUpdateResultItem']
---

# EntitlementConnectionBulkUpdateResultItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection_id** | **str** | Connection ID processed in this row. | [optional] 
**type** | **str** | Requested or resulting connection type for the row. | [optional] 
**status** | **int** | Item-level result status code. | [optional] 
**description** | **str** | Item-level result message. | [optional] 
}

## Example

```python
from sailpoint.entitlement_connections.models.entitlement_connection_bulk_update_result_item import EntitlementConnectionBulkUpdateResultItem

entitlement_connection_bulk_update_result_item = EntitlementConnectionBulkUpdateResultItem(
connection_id='d532fa5cb15748e2873c6a01e5923ec4',
type='JIT',
status=201,
description='success'
)

```
[[Back to top]](#) 

