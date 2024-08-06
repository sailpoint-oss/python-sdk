# ViolationOwnerAssignmentConfigOwnerRef

The owner of the violation assignment config.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Owner type. | [optional] 
**id** | **str** | Owner&#39;s ID. | [optional] 
**name** | **str** | Owner&#39;s name. | [optional] 

## Example

```python
from sailpoint.v2024.models.violation_owner_assignment_config_owner_ref import ViolationOwnerAssignmentConfigOwnerRef

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


