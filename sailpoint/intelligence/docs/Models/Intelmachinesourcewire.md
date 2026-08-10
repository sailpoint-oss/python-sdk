---
id: intelmachinesourcewire
title: Intelmachinesourcewire
pagination_label: Intelmachinesourcewire
sidebar_label: Intelmachinesourcewire
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Intelmachinesourcewire', 'Intelmachinesourcewire'] 
slug: /tools/sdk/python/intelligence/models/intelmachinesourcewire
tags: ['SDK', 'Software Development Kit', 'Intelmachinesourcewire', 'Intelmachinesourcewire']
---

# Intelmachinesourcewire


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Source identifier. | [required]
**name** | **str** | Source display name. | [required]
**type** | **str** | Source type label from upstream. | [required]
}

## Example

```python
from sailpoint.intelligence.models.intelmachinesourcewire import Intelmachinesourcewire

intelmachinesourcewire = Intelmachinesourcewire(
id='60de165099e649cb828553a5e8510fc4',
name='Example Directory',
type='DelimitedFile'
)

```
[[Back to top]](#) 

