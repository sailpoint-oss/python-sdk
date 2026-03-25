---
id: v2026-aggregations
title: Aggregations
pagination_label: Aggregations
sidebar_label: Aggregations
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Aggregations', 'V2026Aggregations'] 
slug: /tools/sdk/python/v2026/models/aggregations
tags: ['SDK', 'Software Development Kit', 'Aggregations', 'V2026Aggregations']
---

# Aggregations


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nested** | [**NestedAggregation**](nested-aggregation) |  | [optional] 
**metric** | [**MetricAggregation**](metric-aggregation) |  | [optional] 
**filter** | [**FilterAggregation**](filter-aggregation) |  | [optional] 
**bucket** | [**BucketAggregation**](bucket-aggregation) |  | [optional] 
}

## Example

```python
from sailpoint.v2026.models.aggregations import Aggregations

aggregations = Aggregations(
nested=sailpoint.v2026.models.nested_aggregation.NestedAggregation(
                    name = 'id', 
                    type = 'access', ),
metric=sailpoint.v2026.models.metric_aggregation.MetricAggregation(
                    name = 'Access Name Count', 
                    type = 'UNIQUE_COUNT', 
                    field = '@access.name', ),
filter=sailpoint.v2026.models.filter_aggregation.FilterAggregation(
                    name = 'Entitlements', 
                    type = 'TERM', 
                    field = 'access.type', 
                    value = 'ENTITLEMENT', ),
bucket=sailpoint.v2026.models.bucket_aggregation.BucketAggregation(
                    name = 'Identity Locations', 
                    type = 'TERMS', 
                    field = 'attributes.city', 
                    size = 100, 
                    min_doc_count = 2, )
)

```
[[Back to top]](#) 

