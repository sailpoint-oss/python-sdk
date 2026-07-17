---
id: role-match-dto
title: RoleMatchDto
pagination_label: RoleMatchDto
sidebar_label: RoleMatchDto
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'RoleMatchDto', 'RoleMatchDto'] 
slug: /tools/sdk/python/identities/models/role-match-dto
tags: ['SDK', 'Software Development Kit', 'RoleMatchDto', 'RoleMatchDto']
---

# RoleMatchDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role_ref** | [**BaseReferenceDto**](base-reference-dto) |  | [optional] 
**matched_attributes** | [**[]ContextAttributeDto**](context-attribute-dto) |  | [optional] 
}

## Example

```python
from sailpoint.identities.models.role_match_dto import RoleMatchDto

role_match_dto = RoleMatchDto(
role_ref=sailpoint.identities.models.base_reference_dto.Base Reference Dto(
                    type = 'IDENTITY', 
                    id = '2c91808568c529c60168cca6f90c1313', 
                    name = 'William Wilson', ),
matched_attributes=[
                    sailpoint.identities.models.context_attribute_dto.Context Attribute Dto(
                        attribute = 'location', 
                        value = Austin, 
                        derived = False, )
                    ]
)

```
[[Back to top]](#) 

