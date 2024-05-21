# RoleAssignmentDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Assignment Id | [optional] 
**role** | [**BaseReferenceDto**](BaseReferenceDto.md) |  | [optional] 
**comments** | **str** | Comments added by the user when the assignment was made | [optional] 
**assignment_source** | **str** | Source describing how this assignment was made | [optional] 
**assigner** | [**BaseReferenceDto**](BaseReferenceDto.md) |  | [optional] 
**assigned_dimensions** | [**List[BaseReferenceDto]**](BaseReferenceDto.md) | Dimensions assigned related to this role | [optional] 
**assignment_context** | [**AssignmentContextDto**](AssignmentContextDto.md) |  | [optional] 
**account_targets** | [**List[RoleTargetDto]**](RoleTargetDto.md) |  | [optional] 
**remove_date** | **str** | Date that the assignment will be removed | [optional] 

## Example

```python
from sailpoint.beta.models.role_assignment_dto import RoleAssignmentDto

# TODO update the JSON string below
json = "{}"
# create an instance of RoleAssignmentDto from a JSON string
role_assignment_dto_instance = RoleAssignmentDto.from_json(json)
# print the JSON string representation of the object
print RoleAssignmentDto.to_json()

# convert the object into a dict
role_assignment_dto_dict = role_assignment_dto_instance.to_dict()
# create an instance of RoleAssignmentDto from a dict
role_assignment_dto_form_dict = role_assignment_dto.from_dict(role_assignment_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


