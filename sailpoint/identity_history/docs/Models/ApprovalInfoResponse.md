---
id: approval-info-response
title: ApprovalInfoResponse
pagination_label: ApprovalInfoResponse
sidebar_label: ApprovalInfoResponse
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'ApprovalInfoResponse', 'ApprovalInfoResponse'] 
slug: /tools/sdk/python/identity-history/models/approval-info-response
tags: ['SDK', 'Software Development Kit', 'ApprovalInfoResponse', 'ApprovalInfoResponse']
---

# ApprovalInfoResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | the id of approver | [optional] 
**name** | **str** | the name of approver | [optional] 
**status** | **str** | the status of the approval request | [optional] 
}

## Example

```python
from sailpoint.identity_history.models.approval_info_response import ApprovalInfoResponse

approval_info_response = ApprovalInfoResponse(
id='8a80828f643d484f01643e14202e2000',
name='John Snow',
status='Approved'
)

```
[[Back to top]](#) 

