# SourceUpdatedActor

Identity who updated the source.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | DTO type of identity who updated the source. | 
**id** | **str** | ID of identity who updated the source. | [optional] 
**name** | **str** | Display name of identity who updated the source. | 

## Example

```python
from sailpoint.beta.models.source_updated_actor import SourceUpdatedActor

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


