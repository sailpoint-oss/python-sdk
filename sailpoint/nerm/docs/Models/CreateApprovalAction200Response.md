---
id: create-approval-action200-response
title: CreateApprovalAction200Response
pagination_label: CreateApprovalAction200Response
sidebar_label: CreateApprovalAction200Response
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'CreateApprovalAction200Response', 'CreateApprovalAction200Response'] 
slug: /tools/sdk/python//models/create-approval-action200-response
tags: ['SDK', 'Software Development Kit', 'CreateApprovalAction200Response', 'CreateApprovalAction200Response']
---

# CreateApprovalAction200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workflow_action** | [**WorkflowAction**](workflow-action) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.create_approval_action200_response import CreateApprovalAction200Response

create_approval_action200_response = CreateApprovalAction200Response(
workflow_action=sailpoint.nerm.models.workflow_action.WorkflowAction(
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

