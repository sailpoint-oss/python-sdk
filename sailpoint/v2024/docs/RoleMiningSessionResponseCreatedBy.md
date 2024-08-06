# RoleMiningSessionResponseCreatedBy

The session created by details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the creator | [optional] 
**display_name** | **str** | The display name of the creator | [optional] 

## Example

```python
from sailpoint.v2024.models.role_mining_session_response_created_by import RoleMiningSessionResponseCreatedBy

# TODO update the JSON string below
json = "{}"
# create an instance of RoleMiningSessionResponseCreatedBy from a JSON string
role_mining_session_response_created_by_instance = RoleMiningSessionResponseCreatedBy.from_json(json)
# print the JSON string representation of the object
print RoleMiningSessionResponseCreatedBy.to_json()

# convert the object into a dict
role_mining_session_response_created_by_dict = role_mining_session_response_created_by_instance.to_dict()
# create an instance of RoleMiningSessionResponseCreatedBy from a dict
role_mining_session_response_created_by_form_dict = role_mining_session_response_created_by.from_dict(role_mining_session_response_created_by_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


