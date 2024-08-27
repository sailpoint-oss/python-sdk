# StartInvocationInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trigger_id** | **str** | Trigger ID | [optional] 
**input** | **object** | Trigger input payload. Its schema is defined in the trigger definition. | [optional] 
**content_json** | **object** | JSON map of invocation metadata | [optional] 

## Example

```python
from sailpoint.v2024.models.start_invocation_input import StartInvocationInput

# TODO update the JSON string below
json = "{}"
# create an instance of StartInvocationInput from a JSON string
start_invocation_input_instance = StartInvocationInput.from_json(json)
# print the JSON string representation of the object
print(StartInvocationInput.to_json())

# convert the object into a dict
start_invocation_input_dict = start_invocation_input_instance.to_dict()
# create an instance of StartInvocationInput from a dict
start_invocation_input_from_dict = StartInvocationInput.from_dict(start_invocation_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


