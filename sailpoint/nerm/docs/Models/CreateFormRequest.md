---
id: create-form-request
title: CreateFormRequest
pagination_label: CreateFormRequest
sidebar_label: CreateFormRequest
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'CreateFormRequest', 'CreateFormRequest'] 
slug: /tools/sdk/python//models/create-form-request
tags: ['SDK', 'Software Development Kit', 'CreateFormRequest', 'CreateFormRequest']
---

# CreateFormRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**forms** | [**[]Forms**](forms) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.create_form_request import CreateFormRequest

create_form_request = CreateFormRequest(
forms=[
                    sailpoint.nerm.models.forms.Forms(
                        uid = 'form_uid', 
                        description = 'Form for creating new profile', 
                        name = 'My Form Name', 
                        archived = False, )
                    ]
)

```
[[Back to top]](#) 

