---
id: advanced-search
title: AdvancedSearch
pagination_label: AdvancedSearch
sidebar_label: AdvancedSearch
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'AdvancedSearch', 'AdvancedSearch'] 
slug: /tools/sdk/python//models/advanced-search
tags: ['SDK', 'Software Development Kit', 'AdvancedSearch', 'AdvancedSearch']
---

# AdvancedSearch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**uid** | **str** |  | [optional] [readonly] 
**label** | **str** |  | [optional] 
**condition_rules_attributes** | [**[]AdvancedSearchConditionRulesAttributesInner**](advanced-search-condition-rules-attributes-inner) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.advanced_search import AdvancedSearch

advanced_search = AdvancedSearch(
id='',
uid='',
label='',
condition_rules_attributes=[
                    null
                    ]
)

```
[[Back to top]](#) 

