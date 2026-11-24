---
id: human-account-subtype-config-human-account-create-approval-config
title: HumanAccountSubtypeConfigHumanAccountCreateApprovalConfig
pagination_label: HumanAccountSubtypeConfigHumanAccountCreateApprovalConfig
sidebar_label: HumanAccountSubtypeConfigHumanAccountCreateApprovalConfig
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'HumanAccountSubtypeConfigHumanAccountCreateApprovalConfig', 'HumanAccountSubtypeConfigHumanAccountCreateApprovalConfig'] 
slug: /tools/sdk/python/human-account-subtypes/models/human-account-subtype-config-human-account-create-approval-config
tags: ['SDK', 'Software Development Kit', 'HumanAccountSubtypeConfigHumanAccountCreateApprovalConfig', 'HumanAccountSubtypeConfigHumanAccountCreateApprovalConfig']
---

# HumanAccountSubtypeConfigHumanAccountCreateApprovalConfig

Approval settings for human account creation requests.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**approvers** | **str** | Comma-separated approver types, for example `manager, sourceOwner`. Approval requests are assigned in the order the approvers are listed. | [optional] 
**comments** |  **Enum** [  'ALL',    'APPROVAL',    'REJECTION',    'OFF' ] | Comment configuration for the approval request. | [optional] 
}

## Example

```python
from sailpoint.human_account_subtypes.models.human_account_subtype_config_human_account_create_approval_config import HumanAccountSubtypeConfigHumanAccountCreateApprovalConfig

human_account_subtype_config_human_account_create_approval_config = HumanAccountSubtypeConfigHumanAccountCreateApprovalConfig(
approvers='manager, sourceOwner',
comments='ALL'
)

```
[[Back to top]](#) 

