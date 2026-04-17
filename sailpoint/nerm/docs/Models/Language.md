---
id: language
title: Language
pagination_label: Language
sidebar_label: Language
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Language', 'Language'] 
slug: /tools/sdk/python//models/language
tags: ['SDK', 'Software Development Kit', 'Language', 'Language']
---

# Language


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default** | **bool** | Set default to True to set a default language, to set another language to default, set default to True on the target language and the current default will become disabled | [optional] 
**enabled** | **bool** | True when the language is enabled, False when it is not | [optional] 
**locale** | **str** | The locale string for the language, current options are- en, fr, es, de, fr-CA | [optional] 
}

## Example

```python
from sailpoint.nerm.models.language import Language

language = Language(
default=True,
enabled=True,
locale='es'
)

```
[[Back to top]](#) 

