---
id: v2026-auto-write-setting-patch
title: AutoWriteSettingPatch
pagination_label: AutoWriteSettingPatch
sidebar_label: AutoWriteSettingPatch
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'AutoWriteSettingPatch', 'V2026AutoWriteSettingPatch'] 
slug: /tools/sdk/python/v2026/models/auto-write-setting-patch
tags: ['SDK', 'Software Development Kit', 'AutoWriteSettingPatch', 'V2026AutoWriteSettingPatch']
---

# AutoWriteSettingPatch

Patch operation for Auto-Write Setting

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**op** |  **Enum** [  'replace' ] | The operation to perform. Only \"replace\" is supported. | [required]
**path** | **str** | The field to update. Allowed values: /enabled, /includedSourceIds, /excludedSourceIds | [required]
**value** | [**AutoWriteSettingPatchValue**](auto-write-setting-patch-value) |  | [required]
}

## Example

```python
from sailpoint.v2026.models.auto_write_setting_patch import AutoWriteSettingPatch

auto_write_setting_patch = AutoWriteSettingPatch(
op='replace',
path='/enabled',
value=true
)

```
[[Back to top]](#) 

