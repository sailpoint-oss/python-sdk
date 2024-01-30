# Identity1

The definition of an Identity according to the Reassignment Configuration service

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the object | [optional] 
**name** | **str** | Human-readable display name of the object | [optional] 

## Example

```python
from sailpoint.beta.models.identity1 import Identity1

# TODO update the JSON string below
json = "{}"
# create an instance of Identity1 from a JSON string
identity1_instance = Identity1.from_json(json)
# print the JSON string representation of the object
print Identity1.to_json()

# convert the object into a dict
identity1_dict = identity1_instance.to_dict()
# create an instance of Identity1 from a dict
identity1_form_dict = identity1.from_dict(identity1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


