# GetRoleAssignments200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Assignment Id | [optional] 
**role** | [**BaseReferenceDto1**](BaseReferenceDto1.md) |  | [optional] 
**comments** | **str** | Comments added by the user when the assignment was made | [optional] 
**assignment_source** | **str** | Source describing how this assignment was made | [optional] 
**assigner** | [**BaseReferenceDto1**](BaseReferenceDto1.md) |  | [optional] 
**assigned_dimensions** | [**List[BaseReferenceDto1]**](BaseReferenceDto1.md) | Dimensions assigned related to this role | [optional] 
**assignment_context** | [**AssignmentContextDto**](AssignmentContextDto.md) |  | [optional] 
**account_targets** | [**List[RoleTargetDto]**](RoleTargetDto.md) |  | [optional] 
**remove_date** | **str** | Date that the assignment will be removed | [optional] 

## Example

```python
from sailpoint.beta.models.get_role_assignments200_response_inner import GetRoleAssignments200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetRoleAssignments200ResponseInner from a JSON string
get_role_assignments200_response_inner_instance = GetRoleAssignments200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(GetRoleAssignments200ResponseInner.to_json())

# convert the object into a dict
get_role_assignments200_response_inner_dict = get_role_assignments200_response_inner_instance.to_dict()
# create an instance of GetRoleAssignments200ResponseInner from a dict
get_role_assignments200_response_inner_from_dict = GetRoleAssignments200ResponseInner.from_dict(get_role_assignments200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


