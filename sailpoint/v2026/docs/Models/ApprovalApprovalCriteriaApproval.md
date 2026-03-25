---
id: v2026-approval-approval-criteria-approval
title: ApprovalApprovalCriteriaApproval
pagination_label: ApprovalApprovalCriteriaApproval
sidebar_label: ApprovalApprovalCriteriaApproval
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'ApprovalApprovalCriteriaApproval', 'V2026ApprovalApprovalCriteriaApproval'] 
slug: /tools/sdk/python/v2026/models/approval-approval-criteria-approval
tags: ['SDK', 'Software Development Kit', 'ApprovalApprovalCriteriaApproval', 'V2026ApprovalApprovalCriteriaApproval']
---

# ApprovalApprovalCriteriaApproval

Criteria for approval

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**calculation_type** |  **Enum** [  'COUNT',    'PERCENT' ] | This defines what the field \"value\" will be used as, either a count or percentage of the total approvers that need to approve | [optional] 
**value** | **int** | The value that needs to be met for the approval criteria | [optional] 
}

## Example

```python
from sailpoint.v2026.models.approval_approval_criteria_approval import ApprovalApprovalCriteriaApproval

approval_approval_criteria_approval = ApprovalApprovalCriteriaApproval(
calculation_type='COUNT',
value=70
)

```
[[Back to top]](#) 

