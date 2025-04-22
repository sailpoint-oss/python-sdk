---
id: beta-access-request-config
title: AccessRequestConfig
pagination_label: AccessRequestConfig
sidebar_label: AccessRequestConfig
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'AccessRequestConfig', 'BetaAccessRequestConfig'] 
slug: /tools/sdk/python/beta/models/access-request-config
tags: ['SDK', 'Software Development Kit', 'AccessRequestConfig', 'BetaAccessRequestConfig']
---

# AccessRequestConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**approvals_must_be_external** | **bool** | If this is true, approvals must be processed by an external system. Also, if this is true, it blocks Request Center access requests and returns an error for any user who isn't an org admin. | [optional] [default to False]
**auto_approval_enabled** | **bool** | If this is true and the requester and reviewer are the same, the request is automatically approved. | [optional] [default to False]
**reauthorization_enabled** | **bool** | If this is true, reauthorization will be enforced for appropriately configured access items. Enablement of this feature is currently in a limited state. | [optional] [default to False]
**request_on_behalf_of_config** | [**RequestOnBehalfOfConfig**](request-on-behalf-of-config) |  | [optional] 
**approval_reminder_and_escalation_config** | [**ApprovalReminderAndEscalationConfig**](approval-reminder-and-escalation-config) |  | [optional] 
**entitlement_request_config** | [**EntitlementRequestConfig1**](entitlement-request-config1) |  | [optional] 
}

## Example

```python
from sailpoint.beta.models.access_request_config import AccessRequestConfig

access_request_config = AccessRequestConfig(
approvals_must_be_external=True,
auto_approval_enabled=True,
reauthorization_enabled=True,
request_on_behalf_of_config=sailpoint.beta.models.request_on_behalf_of_config.RequestOnBehalfOfConfig(
                    allow_request_on_behalf_of_anyone_by_anyone = True, 
                    allow_request_on_behalf_of_employee_by_manager = True, ),
approval_reminder_and_escalation_config=sailpoint.beta.models.approval_reminder_and_escalation_config.ApprovalReminderAndEscalationConfig(
                    days_until_escalation = 0, 
                    days_between_reminders = 0, 
                    max_reminders = 1, 
                    fallback_approver_ref = sailpoint.beta.models.identity_reference_with_name_and_email.IdentityReferenceWithNameAndEmail(
                        type = 'IDENTITY', 
                        id = '5168015d32f890ca15812c9180835d2e', 
                        name = 'Alison Ferguso', 
                        email = 'alison.ferguso@identitysoon.com', ), ),
entitlement_request_config=sailpoint.beta.models.entitlement_request_config_1.EntitlementRequestConfig_1(
                    allow_entitlement_request = True, 
                    request_comments_required = False, 
                    denied_comments_required = False, 
                    grant_request_approval_schemes = 'sourceOwner', )
)

```
[[Back to top]](#) 

