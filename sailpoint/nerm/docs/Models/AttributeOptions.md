---
id: attribute-options
title: AttributeOptions
pagination_label: AttributeOptions
sidebar_label: AttributeOptions
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'AttributeOptions', 'AttributeOptions'] 
slug: /tools/sdk/python//models/attribute-options
tags: ['SDK', 'Software Development Kit', 'AttributeOptions', 'AttributeOptions']
---

# AttributeOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ne_attribute_options** | [**[]AttributeOption**](attribute-option) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.attribute_options import AttributeOptions

attribute_options = AttributeOptions(
ne_attribute_options=[
                    sailpoint.nerm.models.attribute_option.AttributeOption(
                        id = '', 
                        uid = '', 
                        ne_attribute_id = '', 
                        option = '', )
                    ]
)

```
[[Back to top]](#) 

