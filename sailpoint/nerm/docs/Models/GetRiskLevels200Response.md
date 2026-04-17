---
id: get-risk-levels200-response
title: GetRiskLevels200Response
pagination_label: GetRiskLevels200Response
sidebar_label: GetRiskLevels200Response
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'GetRiskLevels200Response', 'GetRiskLevels200Response'] 
slug: /tools/sdk/python//models/get-risk-levels200-response
tags: ['SDK', 'Software Development Kit', 'GetRiskLevels200Response', 'GetRiskLevels200Response']
---

# GetRiskLevels200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**risk_levels** | [**[]RiskLevel**](risk-level) |  | [optional] 
**metadata** | [**Metadata**](metadata) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.get_risk_levels200_response import GetRiskLevels200Response

get_risk_levels200_response = GetRiskLevels200Response(
risk_levels=[
                    sailpoint.nerm.models.risk_level.RiskLevel(
                        id = '', 
                        uid = '', 
                        label = '', 
                        points = 1.337, 
                        order = 0, )
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

