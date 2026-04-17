---
id: get-risk-score200-response
title: GetRiskScore200Response
pagination_label: GetRiskScore200Response
sidebar_label: GetRiskScore200Response
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'GetRiskScore200Response', 'GetRiskScore200Response'] 
slug: /tools/sdk/python//models/get-risk-score200-response
tags: ['SDK', 'Software Development Kit', 'GetRiskScore200Response', 'GetRiskScore200Response']
---

# GetRiskScore200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**risk_score** | [**RiskScore**](risk-score) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.get_risk_score200_response import GetRiskScore200Response

get_risk_score200_response = GetRiskScore200Response(
risk_score=sailpoint.nerm.models.risk_score.RiskScore(
                    id = '', 
                    uid = '', 
                    object_id = '', 
                    object_type = 'Profile', 
                    overall_score = 1.337, 
                    overall_risk_level_id = '', 
                    impact_score = 1.337, 
                    impact_risk_level_id = '', 
                    probability_score = 1.337, 
                    probability_risk_level_id = '', )
)

```
[[Back to top]](#) 

