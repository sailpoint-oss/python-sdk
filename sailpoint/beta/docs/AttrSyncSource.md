# AttrSyncSource

Target source for attribute synchronization.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | DTO type of target source for attribute synchronization. | [optional] 
**id** | **str** | ID of target source for attribute synchronization. | [optional] 
**name** | **str** | Human-readable name of target source for attribute synchronization. | [optional] 

## Example

```python
from sailpoint.beta.models.attr_sync_source import AttrSyncSource

# TODO update the JSON string below
json = "{}"
# create an instance of AttrSyncSource from a JSON string
attr_sync_source_instance = AttrSyncSource.from_json(json)
# print the JSON string representation of the object
print AttrSyncSource.to_json()

# convert the object into a dict
attr_sync_source_dict = attr_sync_source_instance.to_dict()
# create an instance of AttrSyncSource from a dict
attr_sync_source_form_dict = attr_sync_source.from_dict(attr_sync_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


