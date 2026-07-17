---
id: lifecycle-state-dto
title: LifecycleStateDto
pagination_label: LifecycleStateDto
sidebar_label: LifecycleStateDto
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'LifecycleStateDto', 'LifecycleStateDto'] 
slug: /tools/sdk/python/identities/models/lifecycle-state-dto
tags: ['SDK', 'Software Development Kit', 'LifecycleStateDto', 'LifecycleStateDto']
---

# LifecycleStateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state_name** | **str** | The name of the lifecycle state | [required]
**manually_updated** | **bool** | Whether the lifecycle state has been manually or automatically set | [required]
}

## Example

```python
from sailpoint.identities.models.lifecycle_state_dto import LifecycleStateDto

lifecycle_state_dto = LifecycleStateDto(
state_name='active',
manually_updated=True
)

```
[[Back to top]](#) 

