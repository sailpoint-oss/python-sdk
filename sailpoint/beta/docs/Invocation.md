# Invocation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Invocation ID | [optional] 
**trigger_id** | **str** | Trigger ID | [optional] 
**secret** | **str** | Unique invocation secret. | [optional] 
**content_json** | **object** | JSON map of invocation metadata. | [optional] 

## Example

```python
from sailpoint.beta.models.invocation import Invocation

# TODO update the JSON string below
json = "{}"
# create an instance of Invocation from a JSON string
invocation_instance = Invocation.from_json(json)
# print the JSON string representation of the object
print Invocation.to_json()

# convert the object into a dict
invocation_dict = invocation_instance.to_dict()
# create an instance of Invocation from a dict
invocation_form_dict = invocation.from_dict(invocation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


