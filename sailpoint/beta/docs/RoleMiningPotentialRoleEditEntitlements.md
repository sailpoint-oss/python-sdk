# RoleMiningPotentialRoleEditEntitlements


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[str]** | The list of entitlement ids to be edited | [optional] 
**exclude** | **bool** | If true, add ids to be exclusion list. If false, remove ids from the exclusion list. | [optional] 

## Example

```python
from sailpoint.beta.models.role_mining_potential_role_edit_entitlements import RoleMiningPotentialRoleEditEntitlements

# TODO update the JSON string below
json = "{}"
# create an instance of RoleMiningPotentialRoleEditEntitlements from a JSON string
role_mining_potential_role_edit_entitlements_instance = RoleMiningPotentialRoleEditEntitlements.from_json(json)
# print the JSON string representation of the object
print RoleMiningPotentialRoleEditEntitlements.to_json()

# convert the object into a dict
role_mining_potential_role_edit_entitlements_dict = role_mining_potential_role_edit_entitlements_instance.to_dict()
# create an instance of RoleMiningPotentialRoleEditEntitlements from a dict
role_mining_potential_role_edit_entitlements_form_dict = role_mining_potential_role_edit_entitlements.from_dict(role_mining_potential_role_edit_entitlements_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


