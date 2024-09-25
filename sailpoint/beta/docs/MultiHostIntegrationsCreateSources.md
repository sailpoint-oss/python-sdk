# MultiHostIntegrationsCreateSources

This represents sources to be created of same type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Source&#39;s human-readable name. | 
**description** | **str** | Source&#39;s human-readable description. | [optional] 
**connector_attributes** | **Dict[str, object]** | Connector specific configuration. This configuration will differ from type to type. | [optional] 

## Example

```python
from sailpoint.beta.models.multi_host_integrations_create_sources import MultiHostIntegrationsCreateSources

# TODO update the JSON string below
json = "{}"
# create an instance of MultiHostIntegrationsCreateSources from a JSON string
multi_host_integrations_create_sources_instance = MultiHostIntegrationsCreateSources.from_json(json)
# print the JSON string representation of the object
print(MultiHostIntegrationsCreateSources.to_json())

# convert the object into a dict
multi_host_integrations_create_sources_dict = multi_host_integrations_create_sources_instance.to_dict()
# create an instance of MultiHostIntegrationsCreateSources from a dict
multi_host_integrations_create_sources_from_dict = MultiHostIntegrationsCreateSources.from_dict(multi_host_integrations_create_sources_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


