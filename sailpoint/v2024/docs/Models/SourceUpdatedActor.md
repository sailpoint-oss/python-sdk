---
id: v2024-source-updated-actor
title: SourceUpdatedActor
pagination_label: SourceUpdatedActor
sidebar_label: SourceUpdatedActor
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'SourceUpdatedActor', 'V2024SourceUpdatedActor'] 
slug: /tools/sdk/python/v2024/models/source-updated-actor
tags: ['SDK', 'Software Development Kit', 'SourceUpdatedActor', 'V2024SourceUpdatedActor']
---

# SourceUpdatedActor

Identity who updated the source.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** |  **Enum** [  'IDENTITY' ] | DTO type of identity who updated the source. | [required]
**id** | **str** | ID of identity who updated the source. | [optional] 
**name** | **str** | Display name of identity who updated the source. | [required]
}

## Example

```python
from sailpoint.v2024.models.source_updated_actor import SourceUpdatedActor

source_updated_actor = SourceUpdatedActor(
type='IDENTITY',
id='2c7180a46faadee4016fb4e018c20648',
name='William Wilson'
)

```
[[Back to top]](#) 

