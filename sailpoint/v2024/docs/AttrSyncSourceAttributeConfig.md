# AttrSyncSourceAttributeConfig

Specification of source attribute sync mapping configuration for an identity attribute

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the identity attribute | 
**display_name** | **str** | Display name of the identity attribute | 
**enabled** | **bool** | Determines whether or not the attribute is enabled for synchronization | 
**target** | **str** | Name of the source account attribute to which the identity attribute value will be synchronized if enabled | 

## Example

```python
from sailpoint.v2024.models.attr_sync_source_attribute_config import AttrSyncSourceAttributeConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AttrSyncSourceAttributeConfig from a JSON string
attr_sync_source_attribute_config_instance = AttrSyncSourceAttributeConfig.from_json(json)
# print the JSON string representation of the object
print AttrSyncSourceAttributeConfig.to_json()

# convert the object into a dict
attr_sync_source_attribute_config_dict = attr_sync_source_attribute_config_instance.to_dict()
# create an instance of AttrSyncSourceAttributeConfig from a dict
attr_sync_source_attribute_config_form_dict = attr_sync_source_attribute_config.from_dict(attr_sync_source_attribute_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


