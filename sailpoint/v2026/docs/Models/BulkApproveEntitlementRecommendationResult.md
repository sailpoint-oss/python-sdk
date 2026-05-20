---
id: v2026-bulk-approve-entitlement-recommendation-result
title: BulkApproveEntitlementRecommendationResult
pagination_label: BulkApproveEntitlementRecommendationResult
sidebar_label: BulkApproveEntitlementRecommendationResult
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'BulkApproveEntitlementRecommendationResult', 'V2026BulkApproveEntitlementRecommendationResult'] 
slug: /tools/sdk/python/v2026/models/bulk-approve-entitlement-recommendation-result
tags: ['SDK', 'Software Development Kit', 'BulkApproveEntitlementRecommendationResult', 'V2026BulkApproveEntitlementRecommendationResult']
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
from sailpoint.v2026.models.bulk_approve_entitlement_recommendation_result import BulkApproveEntitlementRecommendationResult

bulk_approve_entitlement_recommendation_result = BulkApproveEntitlementRecommendationResult(
id='79db50d4-723c-4aa0-a824-83c2205d82d1',
status='SUCCESS',
failed_reason=''
)

```
[[Back to top]](#) 

