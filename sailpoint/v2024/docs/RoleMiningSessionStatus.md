# RoleMiningSessionStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | [**RoleMiningSessionState**](RoleMiningSessionState.md) |  | [optional] 

## Example

```python
from sailpoint.v2024.models.role_mining_session_status import RoleMiningSessionStatus

# TODO update the JSON string below
json = "{}"
# create an instance of RoleMiningSessionStatus from a JSON string
role_mining_session_status_instance = RoleMiningSessionStatus.from_json(json)
# print the JSON string representation of the object
print RoleMiningSessionStatus.to_json()

# convert the object into a dict
role_mining_session_status_dict = role_mining_session_status_instance.to_dict()
# create an instance of RoleMiningSessionStatus from a dict
role_mining_session_status_form_dict = role_mining_session_status.from_dict(role_mining_session_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


