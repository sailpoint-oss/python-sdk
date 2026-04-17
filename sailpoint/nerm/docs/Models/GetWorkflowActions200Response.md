---
id: get-workflow-actions200-response
title: GetWorkflowActions200Response
pagination_label: GetWorkflowActions200Response
sidebar_label: GetWorkflowActions200Response
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'GetWorkflowActions200Response', 'GetWorkflowActions200Response'] 
slug: /tools/sdk/python//models/get-workflow-actions200-response
tags: ['SDK', 'Software Development Kit', 'GetWorkflowActions200Response', 'GetWorkflowActions200Response']
---

# GetWorkflowActions200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workflow_actions** | [**WorkflowAction**](workflow-action) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.get_workflow_actions200_response import GetWorkflowActions200Response

get_workflow_actions200_response = GetWorkflowActions200Response(
workflow_actions=sailpoint.nerm.models.workflow_action.WorkflowAction(
                    workflow_id = '33f072dd-13b4-41e1-8ea0-16f2a59b57c8', 
                    description = 'Require approval from another user or a group of users with a specific role.', 
                    page_id = '33f072dd-13b4-41e1-8ea0-16f2a59b57c8', 
                    add_requester_as_owner = True, 
                    email_attribute_id = '33f072dd-13b4-41e1-8ea0-16f2a59b57c8', 
                    email_addresses = [johndoe@gmail.com, janedoe@gmail.com], 
                    new_status = 'Active, Inactive, On Leave, Terminated', 
                    archived = False, 
                    skippable = False, 
                    requires_comment = False, )
)

```
[[Back to top]](#) 

