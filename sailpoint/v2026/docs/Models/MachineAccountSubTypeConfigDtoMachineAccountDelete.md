---
id: v2026-machine-account-sub-type-config-dto-machine-account-delete
title: MachineAccountSubTypeConfigDtoMachineAccountDelete
pagination_label: MachineAccountSubTypeConfigDtoMachineAccountDelete
sidebar_label: MachineAccountSubTypeConfigDtoMachineAccountDelete
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'MachineAccountSubTypeConfigDtoMachineAccountDelete', 'V2026MachineAccountSubTypeConfigDtoMachineAccountDelete'] 
slug: /tools/sdk/python/v2026/models/machine-account-sub-type-config-dto-machine-account-delete
tags: ['SDK', 'Software Development Kit', 'MachineAccountSubTypeConfigDtoMachineAccountDelete', 'V2026MachineAccountSubTypeConfigDtoMachineAccountDelete']
---

# MachineAccountSubTypeConfigDtoMachineAccountDelete

Configuration options for machine account deletion, including whether approval is required, the list of authorized approvers, and the types of comments permitted during the approval workflow.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**approval_required** | **bool** | Indicates whether approval is required for an account deletion request. | [optional] [default to False]
**approval_config** | [**ApprovalConfig**](approval-config) |  | [optional] 
}

## Example

```python
from sailpoint.v2026.models.machine_account_sub_type_config_dto_machine_account_delete import MachineAccountSubTypeConfigDtoMachineAccountDelete

machine_account_sub_type_config_dto_machine_account_delete = MachineAccountSubTypeConfigDtoMachineAccountDelete(
approval_required=True,
approval_config=sailpoint.v2026.models.approval_config.ApprovalConfig(
                    approvers = 'sourceOwner, accountOwner, manager, workgroup:f76ff96a-0815-402a-be1a-18cdc693b79f', 
                    comments = 'REJECTION', )
)

```
[[Back to top]](#) 

