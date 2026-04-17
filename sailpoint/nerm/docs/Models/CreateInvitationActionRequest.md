---
id: create-invitation-action-request
title: CreateInvitationActionRequest
pagination_label: CreateInvitationActionRequest
sidebar_label: CreateInvitationActionRequest
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'CreateInvitationActionRequest', 'CreateInvitationActionRequest'] 
slug: /tools/sdk/python//models/create-invitation-action-request
tags: ['SDK', 'Software Development Kit', 'CreateInvitationActionRequest', 'CreateInvitationActionRequest']
---

# CreateInvitationActionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workflow_action** | [**InvitationAction**](invitation-action) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.create_invitation_action_request import CreateInvitationActionRequest

create_invitation_action_request = CreateInvitationActionRequest(
workflow_action=sailpoint.nerm.models.invitation_action.InvitationAction(
                    workflow_id = '33f072dd-13b4-41e1-8ea0-16f2a59b57c8', 
                    description = 'Creates a registration session associated with an email address', 
                    archived = False, 
                    configuration_attributes = sailpoint.nerm.models.invitation_action_configuration_attributes.InvitationAction_configuration_attributes(
                        id = '33f072dd-13b4-41e1-8ea0-16f2a59b57c8', 
                        wait_for_completion = False, 
                        return_profile = False, 
                        portal_id = '33f072dd-13b4-41e1-8ea0-16f2a59b57c8', 
                        registration_workflow_id = '33f072dd-13b4-41e1-8ea0-16f2a59b57c8', 
                        email_attribute_id = '33f072dd-13b4-41e1-8ea0-16f2a59b57c8', 
                        validate_completed_registration = False, 
                        validate_open_registration = False, ), 
                    workflow_action_email_attributes = sailpoint.nerm.models.invitation_action_workflow_action_email_attributes.InvitationAction_workflow_action_email_attributes(
                        id = '33f072dd-13b4-41e1-8ea0-16f2a59b57c8', 
                        workflow_action_id = '33f072dd-13b4-41e1-8ea0-16f2a59b57c8', 
                        email_id = '33f072dd-13b4-41e1-8ea0-16f2a59b57c8', 
                        type = 'StandardEmail', ), )
)

```
[[Back to top]](#) 

