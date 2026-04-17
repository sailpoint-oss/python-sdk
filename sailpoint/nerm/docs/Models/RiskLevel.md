---
id: risk-level
title: RiskLevel
pagination_label: RiskLevel
sidebar_label: RiskLevel
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'RiskLevel', 'RiskLevel'] 
slug: /tools/sdk/python//models/risk-level
tags: ['SDK', 'Software Development Kit', 'RiskLevel', 'RiskLevel']
---

# RiskLevel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**uid** | **str** |  | [optional] [readonly] 
**label** | **str** |  | [optional] 
**points** | **float** |  | [optional] 
**order** | **int** |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.risk_level import RiskLevel

risk_level = RiskLevel(
id='',
uid='',
label='',
points=1.337,
order=0
)

```
[[Back to top]](#) 

