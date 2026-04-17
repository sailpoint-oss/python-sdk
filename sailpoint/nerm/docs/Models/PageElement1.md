---
id: page-element1
title: PageElement1
pagination_label: PageElement1
sidebar_label: PageElement1
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'PageElement1', 'PageElement1'] 
slug: /tools/sdk/python//models/page-element1
tags: ['SDK', 'Software Development Kit', 'PageElement1', 'PageElement1']
---

# PageElement1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The id of the page content | [optional] [readonly] 
**uid** | **str** | The user-specified identifier for the record | [optional] 
**element_type** |  **Enum** [  'PageContent',    'Form' ] | The type of content on the page. | [required]
**page_uid** | **str** | The user-specified identifier of the page record this applies to; one of page_id or page_uid must be present. | [optional] 
**page_id** | **str** | The id of the page record this applies to; one of page_id or page_uid must be present. | [optional] 
**element_uid** | **str** | The user-specified identifier of the record (Form or PageContent) this applies to; one of element_id or element_uid must be present. | [optional] 
**element_id** | **str** | The id of the record (Form or PageContent) this applies to; one of element_id or element_uid must be present. | [optional] 
**order** | **int** | The ordinal position of the attribute in the user-interface page. | [optional] 
}

## Example

```python
from sailpoint.nerm.models.page_element1 import PageElement1

page_element1 = PageElement1(
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

