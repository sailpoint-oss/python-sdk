---
id: ldap-action
title: LdapAction
pagination_label: LdapAction
sidebar_label: LdapAction
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'LdapAction', 'LdapAction'] 
slug: /tools/sdk/python//models/ldap-action
tags: ['SDK', 'Software Development Kit', 'LdapAction', 'LdapAction']
---

# LdapAction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workflow_id** | **str** | The workflow the workflow action belongs to. | [required]
**description** | **str** | The description of the workflow action. | [required]
**archived** | **bool** | If the workflow action is archived or not. | [optional] [default to False]
**store_type** |  **Enum** [  'Local',    'Directory' ] | the type of store. | [required]
**ldap_action_user_roles_attributes** | [**LdapActionLdapActionUserRolesAttributes**](ldap-action-ldap-action-user-roles-attributes) |  | [optional] 
**workflow_action_value_builders_attributes** | [**LdapActionWorkflowActionValueBuildersAttributes**](ldap-action-workflow-action-value-builders-attributes) |  | [optional] 
**workflow_action_directory_groups_attributes** | [**LdapActionWorkflowActionDirectoryGroupsAttributes**](ldap-action-workflow-action-directory-groups-attributes) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.ldap_action import LdapAction

ldap_action = LdapAction(
workflow_id='33f072dd-13b4-41e1-8ea0-16f2a59b57c8',
description='Create a Collaboration user account for this profile.',
archived=False,
store_type='Local',
ldap_action_user_roles_attributes=sailpoint.nerm.models.ldap_action_ldap_action_user_roles_attributes.LdapAction_ldap_action_user_roles_attributes(
                    id = '33f072dd-13b4-41e1-8ea0-16f2a59b57c8', 
                    role_id = '33f072dd-13b4-41e1-8ea0-16f2a59b57c8', ),
workflow_action_value_builders_attributes=sailpoint.nerm.models.ldap_action_workflow_action_value_builders_attributes.LdapAction_workflow_action_value_builders_attributes(
                    id = '33f072dd-13b4-41e1-8ea0-16f2a59b57c8', 
                    workflow_action_id = '33f072dd-13b4-41e1-8ea0-16f2a59b57c8', 
                    value_builder_id = '33f072dd-13b4-41e1-8ea0-16f2a59b57c8', 
                    position = 1, ),
workflow_action_directory_groups_attributes=sailpoint.nerm.models.ldap_action_workflow_action_directory_groups_attributes.LdapAction_workflow_action_directory_groups_attributes(
                    id = '33f072dd-13b4-41e1-8ea0-16f2a59b57c8', 
                    directory_id = '33f072dd-13b4-41e1-8ea0-16f2a59b57c8', 
                    group_label = 'Admin', 
                    group_dn = 'group', )
)

```
[[Back to top]](#) 

