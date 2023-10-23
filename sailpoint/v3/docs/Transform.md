# Transform

The representation of an internally- or customer-defined transform.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Unique name of this transform | 
**type** | **str** | The type of transform operation | 
**attributes** | **object** | Meta-data about the transform. Values in this list are specific to the type of transform to be executed. | 

## Example

```python
from v3.models.transform import Transform

# TODO update the JSON string below
json = "{}"
# create an instance of Transform from a JSON string
transform_instance = Transform.from_json(json)
# print the JSON string representation of the object
print Transform.to_json()

# convert the object into a dict
transform_dict = transform_instance.to_dict()
# create an instance of Transform from a dict
transform_form_dict = transform.from_dict(transform_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


