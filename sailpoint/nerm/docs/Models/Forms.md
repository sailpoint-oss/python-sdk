---
id: forms
title: Forms
pagination_label: Forms
sidebar_label: Forms
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Forms', 'Forms'] 
slug: /tools/sdk/python//models/forms
tags: ['SDK', 'Software Development Kit', 'Forms', 'Forms']
---

# Forms


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
from sailpoint.nerm.models.forms import Forms

forms = Forms(
uid='form_uid',
description='Form for creating new profile',
name='My Form Name',
archived=False
)

```
[[Back to top]](#) 

