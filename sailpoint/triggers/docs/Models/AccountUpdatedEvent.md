---
id: account-updated-event
title: AccountUpdatedEvent
pagination_label: AccountUpdatedEvent
sidebar_label: AccountUpdatedEvent
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'AccountUpdatedEvent', 'AccountUpdatedEvent'] 
slug: /tools/sdk/python/triggers/models/account-updated-event
tags: ['SDK', 'Software Development Kit', 'AccountUpdatedEvent', 'AccountUpdatedEvent']
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
from sailpoint.triggers.models.account_updated_event import AccountUpdatedEvent

account_updated_event = AccountUpdatedEvent(
type='ACCOUNT_UPDATED_V2',
cause='AGGREGATION'
)

```
[[Back to top]](#) 

