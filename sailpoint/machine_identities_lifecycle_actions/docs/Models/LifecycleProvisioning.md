---
id: lifecycle-provisioning
title: LifecycleProvisioning
pagination_label: LifecycleProvisioning
sidebar_label: LifecycleProvisioning
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'LifecycleProvisioning', 'LifecycleProvisioning'] 
slug: /tools/sdk/python/machine-identities-lifecycle-actions/models/lifecycle-provisioning
tags: ['SDK', 'Software Development Kit', 'LifecycleProvisioning', 'LifecycleProvisioning']
---

# LifecycleProvisioning

Provisioning execution window for the lifecycle request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **Lifecycleprovisioningstatus** |  | [optional] 
**started** | **datetime** | Time when provisioning started (ISO-8601). | [optional] 
**ended** | **datetime** | Time when provisioning ended (ISO-8601). | [optional] 
}

## Example

```python
from sailpoint.machine_identities_lifecycle_actions.models.lifecycle_provisioning import LifecycleProvisioning

lifecycle_provisioning = LifecycleProvisioning(
status='NOT_STARTED',
started='2026-05-26T19:05Z',
ended='2026-05-26T19:10Z'
)

```
[[Back to top]](#) 

