---
id: error-message-dto2
title: ErrorMessageDto2
pagination_label: ErrorMessageDto2
sidebar_label: ErrorMessageDto2
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'ErrorMessageDto2', 'ErrorMessageDto2'] 
slug: /tools/sdk/python/gov-certification/models/error-message-dto2
tags: ['SDK', 'Software Development Kit', 'ErrorMessageDto2', 'ErrorMessageDto2']
---

# ErrorMessageDto2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**locale** | **str** | The locale for the message text, a BCP 47 language tag. | [optional] 
**locale_origin** | **LocaleOrigin2** |  | [optional] 
**text** | **str** | Actual text of the error message in the indicated locale. | [optional] 
}

## Example

```python
from sailpoint.gov_certification.models.error_message_dto2 import ErrorMessageDto2

error_message_dto2 = ErrorMessageDto2(
locale='en-US',
locale_origin='DEFAULT',
text='The request was syntactically correct but its content is semantically invalid.'
)

```
[[Back to top]](#) 

