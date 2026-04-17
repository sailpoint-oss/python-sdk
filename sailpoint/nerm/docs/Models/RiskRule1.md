---
id: risk-rule1
title: RiskRule1
pagination_label: RiskRule1
sidebar_label: RiskRule1
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'RiskRule1', 'RiskRule1'] 
slug: /tools/sdk/python//models/risk-rule1
tags: ['SDK', 'Software Development Kit', 'RiskRule1', 'RiskRule1']
---

# RiskRule1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** |  **Enum** [  'RiskRule' ] |  | [required]
**comparison_operator** |  **Enum** [  '==',    '>',    '<' ] |  | [optional] 
**value** | **str** |  | [required]
**secondary_value** |  **Enum** [  'OverallRisk' ] |  | [required]
}

## Example

```python
from sailpoint.nerm.models.risk_rule1 import RiskRule1

risk_rule1 = RiskRule1(
type='RiskRule',
comparison_operator='==',
value='',
secondary_value='OverallRisk'
)

```
[[Back to top]](#) 

