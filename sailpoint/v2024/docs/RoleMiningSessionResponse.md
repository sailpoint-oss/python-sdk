# RoleMiningSessionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | [**RoleMiningSessionScope**](RoleMiningSessionScope.md) |  | [optional] 
**min_num_identities_in_potential_role** | **int** | Minimum number of identities in a potential role | [optional] 
**scoping_method** | **str** | The scoping method of the role mining session | [optional] 
**prescribed_prune_threshold** | **int** | The computed (or prescribed) prune threshold for this session | [optional] 
**prune_threshold** | **int** | The prune threshold to be used for this role mining session | [optional] 
**potential_role_count** | **int** | The number of potential roles | [optional] 
**potential_roles_ready_count** | **int** | The number of potential roles which have completed processing | [optional] 
**status** | [**RoleMiningSessionStatus**](RoleMiningSessionStatus.md) |  | [optional] 
**email_recipient_id** | **str** | The id of the user who will receive an email about the role mining session | [optional] 
**created_by** | [**RoleMiningSessionResponseCreatedBy**](RoleMiningSessionResponseCreatedBy.md) |  | [optional] 
**identity_count** | **int** | The number of identities | [optional] 
**saved** | **bool** | The session&#39;s saved status | [optional] [default to False]
**name** | **str** | The session&#39;s saved name | [optional] 
**data_file_path** | **str** | The data file path of the role mining session | [optional] 
**id** | **str** | Session Id for this role mining session | [optional] 
**created_date** | **datetime** | The date-time when this role mining session was created. | [optional] 
**modified_date** | **datetime** | The date-time when this role mining session was completed. | [optional] 
**type** | [**RoleMiningRoleType**](RoleMiningRoleType.md) |  | [optional] 

## Example

```python
from sailpoint.v2024.models.role_mining_session_response import RoleMiningSessionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RoleMiningSessionResponse from a JSON string
role_mining_session_response_instance = RoleMiningSessionResponse.from_json(json)
# print the JSON string representation of the object
print RoleMiningSessionResponse.to_json()

# convert the object into a dict
role_mining_session_response_dict = role_mining_session_response_instance.to_dict()
# create an instance of RoleMiningSessionResponse from a dict
role_mining_session_response_form_dict = role_mining_session_response.from_dict(role_mining_session_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


