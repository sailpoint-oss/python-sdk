---
id: v2025-account-deleted-event
title: AccountDeletedEvent
pagination_label: AccountDeletedEvent
sidebar_label: AccountDeletedEvent
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'AccountDeletedEvent', 'V2025AccountDeletedEvent'] 
slug: /tools/sdk/python/v2025/models/account-deleted-event
tags: ['SDK', 'Software Development Kit', 'AccountDeletedEvent', 'V2025AccountDeletedEvent']
---

# AccountDeletedEvent

Details about the event.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** |  **Enum** [  'ACCOUNT_DELETED_V2' ] | The type of event. | [required]
**cause** |  **Enum** [  'AGGREGATION',    'PROVISIONING' ] | The cause of the event. | [required]
}

## Example

```python
from sailpoint.v2025.models.account_deleted_event import AccountDeletedEvent

account_deleted_event = AccountDeletedEvent(
type='ACCOUNT_DELETED_V2',
cause='AGGREGATION'
)

```
[[Back to top]](#) 

