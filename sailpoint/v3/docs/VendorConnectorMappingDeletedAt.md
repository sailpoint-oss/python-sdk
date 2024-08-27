# VendorConnectorMappingDeletedAt

An object representing the nullable timestamp of when the mapping was deleted.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time** | **datetime** | The timestamp when the mapping was deleted, represented in ISO 8601 format, if applicable. | [optional] 
**valid** | **bool** | A flag indicating if the &#39;Time&#39; field is set and valid, i.e., if the mapping has been deleted. | [optional] [default to False]

## Example

```python
from sailpoint.v3.models.vendor_connector_mapping_deleted_at import VendorConnectorMappingDeletedAt

# TODO update the JSON string below
json = "{}"
# create an instance of VendorConnectorMappingDeletedAt from a JSON string
vendor_connector_mapping_deleted_at_instance = VendorConnectorMappingDeletedAt.from_json(json)
# print the JSON string representation of the object
print(VendorConnectorMappingDeletedAt.to_json())

# convert the object into a dict
vendor_connector_mapping_deleted_at_dict = vendor_connector_mapping_deleted_at_instance.to_dict()
# create an instance of VendorConnectorMappingDeletedAt from a dict
vendor_connector_mapping_deleted_at_from_dict = VendorConnectorMappingDeletedAt.from_dict(vendor_connector_mapping_deleted_at_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


