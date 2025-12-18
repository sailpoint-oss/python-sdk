---
id: v2025-account-created-event
title: AccountCreatedEvent
pagination_label: AccountCreatedEvent
sidebar_label: AccountCreatedEvent
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'AccountCreatedEvent', 'V2025AccountCreatedEvent'] 
slug: /tools/sdk/python/v2025/models/account-created-event
tags: ['SDK', 'Software Development Kit', 'AccountCreatedEvent', 'V2025AccountCreatedEvent']
---

# AccountCreatedEvent

Details about the event.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** |  **Enum** [  'ACCOUNT_CREATED_V2' ] | The type of event. | [required]
**cause** |  **Enum** [  'AGGREGATION',    'PROVISIONING' ] | The cause of the event. | [required]
}

## Example

```python
from sailpoint.v2025.models.account_created_event import AccountCreatedEvent

account_created_event = AccountCreatedEvent(
type='ACCOUNT_CREATED_V2',
cause='AGGREGATION'
)

```
[[Back to top]](#) 

