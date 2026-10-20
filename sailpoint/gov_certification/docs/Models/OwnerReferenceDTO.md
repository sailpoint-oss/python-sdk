---
id: owner-reference-dto
title: OwnerReferenceDTO
pagination_label: OwnerReferenceDTO
sidebar_label: OwnerReferenceDTO
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'OwnerReferenceDTO', 'OwnerReferenceDTO'] 
slug: /tools/sdk/python/gov-certification/models/owner-reference-dto
tags: ['SDK', 'Software Development Kit', 'OwnerReferenceDTO', 'OwnerReferenceDTO']
---

# OwnerReferenceDTO

Simplified DTO for the owner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The owner id | [optional] 
**name** | **str** | The owner name | [optional] 
**type** |  **Enum** [  'IDENTITY' ] | The type of the owner. Initially only type IDENTITY is supported | [optional] 
}

## Example

```python
from sailpoint.gov_certification.models.owner_reference_dto import OwnerReferenceDTO

owner_reference_dto = OwnerReferenceDTO(
id='2a2fdacca5e345f18bf7970cfbb8fec2',
name='identity 1',
type='IDENTITY'
)

```
[[Back to top]](#) 

