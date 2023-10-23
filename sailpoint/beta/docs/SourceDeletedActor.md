# SourceDeletedActor

The identity that deleted the source.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **object** | The type of object that is referenced | 
**id** | **str** | ID of the object to which this reference applies | 
**name** | **str** | Human-readable display name of the object to which this reference applies | 

## Example

```python
from beta.models.source_deleted_actor import SourceDeletedActor

# TODO update the JSON string below
json = "{}"
# create an instance of SourceDeletedActor from a JSON string
source_deleted_actor_instance = SourceDeletedActor.from_json(json)
# print the JSON string representation of the object
print SourceDeletedActor.to_json()

# convert the object into a dict
source_deleted_actor_dict = source_deleted_actor_instance.to_dict()
# create an instance of SourceDeletedActor from a dict
source_deleted_actor_form_dict = source_deleted_actor.from_dict(source_deleted_actor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


