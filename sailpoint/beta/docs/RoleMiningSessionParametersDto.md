# RoleMiningSessionParametersDto


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the role mining session | [optional] 
**name** | **str** | The session&#39;s saved name | [optional] 
**min_num_identities_in_potential_role** | **int** | Minimum number of identities in a potential role | [optional] 
**prune_threshold** | **int** | The prune threshold to be used or null to calculate prescribedPruneThreshold | [optional] 
**saved** | **bool** | The session&#39;s saved status | [optional] [default to True]
**scope** | [**RoleMiningSessionScope**](RoleMiningSessionScope.md) |  | [optional] 
**type** | [**RoleMiningRoleType**](RoleMiningRoleType.md) |  | [optional] 
**state** | [**RoleMiningSessionState**](RoleMiningSessionState.md) |  | [optional] 
**scoping_method** | [**RoleMiningSessionScopingMethod**](RoleMiningSessionScopingMethod.md) |  | [optional] 

## Example

```python
from sailpoint.beta.models.role_mining_session_parameters_dto import RoleMiningSessionParametersDto

# TODO update the JSON string below
json = "{}"
# create an instance of RoleMiningSessionParametersDto from a JSON string
role_mining_session_parameters_dto_instance = RoleMiningSessionParametersDto.from_json(json)
# print the JSON string representation of the object
print RoleMiningSessionParametersDto.to_json()

# convert the object into a dict
role_mining_session_parameters_dto_dict = role_mining_session_parameters_dto_instance.to_dict()
# create an instance of RoleMiningSessionParametersDto from a dict
role_mining_session_parameters_dto_form_dict = role_mining_session_parameters_dto.from_dict(role_mining_session_parameters_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


