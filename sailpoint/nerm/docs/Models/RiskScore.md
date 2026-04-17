---
id: risk-score
title: RiskScore
pagination_label: RiskScore
sidebar_label: RiskScore
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'RiskScore', 'RiskScore'] 
slug: /tools/sdk/python//models/risk-score
tags: ['SDK', 'Software Development Kit', 'RiskScore', 'RiskScore']
---

# RiskScore


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**uid** | **str** |  | [optional] [readonly] 
**object_id** | **str** |  | [optional] 
**object_type** |  **Enum** [  'Profile',    'WorkflowSession' ] |  | [optional] 
**overall_score** | **float** |  | [optional] 
**overall_risk_level_id** | **str** |  | [optional] 
**impact_score** | **float** |  | [optional] 
**impact_risk_level_id** | **str** |  | [optional] 
**probability_score** | **float** |  | [optional] 
**probability_risk_level_id** | **str** |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.risk_score import RiskScore

risk_score = RiskScore(
id='',
uid='',
object_id='',
object_type='Profile',
overall_score=1.337,
overall_risk_level_id='',
impact_score=1.337,
impact_risk_level_id='',
probability_score=1.337,
probability_risk_level_id=''
)

```
[[Back to top]](#) 

