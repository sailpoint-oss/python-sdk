# RoleAssignmentDtoAssignmentContext


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requested** | [**AccessRequestContext**](AccessRequestContext.md) |  | [optional] 
**matched** | [**List[RoleMatchDto]**](RoleMatchDto.md) |  | [optional] 
**computed_date** | **str** | Date that the assignment will was evaluated | [optional] 

## Example

```python
from sailpoint.v2024.models.role_assignment_dto_assignment_context import RoleAssignmentDtoAssignmentContext

# TODO update the JSON string below
json = "{}"
# create an instance of RoleAssignmentDtoAssignmentContext from a JSON string
role_assignment_dto_assignment_context_instance = RoleAssignmentDtoAssignmentContext.from_json(json)
# print the JSON string representation of the object
print(RoleAssignmentDtoAssignmentContext.to_json())

# convert the object into a dict
role_assignment_dto_assignment_context_dict = role_assignment_dto_assignment_context_instance.to_dict()
# create an instance of RoleAssignmentDtoAssignmentContext from a dict
role_assignment_dto_assignment_context_from_dict = RoleAssignmentDtoAssignmentContext.from_dict(role_assignment_dto_assignment_context_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


