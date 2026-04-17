---
id: page-content-translation
title: PageContentTranslation
pagination_label: PageContentTranslation
sidebar_label: PageContentTranslation
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'PageContentTranslation', 'PageContentTranslation'] 
slug: /tools/sdk/python//models/page-content-translation
tags: ['SDK', 'Software Development Kit', 'PageContentTranslation', 'PageContentTranslation']
---

# PageContentTranslation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The id of the page content | [optional] [readonly] 
**uid** | **str** | The user-specified identifier for the record | [optional] 
**locale** | **str** | The language locale this translation contains. | [optional] 
**value** | **str** | The translated string to present in the user interface. | [optional] 
**created_at** | **datetime** | The date-time the record created. | [optional] [readonly] 
**updated_at** | **datetime** | The date-time the record was last updated. | [optional] [readonly] 
}

## Example

```python
from sailpoint.nerm.models.page_content_translation import PageContentTranslation

page_content_translation = PageContentTranslation(
id='ac4aae0b-4140-49a4-a84c-126762fd0c8f',
uid='page_content_transation_great_es_es',
locale='es-ES',
value='Es stupendo!',
created_at=datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
updated_at=datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
)

```
[[Back to top]](#) 

