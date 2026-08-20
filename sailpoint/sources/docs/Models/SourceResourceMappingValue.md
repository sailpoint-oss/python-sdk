---
id: source-resource-mapping-value
title: SourceResourceMappingValue
pagination_label: SourceResourceMappingValue
sidebar_label: SourceResourceMappingValue
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'SourceResourceMappingValue', 'SourceResourceMappingValue'] 
slug: /tools/sdk/python/sources/models/source-resource-mapping-value
tags: ['SDK', 'Software Development Kit', 'SourceResourceMappingValue', 'SourceResourceMappingValue']
---

# SourceResourceMappingValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataset_id** | **str** | Dataset identifier that owns the resource. | [optional] 
**resource_type** | **str** | Resource type from source schema config. | [optional] 
**object_type** | **str** | Connector object type for the resource. | [optional] 
}

## Example

```python
from sailpoint.sources.models.source_resource_mapping_value import SourceResourceMappingValue

source_resource_mapping_value = SourceResourceMappingValue(
dataset_id='cmdb-servicenow:applications',
resource_type='std:resource',
object_type='account'
)

```
[[Back to top]](#) 

