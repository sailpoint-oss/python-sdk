---
id: get-page-contents200-response
title: GetPageContents200Response
pagination_label: GetPageContents200Response
sidebar_label: GetPageContents200Response
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'GetPageContents200Response', 'GetPageContents200Response'] 
slug: /tools/sdk/python//models/get-page-contents200-response
tags: ['SDK', 'Software Development Kit', 'GetPageContents200Response', 'GetPageContents200Response']
---

# GetPageContents200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | [**PageContent**](page-content) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.get_page_contents200_response import GetPageContents200Response

get_page_contents200_response = GetPageContents200Response(
page=sailpoint.nerm.models.page_content.PageContent(
                    id = 'ac4aae0b-4140-49a4-a84c-126762fd0c8f', 
                    uid = 'first_text_body', 
                    type = 'MediumHeading', 
                    content = 'Lorem Ipsum yadda yaddda bing bang.', 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
)

```
[[Back to top]](#) 

