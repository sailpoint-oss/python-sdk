---
id: bulk-approve-entitlement-recommendation-result
title: BulkApproveEntitlementRecommendationResult
pagination_label: BulkApproveEntitlementRecommendationResult
sidebar_label: BulkApproveEntitlementRecommendationResult
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'BulkApproveEntitlementRecommendationResult', 'BulkApproveEntitlementRecommendationResult'] 
slug: /tools/sdk/python/suggested-entitlement-description/models/bulk-approve-entitlement-recommendation-result
tags: ['SDK', 'Software Development Kit', 'BulkApproveEntitlementRecommendationResult', 'BulkApproveEntitlementRecommendationResult']
---

# BulkApproveEntitlementRecommendationResult

The result for a single item in a bulk entitlement recommendation approval response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the processed recommendation record. | [optional] 
**status** |  **Enum** [  'SUCCESS',    'FAILURE' ] | The outcome of the approval for this item. | [optional] 
**failed_reason** | **str** | The reason for failure if status is FAILURE; null on success. | [optional] 
}

## Example

```python
from sailpoint.suggested_entitlement_description.models.bulk_approve_entitlement_recommendation_result import BulkApproveEntitlementRecommendationResult

bulk_approve_entitlement_recommendation_result = BulkApproveEntitlementRecommendationResult(
id='79db50d4-723c-4aa0-a824-83c2205d82d1',
status='SUCCESS',
failed_reason=''
)

```
[[Back to top]](#) 

