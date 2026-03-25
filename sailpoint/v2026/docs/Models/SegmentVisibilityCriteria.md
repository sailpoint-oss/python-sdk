---
id: v2026-segment-visibility-criteria
title: SegmentVisibilityCriteria
pagination_label: SegmentVisibilityCriteria
sidebar_label: SegmentVisibilityCriteria
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'SegmentVisibilityCriteria', 'V2026SegmentVisibilityCriteria'] 
slug: /tools/sdk/python/v2026/models/segment-visibility-criteria
tags: ['SDK', 'Software Development Kit', 'SegmentVisibilityCriteria', 'V2026SegmentVisibilityCriteria']
---

# SegmentVisibilityCriteria


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expression** | [**Expression**](expression) |  | [optional] 
}

## Example

```python
from sailpoint.v2026.models.segment_visibility_criteria import SegmentVisibilityCriteria

segment_visibility_criteria = SegmentVisibilityCriteria(
expression=sailpoint.v2026.models.expression.Expression(
                    operator = 'EQUALS', 
                    attribute = 'location', 
                    value = sailpoint.v2026.models.value.Value(
                        type = 'STRING', ), 
                    children = [], )
)

```
[[Back to top]](#) 

