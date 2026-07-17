---
id: recommendation-request
title: RecommendationRequest
pagination_label: RecommendationRequest
sidebar_label: RecommendationRequest
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'RecommendationRequest', 'RecommendationRequest'] 
slug: /tools/sdk/python/iai-recommendations/models/recommendation-request
tags: ['SDK', 'Software Development Kit', 'RecommendationRequest', 'RecommendationRequest']
---

# RecommendationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identity_id** | **str** | The identity ID | [optional] 
**item** | [**AccessItemRef**](access-item-ref) |  | [optional] 
}

## Example

```python
from sailpoint.iai_recommendations.models.recommendation_request import RecommendationRequest

recommendation_request = RecommendationRequest(
identity_id='2c938083633d259901633d25c68c00fa',
item=sailpoint.iai_recommendations.models.access_item_ref.Access Item Ref(
                    id = '2c938083633d259901633d2623ec0375', 
                    type = 'ENTITLEMENT', )
)

```
[[Back to top]](#) 

