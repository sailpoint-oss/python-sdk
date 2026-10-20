---
id: alert
title: Alert
pagination_label: Alert
sidebar_label: Alert
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Alert', 'Alert'] 
slug: /tools/sdk/python/gov-certification/models/alert
tags: ['SDK', 'Software Development Kit', 'Alert', 'Alert']
---

# Alert


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**level** |  **Enum** [  'ERROR',    'WARN',    'INFO' ] | Denotes the level of the message | [optional] 
**localizations** | [**[]ErrorMessageDto**](error-message-dto) |  | [optional] 
}

## Example

```python
from sailpoint.gov_certification.models.alert import Alert

alert = Alert(
level='ERROR',
localizations=[
                    sailpoint.gov_certification.models.error_message_dto.ErrorMessageDto(
                        locale = 'en-US', 
                        locale_origin = 'DEFAULT', 
                        text = 'The request was syntactically correct but its content is semantically invalid.', )
                    ]
)

```
[[Back to top]](#) 

