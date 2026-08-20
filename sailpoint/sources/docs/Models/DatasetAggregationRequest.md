---
id: dataset-aggregation-request
title: DatasetAggregationRequest
pagination_label: DatasetAggregationRequest
sidebar_label: DatasetAggregationRequest
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'DatasetAggregationRequest', 'DatasetAggregationRequest'] 
slug: /tools/sdk/python/sources/models/dataset-aggregation-request
tags: ['SDK', 'Software Development Kit', 'DatasetAggregationRequest', 'DatasetAggregationRequest']
---

# DatasetAggregationRequest

Optional request body for starting a dataset aggregation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | **map[string]object** | Connector-specific aggregation configuration. | [optional] 
}

## Example

```python
from sailpoint.sources.models.dataset_aggregation_request import DatasetAggregationRequest

dataset_aggregation_request = DatasetAggregationRequest(
config={"region":"us-east-1"}
)

```
[[Back to top]](#) 

