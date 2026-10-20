---
id: target-reference
title: TargetReference
pagination_label: TargetReference
sidebar_label: TargetReference
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'TargetReference', 'TargetReference'] 
slug: /tools/sdk/python/gov-certification/models/target-reference
tags: ['SDK', 'Software Development Kit', 'TargetReference', 'TargetReference']
---

# TargetReference


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **CertificationItemType** |  | [optional] 
**id** | **str** | Identifier of the target item. | [optional] 
**name** | **str** | Human-readable display name of identity. This is read-only | [optional] 
}

## Example

```python
from sailpoint.gov_certification.models.target_reference import TargetReference

target_reference = TargetReference(
type='ROLE',
id='5168015d32f890ca15812c9180835d2e',
name='Alison Ferguso'
)

```
[[Back to top]](#) 

