---
id: create-identity-collector-v1409-response-messages-inner
title: CreateIdentityCollectorV1409ResponseMessagesInner
pagination_label: CreateIdentityCollectorV1409ResponseMessagesInner
sidebar_label: CreateIdentityCollectorV1409ResponseMessagesInner
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'CreateIdentityCollectorV1409ResponseMessagesInner', 'CreateIdentityCollectorV1409ResponseMessagesInner'] 
slug: /tools/sdk/python/data-access-security/models/create-identity-collector-v1409-response-messages-inner
tags: ['SDK', 'Software Development Kit', 'CreateIdentityCollectorV1409ResponseMessagesInner', 'CreateIdentityCollectorV1409ResponseMessagesInner']
---

# CreateIdentityCollectorV1409ResponseMessagesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**locale** | **str** | The locale for the message text, a BCP 47 language tag. | [optional] 
**locale_origin** | **str** | An indicator of how the locale was selected. | [optional] 
**text** | **str** | Actual text of the error message in the indicated locale. | [optional] 
}

## Example

```python
from sailpoint.data_access_security.models.create_identity_collector_v1409_response_messages_inner import CreateIdentityCollectorV1409ResponseMessagesInner

create_identity_collector_v1409_response_messages_inner = CreateIdentityCollectorV1409ResponseMessagesInner(
locale='en-US',
locale_origin='DEFAULT',
text='An identity collector with the same name already exists.'
)

```
[[Back to top]](#) 

