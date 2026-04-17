---
id: get-advanced-search200-response
title: GetAdvancedSearch200Response
pagination_label: GetAdvancedSearch200Response
sidebar_label: GetAdvancedSearch200Response
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'GetAdvancedSearch200Response', 'GetAdvancedSearch200Response'] 
slug: /tools/sdk/python//models/get-advanced-search200-response
tags: ['SDK', 'Software Development Kit', 'GetAdvancedSearch200Response', 'GetAdvancedSearch200Response']
---

# GetAdvancedSearch200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advanced_search** | [**[]AdvancedSearch**](advanced-search) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.get_advanced_search200_response import GetAdvancedSearch200Response

get_advanced_search200_response = GetAdvancedSearch200Response(
advanced_search=[
                    sailpoint.nerm.models.advanced_search.AdvancedSearch(
                        id = '', 
                        uid = '', 
                        label = '', 
                        condition_rules_attributes = [
                            null
                            ], )
                    ]
)

```
[[Back to top]](#) 

