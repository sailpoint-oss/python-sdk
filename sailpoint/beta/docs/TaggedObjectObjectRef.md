# TaggedObjectObjectRef


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | DTO type | [optional] 
**id** | **str** | ID of the object to which this reference applies | [optional] 
**name** | **str** | Human-readable display name of the object to which this reference applies | [optional] 

## Example

```python
from sailpoint.beta.models.tagged_object_object_ref import TaggedObjectObjectRef

# TODO update the JSON string below
json = "{}"
# create an instance of TaggedObjectObjectRef from a JSON string
tagged_object_object_ref_instance = TaggedObjectObjectRef.from_json(json)
# print the JSON string representation of the object
print TaggedObjectObjectRef.to_json()

# convert the object into a dict
tagged_object_object_ref_dict = tagged_object_object_ref_instance.to_dict()
# create an instance of TaggedObjectObjectRef from a dict
tagged_object_object_ref_form_dict = tagged_object_object_ref.from_dict(tagged_object_object_ref_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


