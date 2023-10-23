# SourceCreatedActor

The identity that created the source.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **object** | The type of object that is referenced | 
**id** | **str** | ID of the object to which this reference applies | 
**name** | **str** | Human-readable display name of the object to which this reference applies | 

## Example

```python
from beta.models.source_created_actor import SourceCreatedActor

# TODO update the JSON string below
json = "{}"
# create an instance of SourceCreatedActor from a JSON string
source_created_actor_instance = SourceCreatedActor.from_json(json)
# print the JSON string representation of the object
print SourceCreatedActor.to_json()

# convert the object into a dict
source_created_actor_dict = source_created_actor_instance.to_dict()
# create an instance of SourceCreatedActor from a dict
source_created_actor_form_dict = source_created_actor.from_dict(source_created_actor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


