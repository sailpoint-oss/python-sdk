---
id: v2026-machine-subtype-approval-config
title: MachineSubtypeApprovalConfig
pagination_label: MachineSubtypeApprovalConfig
sidebar_label: MachineSubtypeApprovalConfig
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'MachineSubtypeApprovalConfig', 'V2026MachineSubtypeApprovalConfig'] 
slug: /tools/sdk/python/v2026/models/machine-subtype-approval-config
tags: ['SDK', 'Software Development Kit', 'MachineSubtypeApprovalConfig', 'V2026MachineSubtypeApprovalConfig']
---

# MachineSubtypeApprovalConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**approvers** | **str** | Comma separated string of approvers.  Following are the options for approver types: manager, sourceOwner, accountOwner, workgroup:{workgroupId} (Governance group).  Approval request will be assigned based on the order of the approvers passed.  Multiple workgroups(governance groups) can be selected as an approver.  >**Note:** accountOwner approver type is only for machine account delete approval settings. | [optional] 
**comments** | **str** | Comment configurations for the approval request.  Following are the options for comments: ALL, OFF, APPROVAL, REJECT. | [optional] 
}

## Example

```python
from sailpoint.v2026.models.machine_subtype_approval_config import MachineSubtypeApprovalConfig

machine_subtype_approval_config = MachineSubtypeApprovalConfig(
approvers='manager, workgroup:1419fc28-a8ed-4a07-9f5c-0cb5dfad6311',
comments='ALL'
)

```
[[Back to top]](#) 

