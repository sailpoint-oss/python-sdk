---
id: create-form-attribute-request
title: CreateFormAttributeRequest
pagination_label: CreateFormAttributeRequest
sidebar_label: CreateFormAttributeRequest
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'CreateFormAttributeRequest', 'CreateFormAttributeRequest'] 
slug: /tools/sdk/python//models/create-form-attribute-request
tags: ['SDK', 'Software Development Kit', 'CreateFormAttributeRequest', 'CreateFormAttributeRequest']
---

# CreateFormAttributeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**form_attribute** | [**FormAttributes**](form-attributes) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.create_form_attribute_request import CreateFormAttributeRequest

create_form_attribute_request = CreateFormAttributeRequest(
form_attribute=sailpoint.nerm.models.form_attributes.FormAttributes(
                    form_id = 'ac4aae0b-4140-49a4-a84c-126762fd0c8f', 
                    ne_attribute_id = 'ac4aae0b-4140-49a4-a84c-126762fd0c8f', 
                    attr_type = 'ne_attribute', 
                    order = 1, )
)

```
[[Back to top]](#) 

