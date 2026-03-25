---
id: v2026-start-application-discovery403-response
title: StartApplicationDiscovery403Response
pagination_label: StartApplicationDiscovery403Response
sidebar_label: StartApplicationDiscovery403Response
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'StartApplicationDiscovery403Response', 'V2026StartApplicationDiscovery403Response'] 
slug: /tools/sdk/python/v2026/models/start-application-discovery403-response
tags: ['SDK', 'Software Development Kit', 'StartApplicationDiscovery403Response', 'V2026StartApplicationDiscovery403Response']
---

# StartApplicationDiscovery403Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detail_code** | **str** | Fine-grained error code providing more detail of the error. | [optional] 
**tracking_id** | **str** | Unique tracking id for the error. | [optional] 
**messages** | [**[]ErrorMessageDto**](error-message-dto) | Generic localized reason for error | [optional] 
**causes** | [**[]ErrorMessageDto**](error-message-dto) | Plain-text descriptive reasons to provide additional detail to the text provided in the messages field | [optional] 
**error** | **str** | Error message when quota is exceeded | [required]
}

## Example

```python
from sailpoint.v2026.models.start_application_discovery403_response import StartApplicationDiscovery403Response

start_application_discovery403_response = StartApplicationDiscovery403Response(
detail_code='400.1 Bad Request Content',
tracking_id='e7eab60924f64aa284175b9fa3309599',
messages=[
                    sailpoint.v2026.models.error_message_dto.Error Message Dto(
                        locale = 'en-US', 
                        locale_origin = 'DEFAULT', 
                        text = 'The request was syntactically correct but its content is semantically invalid.', )
                    ],
causes=[
                    sailpoint.v2026.models.error_message_dto.Error Message Dto(
                        locale = 'en-US', 
                        locale_origin = 'DEFAULT', 
                        text = 'The request was syntactically correct but its content is semantically invalid.', )
                    ],
error=''
)

```
[[Back to top]](#) 

