---
id: intel-access-history-access-items-slice
title: IntelAccessHistoryAccessItemsSlice
pagination_label: IntelAccessHistoryAccessItemsSlice
sidebar_label: IntelAccessHistoryAccessItemsSlice
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'IntelAccessHistoryAccessItemsSlice', 'IntelAccessHistoryAccessItemsSlice'] 
slug: /tools/sdk/python/intelligence/models/intel-access-history-access-items-slice
tags: ['SDK', 'Software Development Kit', 'IntelAccessHistoryAccessItemsSlice', 'IntelAccessHistoryAccessItemsSlice']
---

# IntelAccessHistoryAccessItemsSlice

Access-item history slice embedded in the aggregate identity response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | **[]IntelAccessItemHistoryEvent** | First page of access-item history events for the identity. | [required]
**next** | **str** | Absolute URL to the next access-items page; present only when more results exist. | [optional] 
}

## Example

```python
from sailpoint.intelligence.models.intel_access_history_access_items_slice import IntelAccessHistoryAccessItemsSlice

intel_access_history_access_items_slice = IntelAccessHistoryAccessItemsSlice(
items=[
                    { }
                    ],
next='https://tenant.example.api.cloud.sailpoint.com/v2026/intelligence/identities/ef38f94347e94562b5bb8424a56397d8/access-history/access-items?limit=10&offset=10'
)

```
[[Back to top]](#) 

