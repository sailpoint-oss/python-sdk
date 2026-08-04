---
id: lifecycle-approver-reference
title: LifecycleApproverReference
pagination_label: LifecycleApproverReference
sidebar_label: LifecycleApproverReference
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'LifecycleApproverReference', 'LifecycleApproverReference'] 
slug: /tools/sdk/python/machine-identities-lifecycle-actions/models/lifecycle-approver-reference
tags: ['SDK', 'Software Development Kit', 'LifecycleApproverReference', 'LifecycleApproverReference']
---

# LifecycleApproverReference


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Approver reference type. | [optional] 
**id** | **str** | Identifier of the approver. | [optional] 
**name** | **str** | Display name of the approver. | [optional] 
}

## Example

```python
from sailpoint.machine_identities_lifecycle_actions.models.lifecycle_approver_reference import LifecycleApproverReference

lifecycle_approver_reference = LifecycleApproverReference(
type='IDENTITY',
id='2c9180858082150f0180893dbaf44201',
name='Alex Approver'
)

```
[[Back to top]](#) 

