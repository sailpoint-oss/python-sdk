# RoleMiningSessionDraftRoleDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the draft role | [optional] 
**description** | **str** | Draft role description | [optional] 
**identity_ids** | **List[str]** | The list of identities for this role mining session. | [optional] 
**entitlement_ids** | **List[str]** | The list of entitlement ids for this role mining session. | [optional] 
**excluded_entitlements** | **List[str]** | The list of excluded entitlement ids. | [optional] 
**modified** | **datetime** | Last modified date | [optional] 
**type** | [**RoleMiningRoleType**](RoleMiningRoleType.md) |  | [optional] 
**id** | **str** | Id of the potential draft role | [optional] 
**created_date** | **datetime** | The date-time when this potential draft role was created. | [optional] 
**modified_date** | **datetime** | The date-time when this potential draft role was modified. | [optional] 

## Example

```python
from sailpoint.v2024.models.role_mining_session_draft_role_dto import RoleMiningSessionDraftRoleDto

# TODO update the JSON string below
json = "{}"
# create an instance of RoleMiningSessionDraftRoleDto from a JSON string
role_mining_session_draft_role_dto_instance = RoleMiningSessionDraftRoleDto.from_json(json)
# print the JSON string representation of the object
print RoleMiningSessionDraftRoleDto.to_json()

# convert the object into a dict
role_mining_session_draft_role_dto_dict = role_mining_session_draft_role_dto_instance.to_dict()
# create an instance of RoleMiningSessionDraftRoleDto from a dict
role_mining_session_draft_role_dto_form_dict = role_mining_session_draft_role_dto.from_dict(role_mining_session_draft_role_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


