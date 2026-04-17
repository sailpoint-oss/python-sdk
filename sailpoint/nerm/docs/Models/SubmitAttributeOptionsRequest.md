---
id: submit-attribute-options-request
title: SubmitAttributeOptionsRequest
pagination_label: SubmitAttributeOptionsRequest
sidebar_label: SubmitAttributeOptionsRequest
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'SubmitAttributeOptionsRequest', 'SubmitAttributeOptionsRequest'] 
slug: /tools/sdk/python//models/submit-attribute-options-request
tags: ['SDK', 'Software Development Kit', 'SubmitAttributeOptionsRequest', 'SubmitAttributeOptionsRequest']
---

# SubmitAttributeOptionsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ne_attribute_options** | [**[]AttributeOption1**](attribute-option1) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.submit_attribute_options_request import SubmitAttributeOptionsRequest

submit_attribute_options_request = SubmitAttributeOptionsRequest(
ne_attribute_options=[
                    sailpoint.nerm.models.attribute_option_1.AttributeOption_1(
                        ne_attribute_id = '', 
                        option = '', )
                    ]
)

```
[[Back to top]](#) 

