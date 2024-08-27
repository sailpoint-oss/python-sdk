# GetVendorConnectorMappings405Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_name** | **object** | A message describing the error | [optional] 
**error_message** | **object** | Description of the error | [optional] 
**tracking_id** | **str** | Unique tracking id for the error. | [optional] 

## Example

```python
from sailpoint.v3.models.get_vendor_connector_mappings405_response import GetVendorConnectorMappings405Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetVendorConnectorMappings405Response from a JSON string
get_vendor_connector_mappings405_response_instance = GetVendorConnectorMappings405Response.from_json(json)
# print the JSON string representation of the object
print(GetVendorConnectorMappings405Response.to_json())

# convert the object into a dict
get_vendor_connector_mappings405_response_dict = get_vendor_connector_mappings405_response_instance.to_dict()
# create an instance of GetVendorConnectorMappings405Response from a dict
get_vendor_connector_mappings405_response_from_dict = GetVendorConnectorMappings405Response.from_dict(get_vendor_connector_mappings405_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


