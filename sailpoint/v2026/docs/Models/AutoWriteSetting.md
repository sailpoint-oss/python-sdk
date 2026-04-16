---
id: v2026-auto-write-setting
title: AutoWriteSetting
pagination_label: AutoWriteSetting
sidebar_label: AutoWriteSetting
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'AutoWriteSetting', 'V2026AutoWriteSetting'] 
slug: /tools/sdk/python/v2026/models/auto-write-setting
tags: ['SDK', 'Software Development Kit', 'AutoWriteSetting', 'V2026AutoWriteSetting']
---

# AutoWriteSetting

Auto-Write Setting for SED

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Whether auto-write is currently enabled for the tenant | [optional] [default to False]
**included_source_ids** | **[]str** | Source IDs in the allowlist. Empty array means not in allowlist mode. | [optional] 
**excluded_source_ids** | **[]str** | Source IDs to exclude from auto-write. Always applied. | [optional] 
}

## Example

```python
from sailpoint.v2026.models.auto_write_setting import AutoWriteSetting

auto_write_setting = AutoWriteSetting(
enabled=True,
included_source_ids=[2c91808a7813090a017814552e526349, 2c91808a7813090a017814552e52634a],
excluded_source_ids=[2c91808a7813090a017814552e526350]
)

```
[[Back to top]](#) 

