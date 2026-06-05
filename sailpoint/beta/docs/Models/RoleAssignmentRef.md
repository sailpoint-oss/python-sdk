---
id: beta-role-assignment-ref
title: RoleAssignmentRef
pagination_label: RoleAssignmentRef
sidebar_label: RoleAssignmentRef
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'RoleAssignmentRef', 'BetaRoleAssignmentRef'] 
slug: /tools/sdk/python/beta/models/role-assignment-ref
tags: ['SDK', 'Software Development Kit', 'RoleAssignmentRef', 'BetaRoleAssignmentRef']
---

# RoleAssignmentRef


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Assignment Id | [optional] 
**role** | [**BaseReferenceDto1**](base-reference-dto1) |  | [optional] 
**added_date** | **datetime** | Date that the assignment was added | [optional] 
**start_date** | **datetime** | Date when assignment will be active, if requested with a future date. If null, assignment is active immediately | [optional] 
**remove_date** | **datetime** | Date that the assignment will be removed | [optional] 
}

## Example

```python
from sailpoint.beta.models.role_assignment_ref import RoleAssignmentRef

role_assignment_ref = RoleAssignmentRef(
id='1cbb0705b38c4226b1334eadd8874086',
role=sailpoint.beta.models.base_reference_dto.Base Reference Dto(
                    id = 'ff8081814d977c21014da056804a0af3', 
                    name = 'Github', ),
added_date='2025-07-11T18:45:37.098Z',
start_date='2026-01-22T19:15Z',
remove_date='2026-01-23T19:15Z'
)

```
[[Back to top]](#) 

