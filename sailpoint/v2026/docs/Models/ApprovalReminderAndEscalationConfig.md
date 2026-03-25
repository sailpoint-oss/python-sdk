---
id: v2026-approval-reminder-and-escalation-config
title: ApprovalReminderAndEscalationConfig
pagination_label: ApprovalReminderAndEscalationConfig
sidebar_label: ApprovalReminderAndEscalationConfig
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'ApprovalReminderAndEscalationConfig', 'V2026ApprovalReminderAndEscalationConfig'] 
slug: /tools/sdk/python/v2026/models/approval-reminder-and-escalation-config
tags: ['SDK', 'Software Development Kit', 'ApprovalReminderAndEscalationConfig', 'V2026ApprovalReminderAndEscalationConfig']
---

# ApprovalReminderAndEscalationConfig

Configuration for approval reminder and escalation behavior. Important: Modifying this object will override the sp-approval service's reminderConfig and escalationConfig settings. Changes made here take precedence over any configuration set directly in the sp-approval service. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**days_until_escalation** | **int** | Number of days to wait before the first reminder. If no reminders are configured, then this is the number of days to wait before escalation. | [optional] 
**days_between_reminders** | **int** | Number of days to wait between reminder notifications. | [optional] 
**max_reminders** | **int** | Maximum number of reminder notifications to send to the reviewer before approval escalation. The maximum allowed value is 20. | [optional] 
**fallback_approver_ref** | [**IdentityReferenceWithNameAndEmail**](identity-reference-with-name-and-email) |  | [optional] 
}

## Example

```python
from sailpoint.v2026.models.approval_reminder_and_escalation_config import ApprovalReminderAndEscalationConfig

approval_reminder_and_escalation_config = ApprovalReminderAndEscalationConfig(
days_until_escalation=0,
days_between_reminders=0,
max_reminders=1,
fallback_approver_ref=sailpoint.v2026.models.identity_reference_with_name_and_email.Identity Reference With Name And Email(
                    type = 'IDENTITY', 
                    id = '5168015d32f890ca15812c9180835d2e', 
                    name = 'Alison Ferguso', 
                    email = 'alison.ferguso@identitysoon.com', )
)

```
[[Back to top]](#) 

