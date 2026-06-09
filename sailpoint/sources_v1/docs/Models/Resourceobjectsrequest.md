---
id: resourceobjectsrequest
title: Resourceobjectsrequest
pagination_label: Resourceobjectsrequest
sidebar_label: Resourceobjectsrequest
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Resourceobjectsrequest', 'Resourceobjectsrequest'] 
slug: /tools/sdk/python/v1/models/resourceobjectsrequest
tags: ['SDK', 'Software Development Kit', 'Resourceobjectsrequest', 'Resourceobjectsrequest']
---

# Resourceobjectsrequest

Request model for peek resource objects from source connectors.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object_type** | **str** | The type of resource objects to iterate over. | [optional] [default to 'account']
**max_count** | **int** | The maximum number of resource objects to iterate over and return. | [optional] [default to 25]
}

## Example

```python
from sailpoint.sources_v1.models.resourceobjectsrequest import Resourceobjectsrequest

resourceobjectsrequest = Resourceobjectsrequest(
object_type='account',
max_count=100
)

```
[[Back to top]](#) 

