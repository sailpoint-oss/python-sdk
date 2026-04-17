---
id: get-risk-level200-response
title: GetRiskLevel200Response
pagination_label: GetRiskLevel200Response
sidebar_label: GetRiskLevel200Response
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'GetRiskLevel200Response', 'GetRiskLevel200Response'] 
slug: /tools/sdk/python//models/get-risk-level200-response
tags: ['SDK', 'Software Development Kit', 'GetRiskLevel200Response', 'GetRiskLevel200Response']
---

# GetRiskLevel200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**risk_level** | [**RiskLevel**](risk-level) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.get_risk_level200_response import GetRiskLevel200Response

get_risk_level200_response = GetRiskLevel200Response(
risk_level=sailpoint.nerm.models.risk_level.RiskLevel(
                    id = '', 
                    uid = '', 
                    label = '', 
                    points = 1.337, 
                    order = 0, )
)

```
[[Back to top]](#) 

