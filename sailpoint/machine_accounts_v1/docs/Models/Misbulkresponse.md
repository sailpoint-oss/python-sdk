---
id: misbulkresponse
title: Misbulkresponse
pagination_label: Misbulkresponse
sidebar_label: Misbulkresponse
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Misbulkresponse', 'Misbulkresponse'] 
slug: /tools/sdk/python/v1/models/misbulkresponse
tags: ['SDK', 'Software Development Kit', 'Misbulkresponse', 'Misbulkresponse']
---

# Misbulkresponse

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
from sailpoint.machine_accounts_v1.models.misbulkresponse import Misbulkresponse

misbulkresponse = Misbulkresponse(
id='ef38f94347e94562b5bb8424a56397d8',
status=200,
message='Updated successfully.'
)

```
[[Back to top]](#) 

