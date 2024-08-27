# VendorConnectorMappingUpdatedAt

An object representing the nullable timestamp of the last update.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time** | **datetime** | The timestamp when the mapping was last updated, represented in ISO 8601 format. | [optional] 
**valid** | **bool** | A flag indicating if the &#39;Time&#39; field is set and valid. | [optional] [default to False]

## Example

```python
from sailpoint.beta.models.vendor_connector_mapping_updated_at import VendorConnectorMappingUpdatedAt

# TODO update the JSON string below
json = "{}"
# create an instance of VendorConnectorMappingUpdatedAt from a JSON string
vendor_connector_mapping_updated_at_instance = VendorConnectorMappingUpdatedAt.from_json(json)
# print the JSON string representation of the object
print(VendorConnectorMappingUpdatedAt.to_json())

# convert the object into a dict
vendor_connector_mapping_updated_at_dict = vendor_connector_mapping_updated_at_instance.to_dict()
# create an instance of VendorConnectorMappingUpdatedAt from a dict
vendor_connector_mapping_updated_at_from_dict = VendorConnectorMappingUpdatedAt.from_dict(vendor_connector_mapping_updated_at_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


