# RoleMiningSessionDtoCreatedBy

The session created by details

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the creator | [optional] 
**display_name** | **str** | The display name of the creator | [optional] 

## Example

```python
from sailpoint.beta.models.role_mining_session_dto_created_by import RoleMiningSessionDtoCreatedBy

# TODO update the JSON string below
json = "{}"
# create an instance of RoleMiningSessionDtoCreatedBy from a JSON string
role_mining_session_dto_created_by_instance = RoleMiningSessionDtoCreatedBy.from_json(json)
# print the JSON string representation of the object
print RoleMiningSessionDtoCreatedBy.to_json()

# convert the object into a dict
role_mining_session_dto_created_by_dict = role_mining_session_dto_created_by_instance.to_dict()
# create an instance of RoleMiningSessionDtoCreatedBy from a dict
role_mining_session_dto_created_by_form_dict = role_mining_session_dto_created_by.from_dict(role_mining_session_dto_created_by_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


