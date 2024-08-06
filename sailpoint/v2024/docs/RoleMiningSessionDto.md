# RoleMiningSessionDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | [**RoleMiningSessionScope**](RoleMiningSessionScope.md) |  | [optional] 
**prune_threshold** | **int** | The prune threshold to be used or null to calculate prescribedPruneThreshold | [optional] 
**prescribed_prune_threshold** | **int** | The calculated prescribedPruneThreshold | [optional] 
**min_num_identities_in_potential_role** | **int** | Minimum number of identities in a potential role | [optional] 
**potential_role_count** | **int** | Number of potential roles | [optional] 
**potential_roles_ready_count** | **int** | Number of potential roles ready | [optional] 
**type** | [**RoleMiningRoleType**](RoleMiningRoleType.md) |  | [optional] 
**email_recipient_id** | **str** | The id of the user who will receive an email about the role mining session | [optional] 
**identity_count** | **int** | Number of identities in the population which meet the search criteria or identity list provided | [optional] 
**saved** | **bool** | The session&#39;s saved status | [optional] [default to False]
**name** | **str** | The session&#39;s saved name | [optional] 

## Example

```python
from sailpoint.v2024.models.role_mining_session_dto import RoleMiningSessionDto

# TODO update the JSON string below
json = "{}"
# create an instance of RoleMiningSessionDto from a JSON string
role_mining_session_dto_instance = RoleMiningSessionDto.from_json(json)
# print the JSON string representation of the object
print RoleMiningSessionDto.to_json()

# convert the object into a dict
role_mining_session_dto_dict = role_mining_session_dto_instance.to_dict()
# create an instance of RoleMiningSessionDto from a dict
role_mining_session_dto_form_dict = role_mining_session_dto.from_dict(role_mining_session_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


