# LifecyclestateDeleted

Deleted lifecycle state.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Deleted lifecycle state&#39;s DTO type. | [optional] 
**id** | **str** | Deleted lifecycle state ID. | [optional] 
**name** | **str** | Deleted lifecycle state&#39;s display name. | [optional] 

## Example

```python
from sailpoint.v3.models.lifecyclestate_deleted import LifecyclestateDeleted

# TODO update the JSON string below
json = "{}"
# create an instance of LifecyclestateDeleted from a JSON string
lifecyclestate_deleted_instance = LifecyclestateDeleted.from_json(json)
# print the JSON string representation of the object
print LifecyclestateDeleted.to_json()

# convert the object into a dict
lifecyclestate_deleted_dict = lifecyclestate_deleted_instance.to_dict()
# create an instance of LifecyclestateDeleted from a dict
lifecyclestate_deleted_form_dict = lifecyclestate_deleted.from_dict(lifecyclestate_deleted_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


