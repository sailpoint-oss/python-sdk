---
id: submit-attribute-option200-response
title: SubmitAttributeOption200Response
pagination_label: SubmitAttributeOption200Response
sidebar_label: SubmitAttributeOption200Response
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'SubmitAttributeOption200Response', 'SubmitAttributeOption200Response'] 
slug: /tools/sdk/python//models/submit-attribute-option200-response
tags: ['SDK', 'Software Development Kit', 'SubmitAttributeOption200Response', 'SubmitAttributeOption200Response']
---

# SubmitAttributeOption200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ne_attribute_option** | [**AttributeOption**](attribute-option) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.submit_attribute_option200_response import SubmitAttributeOption200Response

submit_attribute_option200_response = SubmitAttributeOption200Response(
ne_attribute_option=sailpoint.nerm.models.attribute_option.AttributeOption(
                    id = '', 
                    uid = '', 
                    ne_attribute_id = '', 
                    option = '', )
)

```
[[Back to top]](#) 

