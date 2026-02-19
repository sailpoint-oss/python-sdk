---
id: v2026-approval-config
title: ApprovalConfig
pagination_label: ApprovalConfig
sidebar_label: ApprovalConfig
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'ApprovalConfig', 'V2026ApprovalConfig'] 
slug: /tools/sdk/python/v2026/models/approval-config
tags: ['SDK', 'Software Development Kit', 'ApprovalConfig', 'V2026ApprovalConfig']
---

# ApprovalConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**approvers** | **str** | Approvers must be listed as a comma-separated string, with each entry representing an individual or group authorized to approve account creation or deletion requests. | [optional] 
**comments** |  **Enum** [  'APPROVAL',    'REJECTION',    'ALL',    'false' ] | Specifies the approval status for an account creation or deletion request. Allowed values are APPROVAL, REJECTION, ALL, and OFF. | [optional] 
}

## Example

```python
from sailpoint.v2026.models.approval_config import ApprovalConfig

approval_config = ApprovalConfig(
approvers='sourceOwner, accountOwner, manager, workgroup:f76ff96a-0815-402a-be1a-18cdc693b79f',
comments='REJECTION'
)

```
[[Back to top]](#) 

