# TypedReference

A typed reference to the object. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**DtoType**](DtoType.md) |  | 
**id** | **str** | The id of the object.  | 

## Example

```python
from v3.models.typed_reference import TypedReference

# TODO update the JSON string below
json = "{}"
# create an instance of TypedReference from a JSON string
typed_reference_instance = TypedReference.from_json(json)
# print the JSON string representation of the object
print TypedReference.to_json()

# convert the object into a dict
typed_reference_dict = typed_reference_instance.to_dict()
# create an instance of TypedReference from a dict
typed_reference_form_dict = typed_reference.from_dict(typed_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


