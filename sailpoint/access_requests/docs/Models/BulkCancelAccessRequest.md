---
id: bulk-cancel-access-request
title: BulkCancelAccessRequest
pagination_label: BulkCancelAccessRequest
sidebar_label: BulkCancelAccessRequest
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'BulkCancelAccessRequest', 'BulkCancelAccessRequest'] 
slug: /tools/sdk/python/access-requests/models/bulk-cancel-access-request
tags: ['SDK', 'Software Development Kit', 'BulkCancelAccessRequest', 'BulkCancelAccessRequest']
---

# BulkCancelAccessRequest

Request body payload for bulk cancel access request endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_request_ids** | **[]str** | List of access requests ids to cancel the pending requests | [required]
**comment** | **str** | Reason for cancelling the pending access request. | [required]
}

## Example

```python
from sailpoint.access_requests.models.bulk_cancel_access_request import BulkCancelAccessRequest

bulk_cancel_access_request = BulkCancelAccessRequest(
access_request_ids=["2c9180835d2e5168015d32f890ca1581","2c9180835d2e5168015d32f890ca1582"],
comment='I requested this role by mistake.'
)

```
[[Back to top]](#) 

