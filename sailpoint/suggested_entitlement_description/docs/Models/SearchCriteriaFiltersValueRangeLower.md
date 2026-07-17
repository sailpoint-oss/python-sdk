---
id: search-criteria-filters-value-range-lower
title: SearchCriteriaFiltersValueRangeLower
pagination_label: SearchCriteriaFiltersValueRangeLower
sidebar_label: SearchCriteriaFiltersValueRangeLower
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'SearchCriteriaFiltersValueRangeLower', 'SearchCriteriaFiltersValueRangeLower'] 
slug: /tools/sdk/python/suggested-entitlement-description/models/search-criteria-filters-value-range-lower
tags: ['SDK', 'Software Development Kit', 'SearchCriteriaFiltersValueRangeLower', 'SearchCriteriaFiltersValueRangeLower']
---

# SearchCriteriaFiltersValueRangeLower


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | The lower bound value. | [optional] 
**inclusive** | **bool** | Whether the lower bound is inclusive. | [optional] [default to False]
}

## Example

```python
from sailpoint.suggested_entitlement_description.models.search_criteria_filters_value_range_lower import SearchCriteriaFiltersValueRangeLower

search_criteria_filters_value_range_lower = SearchCriteriaFiltersValueRangeLower(
value='10',
inclusive=True
)

```
[[Back to top]](#) 

