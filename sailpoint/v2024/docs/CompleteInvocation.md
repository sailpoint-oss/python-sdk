# CompleteInvocation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**secret** | **str** | Unique invocation secret that was generated when the invocation was created. Required to authenticate to the endpoint. | 
**error** | **str** | The error message to indicate a failed invocation or error if any. | [optional] 
**output** | **object** | Trigger output to complete the invocation. Its schema is defined in the trigger definition. | 

## Example

```python
from sailpoint.v2024.models.complete_invocation import CompleteInvocation

# TODO update the JSON string below
json = "{}"
# create an instance of CompleteInvocation from a JSON string
complete_invocation_instance = CompleteInvocation.from_json(json)
# print the JSON string representation of the object
print CompleteInvocation.to_json()

# convert the object into a dict
complete_invocation_dict = complete_invocation_instance.to_dict()
# create an instance of CompleteInvocation from a dict
complete_invocation_form_dict = complete_invocation.from_dict(complete_invocation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


