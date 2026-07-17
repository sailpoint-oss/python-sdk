---
id: bulk-approve-entitlement-recommendation-request
title: BulkApproveEntitlementRecommendationRequest
pagination_label: BulkApproveEntitlementRecommendationRequest
sidebar_label: BulkApproveEntitlementRecommendationRequest
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'BulkApproveEntitlementRecommendationRequest', 'BulkApproveEntitlementRecommendationRequest'] 
slug: /tools/sdk/python/suggested-entitlement-description/models/bulk-approve-entitlement-recommendation-request
tags: ['SDK', 'Software Development Kit', 'BulkApproveEntitlementRecommendationRequest', 'BulkApproveEntitlementRecommendationRequest']
---

# BulkApproveEntitlementRecommendationRequest

Request body for bulk-approving a set of entitlement recommendations.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**[]BulkApproveEntitlementRecommendationItem**](bulk-approve-entitlement-recommendation-item) | The list of recommendation items to approve. | [required]
}

## Example

```python
from sailpoint.suggested_entitlement_description.models.bulk_approve_entitlement_recommendation_request import BulkApproveEntitlementRecommendationRequest

bulk_approve_entitlement_recommendation_request = BulkApproveEntitlementRecommendationRequest(
items=[{"id":"79db50d4-723c-4aa0-a824-83c2205d82d1","recordType":"SED","description":"Provides access and permissions related to the Delinea Secret Server Cloud system."},{"id":"a1b2c3d4-e5f6-7890-abcd-ef1234567890","recordType":"privilege","privilegeLevel":"high"}]
)

```
[[Back to top]](#) 

