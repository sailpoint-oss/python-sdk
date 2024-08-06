# VendorConnectorMappingUpdatedBy

An object representing the nullable identifier of the user who last updated the mapping.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**string** | **str** | The identifier of the user who last updated the mapping, if available. | [optional] 
**valid** | **bool** | A flag indicating if the &#39;String&#39; field is set and valid. | [optional] [default to False]

## Example

```python
from sailpoint.v3.models.vendor_connector_mapping_updated_by import VendorConnectorMappingUpdatedBy

# TODO update the JSON string below
json = "{}"
# create an instance of VendorConnectorMappingUpdatedBy from a JSON string
vendor_connector_mapping_updated_by_instance = VendorConnectorMappingUpdatedBy.from_json(json)
# print the JSON string representation of the object
print VendorConnectorMappingUpdatedBy.to_json()

# convert the object into a dict
vendor_connector_mapping_updated_by_dict = vendor_connector_mapping_updated_by_instance.to_dict()
# create an instance of VendorConnectorMappingUpdatedBy from a dict
vendor_connector_mapping_updated_by_form_dict = vendor_connector_mapping_updated_by.from_dict(vendor_connector_mapping_updated_by_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


