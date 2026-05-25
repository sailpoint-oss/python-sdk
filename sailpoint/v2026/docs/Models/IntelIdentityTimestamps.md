---
id: v2026-intel-identity-timestamps
title: IntelIdentityTimestamps
pagination_label: IntelIdentityTimestamps
sidebar_label: IntelIdentityTimestamps
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'IntelIdentityTimestamps', 'V2026IntelIdentityTimestamps'] 
slug: /tools/sdk/python/v2026/models/intel-identity-timestamps
tags: ['SDK', 'Software Development Kit', 'IntelIdentityTimestamps', 'V2026IntelIdentityTimestamps']
---

# IntelIdentityTimestamps


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** | Timestamp when the identity record was first created in Identity Security Cloud. | [required]
**modified_at** | **datetime** | Timestamp when the identity record was last modified in Identity Security Cloud. | [required]
}

## Example

```python
from sailpoint.v2026.models.intel_identity_timestamps import IntelIdentityTimestamps

intel_identity_timestamps = IntelIdentityTimestamps(
created_at='2024-01-15T10:30Z',
modified_at='2024-06-20T14:45Z'
)

```
[[Back to top]](#) 

