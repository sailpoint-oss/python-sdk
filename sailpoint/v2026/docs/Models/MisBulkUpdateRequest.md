---
id: v2026-mis-bulk-update-request
title: MisBulkUpdateRequest
pagination_label: MisBulkUpdateRequest
sidebar_label: MisBulkUpdateRequest
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'MisBulkUpdateRequest', 'V2026MisBulkUpdateRequest'] 
slug: /tools/sdk/python/v2026/models/mis-bulk-update-request
tags: ['SDK', 'Software Development Kit', 'MisBulkUpdateRequest', 'V2026MisBulkUpdateRequest']
---

# MisBulkUpdateRequest

Request body for applying the same JSON Patch document to multiple machine identities or machine accounts.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **[]str** | Machine identity or machine account IDs to update. | [required]
**json_patch** | [**[]JsonPatchOperation**](json-patch-operation) | JSON Patch operations to apply to each ID in the request (RFC 6902). | [required]
}

## Example

```python
from sailpoint.v2026.models.mis_bulk_update_request import MisBulkUpdateRequest

mis_bulk_update_request = MisBulkUpdateRequest(
ids=[ef38f94347e94562b5bb8424a56397d8],
json_patch=[{op=replace, path=/description, value=Updated description}]
)

```
[[Back to top]](#) 

