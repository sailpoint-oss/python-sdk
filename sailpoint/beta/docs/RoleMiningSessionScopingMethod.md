# RoleMiningSessionScopingMethod


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** | The scoping method used in the current role mining session. Can be one of these states - MANUAL|AUTO_RM | [optional] 

## Example

```python
from beta.models.role_mining_session_scoping_method import RoleMiningSessionScopingMethod

# TODO update the JSON string below
json = "{}"
# create an instance of RoleMiningSessionScopingMethod from a JSON string
role_mining_session_scoping_method_instance = RoleMiningSessionScopingMethod.from_json(json)
# print the JSON string representation of the object
print RoleMiningSessionScopingMethod.to_json()

# convert the object into a dict
role_mining_session_scoping_method_dict = role_mining_session_scoping_method_instance.to_dict()
# create an instance of RoleMiningSessionScopingMethod from a dict
role_mining_session_scoping_method_form_dict = role_mining_session_scoping_method.from_dict(role_mining_session_scoping_method_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


