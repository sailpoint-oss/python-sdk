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
                        tenant_id = 'd3c10266-1a31-4acc-b01e-44a3d1c56615', 
                        id = '5804e7d6-e04b-400f-9fb8-dff894419a2f', 
                        scope = 'DOMAIN_OBJECT', 
                        reminder_config = sailpoint.v2026.models.approval_config_reminder_config.ApprovalConfig_reminderConfig(
                            enabled = False, 
                            days_until_first_reminder = 0, 
                            reminder_cron_schedule = '1 1 1 1 1', 
                            max_reminders = 5, ), 
                        escalation_config = sailpoint.v2026.models.approval_config_escalation_config.ApprovalConfig_escalationConfig(
                            enabled = True, 
                            days_until_first_escalation = 2, 
                            escalation_cron_schedule = '*/5 * * * *', 
                            escalation_chain = [
                                sailpoint.v2026.models.approval_config_escalation_config_escalation_chain_inner.ApprovalConfig_escalationConfig_escalationChain_inner(
                                    chain_id = 'ef85d1a8-41ef-433a-8153-0b1f59e7b26a', 
                                    tier = 1, 
                                    identity_id = 'fdfda352157d4cc79bb749953131b457', 
                                    identity_type = 'IDENTITY', )
                                ], ), 
                        timeout_config = sailpoint.v2026.models.approval_config_timeout_config.ApprovalConfig_timeoutConfig(
                            enabled = True, 
                            days_until_timeout = 2, 
                            timeout_result = 'EXPIRED', ), 
                        cron_timezone = sailpoint.v2026.models.approval_config_cron_timezone.ApprovalConfig_cronTimezone(
                            location = 'America/New_York', 
                            offset = '', ), 
                        serial_chain = [
                            sailpoint.v2026.models.approval_config_serial_chain_inner.ApprovalConfig_serialChain_inner(
                                chain_id = '23dc206e-2a9e-4f98-93db-8d6e342cca18', 
                                tier = 1, 
                                identity_id = '2c9180858090ea8801809a0465e829da', 
                                identity_type = 'IDENTITY', )
                            ], 
                        requires_comment = 'ALL', 
                        fallback_approver = sailpoint.v2026.models.approval_identity.Approval Identity(
                            email = 'mail@mail.com', 
                            identity_id = '17e633e7d57e481569df76323169deb6a', 
                            members = [
                                sailpoint.v2026.models.approval_identity_members_inner.ApprovalIdentity_members_inner(
                                    email = 'mail@mail.com', 
                                    id = '17e633e7d57e481569df76323169deb6a', 
                                    name = 'Bob Neil', 
                                    type = 'IDENTITY', )
                                ], 
                            name = 'Jim Bob', 
                            owner_of = [
                                sailpoint.v2026.models.approval_identity_owner_of_inner.ApprovalIdentity_ownerOf_inner(
                                    id = 'string', 
                                    name = 'Access Request App', 
                                    type = 'APPLICATION', )
                                ], 
                            serial_order = 0, 
                            type = 'IDENTITY', ), 
                        auto_approve = 'false', ), ),
machine_account_delete=sailpoint.v2026.models.machine_account_sub_type_config_dto_machine_account_delete.MachineAccountSubTypeConfigDto_machineAccountDelete(
                    approval_required = True, 
                    approval_config = sailpoint.v2026.models.approval_config.ApprovalConfig(
                        tenant_id = 'd3c10266-1a31-4acc-b01e-44a3d1c56615', 
                        id = '5804e7d6-e04b-400f-9fb8-dff894419a2f', 
                        scope = 'DOMAIN_OBJECT', 
                        reminder_config = sailpoint.v2026.models.approval_config_reminder_config.ApprovalConfig_reminderConfig(
                            enabled = False, 
                            days_until_first_reminder = 0, 
                            reminder_cron_schedule = '1 1 1 1 1', 
                            max_reminders = 5, ), 
                        escalation_config = sailpoint.v2026.models.approval_config_escalation_config.ApprovalConfig_escalationConfig(
                            enabled = True, 
                            days_until_first_escalation = 2, 
                            escalation_cron_schedule = '*/5 * * * *', 
                            escalation_chain = [
                                sailpoint.v2026.models.approval_config_escalation_config_escalation_chain_inner.ApprovalConfig_escalationConfig_escalationChain_inner(
                                    chain_id = 'ef85d1a8-41ef-433a-8153-0b1f59e7b26a', 
                                    tier = 1, 
                                    identity_id = 'fdfda352157d4cc79bb749953131b457', 
                                    identity_type = 'IDENTITY', )
                                ], ), 
                        timeout_config = sailpoint.v2026.models.approval_config_timeout_config.ApprovalConfig_timeoutConfig(
                            enabled = True, 
                            days_until_timeout = 2, 
                            timeout_result = 'EXPIRED', ), 
                        cron_timezone = sailpoint.v2026.models.approval_config_cron_timezone.ApprovalConfig_cronTimezone(
                            location = 'America/New_York', 
                            offset = '', ), 
                        serial_chain = [
                            sailpoint.v2026.models.approval_config_serial_chain_inner.ApprovalConfig_serialChain_inner(
                                chain_id = '23dc206e-2a9e-4f98-93db-8d6e342cca18', 
                                tier = 1, 
                                identity_id = '2c9180858090ea8801809a0465e829da', 
                                identity_type = 'IDENTITY', )
                            ], 
                        requires_comment = 'ALL', 
                        fallback_approver = sailpoint.v2026.models.approval_identity.Approval Identity(
                            email = 'mail@mail.com', 
                            identity_id = '17e633e7d57e481569df76323169deb6a', 
                            members = [
                                sailpoint.v2026.models.approval_identity_members_inner.ApprovalIdentity_members_inner(
                                    email = 'mail@mail.com', 
                                    id = '17e633e7d57e481569df76323169deb6a', 
                                    name = 'Bob Neil', 
                                    type = 'IDENTITY', )
                                ], 
                            name = 'Jim Bob', 
                            owner_of = [
                                sailpoint.v2026.models.approval_identity_owner_of_inner.ApprovalIdentity_ownerOf_inner(
                                    id = 'string', 
                                    name = 'Access Request App', 
                                    type = 'APPLICATION', )
                                ], 
                            serial_order = 0, 
                            type = 'IDENTITY', ), 
                        auto_approve = 'false', ), )
)

```
[[Back to top]](#) 

