# MultiHostIntegrationsCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Multi-Host Integration&#39;s human-readable name. | 
**description** | **str** | Multi-Host Integration&#39;s human-readable description. | 
**owner** | [**MultiHostIntegrationsOwner**](MultiHostIntegrationsOwner.md) |  | 
**cluster** | [**MultiHostIntegrationsCluster**](MultiHostIntegrationsCluster.md) |  | [optional] 
**connector** | **str** | Connector script name. | 
**connector_attributes** | **Dict[str, object]** | Multi-Host Integration specific configuration. User can add any number of additional attributes. e.g. maxSourcesPerAggGroup, maxAllowedSources etc. | [optional] 
**management_workgroup** | [**MultiHostIntegrationsManagementWorkgroup**](MultiHostIntegrationsManagementWorkgroup.md) |  | [optional] 
**created** | **datetime** | Date-time when the source was created | [optional] 
**modified** | **datetime** | Date-time when the source was last modified. | [optional] 

## Example

```python
from sailpoint.beta.models.multi_host_integrations_create import MultiHostIntegrationsCreate

# TODO update the JSON string below
json = "{}"
# create an instance of MultiHostIntegrationsCreate from a JSON string
multi_host_integrations_create_instance = MultiHostIntegrationsCreate.from_json(json)
# print the JSON string representation of the object
print(MultiHostIntegrationsCreate.to_json())

# convert the object into a dict
multi_host_integrations_create_dict = multi_host_integrations_create_instance.to_dict()
# create an instance of MultiHostIntegrationsCreate from a dict
multi_host_integrations_create_from_dict = MultiHostIntegrationsCreate.from_dict(multi_host_integrations_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


