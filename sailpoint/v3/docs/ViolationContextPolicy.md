# ViolationContextPolicy

The types of objects supported for SOD violations

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **object** | The type of object that is referenced | [optional] 
**id** | **str** | SOD policy ID. | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from sailpoint.v3.models.violation_context_policy import ViolationContextPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of ViolationContextPolicy from a JSON string
violation_context_policy_instance = ViolationContextPolicy.from_json(json)
# print the JSON string representation of the object
print(ViolationContextPolicy.to_json())

# convert the object into a dict
violation_context_policy_dict = violation_context_policy_instance.to_dict()
# create an instance of ViolationContextPolicy from a dict
violation_context_policy_from_dict = ViolationContextPolicy.from_dict(violation_context_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


