---
id: beta-role-assignment-dto-assignment-context
title: RoleAssignmentDtoAssignmentContext
pagination_label: RoleAssignmentDtoAssignmentContext
sidebar_label: RoleAssignmentDtoAssignmentContext
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'RoleAssignmentDtoAssignmentContext', 'BetaRoleAssignmentDtoAssignmentContext'] 
slug: /tools/sdk/python/beta/models/role-assignment-dto-assignment-context
tags: ['SDK', 'Software Development Kit', 'RoleAssignmentDtoAssignmentContext', 'BetaRoleAssignmentDtoAssignmentContext']
---

# RoleAssignmentDtoAssignmentContext


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requested** | [**AccessRequestContext**](access-request-context) |  | [optional] 
**matched** | [**[]RoleMatchDto**](role-match-dto) |  | [optional] 
**computed_date** | **str** | Date that the assignment will was evaluated | [optional] 
}

## Example

```python
from sailpoint.beta.models.role_assignment_dto_assignment_context import RoleAssignmentDtoAssignmentContext

role_assignment_dto_assignment_context = RoleAssignmentDtoAssignmentContext(
requested=sailpoint.beta.models.access_request_context.Access Request Context(
                    context_attributes = [
                        sailpoint.beta.models.context_attribute_dto.Context Attribute Dto(
                            attribute = 'location', 
                            value = Austin, 
                            derived = False, )
                        ], ),
matched=[
                    sailpoint.beta.models.role_match_dto.Role Match Dto(
                        role_ref = sailpoint.beta.models.base_reference_dto.Base Reference Dto(
                            id = 'ff8081814d977c21014da056804a0af3', 
                            name = 'Github', ), 
                        matched_attributes = [
                            sailpoint.beta.models.context_attribute_dto.Context Attribute Dto(
                                attribute = 'location', 
                                value = Austin, 
                                derived = False, )
                            ], )
                    ],
computed_date='Wed Feb 14 10:58:42'
)

```
[[Back to top]](#) 

