# RoleMiningPotentialRole


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_by** | [**RoleMiningSessionResponseCreatedBy**](RoleMiningSessionResponseCreatedBy.md) |  | [optional] 
**density** | **int** | The density of a potential role. | [optional] 
**description** | **str** | The description of a potential role. | [optional] 
**entitlement_count** | **int** | The number of entitlements in a potential role. | [optional] 
**excluded_entitlements** | **List[str]** | The list of entitlement ids to be excluded. | [optional] 
**freshness** | **int** | The freshness of a potential role. | [optional] 
**identity_count** | **int** | The number of identities in a potential role. | [optional] 
**identity_distribution** | [**List[RoleMiningIdentityDistribution]**](RoleMiningIdentityDistribution.md) | Identity attribute distribution. | [optional] 
**identity_ids** | **List[str]** | The list of ids in a potential role. | [optional] 
**name** | **str** | Name of the potential role. | [optional] 
**provision_state** | [**RoleMiningPotentialRoleProvisionState**](RoleMiningPotentialRoleProvisionState.md) |  | [optional] 
**quality** | **int** | The quality of a potential role. | [optional] 
**role_id** | **str** | The roleId of a potential role. | [optional] 
**saved** | **bool** | The potential role&#39;s saved status. | [optional] 
**session** | [**RoleMiningSessionParametersDto**](RoleMiningSessionParametersDto.md) |  | [optional] 
**type** | [**RoleMiningRoleType**](RoleMiningRoleType.md) |  | [optional] 
**id** | **str** | Id of the potential role | [optional] 
**created_date** | **datetime** | The date-time when this potential role was created. | [optional] 
**modified_date** | **datetime** | The date-time when this potential role was modified. | [optional] 

## Example

```python
from sailpoint.v2024.models.role_mining_potential_role import RoleMiningPotentialRole

# TODO update the JSON string below
json = "{}"
# create an instance of RoleMiningPotentialRole from a JSON string
role_mining_potential_role_instance = RoleMiningPotentialRole.from_json(json)
# print the JSON string representation of the object
print(RoleMiningPotentialRole.to_json())

# convert the object into a dict
role_mining_potential_role_dict = role_mining_potential_role_instance.to_dict()
# create an instance of RoleMiningPotentialRole from a dict
role_mining_potential_role_from_dict = RoleMiningPotentialRole.from_dict(role_mining_potential_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


