---
id: aggregations
title: Aggregations
pagination_label: Aggregations
sidebar_label: Aggregations
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Aggregations', 'Aggregations'] 
slug: /tools/sdk/python/v1/models/aggregations
tags: ['SDK', 'Software Development Kit', 'Aggregations', 'Aggregations']
---

# Aggregations


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nested** | [**Nestedaggregation**](nestedaggregation) |  | [optional] 
**metric** | [**Metricaggregation**](metricaggregation) |  | [optional] 
**filter** | [**Filteraggregation**](filteraggregation) |  | [optional] 
**bucket** | [**Bucketaggregation**](bucketaggregation) |  | [optional] 
}

## Example

```python
from sailpoint.access_model_metadata_v1.models.aggregations import Aggregations

aggregations = Aggregations(
nested=sailpoint.access_model_metadata_v1.models.nestedaggregation.nestedaggregation(
                    name = 'id', 
                    type = 'access', ),
metric=sailpoint.access_model_metadata_v1.models.metricaggregation.metricaggregation(
                    name = 'Access Name Count', 
                    type = 'UNIQUE_COUNT', 
                    field = '@access.name', ),
filter=sailpoint.access_model_metadata_v1.models.filteraggregation.filteraggregation(
                    name = 'Entitlements', 
                    type = 'TERM', 
                    field = 'access.type', 
                    value = 'ENTITLEMENT', ),
bucket=sailpoint.access_model_metadata_v1.models.bucketaggregation.bucketaggregation(
                    name = 'Identity Locations', 
                    type = 'TERMS', 
                    field = 'attributes.city', 
                    size = 100, 
                    min_doc_count = 2, )
)

```
[[Back to top]](#) 

