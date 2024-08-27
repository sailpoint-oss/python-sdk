# DeleteVendorConnectorMapping200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | The number of vendor connector mappings successfully deleted. | [optional] 

## Example

```python
from sailpoint.beta.models.delete_vendor_connector_mapping200_response import DeleteVendorConnectorMapping200Response

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteVendorConnectorMapping200Response from a JSON string
delete_vendor_connector_mapping200_response_instance = DeleteVendorConnectorMapping200Response.from_json(json)
# print the JSON string representation of the object
print(DeleteVendorConnectorMapping200Response.to_json())

# convert the object into a dict
delete_vendor_connector_mapping200_response_dict = delete_vendor_connector_mapping200_response_instance.to_dict()
# create an instance of DeleteVendorConnectorMapping200Response from a dict
delete_vendor_connector_mapping200_response_from_dict = DeleteVendorConnectorMapping200Response.from_dict(delete_vendor_connector_mapping200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


