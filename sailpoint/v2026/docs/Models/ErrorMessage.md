---
id: v2026-error-message
title: ErrorMessage
pagination_label: ErrorMessage
sidebar_label: ErrorMessage
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'ErrorMessage', 'V2026ErrorMessage'] 
slug: /tools/sdk/python/v2026/models/error-message
tags: ['SDK', 'Software Development Kit', 'ErrorMessage', 'V2026ErrorMessage']
---

# ErrorMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**locale** | **str** | Locale is the current Locale | [optional] 
**locale_origin** | **str** | LocaleOrigin holds possible values of how the locale was selected | [optional] 
**text** | **str** | Text is the actual text of the error message | [optional] 
}

## Example

```python
from sailpoint.v2026.models.error_message import ErrorMessage

error_message = ErrorMessage(
locale='en-US',
locale_origin='DEFAULT',
text='This is an error'
)

```
[[Back to top]](#) 

