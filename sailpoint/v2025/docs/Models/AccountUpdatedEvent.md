---
id: v2025-account-updated-event
title: AccountUpdatedEvent
pagination_label: AccountUpdatedEvent
sidebar_label: AccountUpdatedEvent
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'AccountUpdatedEvent', 'V2025AccountUpdatedEvent'] 
slug: /tools/sdk/python/v2025/models/account-updated-event
tags: ['SDK', 'Software Development Kit', 'AccountUpdatedEvent', 'V2025AccountUpdatedEvent']
---

# AccountUpdatedEvent

Details about the event.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** |  **Enum** [  'ACCOUNT_UPDATED_V2' ] | The type of event. | [required]
**cause** |  **Enum** [  'AGGREGATION',    'PROVISIONING',    'PASSWORD_CHANGE' ] | The cause of the event. | [required]
}

## Example

```python
from sailpoint.v2025.models.account_updated_event import AccountUpdatedEvent

account_updated_event = AccountUpdatedEvent(
type='ACCOUNT_UPDATED_V2',
cause='AGGREGATION'
)

```
[[Back to top]](#) 

