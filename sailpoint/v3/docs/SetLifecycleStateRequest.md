# SetLifecycleStateRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lifecycle_state_id** | **str** | The ID of the lifecycle state to set | [optional] 

## Example

```python
from sailpoint.v3.models.set_lifecycle_state_request import SetLifecycleStateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetLifecycleStateRequest from a JSON string
set_lifecycle_state_request_instance = SetLifecycleStateRequest.from_json(json)
# print the JSON string representation of the object
print SetLifecycleStateRequest.to_json()

# convert the object into a dict
set_lifecycle_state_request_dict = set_lifecycle_state_request_instance.to_dict()
# create an instance of SetLifecycleStateRequest from a dict
set_lifecycle_state_request_form_dict = set_lifecycle_state_request.from_dict(set_lifecycle_state_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


