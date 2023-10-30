# AttrSyncSourceConfig

Specification of attribute sync configuration for a source

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | [**BaseReferenceDto**](BaseReferenceDto.md) |  | 
**attributes** | [**List[AttrSyncSourceAttributeConfig]**](AttrSyncSourceAttributeConfig.md) | Attribute synchronization configuration for specific identity attributes in the context of a source | 

## Example

```python
from beta.models.attr_sync_source_config import AttrSyncSourceConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AttrSyncSourceConfig from a JSON string
attr_sync_source_config_instance = AttrSyncSourceConfig.from_json(json)
# print the JSON string representation of the object
print AttrSyncSourceConfig.to_json()

# convert the object into a dict
attr_sync_source_config_dict = attr_sync_source_config_instance.to_dict()
# create an instance of AttrSyncSourceConfig from a dict
attr_sync_source_config_form_dict = attr_sync_source_config.from_dict(attr_sync_source_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


