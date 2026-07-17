---
id: access-recommendation-message
title: AccessRecommendationMessage
pagination_label: AccessRecommendationMessage
sidebar_label: AccessRecommendationMessage
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'AccessRecommendationMessage', 'AccessRecommendationMessage'] 
slug: /tools/sdk/python/iai-access-request-recommendations/models/access-recommendation-message
tags: ['SDK', 'Software Development Kit', 'AccessRecommendationMessage', 'AccessRecommendationMessage']
---

# AccessRecommendationMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interpretation** | **str** | Information about why the access item was recommended. | [optional] 
}

## Example

```python
from sailpoint.iai_access_request_recommendations.models.access_recommendation_message import AccessRecommendationMessage

access_recommendation_message = AccessRecommendationMessage(
interpretation='95% of your peers have this access.'
)

```
[[Back to top]](#) 

