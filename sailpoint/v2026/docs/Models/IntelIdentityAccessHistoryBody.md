---
id: v2026-intel-identity-access-history-body
title: IntelIdentityAccessHistoryBody
pagination_label: IntelIdentityAccessHistoryBody
sidebar_label: IntelIdentityAccessHistoryBody
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'IntelIdentityAccessHistoryBody', 'V2026IntelIdentityAccessHistoryBody'] 
slug: /tools/sdk/python/v2026/models/intel-identity-access-history-body
tags: ['SDK', 'Software Development Kit', 'IntelIdentityAccessHistoryBody', 'V2026IntelIdentityAccessHistoryBody']
---

# IntelIdentityAccessHistoryBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**events** | **[]Dict[str, object]** | Each event is relayed from identity-history. Schema varies by event type; consumers should treat unknown fields as opaque using additionalProperties.  | [required]
}

## Example

```python
from sailpoint.v2026.models.intel_identity_access_history_body import IntelIdentityAccessHistoryBody

intel_identity_access_history_body = IntelIdentityAccessHistoryBody(
events=[{id=evt-001, type=LOGIN, dateTime=2024-05-01T12:00:00Z}]
)

```
[[Back to top]](#) 

