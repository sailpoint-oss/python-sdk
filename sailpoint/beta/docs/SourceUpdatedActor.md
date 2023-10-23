# SourceUpdatedActor

The identity or system that performed the update.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **object** | The type of object that is referenced | 
**id** | **str** | ID of the object to which this reference applies | [optional] 
**name** | **str** | Human-readable display name of the object to which this reference applies | 

## Example

```python
from beta.models.source_updated_actor import SourceUpdatedActor

# TODO update the JSON string below
json = "{}"
# create an instance of SourceUpdatedActor from a JSON string
source_updated_actor_instance = SourceUpdatedActor.from_json(json)
# print the JSON string representation of the object
print SourceUpdatedActor.to_json()

# convert the object into a dict
source_updated_actor_dict = source_updated_actor_instance.to_dict()
# create an instance of SourceUpdatedActor from a dict
source_updated_actor_form_dict = source_updated_actor.from_dict(source_updated_actor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


