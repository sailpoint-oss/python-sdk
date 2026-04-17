---
id: create-page-content-translation-request
title: CreatePageContentTranslationRequest
pagination_label: CreatePageContentTranslationRequest
sidebar_label: CreatePageContentTranslationRequest
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'CreatePageContentTranslationRequest', 'CreatePageContentTranslationRequest'] 
slug: /tools/sdk/python//models/create-page-content-translation-request
tags: ['SDK', 'Software Development Kit', 'CreatePageContentTranslationRequest', 'CreatePageContentTranslationRequest']
---

# CreatePageContentTranslationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page_content_translation** | [**PageContentTranslation1**](page-content-translation1) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.create_page_content_translation_request import CreatePageContentTranslationRequest

create_page_content_translation_request = CreatePageContentTranslationRequest(
page_content_translation=sailpoint.nerm.models.page_content_translation_1.PageContentTranslation_1(
                    uid = 'page_content_translation_spanish_great', 
                    page_content_uid = '', 
                    page_content_id = 'ef5d413f-ba18-49e6-9a72-bb115aa133ff', 
                    locale = 'es-ES', 
                    value = 'Es stupendo!', )
)

```
[[Back to top]](#) 

