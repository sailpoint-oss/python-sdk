---
id: create-workflow-page-request
title: CreateWorkflowPageRequest
pagination_label: CreateWorkflowPageRequest
sidebar_label: CreateWorkflowPageRequest
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'CreateWorkflowPageRequest', 'CreateWorkflowPageRequest'] 
slug: /tools/sdk/python//models/create-workflow-page-request
tags: ['SDK', 'Software Development Kit', 'CreateWorkflowPageRequest', 'CreateWorkflowPageRequest']
---

# CreateWorkflowPageRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | [**WorkflowPage**](workflow-page) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.create_workflow_page_request import CreateWorkflowPageRequest

create_workflow_page_request = CreateWorkflowPageRequest(
page=sailpoint.nerm.models.workflow_page.WorkflowPage(
                    uid = 'page_uid', 
                    description = 'Page for workflow', 
                    name = 'My Page Name', 
                    archived = False, 
                    id = '2e06b876-f456-473d-bd65-b6435e0b6b2d', )
)

```
[[Back to top]](#) 

