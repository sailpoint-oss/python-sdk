---
id: get-form-attributes200-response
title: GetFormAttributes200Response
pagination_label: GetFormAttributes200Response
sidebar_label: GetFormAttributes200Response
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'GetFormAttributes200Response', 'GetFormAttributes200Response'] 
slug: /tools/sdk/python//models/get-form-attributes200-response
tags: ['SDK', 'Software Development Kit', 'GetFormAttributes200Response', 'GetFormAttributes200Response']
---

# GetFormAttributes200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**form_attribute** | [**FormAttribute**](form-attribute) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.get_form_attributes200_response import GetFormAttributes200Response

get_form_attributes200_response = GetFormAttributes200Response(
form_attribute=sailpoint.nerm.models.form_attribute.FormAttribute(
                    form_id = 'ac4aae0b-4140-49a4-a84c-126762fd0c8f', 
                    ne_attribute_id = 'ac4aae0b-4140-49a4-a84c-126762fd0c8f', 
                    attr_type = 'ne_attribute', 
                    order = 1, 
                    id = 'ac4aae0b-4140-49a4-a84c-126762fd0c8f', 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
)

```
[[Back to top]](#) 

