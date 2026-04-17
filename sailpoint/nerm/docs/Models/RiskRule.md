---
id: risk-rule
title: RiskRule
pagination_label: RiskRule
sidebar_label: RiskRule
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'RiskRule', 'RiskRule'] 
slug: /tools/sdk/python//models/risk-rule
tags: ['SDK', 'Software Development Kit', 'RiskRule', 'RiskRule']
---

# RiskRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**uid** | **str** |  | [optional] [readonly] 
**type** |  **Enum** [  'RiskRule' ] |  | [required]
**comparison_operator** |  **Enum** [  '==',    '>',    '<' ] |  | [optional] 
**value** | **str** |  | [required]
**secondary_value** |  **Enum** [  'OverallRisk' ] |  | [required]
}

## Example

```python
from sailpoint.nerm.models.risk_rule import RiskRule

risk_rule = RiskRule(
id='',
uid='',
type='RiskRule',
comparison_operator='==',
value='',
secondary_value='OverallRisk'
)

```
[[Back to top]](#) 

