---
id: v2026-bulk-reject-request-dto
title: BulkRejectRequestDTO
pagination_label: BulkRejectRequestDTO
sidebar_label: BulkRejectRequestDTO
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'BulkRejectRequestDTO', 'V2026BulkRejectRequestDTO'] 
slug: /tools/sdk/python/v2026/models/bulk-reject-request-dto
tags: ['SDK', 'Software Development Kit', 'BulkRejectRequestDTO', 'V2026BulkRejectRequestDTO']
---

# BulkRejectRequestDTO

BulkRejectRequestDTO is the input struct that represents the request body required to facilitate a bulk reject action for a set of generic approval requests.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**approval_ids** | **[]str** | Array of Approval IDs to be bulk rejected | [optional] 
**comment** | **str** | Optional comment to include with the bulk reject request | [optional] 
}

## Example

```python
from sailpoint.v2026.models.bulk_reject_request_dto import BulkRejectRequestDTO

bulk_reject_request_dto = BulkRejectRequestDTO(
approval_ids=[38453251-6be2-5f8f-df93-5ce19e295837, 38453251-6be2-5f8f-df93-5ce19e295838],
comment='Bulk reject by admin'
)

```
[[Back to top]](#) 

