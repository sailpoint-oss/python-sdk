---
id: v2026-approval-approve-request
title: ApprovalApproveRequest
pagination_label: ApprovalApproveRequest
sidebar_label: ApprovalApproveRequest
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'ApprovalApproveRequest', 'V2026ApprovalApproveRequest'] 
slug: /tools/sdk/python/v2026/models/approval-approve-request
tags: ['SDK', 'Software Development Kit', 'ApprovalApproveRequest', 'V2026ApprovalApproveRequest']
---

# ApprovalApproveRequest

Approval Approve Request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_attributes** | **map[string]str** | Additional attributes as key-value pairs that are not part of the standard schema but can be included for custom data. | [optional] 
**comment** | **str** | Comment associated with the request. | [optional] 
}

## Example

```python
from sailpoint.v2026.models.approval_approve_request import ApprovalApproveRequest

approval_approve_request = ApprovalApproveRequest(
additional_attributes={additionalProp1=string, additionalProp2=string, additionalProp3=string},
comment='comment'
)

```
[[Back to top]](#) 

