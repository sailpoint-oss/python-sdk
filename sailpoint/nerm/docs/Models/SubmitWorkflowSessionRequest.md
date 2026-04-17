---
id: submit-workflow-session-request
title: SubmitWorkflowSessionRequest
pagination_label: SubmitWorkflowSessionRequest
sidebar_label: SubmitWorkflowSessionRequest
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'SubmitWorkflowSessionRequest', 'SubmitWorkflowSessionRequest'] 
slug: /tools/sdk/python//models/submit-workflow-session-request
tags: ['SDK', 'Software Development Kit', 'SubmitWorkflowSessionRequest', 'SubmitWorkflowSessionRequest']
---

# SubmitWorkflowSessionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workflow_session** | [**WorkflowSession1**](workflow-session1) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.submit_workflow_session_request import SubmitWorkflowSessionRequest

submit_workflow_session_request = SubmitWorkflowSessionRequest(
workflow_session=sailpoint.nerm.models.workflow_session_1.WorkflowSession_1(
                    workflow_id = '33f072dd-13b4-41e1-8ea0-16f2a59b57c8', 
                    requester_id = '33f072dd-13b4-41e1-8ea0-16f2a59b57c8', 
                    requester_type = 'User', 
                    profile_id = '33f072dd-13b4-41e1-8ea0-16f2a59b57c8', 
                    profile_ids = [59ed1cb6-9977-4965-9bfe-f2bcc242523e, 89ed1cb6-9977-4965-9bfe-f2bcc242523e], 
                    attributes = {text_attribute_uid=static text, date_attribute_uid=01/15/2020, profile_select_attribute_uid=79ed1cb6-9977-4965-9bfe-f2bcc242523e, multiple_profile_select_attribute_uid=59ed1cb6-9977-4965-9bfe-f2bcc242523e, 89ed1cb6-9977-4965-9bfe-f2bcc242523e, profile_search_attribute_uid=79ed1cb6-9977-4965-9bfe-f2bcc242523e, multiple_profile_search_attribute_uid=59ed1cb6-9977-4965-9bfe-f2bcc242523e, 89ed1cb6-9977-4965-9bfe-f2bcc242523e, contributor_select_attribute_uid=49ed1cb6-9977-4965-9bfe-f2bcc2425244, contributor_search_attribute_uid=49ed1cb6-9977-4965-9bfe-f2bcc2425244, multiple_contributor_search_attribute_uid=59ed1cb6-9977-4965-9bfe-f2bcc242523e, 89ed1cb6-9977-4965-9bfe-f2bcc242523e, owner_select_attribute_uid=79ed1cb6-9977-4965-9bfe-f2bcc242523e, owner_search_attribute_uid=79ed1cb6-9977-4965-9bfe-f2bcc242523e, dropdown_attribute_uid=yes, no, tags_attribute_uid=yes, no, checkbox_attribute_uid=yes, no, text_area_uid=static text, radio_attribute_uid=yes, no}, )
)

```
[[Back to top]](#) 

