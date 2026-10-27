---
id: machine-account-recommendation-explanation
title: MachineAccountRecommendationExplanation
pagination_label: MachineAccountRecommendationExplanation
sidebar_label: MachineAccountRecommendationExplanation
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'MachineAccountRecommendationExplanation', 'MachineAccountRecommendationExplanation'] 
slug: /tools/sdk/python/machine-account-recommendation/models/machine-account-recommendation-explanation
tags: ['SDK', 'Software Development Kit', 'MachineAccountRecommendationExplanation', 'MachineAccountRecommendationExplanation']
---

# MachineAccountRecommendationExplanation

A reason that contributed to a machine account recommendation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feature** | **str** | Account feature that contributed to the recommendation. | [optional] 
}

## Example

```python
from sailpoint.machine_account_recommendation.models.machine_account_recommendation_explanation import MachineAccountRecommendationExplanation

machine_account_recommendation_explanation = MachineAccountRecommendationExplanation(
feature='high-privilege-grant'
)

```
[[Back to top]](#) 

