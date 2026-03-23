---
id: beta-template-slack-custom-fields
title: TemplateSlackCustomFields
pagination_label: TemplateSlackCustomFields
sidebar_label: TemplateSlackCustomFields
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'TemplateSlackCustomFields', 'BetaTemplateSlackCustomFields'] 
slug: /tools/sdk/python/beta/models/template-slack-custom-fields
tags: ['SDK', 'Software Development Kit', 'TemplateSlackCustomFields', 'BetaTemplateSlackCustomFields']
---

# TemplateSlackCustomFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_type** | **str** | The type of request | [optional] 
**contains_deny** | **str** | Whether the request contains a deny action | [optional] 
**campaign_id** | **str** | The campaign ID | [optional] 
**campaign_status** | **str** | The campaign status | [optional] 
}

## Example

```python
from sailpoint.beta.models.template_slack_custom_fields import TemplateSlackCustomFields

template_slack_custom_fields = TemplateSlackCustomFields(
request_type='',
contains_deny='',
campaign_id='',
campaign_status=''
)

```
[[Back to top]](#) 

