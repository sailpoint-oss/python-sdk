# DisplayReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique ID of the referenced object. | [optional] 
**name** | **str** | The human readable name of the referenced object. | [optional] 
**display_name** | **str** |  | [optional] 

## Example

```python
from sailpoint.v3.models.display_reference import DisplayReference

# TODO update the JSON string below
json = "{}"
# create an instance of DisplayReference from a JSON string
display_reference_instance = DisplayReference.from_json(json)
# print the JSON string representation of the object
print DisplayReference.to_json()

# convert the object into a dict
display_reference_dict = display_reference_instance.to_dict()
# create an instance of DisplayReference from a dict
display_reference_form_dict = display_reference.from_dict(display_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


