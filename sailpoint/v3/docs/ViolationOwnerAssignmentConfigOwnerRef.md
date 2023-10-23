# ViolationOwnerAssignmentConfigOwnerRef


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**DtoType**](DtoType.md) |  | [optional] 
**id** | **str** | ID of the object to which this reference applies | [optional] 
**name** | **str** | Human-readable display name of the object to which this reference applies | [optional] 

## Example

```python
from v3.models.violation_owner_assignment_config_owner_ref import ViolationOwnerAssignmentConfigOwnerRef

# TODO update the JSON string below
json = "{}"
# create an instance of ViolationOwnerAssignmentConfigOwnerRef from a JSON string
violation_owner_assignment_config_owner_ref_instance = ViolationOwnerAssignmentConfigOwnerRef.from_json(json)
# print the JSON string representation of the object
print ViolationOwnerAssignmentConfigOwnerRef.to_json()

# convert the object into a dict
violation_owner_assignment_config_owner_ref_dict = violation_owner_assignment_config_owner_ref_instance.to_dict()
# create an instance of ViolationOwnerAssignmentConfigOwnerRef from a dict
violation_owner_assignment_config_owner_ref_form_dict = violation_owner_assignment_config_owner_ref.from_dict(violation_owner_assignment_config_owner_ref_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


