# CompleteInvocationInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**localized_error** | [**LocalizedMessage**](LocalizedMessage.md) |  | [optional] 
**output** | **object** | Trigger output that completed the invocation. Its schema is defined in the trigger definition. | [optional] 

## Example

```python
from sailpoint.beta.models.complete_invocation_input import CompleteInvocationInput

# TODO update the JSON string below
json = "{}"
# create an instance of CompleteInvocationInput from a JSON string
complete_invocation_input_instance = CompleteInvocationInput.from_json(json)
# print the JSON string representation of the object
print CompleteInvocationInput.to_json()

# convert the object into a dict
complete_invocation_input_dict = complete_invocation_input_instance.to_dict()
# create an instance of CompleteInvocationInput from a dict
complete_invocation_input_form_dict = complete_invocation_input.from_dict(complete_invocation_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


