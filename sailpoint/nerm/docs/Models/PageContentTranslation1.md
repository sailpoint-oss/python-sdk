---
id: page-content-translation1
title: PageContentTranslation1
pagination_label: PageContentTranslation1
sidebar_label: PageContentTranslation1
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'PageContentTranslation1', 'PageContentTranslation1'] 
slug: /tools/sdk/python//models/page-content-translation1
tags: ['SDK', 'Software Development Kit', 'PageContentTranslation1', 'PageContentTranslation1']
---

# PageContentTranslation1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uid** | **str** | The user-specified identifier for the record | [optional] 
**page_content_uid** | **str** | The user-specified identifier of the page content record this translation applies to; one of page_content_id or page_content_uid must be present. | [optional] 
**page_content_id** | **str** | The id of the page content record this translation applies to; one of page_content_id or page_content_uid must be present. | [optional] 
**locale** | **str** | The language locale this translation contains. | [optional] 
**value** | **str** | The translated string to present in the user interface. | [optional] 
}

## Example

```python
from sailpoint.nerm.models.page_content_translation1 import PageContentTranslation1

page_content_translation1 = PageContentTranslation1(
uid='page_content_translation_spanish_great',
page_content_uid='',
page_content_id='ef5d413f-ba18-49e6-9a72-bb115aa133ff',
locale='es-ES',
value='Es stupendo!'
)

```
[[Back to top]](#) 

