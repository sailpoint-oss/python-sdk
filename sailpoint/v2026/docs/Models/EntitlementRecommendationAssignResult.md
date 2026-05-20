---
id: v2026-entitlement-recommendation-assign-result
title: EntitlementRecommendationAssignResult
pagination_label: EntitlementRecommendationAssignResult
sidebar_label: EntitlementRecommendationAssignResult
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'EntitlementRecommendationAssignResult', 'V2026EntitlementRecommendationAssignResult'] 
slug: /tools/sdk/python/v2026/models/entitlement-recommendation-assign-result
tags: ['SDK', 'Software Development Kit', 'EntitlementRecommendationAssignResult', 'V2026EntitlementRecommendationAssignResult']
---

# EntitlementRecommendationAssignResult

Response body returned when entitlement recommendations are successfully queued for assignment.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batch_id** | **str** | The unique identifier of the assignment batch created by this request. | [optional] 
}

## Example

```python
from sailpoint.v2026.models.entitlement_recommendation_assign_result import EntitlementRecommendationAssignResult

entitlement_recommendation_assign_result = EntitlementRecommendationAssignResult(
batch_id='770e8400-e29b-41d4-a716-446655440099'
)

```
[[Back to top]](#) 

