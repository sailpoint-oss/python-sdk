---
id: v2025-role-assignment-dto-assigner
title: RoleAssignmentDtoAssigner
pagination_label: RoleAssignmentDtoAssigner
sidebar_label: RoleAssignmentDtoAssigner
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'RoleAssignmentDtoAssigner', 'V2025RoleAssignmentDtoAssigner'] 
slug: /tools/sdk/python/v2025/models/role-assignment-dto-assigner
tags: ['SDK', 'Software Development Kit', 'RoleAssignmentDtoAssigner', 'V2025RoleAssignmentDtoAssigner']
---

# RoleAssignmentDtoAssigner

The identity that performed the assignment. This could be blank or system

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** |  **Enum** [  'IDENTITY',    'UNKNOWN' ] | Object type | [optional] 
**id** | **str** | ID of the object to which this reference applies | [optional] 
**name** | **str** | Human-readable display name of the object to which this reference applies | [optional] 
}

## Example

```python
from sailpoint.v2025.models.role_assignment_dto_assigner import RoleAssignmentDtoAssigner

role_assignment_dto_assigner = RoleAssignmentDtoAssigner(
type='IDENTITY',
id='2c91808568c529c60168cca6f90c1313',
name='William Wilson'
)

```
[[Back to top]](#) 

