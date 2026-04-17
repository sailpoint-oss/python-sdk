---
id: page-content1
title: PageContent1
pagination_label: PageContent1
sidebar_label: PageContent1
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'PageContent1', 'PageContent1'] 
slug: /tools/sdk/python//models/page-content1
tags: ['SDK', 'Software Development Kit', 'PageContent1', 'PageContent1']
---

# PageContent1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uid** | **str** | The user-specified identifier for the record | [optional] 
**type** |  **Enum** [  'FormHeading',    'LargeHeading',    'MediumHeading',    'SmallHeading',    'Paragraph',    'HtmlContainer',    'Owner',    'RequestProgressBar' ] | The type of content on the page. | [required]
**content** | **str** | The text content to present in this page content record. | [optional] 
}

## Example

```python
from sailpoint.nerm.models.page_content1 import PageContent1

page_content1 = PageContent1(
uid='first_text_body',
type='MediumHeading',
content='Lorem Ipsum yadda yaddda bing bang.'
)

```
[[Back to top]](#) 

