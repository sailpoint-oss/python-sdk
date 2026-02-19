---
id: v2026-machine-account-sub-type-config-dto-machine-account-create
title: MachineAccountSubTypeConfigDtoMachineAccountCreate
pagination_label: MachineAccountSubTypeConfigDtoMachineAccountCreate
sidebar_label: MachineAccountSubTypeConfigDtoMachineAccountCreate
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'MachineAccountSubTypeConfigDtoMachineAccountCreate', 'V2026MachineAccountSubTypeConfigDtoMachineAccountCreate'] 
slug: /tools/sdk/python/v2026/models/machine-account-sub-type-config-dto-machine-account-create
tags: ['SDK', 'Software Development Kit', 'MachineAccountSubTypeConfigDtoMachineAccountCreate', 'V2026MachineAccountSubTypeConfigDtoMachineAccountCreate']
---

# MachineAccountSubTypeConfigDtoMachineAccountCreate

Configuration options for machine account creation, including whether creation is enabled, if approval is required, associated form and entitlement IDs, and detailed approval settings such as approvers and allowed comment types.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_create_enabled** | **bool** | Specifies if the creation of machine accounts is allowed for this subtype. | [optional] [default to False]
**approval_required** | **bool** | Specifies if approval is needed before a machine account can be created for this subtype. | [optional] [default to False]
**form_id** | **str** | formId | [optional] 
**entitlement_id** | **str** | Configuration details specifying who can approve machine account creation requests and the types of comments allowed during the approval process. | [optional] 
**approval_config** | [**ApprovalConfig**](approval-config) |  | [optional] 
}

## Example

```python
from sailpoint.v2026.models.machine_account_sub_type_config_dto_machine_account_create import MachineAccountSubTypeConfigDtoMachineAccountCreate

machine_account_sub_type_config_dto_machine_account_create = MachineAccountSubTypeConfigDtoMachineAccountCreate(
account_create_enabled=True,
approval_required=True,
form_id='4f1bb61b-a0ab-4c0a-b9fb-20f44407b75a',
entitlement_id='858d2151-ff19-464b-ae0d-6938b3af2baf',
approval_config=sailpoint.v2026.models.approval_config.ApprovalConfig(
                    approvers = 'sourceOwner, accountOwner, manager, workgroup:f76ff96a-0815-402a-be1a-18cdc693b79f', 
                    comments = 'REJECTION', )
)

```
[[Back to top]](#) 

