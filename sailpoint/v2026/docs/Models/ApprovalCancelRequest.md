---
id: v2026-approval-cancel-request
title: ApprovalCancelRequest
pagination_label: ApprovalCancelRequest
sidebar_label: ApprovalCancelRequest
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'ApprovalCancelRequest', 'V2026ApprovalCancelRequest'] 
slug: /tools/sdk/python/v2026/models/approval-cancel-request
tags: ['SDK', 'Software Development Kit', 'ApprovalCancelRequest', 'V2026ApprovalCancelRequest']
---

# ApprovalCancelRequest

Request body for cancelling a single approval request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | Optional comment associated with the cancel request. | [optional] 
}

## Example

```python
from sailpoint.v2026.models.approval_cancel_request import ApprovalCancelRequest

approval_cancel_request = ApprovalCancelRequest(
comment='Cancelled by administrator'
)

```
[[Back to top]](#) 

