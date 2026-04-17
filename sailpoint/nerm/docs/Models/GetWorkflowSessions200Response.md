---
id: get-workflow-sessions200-response
title: GetWorkflowSessions200Response
pagination_label: GetWorkflowSessions200Response
sidebar_label: GetWorkflowSessions200Response
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'GetWorkflowSessions200Response', 'GetWorkflowSessions200Response'] 
slug: /tools/sdk/python//models/get-workflow-sessions200-response
tags: ['SDK', 'Software Development Kit', 'GetWorkflowSessions200Response', 'GetWorkflowSessions200Response']
---

# GetWorkflowSessions200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workflow_sessions** | [**[]WorkflowSession**](workflow-session) |  | [optional] 
**metadata** | [**Metadata**](metadata) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.get_workflow_sessions200_response import GetWorkflowSessions200Response

get_workflow_sessions200_response = GetWorkflowSessions200Response(
workflow_sessions=[
                    sailpoint.nerm.models.workflow_session.WorkflowSession(
                        id = '33f072dd-13b4-41e1-8ea0-16f2a59b57c8', 
                        uid = 'wsUid', 
                        workflow_id = '33f072dd-13b4-41e1-8ea0-16f2a59b57c8', 
                        requester_id = '33f072dd-13b4-41e1-8ea0-16f2a59b57c8', 
                        requester_type = 'User', 
                        profile_id = '33f072dd-13b4-41e1-8ea0-16f2a59b57c8', 
                        profile_ids = 59ed1cb6-9977-4965-9bfe-f2bcc242523e, 89ed1cb6-9977-4965-9bfe-f2bcc242523e, 
                        status = 'completed', 
                        attributes = {text_attribute_uid=static text, date_attribute_uid=01/15/2020, profile_select_attribute_uid=Profile Name, profile_search_attribute_uid=Profile Name, multiple_profile_search_attribute_uid=Profile Name,Second Profile Name,Third Profile Name, multiple_profile_select_attribute_uid=Profile Name,Second Profile Name,Third Profile Name, contributor_select_attribute_uid=User Name (user_email@test.com), contributor_search_attribute_uid=User Name (user_email@test.com), multiple_contributor_search_attribute_uid=User Name (user_email@test.com),Second User Name (user_email@test.com),Third User Name (user_email@test.com), owner_select_attribute_uid=User Name (user_email@test.com), owner_search_attribute_uid=User Name (user_email@test.com), dropdown_attribute_uid=yes, no, tags_attribute_uid=yes, no, checkbox_attribute_uid=yes, no, text_area_uid=static text, radio_attribute_uid=yes, no}, )
                    ],
metadata=sailpoint.nerm.models.metadata.Metadata(
                    limit = 56, 
                    offset = 56, 
                    total = 56, 
                    next = '/endpoint?limit=10&offset=60', 
                    previous = '/endpoint?limit=10&offset=40', )
)

```
[[Back to top]](#) 

