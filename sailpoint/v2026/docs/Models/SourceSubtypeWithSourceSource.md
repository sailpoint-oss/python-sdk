---
id: v2026-source-subtype-with-source-source
title: SourceSubtypeWithSourceSource
pagination_label: SourceSubtypeWithSourceSource
sidebar_label: SourceSubtypeWithSourceSource
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'SourceSubtypeWithSourceSource', 'V2026SourceSubtypeWithSourceSource'] 
slug: /tools/sdk/python/v2026/models/source-subtype-with-source-source
tags: ['SDK', 'Software Development Kit', 'SourceSubtypeWithSourceSource', 'V2026SourceSubtypeWithSourceSource']
---

# SourceSubtypeWithSourceSource

Source reference of the subtype.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** |  **Enum** [  'SOURCE' ] | Type of the reference object. | [optional] 
**id** | **str** | Unique identifier for the source. | [optional] 
**name** | **str** | Name of the source. | [optional] 
}

## Example

```python
from sailpoint.v2026.models.source_subtype_with_source_source import SourceSubtypeWithSourceSource

source_subtype_with_source_source = SourceSubtypeWithSourceSource(
type='SOURCE',
id='6d0458373bec4b4b80460992b76016da',
name='Test Source'
)

```
[[Back to top]](#) 

