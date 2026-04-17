---
id: get-risk-scores200-response
title: GetRiskScores200Response
pagination_label: GetRiskScores200Response
sidebar_label: GetRiskScores200Response
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'GetRiskScores200Response', 'GetRiskScores200Response'] 
slug: /tools/sdk/python//models/get-risk-scores200-response
tags: ['SDK', 'Software Development Kit', 'GetRiskScores200Response', 'GetRiskScores200Response']
---

# GetRiskScores200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**risk_scores** | [**[]RiskScore**](risk-score) |  | [optional] 
**metadata** | [**Metadata**](metadata) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.get_risk_scores200_response import GetRiskScores200Response

get_risk_scores200_response = GetRiskScores200Response(
risk_scores=[
                    sailpoint.nerm.models.risk_score.RiskScore(
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
                    ],
metadata=sailpoint.nerm.models.metadata.Metadata(
                    limit = 56, 
                    offset = 56, 
                    total = 56, 
                    next = '/endpoint?limit=10&offset=60', 
                    previous = '/endpoint?limit=10&offset=40', )
)

```
[[Back to top]](#) 

