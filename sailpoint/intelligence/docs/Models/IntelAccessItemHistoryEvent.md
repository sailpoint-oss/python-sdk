---
id: intel-access-item-history-event
title: IntelAccessItemHistoryEvent
pagination_label: IntelAccessItemHistoryEvent
sidebar_label: IntelAccessItemHistoryEvent
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'IntelAccessItemHistoryEvent', 'IntelAccessItemHistoryEvent'] 
slug: /tools/sdk/python/intelligence/models/intel-access-item-history-event
tags: ['SDK', 'Software Development Kit', 'IntelAccessItemHistoryEvent', 'IntelAccessItemHistoryEvent']
---

# IntelAccessItemHistoryEvent

Access-item history event. Supported eventTypes are AccessItemAssociated, AccessItemRemoved, and AccountStatusChanged. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_type** |  **Enum** [  'AccessItemAssociated',    'AccessItemRemoved',    'AccountStatusChanged' ] | Type of access-item history event. | [required]
**date_time** | **datetime** | Event timestamp. | [optional] 
}

## Example

```python
from sailpoint.intelligence.models.intel_access_item_history_event import IntelAccessItemHistoryEvent

intel_access_item_history_event = IntelAccessItemHistoryEvent(
event_type='AccessItemRemoved',
date_time='2026-05-11T09:40:04.496Z'
)

```
[[Back to top]](#) 

