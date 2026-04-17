---
id: page-content
title: PageContent
pagination_label: PageContent
sidebar_label: PageContent
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'PageContent', 'PageContent'] 
slug: /tools/sdk/python//models/page-content
tags: ['SDK', 'Software Development Kit', 'PageContent', 'PageContent']
---

# PageContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The id of the page content | [optional] [readonly] 
**uid** | **str** | The user-specified identifier for the record | [optional] 
**type** |  **Enum** [  'FormHeading',    'LargeHeading',    'MediumHeading',    'SmallHeading',    'Paragraph',    'HtmlContainer',    'Owner',    'RequestProgressBar' ] | The type of content on the page. | [required]
**content** | **str** | The text content to present in this page content record. | [optional] 
**created_at** | **datetime** | The date-time the record created. | [optional] [readonly] 
**updated_at** | **datetime** | The date-time the record was last updated. | [optional] [readonly] 
}

## Example

```python
from sailpoint.nerm.models.page_content import PageContent

page_content = PageContent(
id='ac4aae0b-4140-49a4-a84c-126762fd0c8f',
uid='first_text_body',
type='MediumHeading',
content='Lorem Ipsum yadda yaddda bing bang.',
created_at=datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
updated_at=datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
)

```
[[Back to top]](#) 

