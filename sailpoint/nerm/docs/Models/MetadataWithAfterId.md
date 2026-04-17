---
id: metadata-with-after-id
title: MetadataWithAfterId
pagination_label: MetadataWithAfterId
sidebar_label: MetadataWithAfterId
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'MetadataWithAfterId', 'MetadataWithAfterId'] 
slug: /tools/sdk/python//models/metadata-with-after-id
tags: ['SDK', 'Software Development Kit', 'MetadataWithAfterId', 'MetadataWithAfterId']
---

# MetadataWithAfterId


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** | The maximum number of records to return in the search | [optional] 
**offset** | **int** | The number of records to skip before starting to return results. | [optional] 
**total** | **int** | The total number of records available matching the search criteria. | [optional] 
**next** | **str** | The ID of the first record in the next set of results | [optional] 
**previous** | **str** | The ID of the last record in the previous set of results | [optional] 
**after_id** | **str** | The ID from which the search will start, ignoring all records before it. | [optional] 
}

## Example

```python
from sailpoint.nerm.models.metadata_with_after_id import MetadataWithAfterId

metadata_with_after_id = MetadataWithAfterId(
limit=56,
offset=56,
total=56,
next='/endpoint?limit=10&offset=60',
previous='/endpoint?limit=10&offset=40',
after_id='4eaa719f-4312-4c5b-9264-d0eb04d4a02a'
)

```
[[Back to top]](#) 

