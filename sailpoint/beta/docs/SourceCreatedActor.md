# SourceCreatedActor

Identity who created the source.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | DTO type of identity who created the source. | 
**id** | **str** | ID of identity who created the source. | 
**name** | **str** | Display name of identity who created the source. | 

## Example

```python
from sailpoint.beta.models.source_created_actor import SourceCreatedActor

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


