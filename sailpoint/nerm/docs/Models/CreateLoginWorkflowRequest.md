---
id: create-login-workflow-request
title: CreateLoginWorkflowRequest
pagination_label: CreateLoginWorkflowRequest
sidebar_label: CreateLoginWorkflowRequest
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'CreateLoginWorkflowRequest', 'CreateLoginWorkflowRequest'] 
slug: /tools/sdk/python//models/create-login-workflow-request
tags: ['SDK', 'Software Development Kit', 'CreateLoginWorkflowRequest', 'CreateLoginWorkflowRequest']
---

# CreateLoginWorkflowRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workflow** | [**LoginWorkflow**](login-workflow) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.create_login_workflow_request import CreateLoginWorkflowRequest

create_login_workflow_request = CreateLoginWorkflowRequest(
workflow=sailpoint.nerm.models.login_workflow.LoginWorkflow(
                    profile_type_id = '33f072dd-13b4-41e1-8ea0-16f2a59b57c8', 
                    status = 'Enabled', 
                    uid = 'my_uid', 
                    name = 'my_workflow', 
                    options = sailpoint.nerm.models.login_workflow_options.LoginWorkflow_options(
                        expiration_time = 1, ), 
                    disable_failure_email_notifications = False, )
)

```
[[Back to top]](#) 

