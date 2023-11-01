# TaggedObjectDto


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | DTO type | [optional] 
**id** | **str** | ID of the object to which this reference applies | [optional] 
**name** | **str** | Human-readable display name of the object to which this reference applies | [optional] 

## Example

```python
from beta.models.tagged_object_dto import TaggedObjectDto

# TODO update the JSON string below
json = "{}"
# create an instance of TaggedObjectDto from a JSON string
tagged_object_dto_instance = TaggedObjectDto.from_json(json)
# print the JSON string representation of the object
print TaggedObjectDto.to_json()

# convert the object into a dict
tagged_object_dto_dict = tagged_object_dto_instance.to_dict()
# create an instance of TaggedObjectDto from a dict
tagged_object_dto_form_dict = tagged_object_dto.from_dict(tagged_object_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


