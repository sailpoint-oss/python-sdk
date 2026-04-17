---
id: update-page-content-translation-by-id-request
title: UpdatePageContentTranslationByIdRequest
pagination_label: UpdatePageContentTranslationByIdRequest
sidebar_label: UpdatePageContentTranslationByIdRequest
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'UpdatePageContentTranslationByIdRequest', 'UpdatePageContentTranslationByIdRequest'] 
slug: /tools/sdk/python//models/update-page-content-translation-by-id-request
tags: ['SDK', 'Software Development Kit', 'UpdatePageContentTranslationByIdRequest', 'UpdatePageContentTranslationByIdRequest']
---

# UpdatePageContentTranslationByIdRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page_content_translation** | [**PageContent1**](page-content1) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.update_page_content_translation_by_id_request import UpdatePageContentTranslationByIdRequest

update_page_content_translation_by_id_request = UpdatePageContentTranslationByIdRequest(
page_content_translation=sailpoint.nerm.models.page_content_1.PageContent_1(
                    uid = 'first_text_body', 
                    type = 'MediumHeading', 
                    content = 'Lorem Ipsum yadda yaddda bing bang.', )
)

```
[[Back to top]](#) 

