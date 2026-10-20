---
id: source-reference-dto
title: SourceReferenceDTO
pagination_label: SourceReferenceDTO
sidebar_label: SourceReferenceDTO
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'SourceReferenceDTO', 'SourceReferenceDTO'] 
slug: /tools/sdk/python/gov-certification/models/source-reference-dto
tags: ['SDK', 'Software Development Kit', 'SourceReferenceDTO', 'SourceReferenceDTO']
---

# SourceReferenceDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The source ID | [optional] 
**type** | **str** | The source type, will always be \"SOURCE\" | [optional] 
**name** | **str** | The source name | [optional] 
}

## Example

```python
from sailpoint.gov_certification.models.source_reference_dto import SourceReferenceDTO

source_reference_dto = SourceReferenceDTO(
id='2c9180827ca885d7017ca8ce28a000eb',
type='SOURCE',
name='ODS-AD-Source'
)

```
[[Back to top]](#) 

