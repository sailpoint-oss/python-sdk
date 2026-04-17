---
id: create-page-content-request
title: CreatePageContentRequest
pagination_label: CreatePageContentRequest
sidebar_label: CreatePageContentRequest
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'CreatePageContentRequest', 'CreatePageContentRequest'] 
slug: /tools/sdk/python//models/create-page-content-request
tags: ['SDK', 'Software Development Kit', 'CreatePageContentRequest', 'CreatePageContentRequest']
---

# CreatePageContentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page_content** | [**PageContent1**](page-content1) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.create_page_content_request import CreatePageContentRequest

create_page_content_request = CreatePageContentRequest(
page_content=sailpoint.nerm.models.page_content_1.PageContent_1(
                    uid = 'first_text_body', 
                    type = 'MediumHeading', 
                    content = 'Lorem Ipsum yadda yaddda bing bang.', )
)

```
[[Back to top]](#) 

