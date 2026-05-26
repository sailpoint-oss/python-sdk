---
id: v2026-mis-bulk-request
title: MisBulkRequest
pagination_label: MisBulkRequest
sidebar_label: MisBulkRequest
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'MisBulkRequest', 'V2026MisBulkRequest'] 
slug: /tools/sdk/python/v2026/models/mis-bulk-request
tags: ['SDK', 'Software Development Kit', 'MisBulkRequest', 'V2026MisBulkRequest']
---

# MisBulkRequest

Request body listing machine identity or machine account IDs for a bulk operation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **[]str** | Machine identity or machine account IDs to include in the bulk operation. | [required]
}

## Example

```python
from sailpoint.v2026.models.mis_bulk_request import MisBulkRequest

mis_bulk_request = MisBulkRequest(
ids=[ef38f94347e94562b5bb8424a56397d8, 2c91808a7813090a017814121919ecca]
)

```
[[Back to top]](#) 

