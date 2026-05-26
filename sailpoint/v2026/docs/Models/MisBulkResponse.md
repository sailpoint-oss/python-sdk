---
id: v2026-mis-bulk-response
title: MisBulkResponse
pagination_label: MisBulkResponse
sidebar_label: MisBulkResponse
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'MisBulkResponse', 'V2026MisBulkResponse'] 
slug: /tools/sdk/python/v2026/models/mis-bulk-response
tags: ['SDK', 'Software Development Kit', 'MisBulkResponse', 'V2026MisBulkResponse']
---

# MisBulkResponse

Per-ID result for a machine identity or machine account bulk operation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Machine identity or machine account ID from the request. | [required]
**status** | **int** | HTTP status code for this ID. For example, 200 indicates success, 404 indicates the resource was not found or is not accessible to the caller, and 409 indicates a conflict such as a duplicate ID in the batch. | [required]
**message** | **str** | Human-readable detail for this result. | [optional] 
}

## Example

```python
from sailpoint.v2026.models.mis_bulk_response import MisBulkResponse

mis_bulk_response = MisBulkResponse(
id='ef38f94347e94562b5bb8424a56397d8',
status=200,
message='Updated successfully.'
)

```
[[Back to top]](#) 

