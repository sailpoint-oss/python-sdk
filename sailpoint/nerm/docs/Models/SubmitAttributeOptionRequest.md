---
id: submit-attribute-option-request
title: SubmitAttributeOptionRequest
pagination_label: SubmitAttributeOptionRequest
sidebar_label: SubmitAttributeOptionRequest
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'SubmitAttributeOptionRequest', 'SubmitAttributeOptionRequest'] 
slug: /tools/sdk/python//models/submit-attribute-option-request
tags: ['SDK', 'Software Development Kit', 'SubmitAttributeOptionRequest', 'SubmitAttributeOptionRequest']
---

# SubmitAttributeOptionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ne_attribute_option** | [**AttributeOption1**](attribute-option1) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.submit_attribute_option_request import SubmitAttributeOptionRequest

submit_attribute_option_request = SubmitAttributeOptionRequest(
ne_attribute_option=sailpoint.nerm.models.attribute_option_1.AttributeOption_1(
                    ne_attribute_id = '', 
                    option = '', )
)

```
[[Back to top]](#) 

