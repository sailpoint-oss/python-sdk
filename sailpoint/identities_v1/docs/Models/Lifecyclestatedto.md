---
id: lifecyclestatedto
title: Lifecyclestatedto
pagination_label: Lifecyclestatedto
sidebar_label: Lifecyclestatedto
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Lifecyclestatedto', 'Lifecyclestatedto'] 
slug: /tools/sdk/python/v1/models/lifecyclestatedto
tags: ['SDK', 'Software Development Kit', 'Lifecyclestatedto', 'Lifecyclestatedto']
---

# Lifecyclestatedto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state_name** | **str** | The name of the lifecycle state | [required]
**manually_updated** | **bool** | Whether the lifecycle state has been manually or automatically set | [required]
}

## Example

```python
from sailpoint.identities_v1.models.lifecyclestatedto import Lifecyclestatedto

lifecyclestatedto = Lifecyclestatedto(
state_name='active',
manually_updated=True
)

```
[[Back to top]](#) 

