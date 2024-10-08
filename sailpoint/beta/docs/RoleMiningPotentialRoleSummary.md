# RoleMiningPotentialRoleSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Id of the potential role | [optional] 
**name** | **str** | Name of the potential role | [optional] 
**potential_role_ref** | [**RoleMiningPotentialRoleRef**](RoleMiningPotentialRoleRef.md) |  | [optional] 
**identity_count** | **int** | The number of identities in a potential role. | [optional] 
**entitlement_count** | **int** | The number of entitlements in a potential role. | [optional] 
**identity_group_status** | **str** | The status for this identity group which can be \&quot;REQUESTED\&quot; or \&quot;OBTAINED\&quot; | [optional] 
**provision_state** | [**RoleMiningPotentialRoleProvisionState**](RoleMiningPotentialRoleProvisionState.md) |  | [optional] 
**role_id** | **str** | ID of the provisioned role in IIQ or IDN.  Null if this potential role has not been provisioned. | [optional] 
**density** | **int** | The density metric (0-100) of this potential role. Higher density values indicate higher similarity amongst the identities. | [optional] 
**freshness** | **int** | The freshness metric (0-100) of this potential role. Higher freshness values indicate this potential role is more distinctive compared to existing roles. | [optional] 
**quality** | **int** | The quality metric (0-100) of this potential role. Higher quality values indicate this potential role has high density and freshness. | [optional] 
**type** | [**RoleMiningRoleType**](RoleMiningRoleType.md) |  | [optional] 
**created_by** | [**RoleMiningPotentialRoleSummaryCreatedBy**](RoleMiningPotentialRoleSummaryCreatedBy.md) |  | [optional] 
**created_date** | **datetime** | The date-time when this potential role was created. | [optional] 
**saved** | **bool** | The potential role&#39;s saved status | [optional] [default to False]
**description** | **str** | Description of the potential role | [optional] 
**session** | [**RoleMiningSessionParametersDto**](RoleMiningSessionParametersDto.md) |  | [optional] 

## Example

```python
from sailpoint.beta.models.role_mining_potential_role_summary import RoleMiningPotentialRoleSummary

# TODO update the JSON string below
json = "{}"
# create an instance of RoleMiningPotentialRoleSummary from a JSON string
role_mining_potential_role_summary_instance = RoleMiningPotentialRoleSummary.from_json(json)
# print the JSON string representation of the object
print(RoleMiningPotentialRoleSummary.to_json())

# convert the object into a dict
role_mining_potential_role_summary_dict = role_mining_potential_role_summary_instance.to_dict()
# create an instance of RoleMiningPotentialRoleSummary from a dict
role_mining_potential_role_summary_from_dict = RoleMiningPotentialRoleSummary.from_dict(role_mining_potential_role_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


