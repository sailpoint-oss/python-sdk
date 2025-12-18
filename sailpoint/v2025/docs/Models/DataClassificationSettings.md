---
id: v2025-data-classification-settings
title: DataClassificationSettings
pagination_label: DataClassificationSettings
sidebar_label: DataClassificationSettings
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'DataClassificationSettings', 'V2025DataClassificationSettings'] 
slug: /tools/sdk/python/v2025/models/data-classification-settings
tags: ['SDK', 'Software Development Kit', 'DataClassificationSettings', 'V2025DataClassificationSettings']
---

# DataClassificationSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_enabled** | **bool** | Indicates whether the feature or configuration is enabled. | [optional] [default to False]
**cluster_id** | **str** | The identifier of the cluster associated with this configuration, if applicable. | [optional] 
}

## Example

```python
from sailpoint.v2025.models.data_classification_settings import DataClassificationSettings

data_classification_settings = DataClassificationSettings(
is_enabled=True,
cluster_id='cluster-001'
)

```
[[Back to top]](#) 

