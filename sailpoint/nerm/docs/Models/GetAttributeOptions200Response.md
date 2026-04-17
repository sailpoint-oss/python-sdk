---
id: get-attribute-options200-response
title: GetAttributeOptions200Response
pagination_label: GetAttributeOptions200Response
sidebar_label: GetAttributeOptions200Response
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'GetAttributeOptions200Response', 'GetAttributeOptions200Response'] 
slug: /tools/sdk/python//models/get-attribute-options200-response
tags: ['SDK', 'Software Development Kit', 'GetAttributeOptions200Response', 'GetAttributeOptions200Response']
---

# GetAttributeOptions200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ne_attribute_options** | [**[]AttributeOption**](attribute-option) |  | [optional] 
**metadata** | [**Metadata**](metadata) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.get_attribute_options200_response import GetAttributeOptions200Response

get_attribute_options200_response = GetAttributeOptions200Response(
ne_attribute_options=[
                    sailpoint.nerm.models.attribute_option.AttributeOption(
                        id = '', 
                        uid = '', 
                        ne_attribute_id = '', 
                        option = '', )
                    ],
metadata=sailpoint.nerm.models.metadata.Metadata(
                    limit = 56, 
                    offset = 56, 
                    total = 56, 
                    next = '/endpoint?limit=10&offset=60', 
                    previous = '/endpoint?limit=10&offset=40', )
)

```
[[Back to top]](#) 

