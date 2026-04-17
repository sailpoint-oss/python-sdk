---
id: get-forms200-response
title: GetForms200Response
pagination_label: GetForms200Response
sidebar_label: GetForms200Response
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'GetForms200Response', 'GetForms200Response'] 
slug: /tools/sdk/python//models/get-forms200-response
tags: ['SDK', 'Software Development Kit', 'GetForms200Response', 'GetForms200Response']
---

# GetForms200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**forms** | [**[]Form**](form) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.get_forms200_response import GetForms200Response

get_forms200_response = GetForms200Response(
forms=[
                    sailpoint.nerm.models.form.Form(
                        uid = 'form_uid', 
                        description = 'Form for creating new profile', 
                        name = 'My Form Name', 
                        archived = False, 
                        id = '2e06b876-f456-473d-bd65-b6435e0b6b2d', )
                    ]
)

```
[[Back to top]](#) 

