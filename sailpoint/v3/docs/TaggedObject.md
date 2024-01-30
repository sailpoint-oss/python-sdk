# TaggedObject

Tagged object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object_ref** | [**TaggedObjectDto**](TaggedObjectDto.md) |  | [optional] 
**tags** | **List[str]** | Labels to be applied to an Object | [optional] 

## Example

```python
from sailpoint.v3.models.tagged_object import TaggedObject

# TODO update the JSON string below
json = "{}"
# create an instance of TaggedObject from a JSON string
tagged_object_instance = TaggedObject.from_json(json)
# print the JSON string representation of the object
print TaggedObject.to_json()

# convert the object into a dict
tagged_object_dict = tagged_object_instance.to_dict()
# create an instance of TaggedObject from a dict
tagged_object_form_dict = tagged_object.from_dict(tagged_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


