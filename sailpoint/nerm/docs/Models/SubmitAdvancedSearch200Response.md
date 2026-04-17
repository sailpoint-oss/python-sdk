---
id: submit-advanced-search200-response
title: SubmitAdvancedSearch200Response
pagination_label: SubmitAdvancedSearch200Response
sidebar_label: SubmitAdvancedSearch200Response
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'SubmitAdvancedSearch200Response', 'SubmitAdvancedSearch200Response'] 
slug: /tools/sdk/python//models/submit-advanced-search200-response
tags: ['SDK', 'Software Development Kit', 'SubmitAdvancedSearch200Response', 'SubmitAdvancedSearch200Response']
---

# SubmitAdvancedSearch200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advanced_search** | [**AdvancedSearch**](advanced-search) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.submit_advanced_search200_response import SubmitAdvancedSearch200Response

submit_advanced_search200_response = SubmitAdvancedSearch200Response(
advanced_search=sailpoint.nerm.models.advanced_search.AdvancedSearch(
                    id = '', 
                    uid = '', 
                    label = '', 
                    condition_rules_attributes = [
                        null
                        ], )
)

```
[[Back to top]](#) 

