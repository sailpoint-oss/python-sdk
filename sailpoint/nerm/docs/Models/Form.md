---
id: form
title: Form
pagination_label: Form
sidebar_label: Form
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Form', 'Form'] 
slug: /tools/sdk/python//models/form
tags: ['SDK', 'Software Development Kit', 'Form', 'Form']
---

# Form


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uid** | **str** | The user-specified identifier of the form | [optional] 
**description** | **str** | The description of the form | [optional] 
**name** | **str** | The name of the form | [optional] 
**archived** | **bool** | Determines whether the form is archived | [optional] 
**id** | **str** | The id of the form | [optional] [readonly] 
}

## Example

```python
from sailpoint.nerm.models.form import Form

form = Form(
uid='form_uid',
description='Form for creating new profile',
name='My Form Name',
archived=False,
id='2e06b876-f456-473d-bd65-b6435e0b6b2d'
)

```
[[Back to top]](#) 

