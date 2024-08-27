# RoleAssignmentRef


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Assignment Id | [optional] 
**role** | [**BaseReferenceDto**](BaseReferenceDto.md) |  | [optional] 

## Example

```python
from sailpoint.beta.models.role_assignment_ref import RoleAssignmentRef

# TODO update the JSON string below
json = "{}"
# create an instance of RoleAssignmentRef from a JSON string
role_assignment_ref_instance = RoleAssignmentRef.from_json(json)
# print the JSON string representation of the object
print(RoleAssignmentRef.to_json())

# convert the object into a dict
role_assignment_ref_dict = role_assignment_ref_instance.to_dict()
# create an instance of RoleAssignmentRef from a dict
role_assignment_ref_from_dict = RoleAssignmentRef.from_dict(role_assignment_ref_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


