---
id: metadata
title: Metadata
pagination_label: Metadata
sidebar_label: Metadata
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Metadata', 'Metadata'] 
slug: /tools/sdk/python//models/metadata
tags: ['SDK', 'Software Development Kit', 'Metadata', 'Metadata']
---

# Metadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** |  | [optional] 
**offset** | **int** |  | [optional] 
**total** | **int** |  | [optional] 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.metadata import Metadata

metadata = Metadata(
limit=56,
offset=56,
total=56,
next='/endpoint?limit=10&offset=60',
previous='/endpoint?limit=10&offset=40'
)

```
[[Back to top]](#) 

