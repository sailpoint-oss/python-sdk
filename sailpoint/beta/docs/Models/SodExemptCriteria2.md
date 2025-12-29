---
id: beta-sod-exempt-criteria2
title: SodExemptCriteria2
pagination_label: SodExemptCriteria2
sidebar_label: SodExemptCriteria2
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'SodExemptCriteria2', 'BetaSodExemptCriteria2'] 
slug: /tools/sdk/python/beta/models/sod-exempt-criteria2
tags: ['SDK', 'Software Development Kit', 'SodExemptCriteria2', 'BetaSodExemptCriteria2']
---

# SodExemptCriteria2

Details of the Entitlement criteria

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**existing** | **bool** | If the entitlement already belonged to the user or not. | [optional] [default to False]
**type** | [**DtoType**](dto-type) |  | [optional] 
**id** | **str** | Entitlement ID | [optional] 
**name** | **str** | Entitlement name | [optional] 
}

## Example

```python
from sailpoint.beta.models.sod_exempt_criteria2 import SodExemptCriteria2

sod_exempt_criteria2 = SodExemptCriteria2(
existing=True,
type='IDENTITY',
id='2c918085771e9d3301773b3cb66f6398',
name='My HR Entitlement'
)

```
[[Back to top]](#) 

