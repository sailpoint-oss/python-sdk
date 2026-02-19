---
id: v2026-machine-account-sub-type-config-dto
title: MachineAccountSubTypeConfigDto
pagination_label: MachineAccountSubTypeConfigDto
sidebar_label: MachineAccountSubTypeConfigDto
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'MachineAccountSubTypeConfigDto', 'V2026MachineAccountSubTypeConfigDto'] 
slug: /tools/sdk/python/v2026/models/machine-account-sub-type-config-dto
tags: ['SDK', 'Software Development Kit', 'MachineAccountSubTypeConfigDto', 'V2026MachineAccountSubTypeConfigDto']
---

# MachineAccountSubTypeConfigDto

Contains comprehensive configuration details for machine account subtype approval, including creation and deletion approval requirements, approver lists, form and entitlement references, and approval status options.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subtype_id** | **str** | Unique identifier representing the specific subtype of the machine account, used to distinguish between different machine account categories. | [optional] 
**machine_account_create** | [**MachineAccountSubTypeConfigDtoMachineAccountCreate**](machine-account-sub-type-config-dto-machine-account-create) |  | [optional] 
**machine_account_delete** | [**MachineAccountSubTypeConfigDtoMachineAccountDelete**](machine-account-sub-type-config-dto-machine-account-delete) |  | [optional] 
}

## Example

```python
from sailpoint.v2026.models.machine_account_sub_type_config_dto import MachineAccountSubTypeConfigDto

machine_account_sub_type_config_dto = MachineAccountSubTypeConfigDto(
subtype_id='1419fc28-a8ed-4a07-9f5c-0cb5dfad6311',
machine_account_create=sailpoint.v2026.models.machine_account_sub_type_config_dto_machine_account_create.MachineAccountSubTypeConfigDto_machineAccountCreate(
                    account_create_enabled = True, 
                    approval_required = True, 
                    form_id = '4f1bb61b-a0ab-4c0a-b9fb-20f44407b75a', 
                    entitlement_id = '858d2151-ff19-464b-ae0d-6938b3af2baf', 
                    approval_config = sailpoint.v2026.models.approval_config.ApprovalConfig(
                        approvers = 'sourceOwner, accountOwner, manager, workgroup:f76ff96a-0815-402a-be1a-18cdc693b79f', 
                        comments = 'REJECTION', ), ),
machine_account_delete=sailpoint.v2026.models.machine_account_sub_type_config_dto_machine_account_delete.MachineAccountSubTypeConfigDto_machineAccountDelete(
                    approval_required = True, 
                    approval_config = sailpoint.v2026.models.approval_config.ApprovalConfig(
                        approvers = 'sourceOwner, accountOwner, manager, workgroup:f76ff96a-0815-402a-be1a-18cdc693b79f', 
                        comments = 'REJECTION', ), )
)

```
[[Back to top]](#) 

