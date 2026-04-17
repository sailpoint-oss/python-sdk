---
id: invitation-action-configuration-attributes
title: InvitationActionConfigurationAttributes
pagination_label: InvitationActionConfigurationAttributes
sidebar_label: InvitationActionConfigurationAttributes
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'InvitationActionConfigurationAttributes', 'InvitationActionConfigurationAttributes'] 
slug: /tools/sdk/python//models/invitation-action-configuration-attributes
tags: ['SDK', 'Software Development Kit', 'InvitationActionConfigurationAttributes', 'InvitationActionConfigurationAttributes']
---

# InvitationActionConfigurationAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | the id. | [optional] 
**wait_for_completion** | **bool** | If the invitation action should pause the parent workflow to wait for completion. | [optional] 
**return_profile** | **bool** | If the invitation action should return a profile. | [optional] 
**portal_id** | **str** | the id of the portal. | [optional] 
**registration_workflow_id** | **str** | the id of the registration workflow. | [optional] 
**email_attribute_id** | **str** | the id of the email attribute. | [optional] 
**validate_completed_registration** | **bool** | If the action should validate against completed registrations by email address. | [optional] 
**validate_open_registration** | **bool** | If the action should validate against open registrations by email address. | [optional] 
}

## Example

```python
from sailpoint.nerm.models.invitation_action_configuration_attributes import InvitationActionConfigurationAttributes

invitation_action_configuration_attributes = InvitationActionConfigurationAttributes(
id='33f072dd-13b4-41e1-8ea0-16f2a59b57c8',
wait_for_completion=False,
return_profile=False,
portal_id='33f072dd-13b4-41e1-8ea0-16f2a59b57c8',
registration_workflow_id='33f072dd-13b4-41e1-8ea0-16f2a59b57c8',
email_attribute_id='33f072dd-13b4-41e1-8ea0-16f2a59b57c8',
validate_completed_registration=False,
validate_open_registration=False
)

```
[[Back to top]](#) 

