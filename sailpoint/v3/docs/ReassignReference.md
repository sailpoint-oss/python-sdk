# ReassignReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of item or identity being reassigned. | 
**type** | **str** | The type of item or identity being reassigned. | 

## Example

```python
from sailpoint.v3.models.reassign_reference import ReassignReference

# TODO update the JSON string below
json = "{}"
# create an instance of ReassignReference from a JSON string
reassign_reference_instance = ReassignReference.from_json(json)
# print the JSON string representation of the object
print ReassignReference.to_json()

# convert the object into a dict
reassign_reference_dict = reassign_reference_instance.to_dict()
# create an instance of ReassignReference from a dict
reassign_reference_form_dict = reassign_reference.from_dict(reassign_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


