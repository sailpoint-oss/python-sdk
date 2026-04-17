---
id: ldap-action-workflow-action-directory-groups-attributes
title: LdapActionWorkflowActionDirectoryGroupsAttributes
pagination_label: LdapActionWorkflowActionDirectoryGroupsAttributes
sidebar_label: LdapActionWorkflowActionDirectoryGroupsAttributes
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'LdapActionWorkflowActionDirectoryGroupsAttributes', 'LdapActionWorkflowActionDirectoryGroupsAttributes'] 
slug: /tools/sdk/python//models/ldap-action-workflow-action-directory-groups-attributes
tags: ['SDK', 'Software Development Kit', 'LdapActionWorkflowActionDirectoryGroupsAttributes', 'LdapActionWorkflowActionDirectoryGroupsAttributes']
---

# LdapActionWorkflowActionDirectoryGroupsAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | the id. | [optional] 
**directory_id** | **str** | the id of the directory. | [optional] 
**group_label** | **str** | the group label. | [optional] 
**group_dn** | **str** | the group dn. | [optional] 
}

## Example

```python
from sailpoint.nerm.models.ldap_action_workflow_action_directory_groups_attributes import LdapActionWorkflowActionDirectoryGroupsAttributes

ldap_action_workflow_action_directory_groups_attributes = LdapActionWorkflowActionDirectoryGroupsAttributes(
id='33f072dd-13b4-41e1-8ea0-16f2a59b57c8',
directory_id='33f072dd-13b4-41e1-8ea0-16f2a59b57c8',
group_label='Admin',
group_dn='group'
)

```
[[Back to top]](#) 

