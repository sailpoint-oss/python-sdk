---
id: v2024-template-slack-auto-approval-data
title: TemplateSlackAutoApprovalData
pagination_label: TemplateSlackAutoApprovalData
sidebar_label: TemplateSlackAutoApprovalData
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'TemplateSlackAutoApprovalData', 'V2024TemplateSlackAutoApprovalData'] 
slug: /tools/sdk/python/v2024/models/template-slack-auto-approval-data
tags: ['SDK', 'Software Development Kit', 'TemplateSlackAutoApprovalData', 'V2024TemplateSlackAutoApprovalData']
---

# TemplateSlackAutoApprovalData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_auto_approved** | **str** | Whether the request was auto-approved | [optional] 
**item_id** | **str** | The item ID | [optional] 
**item_type** | **str** | The item type | [optional] 
**auto_approval_message_json** | **str** | JSON message for auto-approval | [optional] 
**auto_approval_title** | **str** | Title for auto-approval | [optional] 
}

## Example

```python
from sailpoint.v2024.models.template_slack_auto_approval_data import TemplateSlackAutoApprovalData

template_slack_auto_approval_data = TemplateSlackAutoApprovalData(
is_auto_approved='',
item_id='',
item_type='',
auto_approval_message_json='',
auto_approval_title=''
)

```
[[Back to top]](#) 

