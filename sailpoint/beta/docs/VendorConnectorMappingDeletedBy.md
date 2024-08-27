# VendorConnectorMappingDeletedBy

An object representing the nullable identifier of the user who deleted the mapping.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**string** | **str** | The identifier of the user who deleted the mapping, if applicable. | [optional] 
**valid** | **bool** | A flag indicating if the &#39;String&#39; field is set and valid, i.e., if the mapping has been deleted. | [optional] [default to False]

## Example

```python
from sailpoint.beta.models.vendor_connector_mapping_deleted_by import VendorConnectorMappingDeletedBy

# TODO update the JSON string below
json = "{}"
# create an instance of VendorConnectorMappingDeletedBy from a JSON string
vendor_connector_mapping_deleted_by_instance = VendorConnectorMappingDeletedBy.from_json(json)
# print the JSON string representation of the object
print(VendorConnectorMappingDeletedBy.to_json())

# convert the object into a dict
vendor_connector_mapping_deleted_by_dict = vendor_connector_mapping_deleted_by_instance.to_dict()
# create an instance of VendorConnectorMappingDeletedBy from a dict
vendor_connector_mapping_deleted_by_from_dict = VendorConnectorMappingDeletedBy.from_dict(vendor_connector_mapping_deleted_by_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


