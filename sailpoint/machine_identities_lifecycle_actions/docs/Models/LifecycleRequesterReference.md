---
id: lifecycle-requester-reference
title: LifecycleRequesterReference
pagination_label: LifecycleRequesterReference
sidebar_label: LifecycleRequesterReference
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'LifecycleRequesterReference', 'LifecycleRequesterReference'] 
slug: /tools/sdk/python/machine-identities-lifecycle-actions/models/lifecycle-requester-reference
tags: ['SDK', 'Software Development Kit', 'LifecycleRequesterReference', 'LifecycleRequesterReference']
---

# LifecycleRequesterReference


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Requester reference type. | [optional] 
**id** | **str** | Identifier of the requester. | [optional] 
**name** | **str** | Display name of the requester. | [optional] 
}

## Example

```python
from sailpoint.machine_identities_lifecycle_actions.models.lifecycle_requester_reference import LifecycleRequesterReference

lifecycle_requester_reference = LifecycleRequesterReference(
type='IDENTITY',
id='2c9180858082150f0180893dbaf44201',
name='Pat Manager'
)

```
[[Back to top]](#) 

