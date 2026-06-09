---
id: rolematchdto
title: Rolematchdto
pagination_label: Rolematchdto
sidebar_label: Rolematchdto
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Rolematchdto', 'Rolematchdto'] 
slug: /tools/sdk/python/v1/models/rolematchdto
tags: ['SDK', 'Software Development Kit', 'Rolematchdto', 'Rolematchdto']
---

# Rolematchdto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role_ref** | [**Basereferencedto**](basereferencedto) |  | [optional] 
**matched_attributes** | [**[]Contextattributedto**](contextattributedto) |  | [optional] 
}

## Example

```python
from sailpoint.identities_v1.models.rolematchdto import Rolematchdto

rolematchdto = Rolematchdto(
role_ref=sailpoint.identities_v1.models.base_reference_dto.Base Reference Dto(
                    type = 'IDENTITY', 
                    id = '2c91808568c529c60168cca6f90c1313', 
                    name = 'William Wilson', ),
matched_attributes=[
                    sailpoint.identities_v1.models.context_attribute_dto.Context Attribute Dto(
                        attribute = 'location', 
                        value = Austin, 
                        derived = False, )
                    ]
)

```
[[Back to top]](#) 

