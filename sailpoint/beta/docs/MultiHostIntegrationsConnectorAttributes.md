# MultiHostIntegrationsConnectorAttributes

Connector specific configuration. This configuration will differ for Multi-Host Integration type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_allowed_sources** | **int** | Maximum sources allowed count of a Multi-Host Integration | [optional] 
**last_source_upload_count** | **int** | Last upload sources count of a Multi-Host Integration | [optional] 
**connector_file_upload_history** | [**MultiHostIntegrationsConnectorAttributesConnectorFileUploadHistory**](MultiHostIntegrationsConnectorAttributesConnectorFileUploadHistory.md) |  | [optional] 
**multihost_status** | **str** | Multi-Host integration status. | [optional] 
**show_account_schema** | **bool** | Show account schema | [optional] [default to True]
**show_entitlement_schema** | **bool** | Show entitlement schema | [optional] [default to True]
**multi_host_attributes** | [**MultiHostIntegrationsConnectorAttributesMultiHostAttributes**](MultiHostIntegrationsConnectorAttributesMultiHostAttributes.md) |  | [optional] 

## Example

```python
from sailpoint.beta.models.multi_host_integrations_connector_attributes import MultiHostIntegrationsConnectorAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of MultiHostIntegrationsConnectorAttributes from a JSON string
multi_host_integrations_connector_attributes_instance = MultiHostIntegrationsConnectorAttributes.from_json(json)
# print the JSON string representation of the object
print(MultiHostIntegrationsConnectorAttributes.to_json())

# convert the object into a dict
multi_host_integrations_connector_attributes_dict = multi_host_integrations_connector_attributes_instance.to_dict()
# create an instance of MultiHostIntegrationsConnectorAttributes from a dict
multi_host_integrations_connector_attributes_from_dict = MultiHostIntegrationsConnectorAttributes.from_dict(multi_host_integrations_connector_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


