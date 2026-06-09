---
id: accountdeleted-event
title: AccountdeletedEvent
pagination_label: AccountdeletedEvent
sidebar_label: AccountdeletedEvent
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'AccountdeletedEvent', 'AccountdeletedEvent'] 
slug: /tools/sdk/python/v1/models/accountdeleted-event
tags: ['SDK', 'Software Development Kit', 'AccountdeletedEvent', 'AccountdeletedEvent']
---

# AccountdeletedEvent

Details about the event.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** |  **Enum** [  'ACCOUNT_DELETED_V2' ] | The type of event. | [required]
**cause** |  **Enum** [  'AGGREGATION',    'PROVISIONING' ] | The cause of the event. | [required]
}

## Example

```python
from sailpoint.triggers_v1.models.accountdeleted_event import AccountdeletedEvent

accountdeleted_event = AccountdeletedEvent(
type='ACCOUNT_DELETED_V2',
cause='AGGREGATION'
)

```
[[Back to top]](#) 

