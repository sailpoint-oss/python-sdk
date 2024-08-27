# RoleMiningPotentialRoleProvisionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role_name** | **str** | Name of the new role being created | [optional] 
**role_description** | **str** | Short description of the new role being created | [optional] 
**owner_id** | **str** | ID of the identity that will own this role | [optional] 
**include_identities** | **bool** | When true, create access requests for the identities associated with the potential role | [optional] [default to False]
**directly_assigned_entitlements** | **bool** | When true, assign entitlements directly to the role; otherwise, create access profiles containing the entitlements | [optional] [default to False]

## Example

```python
from sailpoint.beta.models.role_mining_potential_role_provision_request import RoleMiningPotentialRoleProvisionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RoleMiningPotentialRoleProvisionRequest from a JSON string
role_mining_potential_role_provision_request_instance = RoleMiningPotentialRoleProvisionRequest.from_json(json)
# print the JSON string representation of the object
print(RoleMiningPotentialRoleProvisionRequest.to_json())

# convert the object into a dict
role_mining_potential_role_provision_request_dict = role_mining_potential_role_provision_request_instance.to_dict()
# create an instance of RoleMiningPotentialRoleProvisionRequest from a dict
role_mining_potential_role_provision_request_from_dict = RoleMiningPotentialRoleProvisionRequest.from_dict(role_mining_potential_role_provision_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


