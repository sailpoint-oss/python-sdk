---
id: segment-visibility-criteria
title: SegmentVisibilityCriteria
pagination_label: SegmentVisibilityCriteria
sidebar_label: SegmentVisibilityCriteria
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'SegmentVisibilityCriteria', 'SegmentVisibilityCriteria'] 
slug: /tools/sdk/python/v1/models/segment-visibility-criteria
tags: ['SDK', 'Software Development Kit', 'SegmentVisibilityCriteria', 'SegmentVisibilityCriteria']
---

# SegmentVisibilityCriteria


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expression** | [**Expression**](expression) |  | [optional] 
}

## Example

```python
from sailpoint.segments_v1.models.segment_visibility_criteria import SegmentVisibilityCriteria

segment_visibility_criteria = SegmentVisibilityCriteria(
expression=sailpoint.segments_v1.models.expression.Expression(
                    operator = 'EQUALS', 
                    attribute = 'location', 
                    value = sailpoint.segments_v1.models.value.Value(
                        type = 'STRING', ), 
                    children = [], )
)

```
[[Back to top]](#) 

