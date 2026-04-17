---
id: workflow-page
title: WorkflowPage
pagination_label: WorkflowPage
sidebar_label: WorkflowPage
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'WorkflowPage', 'WorkflowPage'] 
slug: /tools/sdk/python//models/workflow-page
tags: ['SDK', 'Software Development Kit', 'WorkflowPage', 'WorkflowPage']
---

# WorkflowPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uid** | **str** | The user-specified identifier of the page | [optional] 
**description** | **str** | The description of the page | [optional] 
**name** | **str** | The name of the page | [optional] 
**archived** | **bool** | Determines whether the page is archived | [optional] 
**id** | **str** | The id of the form | [optional] [readonly] 
}

## Example

```python
from sailpoint.nerm.models.workflow_page import WorkflowPage

workflow_page = WorkflowPage(
uid='page_uid',
description='Page for workflow',
name='My Page Name',
archived=False,
id='2e06b876-f456-473d-bd65-b6435e0b6b2d'
)

```
[[Back to top]](#) 

