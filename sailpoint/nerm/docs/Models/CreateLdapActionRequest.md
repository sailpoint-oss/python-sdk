---
id: create-ldap-action-request
title: CreateLdapActionRequest
pagination_label: CreateLdapActionRequest
sidebar_label: CreateLdapActionRequest
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'CreateLdapActionRequest', 'CreateLdapActionRequest'] 
slug: /tools/sdk/python//models/create-ldap-action-request
tags: ['SDK', 'Software Development Kit', 'CreateLdapActionRequest', 'CreateLdapActionRequest']
---

# CreateLdapActionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workflow_action** | [**LdapAction**](ldap-action) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.create_ldap_action_request import CreateLdapActionRequest

create_ldap_action_request = CreateLdapActionRequest(
workflow_action=sailpoint.nerm.models.ldap_action.LdapAction(
                    workflow_id = '33f072dd-13b4-41e1-8ea0-16f2a59b57c8', 
                    description = 'Create a Collaboration user account for this profile.', 
                    archived = False, 
                    store_type = 'Local', 
                    ldap_action_user_roles_attributes = sailpoint.nerm.models.ldap_action_ldap_action_user_roles_attributes.LdapAction_ldap_action_user_roles_attributes(
                        id = '33f072dd-13b4-41e1-8ea0-16f2a59b57c8', 
                        role_id = '33f072dd-13b4-41e1-8ea0-16f2a59b57c8', ), 
                    workflow_action_value_builders_attributes = sailpoint.nerm.models.ldap_action_workflow_action_value_builders_attributes.LdapAction_workflow_action_value_builders_attributes(
                        id = '33f072dd-13b4-41e1-8ea0-16f2a59b57c8', 
                        workflow_action_id = '33f072dd-13b4-41e1-8ea0-16f2a59b57c8', 
                        value_builder_id = '33f072dd-13b4-41e1-8ea0-16f2a59b57c8', 
                        position = 1, ), 
                    workflow_action_directory_groups_attributes = sailpoint.nerm.models.ldap_action_workflow_action_directory_groups_attributes.LdapAction_workflow_action_directory_groups_attributes(
                        id = '33f072dd-13b4-41e1-8ea0-16f2a59b57c8', 
                        directory_id = '33f072dd-13b4-41e1-8ea0-16f2a59b57c8', 
                        group_label = 'Admin', 
                        group_dn = 'group', ), )
)

```
[[Back to top]](#) 

