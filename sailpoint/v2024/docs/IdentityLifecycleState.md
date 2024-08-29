# IdentityLifecycleState


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state_name** | **str** | The name of the lifecycle state | 
**manually_updated** | **bool** | Whether the lifecycle state has been manually or automatically set | 

## Example

```python
from sailpoint.v2024.models.identity_lifecycle_state import IdentityLifecycleState

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityLifecycleState from a JSON string
identity_lifecycle_state_instance = IdentityLifecycleState.from_json(json)
# print the JSON string representation of the object
print(IdentityLifecycleState.to_json())

# convert the object into a dict
identity_lifecycle_state_dict = identity_lifecycle_state_instance.to_dict()
# create an instance of IdentityLifecycleState from a dict
identity_lifecycle_state_from_dict = IdentityLifecycleState.from_dict(identity_lifecycle_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


