# ViolationOwnerAssignmentConfig


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assignment_rule** | **str** | Details about the violations owner. MANAGER - identity&#39;s manager STATIC - Governance Group or Identity | [optional] 
**owner_ref** | [**ViolationOwnerAssignmentConfigOwnerRef**](ViolationOwnerAssignmentConfigOwnerRef.md) |  | [optional] 

## Example

```python
from sailpoint.v3.models.violation_owner_assignment_config import ViolationOwnerAssignmentConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ViolationOwnerAssignmentConfig from a JSON string
violation_owner_assignment_config_instance = ViolationOwnerAssignmentConfig.from_json(json)
# print the JSON string representation of the object
print ViolationOwnerAssignmentConfig.to_json()

# convert the object into a dict
violation_owner_assignment_config_dict = violation_owner_assignment_config_instance.to_dict()
# create an instance of ViolationOwnerAssignmentConfig from a dict
violation_owner_assignment_config_form_dict = violation_owner_assignment_config.from_dict(violation_owner_assignment_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


