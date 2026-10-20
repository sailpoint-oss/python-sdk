---
id: reassign
title: Reassign
pagination_label: Reassign
sidebar_label: Reassign
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Reassign', 'Reassign'] 
slug: /tools/sdk/python/gov-certification/models/reassign
tags: ['SDK', 'Software Development Kit', 'Reassign', 'Reassign']
---

# Reassign


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of item or subject being reassigned. | [required]
**type** | **ReassignEntityType** |  | [required]
}

## Example

```python
from sailpoint.gov_certification.models.reassign import Reassign

reassign = Reassign(
id='ef38f943-47e9-4562-b5bb-8424a56397d8',
type='ITEM'
)

```
[[Back to top]](#) 

