# VendorConnectorMapping


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier for the vendor-connector mapping. | [optional] 
**vendor** | **str** | The name of the vendor. | [optional] 
**connector** | **str** | The name of the connector. | [optional] 
**created_at** | **datetime** | The creation timestamp of the mapping. | [optional] 
**created_by** | **str** | The identifier of the user who created the mapping. | [optional] 
**updated_at** | [**VendorConnectorMappingUpdatedAt**](VendorConnectorMappingUpdatedAt.md) |  | [optional] 
**updated_by** | [**VendorConnectorMappingUpdatedBy**](VendorConnectorMappingUpdatedBy.md) |  | [optional] 
**deleted_at** | [**VendorConnectorMappingDeletedAt**](VendorConnectorMappingDeletedAt.md) |  | [optional] 
**deleted_by** | [**VendorConnectorMappingDeletedBy**](VendorConnectorMappingDeletedBy.md) |  | [optional] 

## Example

```python
from sailpoint.beta.models.vendor_connector_mapping import VendorConnectorMapping

# TODO update the JSON string below
json = "{}"
# create an instance of VendorConnectorMapping from a JSON string
vendor_connector_mapping_instance = VendorConnectorMapping.from_json(json)
# print the JSON string representation of the object
print VendorConnectorMapping.to_json()

# convert the object into a dict
vendor_connector_mapping_dict = vendor_connector_mapping_instance.to_dict()
# create an instance of VendorConnectorMapping from a dict
vendor_connector_mapping_form_dict = vendor_connector_mapping.from_dict(vendor_connector_mapping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


