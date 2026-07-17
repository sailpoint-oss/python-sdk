---
id: sod-policy-dto2
title: SodPolicyDto2
pagination_label: SodPolicyDto2
sidebar_label: SodPolicyDto2
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'SodPolicyDto2', 'SodPolicyDto2'] 
slug: /tools/sdk/python/sod-violations/models/sod-policy-dto2
tags: ['SDK', 'Software Development Kit', 'SodPolicyDto2', 'SodPolicyDto2']
---

# SodPolicyDto2

SOD policy.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** |  **Enum** [  'SOD_POLICY' ] | SOD policy DTO type. | [optional] 
**id** | **str** | SOD policy ID. | [optional] 
**name** | **str** | SOD policy display name. | [optional] 
}

## Example

```python
from sailpoint.sod_violations.models.sod_policy_dto2 import SodPolicyDto2

sod_policy_dto2 = SodPolicyDto2(
type='SOD_POLICY',
id='0f11f2a4-7c94-4bf3-a2bd-742580fe3bde',
name='Business SOD Policy'
)

```
[[Back to top]](#) 

