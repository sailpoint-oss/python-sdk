---
id: completed-approval-pre-approval-trigger-result
title: CompletedApprovalPreApprovalTriggerResult
pagination_label: CompletedApprovalPreApprovalTriggerResult
sidebar_label: CompletedApprovalPreApprovalTriggerResult
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'CompletedApprovalPreApprovalTriggerResult', 'CompletedApprovalPreApprovalTriggerResult'] 
slug: /tools/sdk/python/access-request-approvals/models/completed-approval-pre-approval-trigger-result
tags: ['SDK', 'Software Development Kit', 'CompletedApprovalPreApprovalTriggerResult', 'CompletedApprovalPreApprovalTriggerResult']
---

# CompletedApprovalPreApprovalTriggerResult

If the access request submitted event trigger is configured and this access request was intercepted by it, then this is the result of the trigger's decision to either approve or deny the request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | The comment from the trigger | [optional] 
**decision** | **CompletedApprovalState** |  | [optional] 
**reviewer** | **str** | The name of the approver | [optional] 
**var_date** | **datetime** | The date and time the trigger decided on the request | [optional] 
}

## Example

```python
from sailpoint.access_request_approvals.models.completed_approval_pre_approval_trigger_result import CompletedApprovalPreApprovalTriggerResult

completed_approval_pre_approval_trigger_result = CompletedApprovalPreApprovalTriggerResult(
comment='This request was autoapproved by our automated ETS subscriber',
decision='APPROVED',
reviewer='Automated AR Approval',
var_date='2022-06-07T19:18:40.748Z'
)

```
[[Back to top]](#) 

