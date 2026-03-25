---
id: v2026-search-aggregation-specification
title: SearchAggregationSpecification
pagination_label: SearchAggregationSpecification
sidebar_label: SearchAggregationSpecification
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'SearchAggregationSpecification', 'V2026SearchAggregationSpecification'] 
slug: /tools/sdk/python/v2026/models/search-aggregation-specification
tags: ['SDK', 'Software Development Kit', 'SearchAggregationSpecification', 'V2026SearchAggregationSpecification']
---

# SearchAggregationSpecification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nested** | [**NestedAggregation**](nested-aggregation) |  | [optional] 
**metric** | [**MetricAggregation**](metric-aggregation) |  | [optional] 
**filter** | [**FilterAggregation**](filter-aggregation) |  | [optional] 
**bucket** | [**BucketAggregation**](bucket-aggregation) |  | [optional] 
**sub_aggregation** | [**SubSearchAggregationSpecification**](sub-search-aggregation-specification) |  | [optional] 
}

## Example

```python
from sailpoint.v2026.models.search_aggregation_specification import SearchAggregationSpecification

search_aggregation_specification = SearchAggregationSpecification(
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
                    min_doc_count = 2, ),
sub_aggregation=
)

```
[[Back to top]](#) 

