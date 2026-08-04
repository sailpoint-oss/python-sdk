---
id: lifecycle-owner-reference
title: LifecycleOwnerReference
pagination_label: LifecycleOwnerReference
sidebar_label: LifecycleOwnerReference
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'LifecycleOwnerReference', 'LifecycleOwnerReference'] 
slug: /tools/sdk/python/machine-identities-lifecycle-actions/models/lifecycle-owner-reference
tags: ['SDK', 'Software Development Kit', 'LifecycleOwnerReference', 'LifecycleOwnerReference']
---

# LifecycleOwnerReference


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** |  **Enum** [  'IDENTITY',    'WORKGROUP' ] | Owner reference type. | [optional] 
**id** | **str** | Identifier of the owner. | [optional] 
**name** | **str** | Display name of the owner. | [optional] 
}

## Example

```python
from sailpoint.machine_identities_lifecycle_actions.models.lifecycle_owner_reference import LifecycleOwnerReference

lifecycle_owner_reference = LifecycleOwnerReference(
type='IDENTITY',
id='2c9180858082150f0180893dbaf44201',
name='Pat Manager'
)

```
[[Back to top]](#) 

