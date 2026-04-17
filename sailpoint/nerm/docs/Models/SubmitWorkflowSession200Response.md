---
id: submit-workflow-session200-response
title: SubmitWorkflowSession200Response
pagination_label: SubmitWorkflowSession200Response
sidebar_label: SubmitWorkflowSession200Response
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'SubmitWorkflowSession200Response', 'SubmitWorkflowSession200Response'] 
slug: /tools/sdk/python//models/submit-workflow-session200-response
tags: ['SDK', 'Software Development Kit', 'SubmitWorkflowSession200Response', 'SubmitWorkflowSession200Response']
---

# SubmitWorkflowSession200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workflow_session** | [**WorkflowSession**](workflow-session) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.submit_workflow_session200_response import SubmitWorkflowSession200Response

submit_workflow_session200_response = SubmitWorkflowSession200Response(
workflow_session=sailpoint.nerm.models.workflow_session.WorkflowSession(
                    id = '33f072dd-13b4-41e1-8ea0-16f2a59b57c8', 
                    uid = 'wsUid', 
                    workflow_id = '33f072dd-13b4-41e1-8ea0-16f2a59b57c8', 
                    requester_id = '33f072dd-13b4-41e1-8ea0-16f2a59b57c8', 
                    requester_type = 'User', 
                    profile_id = '33f072dd-13b4-41e1-8ea0-16f2a59b57c8', 
                    profile_ids = 59ed1cb6-9977-4965-9bfe-f2bcc242523e, 89ed1cb6-9977-4965-9bfe-f2bcc242523e, 
                    status = 'completed', 
                    attributes = {text_attribute_uid=static text, date_attribute_uid=01/15/2020, profile_select_attribute_uid=Profile Name, profile_search_attribute_uid=Profile Name, multiple_profile_search_attribute_uid=Profile Name,Second Profile Name,Third Profile Name, multiple_profile_select_attribute_uid=Profile Name,Second Profile Name,Third Profile Name, contributor_select_attribute_uid=User Name (user_email@test.com), contributor_search_attribute_uid=User Name (user_email@test.com), multiple_contributor_search_attribute_uid=User Name (user_email@test.com),Second User Name (user_email@test.com),Third User Name (user_email@test.com), owner_select_attribute_uid=User Name (user_email@test.com), owner_search_attribute_uid=User Name (user_email@test.com), dropdown_attribute_uid=yes, no, tags_attribute_uid=yes, no, checkbox_attribute_uid=yes, no, text_area_uid=static text, radio_attribute_uid=yes, no}, )
)

```
[[Back to top]](#) 

