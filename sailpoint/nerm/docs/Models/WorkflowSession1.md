---
id: workflow-session1
title: WorkflowSession1
pagination_label: WorkflowSession1
sidebar_label: WorkflowSession1
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'WorkflowSession1', 'WorkflowSession1'] 
slug: /tools/sdk/python//models/workflow-session1
tags: ['SDK', 'Software Development Kit', 'WorkflowSession1', 'WorkflowSession1']
---

# WorkflowSession1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workflow_id** | **str** | The workflow id. | [required]
**requester_id** | **str** | The requester's id. | [required]
**requester_type** |  **Enum** [  'User',    'NeprofileUser',    'NeaccessUser' ] | The requester type. | [required]
**profile_id** | **str** | The profile this workflow session will be working with. Only Applicable for Update workflows | [optional] 
**profile_ids** | **[]str** | The profiles this workflow session will be working with. Only Applicable for Batch workflows | [optional] 
**attributes** | **map[string]str** | The attributes associated with the workflow session. | [optional] 
}

## Example

```python
from sailpoint.nerm.models.workflow_session1 import WorkflowSession1

workflow_session1 = WorkflowSession1(
workflow_id='33f072dd-13b4-41e1-8ea0-16f2a59b57c8',
requester_id='33f072dd-13b4-41e1-8ea0-16f2a59b57c8',
requester_type='User',
profile_id='33f072dd-13b4-41e1-8ea0-16f2a59b57c8',
profile_ids=[59ed1cb6-9977-4965-9bfe-f2bcc242523e, 89ed1cb6-9977-4965-9bfe-f2bcc242523e],
attributes={text_attribute_uid=static text, date_attribute_uid=01/15/2020, profile_select_attribute_uid=79ed1cb6-9977-4965-9bfe-f2bcc242523e, multiple_profile_select_attribute_uid=59ed1cb6-9977-4965-9bfe-f2bcc242523e, 89ed1cb6-9977-4965-9bfe-f2bcc242523e, profile_search_attribute_uid=79ed1cb6-9977-4965-9bfe-f2bcc242523e, multiple_profile_search_attribute_uid=59ed1cb6-9977-4965-9bfe-f2bcc242523e, 89ed1cb6-9977-4965-9bfe-f2bcc242523e, contributor_select_attribute_uid=49ed1cb6-9977-4965-9bfe-f2bcc2425244, contributor_search_attribute_uid=49ed1cb6-9977-4965-9bfe-f2bcc2425244, multiple_contributor_search_attribute_uid=59ed1cb6-9977-4965-9bfe-f2bcc242523e, 89ed1cb6-9977-4965-9bfe-f2bcc242523e, owner_select_attribute_uid=79ed1cb6-9977-4965-9bfe-f2bcc242523e, owner_search_attribute_uid=79ed1cb6-9977-4965-9bfe-f2bcc242523e, dropdown_attribute_uid=yes, no, tags_attribute_uid=yes, no, checkbox_attribute_uid=yes, no, text_area_uid=static text, radio_attribute_uid=yes, no}
)

```
[[Back to top]](#) 

