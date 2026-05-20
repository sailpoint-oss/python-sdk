---
id: v2026-entitlement-recommendation-assignee-one-of
title: EntitlementRecommendationAssigneeOneOf
pagination_label: EntitlementRecommendationAssigneeOneOf
sidebar_label: EntitlementRecommendationAssigneeOneOf
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'EntitlementRecommendationAssigneeOneOf', 'V2026EntitlementRecommendationAssigneeOneOf'] 
slug: /tools/sdk/python/v2026/models/entitlement-recommendation-assignee-one-of
tags: ['SDK', 'Software Development Kit', 'EntitlementRecommendationAssigneeOneOf', 'V2026EntitlementRecommendationAssigneeOneOf']
---

# EntitlementRecommendationAssigneeOneOf

Assign to a specific identity or governance group. The value field is required and must be the ID of the identity or governance group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** |  **Enum** [  'IDENTITY',    'GOVERNANCE_GROUP' ] | The type of assignee. | [required]
**value** | **str** | The ID of the identity or governance group to assign to. | [required]
}

## Example

```python
from sailpoint.v2026.models.entitlement_recommendation_assignee_one_of import EntitlementRecommendationAssigneeOneOf

entitlement_recommendation_assignee_one_of = EntitlementRecommendationAssigneeOneOf(
type='IDENTITY',
value='2c91808a7f3b2e8a017f3c3e5f6d0099'
)

```
[[Back to top]](#) 

