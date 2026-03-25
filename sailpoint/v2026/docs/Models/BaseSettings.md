---
id: v2026-base-settings
title: BaseSettings
pagination_label: BaseSettings
sidebar_label: BaseSettings
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'BaseSettings', 'V2026BaseSettings'] 
slug: /tools/sdk/python/v2026/models/base-settings
tags: ['SDK', 'Software Development Kit', 'BaseSettings', 'V2026BaseSettings']
---

# BaseSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_enabled** | **bool** | Indicates whether the feature or configuration is enabled. | [optional] [default to False]
**cluster_id** | **str** | The identifier of the cluster associated with this configuration, if applicable. | [optional] 
}

## Example

```python
from sailpoint.v2026.models.base_settings import BaseSettings

base_settings = BaseSettings(
is_enabled=True,
cluster_id='cluster-001'
)

```
[[Back to top]](#) 

