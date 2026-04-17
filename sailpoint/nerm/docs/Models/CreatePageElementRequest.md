---
id: create-page-element-request
title: CreatePageElementRequest
pagination_label: CreatePageElementRequest
sidebar_label: CreatePageElementRequest
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'CreatePageElementRequest', 'CreatePageElementRequest'] 
slug: /tools/sdk/python//models/create-page-element-request
tags: ['SDK', 'Software Development Kit', 'CreatePageElementRequest', 'CreatePageElementRequest']
---

# CreatePageElementRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page_element** | [**PageElement1**](page-element1) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.create_page_element_request import CreatePageElementRequest

create_page_element_request = CreatePageElementRequest(
page_element=sailpoint.nerm.models.page_element_1.PageElement_1(
                    id = 'ac4aae0b-4140-49a4-a84c-126762fd0c8f', 
                    uid = 'first_text_body', 
                    element_type = 'PageContent', 
                    page_uid = '', 
                    page_id = 'ef5d413f-ba18-49e6-9a72-bb115aa133ff', 
                    element_uid = '', 
                    element_id = 'ef5d413f-ba18-49e6-9a72-bb115aa133ff', 
                    order = 1, )
)

```
[[Back to top]](#) 

