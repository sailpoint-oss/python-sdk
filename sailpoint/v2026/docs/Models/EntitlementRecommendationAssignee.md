---
id: v2026-entitlement-recommendation-assignee
title: EntitlementRecommendationAssignee
pagination_label: EntitlementRecommendationAssignee
sidebar_label: EntitlementRecommendationAssignee
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'EntitlementRecommendationAssignee', 'V2026EntitlementRecommendationAssignee'] 
slug: /tools/sdk/python/v2026/models/entitlement-recommendation-assignee
tags: ['SDK', 'Software Development Kit', 'EntitlementRecommendationAssignee', 'V2026EntitlementRecommendationAssignee']
---

# EntitlementRecommendationAssignee

Describes the target assignee for entitlement recommendations.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** |  **Enum** [  'IDENTITY',    'GOVERNANCE_GROUP',    'SOURCE_OWNER',    'ENTITLEMENT_OWNER' ] | The type of assignee. | [required]
**value** | **str** | The ID of the identity or governance group to assign to. | [required]
}

## Example

```python
from sailpoint.v2026.models.entitlement_recommendation_assignee import EntitlementRecommendationAssignee

entitlement_recommendation_assignee = EntitlementRecommendationAssignee(
type='IDENTITY',
value='2c91808a7f3b2e8a017f3c3e5f6d0099'
)

```
[[Back to top]](#) 

