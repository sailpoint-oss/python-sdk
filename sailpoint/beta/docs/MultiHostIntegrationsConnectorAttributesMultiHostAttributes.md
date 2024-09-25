# MultiHostIntegrationsConnectorAttributesMultiHostAttributes

Attributes of Multi-Host Integration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** | Password. | [optional] 
**connector_files** | **str** | Connector file. | [optional] 
**auth_type** | **str** | Authentication type. | [optional] 
**user** | **str** | Username. | [optional] 

## Example

```python
from sailpoint.beta.models.multi_host_integrations_connector_attributes_multi_host_attributes import MultiHostIntegrationsConnectorAttributesMultiHostAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of MultiHostIntegrationsConnectorAttributesMultiHostAttributes from a JSON string
multi_host_integrations_connector_attributes_multi_host_attributes_instance = MultiHostIntegrationsConnectorAttributesMultiHostAttributes.from_json(json)
# print the JSON string representation of the object
print(MultiHostIntegrationsConnectorAttributesMultiHostAttributes.to_json())

# convert the object into a dict
multi_host_integrations_connector_attributes_multi_host_attributes_dict = multi_host_integrations_connector_attributes_multi_host_attributes_instance.to_dict()
# create an instance of MultiHostIntegrationsConnectorAttributesMultiHostAttributes from a dict
multi_host_integrations_connector_attributes_multi_host_attributes_from_dict = MultiHostIntegrationsConnectorAttributesMultiHostAttributes.from_dict(multi_host_integrations_connector_attributes_multi_host_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


