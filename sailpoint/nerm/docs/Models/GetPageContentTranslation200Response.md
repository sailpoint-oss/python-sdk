---
id: get-page-content-translation200-response
title: GetPageContentTranslation200Response
pagination_label: GetPageContentTranslation200Response
sidebar_label: GetPageContentTranslation200Response
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'GetPageContentTranslation200Response', 'GetPageContentTranslation200Response'] 
slug: /tools/sdk/python//models/get-page-content-translation200-response
tags: ['SDK', 'Software Development Kit', 'GetPageContentTranslation200Response', 'GetPageContentTranslation200Response']
---

# GetPageContentTranslation200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page_content_translation** | [**PageContentTranslation**](page-content-translation) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.get_page_content_translation200_response import GetPageContentTranslation200Response

get_page_content_translation200_response = GetPageContentTranslation200Response(
page_content_translation=sailpoint.nerm.models.page_content_translation.PageContentTranslation(
                    id = 'ac4aae0b-4140-49a4-a84c-126762fd0c8f', 
                    uid = 'page_content_transation_great_es_es', 
                    locale = 'es-ES', 
                    value = 'Es stupendo!', 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
)

```
[[Back to top]](#) 

