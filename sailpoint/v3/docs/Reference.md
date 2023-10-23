# Reference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique ID of the referenced object. | [optional] 
**name** | **str** | The human readable name of the referenced object. | [optional] 

## Example

```python
from v3.models.reference import Reference

# TODO update the JSON string below
json = "{}"
# create an instance of Reference from a JSON string
reference_instance = Reference.from_json(json)
# print the JSON string representation of the object
print Reference.to_json()

# convert the object into a dict
reference_dict = reference_instance.to_dict()
# create an instance of Reference from a dict
reference_form_dict = reference.from_dict(reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


