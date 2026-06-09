---
id: roleassignmentref
title: Roleassignmentref
pagination_label: Roleassignmentref
sidebar_label: Roleassignmentref
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Roleassignmentref', 'Roleassignmentref'] 
slug: /tools/sdk/python/v1/models/roleassignmentref
tags: ['SDK', 'Software Development Kit', 'Roleassignmentref', 'Roleassignmentref']
---

# Roleassignmentref


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Assignment Id | [optional] 
**role** | [**Basereferencedto**](basereferencedto) |  | [optional] 
**added_date** | **datetime** | Date that the assignment was added | [optional] 
**remove_date** | **datetime** | Date that the assignment will be removed | [optional] 
}

## Example

```python
from sailpoint.identities_v1.models.roleassignmentref import Roleassignmentref

roleassignmentref = Roleassignmentref(
id='1cbb0705b38c4226b1334eadd8874086',
role=sailpoint.identities_v1.models.base_reference_dto.Base Reference Dto(
                    type = 'IDENTITY', 
                    id = '2c91808568c529c60168cca6f90c1313', 
                    name = 'William Wilson', ),
added_date='2025-07-11T18:45:37.098Z',
remove_date='2026-01-23T19:15Z'
)

```
[[Back to top]](#) 

