# SourceDeletedActor

Identity who deleted the source.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | DTO type of identity who deleted the source. | 
**id** | **str** | ID of identity who deleted the source. | 
**name** | **str** | Display name of identity who deleted the source. | 

## Example

```python
from sailpoint.v2024.models.source_deleted_actor import SourceDeletedActor

# TODO update the JSON string below
json = "{}"
# create an instance of SourceDeletedActor from a JSON string
source_deleted_actor_instance = SourceDeletedActor.from_json(json)
# print the JSON string representation of the object
print(SourceDeletedActor.to_json())

# convert the object into a dict
source_deleted_actor_dict = source_deleted_actor_instance.to_dict()
# create an instance of SourceDeletedActor from a dict
source_deleted_actor_from_dict = SourceDeletedActor.from_dict(source_deleted_actor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


