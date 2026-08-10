---
id: intelmachineuserentitlement
title: Intelmachineuserentitlement
pagination_label: Intelmachineuserentitlement
sidebar_label: Intelmachineuserentitlement
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Intelmachineuserentitlement', 'Intelmachineuserentitlement'] 
slug: /tools/sdk/python/intelligence/models/intelmachineuserentitlement
tags: ['SDK', 'Software Development Kit', 'Intelmachineuserentitlement', 'Intelmachineuserentitlement']
---

# Intelmachineuserentitlement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_id** | **str** | Source identifier for the entitlement. | [required]
**entitlement_id** | **str** | Entitlement identifier on the source. | [required]
**display_name** | **str** | Display name for the entitlement. | [required]
**source** | [**Intelmachinesourcewire**](intelmachinesourcewire) | Resolved source metadata when available upstream. | [optional] 
}

## Example

```python
from sailpoint.intelligence.models.intelmachineuserentitlement import Intelmachineuserentitlement

intelmachineuserentitlement = Intelmachineuserentitlement(
source_id='60de165099e649cb828553a5e8510fc4',
entitlement_id='ent-001',
display_name='Example_Entitlement',
source=sailpoint.intelligence.models.intelmachinesourcewire.Intelmachinesourcewire(
                    id = '60de165099e649cb828553a5e8510fc4', 
                    name = 'Example Directory', 
                    type = 'DelimitedFile', )
)

```
[[Back to top]](#) 

