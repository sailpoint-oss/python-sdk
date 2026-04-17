---
id: form1
title: Form1
pagination_label: Form1
sidebar_label: Form1
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Form1', 'Form1'] 
slug: /tools/sdk/python//models/form1
tags: ['SDK', 'Software Development Kit', 'Form1', 'Form1']
---

# Form1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uid** | **str** | The user-specified identifier of the form | [optional] 
**description** | **str** | The description of the form | [optional] 
**name** | **str** | The name of the form | [optional] 
**archived** | **bool** | Determines whether the form is archived | [optional] 
}

## Example

```python
from sailpoint.nerm.models.form1 import Form1

form1 = Form1(
uid='form_uid',
description='Form for creating new profile',
name='My Form Name',
archived=False
)

```
[[Back to top]](#) 

