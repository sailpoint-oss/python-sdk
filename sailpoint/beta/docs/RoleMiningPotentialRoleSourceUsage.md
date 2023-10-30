# RoleMiningPotentialRoleSourceUsage


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The identity ID | [optional] 
**display_name** | **str** | Display name for the identity | [optional] 
**email** | **str** | Email address for the identity | [optional] 
**usage_count** | **int** | The number of days there has been usage of the source by the identity. | [optional] 

## Example

```python
from beta.models.role_mining_potential_role_source_usage import RoleMiningPotentialRoleSourceUsage

# TODO update the JSON string below
json = "{}"
# create an instance of RoleMiningPotentialRoleSourceUsage from a JSON string
role_mining_potential_role_source_usage_instance = RoleMiningPotentialRoleSourceUsage.from_json(json)
# print the JSON string representation of the object
print RoleMiningPotentialRoleSourceUsage.to_json()

# convert the object into a dict
role_mining_potential_role_source_usage_dict = role_mining_potential_role_source_usage_instance.to_dict()
# create an instance of RoleMiningPotentialRoleSourceUsage from a dict
role_mining_potential_role_source_usage_form_dict = role_mining_potential_role_source_usage.from_dict(role_mining_potential_role_source_usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


