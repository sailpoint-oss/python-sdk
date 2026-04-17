---
id: get-profile-type-attributes200-response
title: GetProfileTypeAttributes200Response
pagination_label: GetProfileTypeAttributes200Response
sidebar_label: GetProfileTypeAttributes200Response
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'GetProfileTypeAttributes200Response', 'GetProfileTypeAttributes200Response'] 
slug: /tools/sdk/python//models/get-profile-type-attributes200-response
tags: ['SDK', 'Software Development Kit', 'GetProfileTypeAttributes200Response', 'GetProfileTypeAttributes200Response']
---

# GetProfileTypeAttributes200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile_type_attributes** | [**ProfileTypeAttributes**](profile-type-attributes) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.get_profile_type_attributes200_response import GetProfileTypeAttributes200Response

get_profile_type_attributes200_response = GetProfileTypeAttributes200Response(
profile_type_attributes=sailpoint.nerm.models.profile_type_attributes.ProfileTypeAttributes(
                    count = 5, 
                    records = [
                        sailpoint.nerm.models.profile_type_attribute.ProfileTypeAttribute(
                            id = '1246d8b3-ac29-4015-8154-dea4434a73fa', 
                            uid = '1246d8b3-ac29-4015-8154-dea4434a73fa', 
                            label = 'object', 
                            synced = '1246d8b3-ac29-4015-8154-dea4434a73fa', )
                        ], )
)

```
[[Back to top]](#) 

