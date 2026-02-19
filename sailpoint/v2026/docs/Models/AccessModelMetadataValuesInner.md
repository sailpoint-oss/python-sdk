---
id: v2026-access-model-metadata-values-inner
title: AccessModelMetadataValuesInner
pagination_label: AccessModelMetadataValuesInner
sidebar_label: AccessModelMetadataValuesInner
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'AccessModelMetadataValuesInner', 'V2026AccessModelMetadataValuesInner'] 
slug: /tools/sdk/python/v2026/models/access-model-metadata-values-inner
tags: ['SDK', 'Software Development Kit', 'AccessModelMetadataValuesInner', 'V2026AccessModelMetadataValuesInner']
---

# AccessModelMetadataValuesInner

An individual value to assign to the metadata item

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | The value to assign to the metdata item | [optional] 
**name** | **str** | Display name of the value | [optional] 
**status** | **str** | The status of the individual value | [optional] 
}

## Example

```python
from sailpoint.v2026.models.access_model_metadata_values_inner import AccessModelMetadataValuesInner

access_model_metadata_values_inner = AccessModelMetadataValuesInner(
value='development',
name='Development',
status='active'
)

```
[[Back to top]](#) 

