---
id: v2026-create-source-subtype-request
title: CreateSourceSubtypeRequest
pagination_label: CreateSourceSubtypeRequest
sidebar_label: CreateSourceSubtypeRequest
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'CreateSourceSubtypeRequest', 'V2026CreateSourceSubtypeRequest'] 
slug: /tools/sdk/python/v2026/models/create-source-subtype-request
tags: ['SDK', 'Software Development Kit', 'CreateSourceSubtypeRequest', 'V2026CreateSourceSubtypeRequest']
---

# CreateSourceSubtypeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_id** | **str** | ID of the source where subtype is created. | [required]
**technical_name** | **str** | Technical name of the subtype. | [required]
**display_name** | **str** | Display name of the subtype. | [required]
**description** | **str** | Description of the subtype. | [required]
**type** | **str** | Type of the subtype. | [optional] 
}

## Example

```python
from sailpoint.v2026.models.create_source_subtype_request import CreateSourceSubtypeRequest

create_source_subtype_request = CreateSourceSubtypeRequest(
source_id='6d0458373bec4b4b80460992b76016da',
technical_name='foo',
display_name='Mr Foo',
description='fighters',
type='MACHINE'
)

```
[[Back to top]](#) 

