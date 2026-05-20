---
id: v2025-approval-config-escalation-config-escalation-chain-inner
title: ApprovalConfigEscalationConfigEscalationChainInner
pagination_label: ApprovalConfigEscalationConfigEscalationChainInner
sidebar_label: ApprovalConfigEscalationConfigEscalationChainInner
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'ApprovalConfigEscalationConfigEscalationChainInner', 'V2025ApprovalConfigEscalationConfigEscalationChainInner'] 
slug: /tools/sdk/python/v2025/models/approval-config-escalation-config-escalation-chain-inner
tags: ['SDK', 'Software Development Kit', 'ApprovalConfigEscalationConfigEscalationChainInner', 'V2025ApprovalConfigEscalationConfigEscalationChainInner']
---

# ApprovalConfigEscalationConfigEscalationChainInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tier** | **int** | Starting at 1 defines the order in which the identities will get assigned | [optional] 
**identity_id** | **str** | Optional Identity ID of the type of identity defined in the 'identityType' field. | [optional] 
**identity_type** |  **Enum** [  'IDENTITY',    'MANAGER_OF',    'ACCOUNT_OWNER',    'MACHINE_ACCOUNT_OWNER',    'MACHINE_IDENTITY_OWNER',    'MANAGER_OF_REQUESTED_TARGET_OWNER',    'MANAGER_OF_MACHINE_IDENTITY_OWNER',    'MANAGER_OF_ACCOUNT_OWNER',    'MANAGER_OF_MACHINE_ACCOUNT_OWNER',    'MANAGER_OF_REQUESTER',    'MANAGER_OF_REQUESTER_OWNER',    'MANAGER_OF_OWNER',    'ACCESS_PROFILE_OWNER',    'APPLICATION_OWNER',    'ENTITLEMENT_OWNER',    'ROLE_OWNER',    'SOURCE_OWNER',    'ACCESS_PROFILE_PRIMARY_OWNER',    'APPLICATION_PRIMARY_OWNER',    'ENTITLEMENT_PRIMARY_OWNER',    'ROLE_PRIMARY_OWNER',    'SOURCE_PRIMARY_OWNER' ] | Type of identityId in the escalation chain. | [optional] 
}

## Example

```python
from sailpoint.v2025.models.approval_config_escalation_config_escalation_chain_inner import ApprovalConfigEscalationConfigEscalationChainInner

approval_config_escalation_config_escalation_chain_inner = ApprovalConfigEscalationConfigEscalationChainInner(
tier=1,
identity_id='fdfda352157d4cc79bb749953131b457',
identity_type='IDENTITY'
)

```
[[Back to top]](#) 

