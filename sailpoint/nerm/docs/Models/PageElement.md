---
id: page-element
title: PageElement
pagination_label: PageElement
sidebar_label: PageElement
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'PageElement', 'PageElement'] 
slug: /tools/sdk/python//models/page-element
tags: ['SDK', 'Software Development Kit', 'PageElement', 'PageElement']
---

# PageElement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The id of the page element | [optional] [readonly] 
**uid** | **str** | The user-specified identifier for the record | [optional] 
**element_type** |  **Enum** [  'PageContent',    'Form' ] | The type of content on the page. | [required]
**page_uid** | **str** | The user-specified identifier of the page record this applies to; one of page_id or page_uid must be present. | [optional] 
**page_id** | **str** | The id of the page record this applies to; one of page_id or page_uid must be present. | [optional] 
**element_uid** | **str** | The user-specified identifier of the record (Form or PageContent) this applies to; one of element_id or element_uid must be present. | [optional] 
**element_id** | **str** | The id of the record (Form or PageContent) this applies to; one of element_id or element_uid must be present. | [optional] 
**order** | **int** | The position of the attribute in the ProfileType's naming | [optional] 
}

## Example

```python
from sailpoint.nerm.models.page_element import PageElement

page_element = PageElement(
id='ac4aae0b-4140-49a4-a84c-126762fd0c8f',
uid='first_text_body',
element_type='PageContent',
page_uid='',
page_id='ef5d413f-ba18-49e6-9a72-bb115aa133ff',
element_uid='',
element_id='ef5d413f-ba18-49e6-9a72-bb115aa133ff',
order=1
)

```
[[Back to top]](#) 

