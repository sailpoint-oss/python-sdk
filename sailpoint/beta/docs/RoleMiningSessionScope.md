# RoleMiningSessionScope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identity_ids** | **List[str]** | The list of identities for this role mining session. | [optional] 
**criteria** | **str** | The \&quot;search\&quot; criteria that produces the list of identities for this role mining session. | [optional] 
**attribute_filter_criteria** | **List[object]** | The filter criteria for this role mining session. | [optional] 

## Example

```python
from sailpoint.beta.models.role_mining_session_scope import RoleMiningSessionScope

# TODO update the JSON string below
json = "{}"
# create an instance of RoleMiningSessionScope from a JSON string
role_mining_session_scope_instance = RoleMiningSessionScope.from_json(json)
# print the JSON string representation of the object
print(RoleMiningSessionScope.to_json())

# convert the object into a dict
role_mining_session_scope_dict = role_mining_session_scope_instance.to_dict()
# create an instance of RoleMiningSessionScope from a dict
role_mining_session_scope_from_dict = RoleMiningSessionScope.from_dict(role_mining_session_scope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


