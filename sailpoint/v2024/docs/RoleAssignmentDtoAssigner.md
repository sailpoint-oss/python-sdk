# RoleAssignmentDtoAssigner

The identity that performed the assignment. This could be blank or system

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Object type | [optional] 
**id** | **str** | ID of the object to which this reference applies | [optional] 
**name** | **str** | Human-readable display name of the object to which this reference applies | [optional] 

## Example

```python
from sailpoint.v2024.models.role_assignment_dto_assigner import RoleAssignmentDtoAssigner

# TODO update the JSON string below
json = "{}"
# create an instance of RoleAssignmentDtoAssigner from a JSON string
role_assignment_dto_assigner_instance = RoleAssignmentDtoAssigner.from_json(json)
# print the JSON string representation of the object
print(RoleAssignmentDtoAssigner.to_json())

# convert the object into a dict
role_assignment_dto_assigner_dict = role_assignment_dto_assigner_instance.to_dict()
# create an instance of RoleAssignmentDtoAssigner from a dict
role_assignment_dto_assigner_from_dict = RoleAssignmentDtoAssigner.from_dict(role_assignment_dto_assigner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


