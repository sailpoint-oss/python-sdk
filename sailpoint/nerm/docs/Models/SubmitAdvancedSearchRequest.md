---
id: submit-advanced-search-request
title: SubmitAdvancedSearchRequest
pagination_label: SubmitAdvancedSearchRequest
sidebar_label: SubmitAdvancedSearchRequest
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'SubmitAdvancedSearchRequest', 'SubmitAdvancedSearchRequest'] 
slug: /tools/sdk/python//models/submit-advanced-search-request
tags: ['SDK', 'Software Development Kit', 'SubmitAdvancedSearchRequest', 'SubmitAdvancedSearchRequest']
---

# SubmitAdvancedSearchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advanced_search** | [**AdvancedSearch1**](advanced-search1) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.submit_advanced_search_request import SubmitAdvancedSearchRequest

submit_advanced_search_request = SubmitAdvancedSearchRequest(
advanced_search=sailpoint.nerm.models.advanced_search_1.AdvancedSearch_1(
                    label = '', 
                    condition_rules_attributes = [
                        null
                        ], )
)

```
[[Back to top]](#) 

