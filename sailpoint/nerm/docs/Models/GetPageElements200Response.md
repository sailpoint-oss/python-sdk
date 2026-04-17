---
id: get-page-elements200-response
title: GetPageElements200Response
pagination_label: GetPageElements200Response
sidebar_label: GetPageElements200Response
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'GetPageElements200Response', 'GetPageElements200Response'] 
slug: /tools/sdk/python//models/get-page-elements200-response
tags: ['SDK', 'Software Development Kit', 'GetPageElements200Response', 'GetPageElements200Response']
---

# GetPageElements200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page_element** | [**PageElement**](page-element) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.get_page_elements200_response import GetPageElements200Response

get_page_elements200_response = GetPageElements200Response(
page_element=sailpoint.nerm.models.page_element.PageElement(
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

