---
id: v2026-visibility-criteria
title: VisibilityCriteria
pagination_label: VisibilityCriteria
sidebar_label: VisibilityCriteria
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'VisibilityCriteria', 'V2026VisibilityCriteria'] 
slug: /tools/sdk/python/v2026/models/visibility-criteria
tags: ['SDK', 'Software Development Kit', 'VisibilityCriteria', 'V2026VisibilityCriteria']
---

# VisibilityCriteria


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expression** | [**Expression**](expression) |  | [optional] 
}

## Example

```python
from sailpoint.v2026.models.visibility_criteria import VisibilityCriteria

visibility_criteria = VisibilityCriteria(
expression=sailpoint.v2026.models.expression.Expression(
                    operator = 'EQUALS', 
                    attribute = 'location', 
                    value = sailpoint.v2026.models.value.Value(
                        type = 'STRING', ), 
                    children = [], )
)

```
[[Back to top]](#) 

