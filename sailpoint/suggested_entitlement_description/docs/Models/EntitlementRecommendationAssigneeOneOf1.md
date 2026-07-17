---
id: entitlement-recommendation-assignee-one-of1
title: EntitlementRecommendationAssigneeOneOf1
pagination_label: EntitlementRecommendationAssigneeOneOf1
sidebar_label: EntitlementRecommendationAssigneeOneOf1
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'EntitlementRecommendationAssigneeOneOf1', 'EntitlementRecommendationAssigneeOneOf1'] 
slug: /tools/sdk/python/suggested-entitlement-description/models/entitlement-recommendation-assignee-one-of1
tags: ['SDK', 'Software Development Kit', 'EntitlementRecommendationAssigneeOneOf1', 'EntitlementRecommendationAssigneeOneOf1']
---

# EntitlementRecommendationAssigneeOneOf1

Assign to the source owner or entitlement owner role. No value field is required.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** |  **Enum** [  'SOURCE_OWNER',    'ENTITLEMENT_OWNER' ] | The type of assignee. | [required]
}

## Example

```python
from sailpoint.suggested_entitlement_description.models.entitlement_recommendation_assignee_one_of1 import EntitlementRecommendationAssigneeOneOf1

entitlement_recommendation_assignee_one_of1 = EntitlementRecommendationAssigneeOneOf1(
type='SOURCE_OWNER'
)

```
[[Back to top]](#) 

