---
id: v2026-prompt-insights-metrics
title: PromptInsightsMetrics
pagination_label: PromptInsightsMetrics
sidebar_label: PromptInsightsMetrics
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'PromptInsightsMetrics', 'V2026PromptInsightsMetrics'] 
slug: /tools/sdk/python/v2026/models/prompt-insights-metrics
tags: ['SDK', 'Software Development Kit', 'PromptInsightsMetrics', 'V2026PromptInsightsMetrics']
---

# PromptInsightsMetrics

Aggregate prompt insights metrics for the requested time window.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prompts_scanned** | **int** | Count of prompts scanned in the interval. | [optional] 
**prompts_redacted** | **int** | Count of prompts redacted in the interval. | [optional] 
}

## Example

```python
from sailpoint.v2026.models.prompt_insights_metrics import PromptInsightsMetrics

prompt_insights_metrics = PromptInsightsMetrics(
prompts_scanned=125000,
prompts_redacted=89
)

```
[[Back to top]](#) 

