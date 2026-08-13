---
id: approval-reject-request
title: ApprovalRejectRequest
pagination_label: ApprovalRejectRequest
sidebar_label: ApprovalRejectRequest
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'ApprovalRejectRequest', 'ApprovalRejectRequest'] 
slug: /tools/sdk/python/approvals/models/approval-reject-request
tags: ['SDK', 'Software Development Kit', 'ApprovalRejectRequest', 'ApprovalRejectRequest']
---

# ApprovalRejectRequest

Request body for rejecting an approval request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | Comment associated with the reject request. | [optional] 
**override_approver_id** | **str** | Optional field for ServiceNow Administrators to specify which member of a governance group to override/reject on behalf of. | [optional] 
}

## Example

```python
from sailpoint.approvals.models.approval_reject_request import ApprovalRejectRequest

approval_reject_request = ApprovalRejectRequest(
comment='string',
override_approver_id='12345678901234567890123456789012'
)

```
[[Back to top]](#) 

